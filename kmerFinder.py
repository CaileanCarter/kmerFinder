#A script which takes a FASTQ file and makes a hash table of k-mers and orders them in frequency
from Bio.SeqIO.QualityIO import FastqGeneralIterator
import collections
import sys

#summary holds key information about the FASTQ file and the data pulled from it. This will be outputted in the Report Summary
summary = collections.defaultdict(int)

#kmer holds all the kmers and the counts in a Counter dict subclass
kmer = collections.Counter()

#wonder what search does? It searches for k-mers.          
def search():
    find = input().lower()
    if find == "exit" or find == "stop":
        sys.exit()
    print("%s  count: %i" % (find, kmer[find]))
    search()

#start
if __name__ == "__main__":
    

    print("""k-mer Finder v1.0   15/02/2020 

k-mer Finder identifies the k-mers from a FASTQ file. 
    
Please answer the following questions
""")

    path = input("Please enter the file path with file extension:  ")

    print("""
Reading FASTQ file...""")
    if path[-5:].upper() != "FASTQ" and path[-3:].upper() != "TXT":
        print("Error: file is not supported...")
        sys.exit()
    print("Done")

    minKMER = int(input("What will be the minimum k-mer size?:  "))
    if minKMER < 1: #some simple error management
        print("Minimum K-mer cannot be less than one...")
        sys.exit()
        
    maxKMER = int(input("What will be the maximum k-mer size?:  "))
    if maxKMER < minKMER: #some simple error management
        print("Maximum K-mer size cannot be smaller than minimum K-mer size")
        sys.exit()
        

    print("""
Your FASTQ file is now being processed. Depending on the file size this may take a while.
Thank you for your patience.
""")

    print("Finding k-mers...")

    #this block takes all the reads and passes them through the kmer finder
    for title, rec, qual in FastqGeneralIterator(path):
            summary["Total records"] += 1
            summary["Total sequence length (bp)"] += len(rec)

            [[kmer.update([str(rec[i:i+mer])]) for i in range(0, len(rec)-mer, 1)] for mer in range(minKMER, maxKMER+1)]

    summary["k-mer total"] = sum(kmer.values())

    print("Done")

    print("Building report summary...")

    print("""
__________________________
Report Summary
""")

    [print("%s:  %i" % (key, element)) for key, element in zip(summary.keys(), summary.values())]
        
    #this block is a bit of error management
    if len(kmer) == 0:
        print("k-mer total:  0")
        print("Error: No k-mers found")
        sys.exit()
    
    print("""
__________________________
Fifteen most common K-mers: 
""")
    
    [print("%s  count: %i" % (a,b)) for (a, b) in kmer.most_common(15)]
    
    print("""
________________________________________________
Type a k-mer sequence to see how often it occurs""")
    search()
