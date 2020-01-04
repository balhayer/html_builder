"""
Queue implementation built on top of nodes.
file: cs_queue.py
authors: CS @ rit.edu and Vishnu Muthuswamy

This is Queue datatype implemented by a mutable linked node sequence.
"""

from website_part_node import Node
from dataclasses import dataclass
from typing import Union

@dataclass
class Queue:
    size: int
    front: Union[None, 'Node']
    back: Union[None, 'Node']

def make_empty_queue():
    """
    Returns a new queue with size initialized to zero and
    the front and back fields initialized to the empty sequence.
    """
    return Queue(0, None, None)

def enqueue(queue, contents):
    """
    Insert an element into the back of the queue. (Returns None)
    """
    newnode = Node(contents, None)
    if is_empty(queue):
        queue.front = newnode
    else:
        queue.back.rest = newnode
    queue.back = newnode
    queue.size = queue.size + 1
    
def dequeue(queue):
    """
    Remove the front element from the queue. (returns removed value)
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("dequeue on empty queue") 
    removed = queue.front.contents
    queue.front = queue.front.rest
    if is_empty(queue):
        queue.back = None
    queue.size = queue.size - 1
    return removed
    
def front(queue):
    """
    Access and return the first element in the queue without removing it.
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("front on empty queue") 
    return queue.front.contents
    
def back(queue):
    """
    Access and return the last element in the queue without removing it
    precondition: queue is not empty.
    """
    if is_empty(queue):
        raise IndexError("back on empty queue") 
    return queue.back.contents
    
def is_empty(queue):
    """
    Is the queue empty?
    """
    return queue.front is None

