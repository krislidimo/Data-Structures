import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList



class LRUCache:
  """
  Our LRUCache class keeps track of the max number of nodes it
  can hold, the current number of nodes it is holding, a doubly-
  linked list that holds the key-value entries in the correct 
  order, as well as a storage dict that provides fast access
  to every node stored in the cache.
  """
  def __init__(self, limit=10):
    self.limit = limit
    self.size = 0
    self.dll = DoublyLinkedList()
    self.storage = {}

  """
  Retrieves the value associated with the given key. Also
  needs to move the key-value pair to the end of the order
  such that the pair is considered most-recently used.
  Returns the value associated with the key or None if the
  key-value pair doesn't exist in the cache. 
  """
  def get(self, key):
    if key not in self.storage.keys():
      return None
    else:
      currentNode = self.dll.head
      while self.dll.head is not None and self.dll.head.key != key:
        currentNode = currentNode.next
      self.dll.move_to_front(currentNode)

      return self.storage.key
  """
  Adds the given key-value pair to the cache. The newly-
  added pair should be considered the most-recently used
  entry in the cache. If the cache is already at max capacity
  before this entry is added, then the oldest entry in the
  cache needs to be removed to make room. Additionally, in the
  case that the key already exists in the cache, we simply 
  want to overwrite the old value associated with the key with
  the newly-specified value. 
  """
  def set(self, key, value):
    if key not in self.storage.keys(): # key dosn't exist, set new key
      self.storage.update({key:value})
      self.dll.add_to_head(key, value)
    else: # key exist, update key
      if self.storage[key] != value:
        self.storage[key] = value;

        currentNode = self.dll.head
        while currentNode is not None and self.dll.head.key != key:
          currentNode = currentNode.next
        self.dll.move_to_front(currentNode)

    if self.size > self.limit:
      del self.storage[self.dll.tail.key]
      self.dll.remove_from_tail()