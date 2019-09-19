import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack

class bNode:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

  def __str__(self):
    return f'\n--------------\n' \
      f'value: {self.value}\n' \
      f'left: \t{self.left}\n' \
      f'right: \t{self.right}\n' \
      '--------------\n' 

class BinarySearchTree:
  def __init__(self, rootValue):
    self.root = bNode(rootValue)

  def insertHelper(self, value, node):
    target = node.left if node.value > value else node.right
    if target == None:
      if node.value > value:
        node.left = bNode(value)
      else:
        node.right = bNode(value)
      return value
    else:
      return self.insertHelper(value, target)

  def containsHelper(self, value, node):
    target = node.left if node.value > value else node.right
    if (target == None) or (target.value == value):
      return True if target and target.value == value else False
    else:
      return self.containsHelper(value, target)

  def getMaxHelper(self, node):
    target = node.right
    if target == None:
      return node.value
    else:
      return self.getMaxHelper(target)

  # Insert the given value into the tree
  def insert(self, value):
    return self.insertHelper(value, self.root)

  # Return True if the tree contains the value
  # False if it does not
  def contains(self, value):
    return self.containsHelper(value, self.root)

  # Return the maximum value found in the tree
  def get_max(self):
    return self.getMaxHelper(self.root)

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def for_each(self, cb):
    cb(self.value)
    if self.left:
      self.left.for_each(cb)
    if self.right:
      self.right.for_each(cb)

 # DAY 2 Project -----------------------

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self, node):
    pass

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    pass

  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    pass

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    pass

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    pass

# bst = BinarySearchTree(5)

# print(bst.insert(2))
# print(bst.insert(3))
# print(bst.insert(7))
# print(bst.insert(6))
# print(bst.contains(9))
# print(bst.get_max())
# print(bst.root.left.right.value)
# print(bst.root)
