# Huffman Encoding using Greedy Strategy

class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right


def Huffman_Encoding(data):
    freq = {}

    for ch in data:
        freq[ch] = freq.get(ch, 0) + 1

    print("Symbols:", list(freq.keys()))
    print("Probabilities:", list(freq.values()))

    nodes = []

    for ch in freq:
        nodes.append(Node(freq[ch], ch))

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.prob)

        left = nodes.pop(0)
        right = nodes.pop(0)

        nodes.append(Node(
            left.prob + right.prob,
            left.symbol + right.symbol,
            left, right
        ))

    codes = {}

    def generate(node, code=""):
        if node.left is None and node.right is None:
            codes[node.symbol] = code
        else:
            generate(node.left, code + "0")
            generate(node.right, code + "1")

    generate(nodes[0])

    print("Symbols with codes:", codes)

    encoded = ""

    for ch in data:
        encoded += codes[ch]

    print("Space before compression:", len(data) * 8, "bits")
    print("Space after compression:", len(encoded), "bits")
    print("Encoded output:", encoded)


data = "AAAAAAABCCCCCCDDDEEEEE"
print(data)

Huffman_Encoding(data)
