#!/usr/bin/env python 
# -*- coding: utf-8 -*-
#
# Authors:
#   Nora Kearns <nora.c.kearns@gmail.com>

# Problem sourced from: https://epicbio.medium.com/engineeringinterviewblogpost-63cccd202672

"""
Produce a count of the number of times each spacer is sequenced.
"""

import argparse
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
import regex
import pandas as pd


def find_spacer(scaffold:str, sequence: str) -> str:
    '''
    Search for scaffold sequence. If found, return the 20 bases upstream (the spacer sequence).
    '''
    scaffold_start_pos = sequence.find(scaffold)
    if scaffold_start_pos != -1:
        spacer_start_pos = scaffold_start_pos - 20
        return sequence[spacer_start_pos:(spacer_start_pos+20)]
    else:
        return "spacer not found"

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("fastq", help="Input fastq")
    parser.add_argument("guides", help="Input list of guides")
    parser.add_argument("output", help="Output counts file")
    args = parser.parse_args()

    scaffold = 'GTTTAAGAGCTAAGCTGGA'
    spacer_len = 20

    # initialize dictionary of {guide: n} with guides as keys and values initlaized to 0
    guide_df = pd.read_csv(args.guides, header=None, names=['guide'])
    guide_dict = {guide: 0 for guide in guide_df['guide']}

    for record in SeqIO.parse(args.fastq, 'fastq'):
        sequence = str(record.seq)
        # parse spacer from sequence
        spacer_seq = find_spacer(scaffold, sequence)
        # add a count to the corresponding guide in the dictionary
        if spacer_seq in guide_dict.keys():
            guide_dict[spacer_seq] +=1 
    
    # write out results
    count_df = pd.DataFrame(guide_dict.items())
    count_df.columns = ['guide','count']
    count_df.to_csv(args.output, sep = '\t')

if __name__ == "__main__":
    main()