#
# I found this exercise on Rosalind. Rosalind is a platform for learning
# bioinformatics through problem solving.
#
# This is my solution to the following problem:
#
# Given:  A DNA string s of length at most 1000 nt.
# Return: Four integers (separated by spaces) counting
#         the respective number of times that the symbols
#         'A', 'C', 'G', and 'T' occur in s.

s = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

def count_symbols(s):
    """ PRE: all symbols in s are an element of set ('A','C','G','T')
    """
    count = { 'A':0, 'C':0, 'G':0, 'T':0, }
    
    for i in xrange(len(s)):
        count[s[i]] += 1
    
    return "%d %d %d %d" % (count['A'], count['C'], count['G'], count['T'])

print count_symbols(s)
