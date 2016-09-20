
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

def generate_node_list(freq_table):
    node_list = []
    sorted_freq_list = sorted(freq_table, key=freq_table.get, reverse=True)
    for i in sorted_freq_list:
        new_node = Tree()
        new_node.key = i
        new_node.value = freq_table[i]
        node_list.append(new_node)
    return node_list

def get_encoded_string(input_text):
    encoded_string = ""
    for c in input_text:
        encoded_string += str(code_table[c])

    return encoded_string

def get_efficiency(original_string, encoded_string):
    return (1 - ((len(encoded_string)/(len(original_string)*16)))) * 100

def print_node(tree, tabs):
    if(tree.key == ''):
        print(str('\t' * tabs) + "* : " + str(tree.value))
    else:
        print(str('\t' * tabs) + str(tree.key) +" : " + str(tree.value))

def print_tree(tree, level=0):
    if(tree is not None):
        print_node(tree, level)
        print_tree(tree.left, level+1)
        print_tree(tree.right, level+1)


print("Inserte nombre de archivo a codificar: ")
file_name = input()

with open(file_name) as f:
    input_text = f.read()

input_text = str(input_text)
node_list = generate_node_list(generate_freq_table(input_text))
tree = generate_huffman_tree(node_list)
generate_huffman_code(tree)

print("\nOriginal text:")
print (input_text)
print("\nCode table:")
print(code_table)
print("\nEncoded string:")
print(get_encoded_string(input_text))
print("\nEfficiency:")
print(str(get_efficiency(input_text, get_encoded_string(input_text))) + "%")

print_tree(tree)
