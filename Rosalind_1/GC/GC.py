#Set up
from Bio.Seq import Seq
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

#Loading file
records =  SeqIO.parse("rosalind_gc.fasta", "fasta")

#Calculating GC content
for record in records:
    percentage = (100*(
        (record.seq.count('G') 
         + record.seq.count('C'))))/ len(record.seq)
    print(f'{record.name} {percentage:.6f}')