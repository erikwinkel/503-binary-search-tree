class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return f'{self.data}'


class BinaryTree:
  # here we will add the constructor
  def __init__(self):
      self.root = None

  def insert(self, data):
    '''
      Insert(data: any) -> None:\n 
      creates a new Node from the data passed in and adds it to the tree
      If the data is already in the tree, does not insert it again
    '''
    # make a node from the data
    new_node = Node(data)

    # if there is no root, set node as root
    if not self.root:
        self.root = new_node
        return

    # loop over tree starting at root
    current_node = self.root
    while current_node:
        if new_node.data < current_node.data:
            if not current_node.left:
                current_node.left = new_node
                return
            else:
                current_node = current_node.left
        elif new_node.data > current_node.data:
            if not current_node.right:
                current_node.right = new_node
                return
            else:
                current_node = current_node.right
        else:
            return

  def search(self, val):
    '''
      search(value: any) -> value or bool:\n 
      Performs depth first search
      Search the Tree for a node with the given value
      If the node exists, return it
      If the node doesn't exist, return false
    '''
    current_node = self.root
    while current_node:
        if val < current_node.data:
            current_node = current_node.left
        elif val > current_node.data:
            current_node = current_node.right
        else:
            return current_node
    return False

  def print(self, node=None):
    '''
      print(node=optional: Node) -> None:\n
      prints out all values recursively (in a breadth first search fashion)
      defualt start is at root node
    '''
    # check if this is the first recursion
    if not node:
        node = self.root

    # print node

    if node.left:
        self.print(node.left)
    print(node)
    if node.right:
        self.print(node.right)
    
  def print_BFS(self, node):
      if not node:
          return

      queue = []

      queue.append(node)

      while(len(queue) > 0):
          print(queue[0].data)
          node = queue.pop(0)

          if node.left is not None:
              queue.append(node.left)

  def size(self, node=None):
    '''
      size(node=optional: Node) -> int:\n 
      performs breadth first search
      Calculate the number of nodes in the tree, starting from the given node
      If no node is provided, we can use the root as a sensible default
    '''
    if not node:
        return 0
    else:
        return 1 + self.size(node.left) + self.size(node.right)

  def height(self, node=None):
    '''
      height(node=optional: Node) -> int:\n 
      perform breadth first search
      Calculate the maximum amount of nodes in any one path from the given node
      If not given a specific node, default to using the root node
    '''
    if not node: return 0
    left_count = 1 + self.height(node.left)
    right_count = 1 + self.height(node.right)
    if left_count > right_count:
        return left_count
    else: return right_count

  def get_max(self):
    '''
      getMax() -> int:\n 
      perform depth first search
      Calculate the maximum value held in the tree
    '''
    if not self.root: return None

    current_node = self.root
    while current_node.right:
        current_node = current_node.right
    return current_node.data

  def get_min(self):
    '''
      getMin() -> int:\n 
      perform depth first search
      Calculate the minimum value held in the tree
    '''
    if not self.root: return None

    current_node = self.root
    while current_node.left:
        current_node = current_node.left
    return current_node.data
