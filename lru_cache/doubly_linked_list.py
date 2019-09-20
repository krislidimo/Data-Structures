"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, key, value, prev=None, next=None):
    self.key = key
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, key, value):
    current_next = self.next
    self.next = ListNode(key, value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, key, value):
    current_prev = self.prev
    self.prev = ListNode(key, value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, key, value):
    if self.length == 0:
      node = ListNode(key, value, None, None)
      self.head = node
      self.tail = node
      self.length += 1
      return node
    elif self.length > 0:
      node = ListNode(key, value, None, self.head)
      self.head.prev = node
      self.head = node
      self.length +=1
      return node
  
  """Removes the List's current head node, making the
  current head's next node the new head of the List.
  Returns the value of the removed Node."""
  def remove_from_head(self):
    removedNodeValue = None

    if self.length == 0:
      pass
    elif self.length == 1:
      removedNodeValue = self.head.value
      self.head = None
      self.tail = None
      self.length = 0
    else:
      removedNodeValue = self.head.value
      self.head = self.head.next
      self.head.prev = None
      self.length -= 1

    return removedNodeValue

  """Wraps the given value in a ListNode and inserts it 
  as the new tail of the list. Don't forget to handle 
  the old tail node's next pointer accordingly."""
  def add_to_tail(self, key, value):
    if self.length == 0:
      node = ListNode(key, value, None, None)
      self.head = node
      self.tail = node
      self.length += 1
    elif self.length > 0:
      node = ListNode(key, value, self.tail, None)
      self.tail.next = node
      self.tail = node
      self.length +=1

  """Removes the List's current tail node, making the 
  current tail's previous node the new tail of the List.
  Returns the value of the removed Node."""
  def remove_from_tail(self):
    removedNodeValue = self.tail.value

    if self.length == 0:
      pass
    elif self.length == 1:
      self.head = None
      self.tail = None
      self.length = 0
    else:
      self.tail = self.tail.prev
      self.tail.next = None
      self.length -= 1

    return removedNodeValue


  """Removes the input node from its current spot in the 
  List and inserts it as the new head node of the List."""
  def move_to_front(self, node):
    if self.length <= 1 or self.head == node:
      pass
    elif self.length > 1 and self.tail == node:
      self.tail = self.tail.prev
      self.tail.next = None
      node.prev = None
      node.next = self.head 
      self.head.prev = node
      self.head = node
    else:
      self.head.prev = node
      node.prev = None
      node.next = self.head
      self.head = node

  """Removes the input node from its current spot in the 
  List and inserts it as the new tail node of the List."""
  def move_to_end(self, node):
    if self.length <= 1 or self.tail == node:
      pass
    elif self.length > 1 and self.head == node:
      self.head = self.head.next
      self.head.prev = None
      node.next = None
      node.prev = self.tail 
      self.tail.next = node
      self.tail = node
    else:
      self.tail.next = node
      node.next = None
      node.prev = self.tail
      self.tail = node

  """Removes a node from the list and handles cases where
  the node was the head or the tail"""
  def delete(self, node):
    if self.length == 1:
      self.head = None
      self.tail = None
    elif self.head == node:
      self.head = node.next
      self.head.prev = None
    elif self.tail == node:
      self.tail = node.prev
      self.tail.next = None
    else: 
      node.next.prev = node.prev
      node.prev.next = node.next
    node.next = None
    node.prev = None
    self.length -= 1
    
  """Returns the highest value currently in the list"""
  def get_max(self):
    maxValue = None

    if self.length == 0:
      pass
    elif self.length == 1:
      maxValue = self.head.value
    else:
      maxValue = self.head.value
      temp = self.head.next
      while temp is not None:
        if temp.value > maxValue:
          maxValue = temp.value
        temp = temp.next

    return maxValue

