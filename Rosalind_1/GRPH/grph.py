from Bio import SeqIO



def overlap_edges(data, length):
    """Takes FASTA file as input and returns
    names of sequences that have overalped edges
    at specified length. 
    """
    records = list(SeqIO.parse(data, "fasta"))
    for record_1 in records:
        for record_2 in records:
            name_1, seq_1 = record_1.id, record_1.seq
            name_2, seq_2 = record_2.id, record_2.seq
            if seq_1 == seq_2:
                continue
            sx = seq_1[-length:]
            px = seq_2[:length]
            if px == sx:
                overlaps = print(name_1, name_2)
    return overlaps


overlap_edges("grph.fasta", 3)