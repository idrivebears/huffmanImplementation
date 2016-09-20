import tkinter

code_table = {}

class Tree(object):
    def __init__(self):
        self.key = ''
        self.value = 0   #frequency
        self.right = None
        self.left = None

    def __lt__(self, other):
        if(self.value < other.value):
            return True

def generate_freq_table(text):
    freq_table = {}

    for c in input_text:
        if c in freq_table:
            # Update key's value on table
            freq_table[c] = freq_table[c] + 1
        else:
            # Add key to table
            freq_table[c] = 1
    return freq_table

def print_node_list(list):
    for n in list:
        print (str(n.key) + ":" + str(n.value))

# Given a sorted list of nodes, build the huffman tree
# sorted = smallest items at beginning of queue
def generate_huffman_tree(node_list):
    while(len(node_list) >= 2):
        #Take first two items and merge
        node1 = node_list.pop()
        node2 = node_list.pop()
        #Create new node
        new_node = Tree()
        new_node.value = node1.value + node2.value # Sum of frequencies
        new_node.left = node1
        new_node.right = node2
        # insert node into tree
        node_list.append(new_node)
        # "priority queue"
        node_list.sort()
        node_list.reverse()
    return node_list.pop()

def generate_huffman_code(tree, code=""):
    if(tree.left is None and tree.right is None):
        # Leaf
        code_table[tree.key] = code
    else:
        generate_huffman_code(tree.left, code+"0")
        generate_huffman_code(tree.right, code+"1")

# :::::::::User interaction:::::::
print("Please enter a text to be coded:")
input_text = input()

print("Now coding: " + input_text + "...")

# Sort dictionary by frequency into a list
freq_table = generate_freq_table(input_text)
sorted_freq_list = sorted(freq_table, key=freq_table.get, reverse=True)

# Will contain list of nodes to convert into tree
node_list = []

# Create nodes and add to a list
for i in sorted_freq_list:
    new_node = Tree()
    new_node.key = i
    new_node.value = freq_table[i]
    node_list.append(new_node)

tree = generate_huffman_tree(node_list)

generate_huffman_code(tree)
'''
print("Code table:")
print(code_table)
print("Encoded string:")
for c in input_text:
    print(code_table[c], end = '')
'''
