from huffman import Huffman
from math import log2, ceil

#
#  YOUR CODE THAT READS mobydick.txt INTO
#  A STRING CALLED string GOES HERE.
#

tree = Huffman(string)

numchars = len(set(string))
print(f"number of distinct characters: {numchars}")
numbits = ceil(log2(numchars)) # no. of bits required for a fixed-length code
len1 = len(string) * numbits
print(f"{numbits}-bits/character length: {len1}")
len2 = len(tree.encode(string))
print(f"huffman-encoding length: {len2} ({100*len2/len1:.1f}% of {len1})")

print("\nentropy:")
entropy = tree.entropy()
print(f"Shannon: {entropy[0]:.2f} (information-theoretic lowerbound)")
print(f"Huffman: {entropy[1]:.2f} average bits/character")
