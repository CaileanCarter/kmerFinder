# kmerFinder

Identifies k-mers from a DNA sequence in a FASTQ file format and returns the five most common k-mers. Allows for user searches of k-mers. 

When the script is run, the user is given a brief description of the script and is asked to answer the following questions:

1. What is the FASTQ file path?

2. What is the minimum k-mer size?

3. What is the maximum k-mer size?

k-mers are held in a Counter dictionary which counts the occurrence of the key. From there, a report is generated which shows the total number of kmers in the FASTQ file and the total length of reads in the FASTQ file. The output then provides a list of the 15 most commonly occurring k-mers. The script ends with a user input to find how often a user-specified k-mer occurs by typing their chosen sequence.

 