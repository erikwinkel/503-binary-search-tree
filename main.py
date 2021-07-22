from BinaryTree import Node
from BinaryTree import BinaryTree

my_node = Node('hello')

my_bst = BinaryTree()
my_bst.insert(10)
my_bst.insert(12)
my_bst.insert(8)
my_bst.insert(15)
my_bst.insert(9)
my_bst.insert(3)
my_bst.insert(21)
my_bst.insert(7)

print(my_bst.size(my_bst.root))
