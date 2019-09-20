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

  def for_each_helper(self, cb, node):
    cb(node.value)
    if node.left:
      self.for_each_helper(cb, node.left)
    if node.right:
      self.for_each_helper(cb, node.right)

  # Call the function `cb` on the value of each node
  # You may use a recursive or iterative approach
  def for_each(self, cb):
    self.for_each_helper(cb, self.root)

 # DAY 2 Project -----------------------

  #                Stack    
  #      4         |   |\
  #    /   \       | 6 |     Queue
  #   2     6      | 2 |    >-------------->
  #  / \   / \    \| 4 |      7 5 3 1 6 2 4
  # 1   3 5   7    -----    >-------------->              

  # Print all the values in order from low to high
  # Hint:  Use a recursive, depth first traversal
  def in_order_print(self, node):
    if node is not None:
      self.in_order_print(node.left)
      print(node.value)
      self.in_order_print(node.right)

  # Print the value of every node, starting with the given node,
  # in an iterative breadth first traversal
  def bft_print(self, node):
    q = Queue()
    q.enqueue(node)
    while q.len() > 0:
      current = q.dequeue()
      print(current.value)
      current.left and q.enqueue(current.left)
      current.right and q.enqueue(current.right)


  # Print the value of every node, starting with the given node,
  # in an iterative depth first traversal
  def dft_print(self, node):
    stack = Stack()
    stack.push(node)
    while stack.len() > 0:
      current = stack.pop()
      print(current.value)
      current.left and stack.push(current.left)
      current.right and stack.push(current.right)

  # STRETCH Goals -------------------------
  # Note: Research may be required

  # Print In-order recursive DFT
  def pre_order_dft(self, node):
    if node is not None:
      print(node.value)
      self.pre_order_dft(node.left)
      self.pre_order_dft(node.right)

  # Print Post-order recursive DFT
  def post_order_dft(self, node):
    if node is not None:
      self.post_order_dft(node.left)
      self.post_order_dft(node.right)
      print(node.value)