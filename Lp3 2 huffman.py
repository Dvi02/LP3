
class Node:
    def __init__(self, prob, symbol, left=None, right=None):
        self.prob = prob
        self.symbol = symbol
        self.left = left
        self.right = right
        self.code = ""


# Calculate the frequency of each symbol
def Calculate_Probability(data):
    symbols = {}
    for element in data:
        symbols[element] = symbols.get(element, 0) + 1
    return symbols


# Generate Huffman codes
def Calculate_Codes(node, current_code="", coding=None):
    if coding is None:
        coding = {}

    if node.left is None and node.right is None:
        coding[node.symbol] = current_code or "0"
        return coding

    Calculate_Codes(node.left, current_code + "0", coding)
    Calculate_Codes(node.right, current_code + "1", coding)
    return coding


# Encode the input data
def Output_Encoded(data, coding):
    encoding_output = []
    for char in data:
        encoding_output.append(coding[char])
    return "".join(encoding_output)


# Calculate space usage before and after compression
def Total_Gain(data, coding):
    before_compression = len(data) * 8
    after_compression = sum(
        data.count(symbol) * len(coding[symbol])
        for symbol in coding
    )

    print("Space usage before compression (in bits):", before_compression)
    print("Space usage after compression (in bits):", after_compression)


# Huffman Encoding using a greedy strategy
def Huffman_Encoding(data):
    symbol_probs = Calculate_Probability(data)

    print("Symbols:", list(symbol_probs.keys()))
    print("Probabilities:", list(symbol_probs.values()))

    nodes = [
        Node(freq, symbol)
        for symbol, freq in symbol_probs.items()
    ]

    while len(nodes) > 1:
        # Select the two nodes with the smallest frequencies
        nodes = sorted(nodes, key=lambda x: x.prob)

        left = nodes.pop(0)
        right = nodes.pop(0)

        left.code = "0"
        right.code = "1"

        # Combine the two smallest nodes
        new_node = Node(
            left.prob + right.prob,
            left.symbol + right.symbol,
            left,
            right
        )

        nodes.append(new_node)

    huffman_encoding = Calculate_Codes(nodes[0])
    print("Huffman codes:", huffman_encoding)

    Total_Gain(data, huffman_encoding)

    encoded_output = Output_Encoded(data, huffman_encoding)
    print("Encoded output:", encoded_output)

    return encoded_output, huffman_encoding


# Main program
data = input("Enter the string to encode: ")

if data:
    encoded_output, huffman_encoding = Huffman_Encoding(data)
else:
    print("Please enter a non-empty string.")
