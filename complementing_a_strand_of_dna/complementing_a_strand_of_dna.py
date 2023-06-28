def complementing_a_strand_of_dna(filename):
    dataset = open(filename, 'r').read()
    complementary_strand = dataset[::-1]
    temp = ''
    for nucleotide in complementary_strand:
        if nucleotide == 'A':
            temp += 'T'
        elif nucleotide == 'T':
            temp += 'A'
        elif nucleotide == 'C':
            temp += 'G'
        elif nucleotide == 'G':
            temp += 'C'
        else:
            pass
    complementary_strand = temp
    return complementary_strand

print(complementing_a_strand_of_dna('rosalind_revc.txt'))