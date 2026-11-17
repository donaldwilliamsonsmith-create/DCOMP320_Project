import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
        
    return heap[0]

def generate_codes(node, current_code="", codes=None):
    if codes is None:
        codes = {}
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
    return codes

if __name__ == "__main__":
    # Given symbols and frequencies: a: 2, b: 4, c: 8, d: 16, e: 16
    frequencies = {'a': 2, 'b': 4, 'c': 8, 'd': 16, 'e': 16}
    
    root = build_huffman_tree(frequencies)
    huffman_codes = generate_codes(root)
    
    print("--- Huffman Coding Results ---")
    for char, code in huffman_codes.items():
        print(f"Symbol '{char}': Code -> {code}")
        
    total_bits = sum(frequencies[char] * len(code) for char, code in huffman_codes.items())
    print(f"Total encoded string length: {total_bits} bits") 