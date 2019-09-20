import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
  def __init__(self):
    self.size = 0
    # Why is our DLL a good choice to store our elements?
    self.storage = DoublyLinkedList()

  def push(self, value):
    self.storage.add_to_head(value)
    self.size = self.storage.length
  
  def pop(self):
    removed = self.storage.remove_from_head()
    self.size = self.storage.length
    return removed

  def len(self):
    return self.size
