import heapq
from collections import Counter

class Node:
    def __init__(self,char,freq):

        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self,other):
        return self.freq < other.freq

def build_huffman_tree(freq_dict):
    heap = [Node(char,freq) for char,freq in freq_dict.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        combined = Node(None,left.freq + right.freq)
        combined.left = left
        combined.right = right
        heapq.heappush(heap,combined)

    return heap[0]

def generate_huffman_codes(node,current_code,huffman_codes):

    if node is None:
        return
    
    generate_huffman_codes(node.left,current_code+'0',huffman_codes)
    generate_huffman_codes(node.right,current_code+'1',huffman_codes)

    if node.char is not None:
        huffman_codes[node.char] = current_code


def main():

    file_name = 'huffman.txt'

    with open(file_name,'r') as file:
        text = file.read()

    freq_dict = Counter(text)       # The Counter class creates a dictionary-like object with the elements as keys and their frequencies as values.
    node = build_huffman_tree(freq_dict)

    huffman_codes = {}
    generate_huffman_codes(node,'',huffman_codes)

    print("Frequencies of Symbols: ")
    for char,freq in freq_dict.items():
        print(f"{char} => {freq}")

    print("\nEncoded Symbols: ")
    for char,code in huffman_codes.items():
        print(f"{char} => {code}")

main()
