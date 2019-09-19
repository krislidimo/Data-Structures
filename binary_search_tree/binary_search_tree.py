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

  def insert(self, value):
    return self.insertHelper(value, self.root)

  def contains(self, value):
    return self.containsHelper(value, self.root)

  def get_max(self):
    return self.getMaxHelper(self.root)

  def for_each(self, cb):
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
