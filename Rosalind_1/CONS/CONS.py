#Set up
from Bio import motifs
from Bio import SeqIO
from Bio.SeqRecord import SeqRecord

# Loading data
fasta_seq = SeqIO.parse('rosalind_cons.fasta', 'fasta')

# Consensus and Profile
for record in fasta_seq:
    instances = SeqRecord(record.seq)
    motif = motifs.create(instances)
    print(motif.consensus)
    print(motif.counts)

    