# Epic_demo
Solution to Epic Bio's technical interview question

## Problem description
#### Input:
- 3' scaffold sequence: GTTTAAGAGCTAAGCTGGAAACAGCATAGCAAGTTTAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT;
- Promoter sequence: TTTTTTG;
- text file of spacer sequences: guide_RNA_seq.txt;
- fastq files of sequenced guide RNAs: sequenced_guides.fastq. We can assume that we are only working with the actual sequence parts of the fastq files and ignore quality scores.

A sequenced guide RNA should (in theory) have the promoter sequence followed by the spacer sequence, then the 3' scaffold sequence, flanked on other sides by other stuff. This other stuff doesn’t matter but is sequenced anyways because the length of the promoter + spacer + scaffold is much smaller than the length of a standard read. As an aside, this is not exactly how most CRISPR screening data will look like but the problem will help to give insight into evaluating how the candidate responds to new problems.

An example of a functional guide RNA and a sequenced read corresponding to the spacer.

<img width="458" alt="Screen Shot 2023-06-03 at 7 17 00 AM" src="https://github.com/norakearns/Epic_demo/assets/59736592/914a5acf-b241-4689-b77a-222f886e1360">

The goal of the problem is to produce a count of the number of times each spacer is sequenced. Note that each sequenced read should only have one spacer.

## Data

- a text file of spacer sequences, each 20 base pairs long
```
! head guide_RNA_seq.txt
AAGTGAGCTCTTACGGGAAT
GAATGTAGTTTTAGCCCTCC
GGGATTCTATTTAGCCCGCC
TCTGATGATACCCATGCCAC
AGATTCACAGAGGCAACCTG
GGCACAGCTCTCCTAGCCTG
ATGCTTTAAAAAGACCTCTC
AAGGATAGAGCTTCGCAGAA
GCATTTTGATTAACGAATGT
AGACTCTAGGTCGGACGGGC
```
- fastq file of sequenced guides (simulated) that correspond to the output of the (theoretical experiment).

```
! head -12 sequenced_guides.fastq
@CP009257.1_0_0/1
AGCTAAACTCAATGTAAATGCACAAAATAATTGGTTAAATCCTGTTAGTCGAGAAATTCAGTCAACTACACCACTCCGTTTGAGTTTTTCAAATAATCCAAACGAAGATCTACAGATTTATCAAGG
+
BBBBBFFFFF<FFFFFFFFFFFFFFFFFBFF<FFFBFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFFF<FFFBBFFFFFFFFF/FFFFFFF<FFFF<
@CP009257.1_1_0/1
TGTGTGCTCAAGTTTTTTTGAAGTGAGCTCTTACGGGAATGTTTAAGAGCTAAGCTGGAAACAGCATAGCAAGTTTAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT
+
BBBBBFFFFFFFFFF<FFFFFFFFFFFFFFF/FFFFFFFFFFFFFFFFFFFFFFFFFFFFBFFBFFFFFFFFFFFFFFFFF<FFFBFB/<FBFFFFFFFFBFBFF/FFFFFFFFBFBFFFFFBFFF
@CP009257.1_2_0/1
AATGTATCGTTTTTTGGCTTAAGTCACTGCAGCCAGGTTTAAGAGCTAAGCTGGAAACAGCATAGCAAGTTTAAATAAGGCTAGTCCGTTATCAACTTGAAAAAGTGGCACCGAGTCGGTGCTTTTTTT
+
BBBBBFFFFFFFFFFFFFFFFFFFFFFFFFBBFFFFFFFFFFFFFF/FFFFFFFFFFBFFFF<FFBFFFFFFFFFFFFFF<FFBFFFFFFFFFFFFFBFFFFF<FBFFFFFFFFFFFFFFFFFFFF

```

