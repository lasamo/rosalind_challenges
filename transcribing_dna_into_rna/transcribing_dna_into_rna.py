def transcribing_dna_into_rna(filename):
    dataset = open(filename, 'r').read()
    rna_string = dataset.replace('T', 'U')
    return rna_string

result = transcribing_dna_into_rna('rosalind_rna.txt')

print(result)