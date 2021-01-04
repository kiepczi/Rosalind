# counting nucleotides from a string

s = open("rosalind_dna.txt")

for nucleotides in s:
    print(nucleotides.count('A'), 
          nucleotides.count('C'), 
          nucleotides.count('G'), 
          nucleotides.count('T'))



# counting nucleotides from a fasta

from Bio import SeqIO

def counting_nucleotide(fasta_file, nucleotide):
    """Counts nucleotide usage for a given fasta file.
    """
    
    fasta_seq = SeqIO.parse(fasta_file, 'fasta')
    
    n = nucleotide
    n_count = 0
    for seq in fasta_seq:
        for char in seq:
            if char in nucleotide:
                n_count += 1
    return print(n_count)

counting_nucleotide('sequence.fasta', 'A')
counting_nucleotide('sequence.fasta', 'C')
counting_nucleotide('sequence.fasta', 'G')
counting_nucleotide('sequence.fasta', 'T')