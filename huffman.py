from pqueue import PriorityQueue
from math import log2, ceil


class Node(object):
    def __init__(self, data="", left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self, level=0):
        """Return a string representation (of the tree with root self).

        Left-to-right tree-wise is top-to-bottom in the output string.
        Note: For instances of the PrefixCodeTree class below, one can
        read off the map from bitstrings to letters from this string.
        """
        s = "   " * level + str(self.data) + "\n"
        for child in [self.left, self.right]:
            if child is not None:
                s += child.__str__(level + 1)
        return s


class PrefixCodeTree:
    def __init__(self):
        self.root = Node()

    def __str__(self):
        return str(self.root)

    def decode(self, bitstring):
        """Return the human readable string associated to bitstring."""

        #
        # YOUR SOLUTION CODE FROM LAST WEEK'S LAB GOES HERE
        #

    def encode(self, string):
        """Return the bitstring associated to human readable string."""
        get_code(self.root)

        #
        # MORE OF YOUR CODE GOES HERE
        #

bitstring2char = {}

def get_code(node, bitstring=""):
    """Helper function for the encode method above.

    If node is the root of a prefix code tree, then this recursively
    builds the dictionary bitstring2char that maps bitstrings to char-
    acters for that tree.
    """

    #
    # EVEN MORE OF YOUR CODE GOES HERE
    #


class Huffman(PrefixCodeTree):

    def __init__(self, string):
        super().__init__()
        assert string != '', "please encode a non-empty string"

        # get the frequencies of each char in string
        char2freq = {}
        for char in string:
            char2freq[char] = char2freq.setdefault(char, 0) + 1

        # build the Huffman tree:
        if len(char2freq.keys()) == 1:
            self.root = Node("root", Node(list(char2freq.keys())[0]))
        else:
            q = PriorityQueue()
            for char, freq in char2freq.items():
                q.enqueue((freq, Node("`--" + char)))
            while q.length() > 1:
                lfreq, lnode = q.dequeue()
                rfreq, rnode = q.dequeue()
                q.enqueue((lfreq + rfreq, Node("`--", lnode, rnode)))
            self.root = q.dequeue()[1]
            self.root.data = "root"

        self.char2freq = char2freq

    def entropy(self):
        """Return the Shannon entropy and actual average bits per character."""
        n = sum(list(self.char2freq.values()))
        shannon = -sum([f/n*log2(f/n) for f in self.char2freq.values()])
        char2bitstring = {v: k for k, v in bitstring2char.items()}
        average = sum([f*len(char2bitstring[c]) for c,f in self.char2freq.items()])/n
        return shannon, average


if __name__ == "__main__":

    string = 'Aaron said, "I am an aardvark!"'
    tree = Huffman(string)
    print(tree)

    print("encoding:")
    bitstring = tree.encode(string)
    print(bitstring)
    print("decoding:")
    print(tree.decode(bitstring))

    numchars = len(bitstring2char.values())
    print(f"number of distinct characters: {numchars}")
    numbits = ceil(log2(numchars)) # no. of bits required for a fixed-length code
    len1 = len(string) * numbits
    print(f"{numbits}-bits/character length: {len1}")
    len2 = len(tree.encode(string))
    if len1:
        print(f"huffman-encoding length: {len2} ({100*len2/len1:.1f}% of {len1})")

    print("\nentropy:")
    entropy = tree.entropy()
    print(f"Shannon: {entropy[0]:.2f} (information-theoretic lowerbound)")
    print(f"Huffman: {entropy[1]:.2f} average bits per character")
