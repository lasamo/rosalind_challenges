def counting_dna_nucleotides(filename):
    dataset = open(filename, 'r').read()
    ct_A = dataset.count('A')
    ct_C = dataset.count('C')
    ct_G = dataset.count('G')
    ct_T = dataset.count('T')
    print(f'{ct_A} {ct_C} {ct_G} {ct_T}')
    return{'A': ct_A, 'C': ct_C, 'G': ct_G, 'T': ct_T}

result = counting_dna_nucleotides('rosalind_dna.txt')