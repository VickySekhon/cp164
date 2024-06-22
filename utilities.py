"""
-------------------------------------------------------
[Utilities Data Structure]
-------------------------------------------------------
Author:  Vicky Sekhon
ID:      169024498
Email:   sekh4498@mylaurier.ca
__updated__ = "2023-01-28"
-------------------------------------------------------
"""

from Stack_array import Stack
from Queue_array import Queue
from Priority_Queue_array import Priority_Queue
from List_array import List

def array_to_stack(stack, source):
    """
    -------------------------------------------------------
    Pushes contents of source onto stack. At finish, source is empty.
    Last value in source is at bottom of stack,
    first value in source is on top of stack.
    Use: array_to_stack(stack, source)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(source) != 0:
        stack.push(source.pop())
        
    return


def stack_to_array(stack, target):
    """
    -------------------------------------------------------
    Pops contents of stack into target. At finish, stack is empty.
    Top value of stack is at end of target,
    bottom value of stack is at beginning of target.
    Use: stack_to_array(stack, target)
    -------------------------------------------------------
    Parameters:
        stack - a Stack object (Stack)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    
    while not stack.is_empty():
        target.append(stack.pop())
    
    return


def stack_test(source):
    """
    -------------------------------------------------------
    Tests the methods of Stack for empty and
    non-empty stacks using the data in source:
    is_empty, push, pop, peek
    (Testing pop and peek while empty throws exceptions)
    Use: stack_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """

    stack = Stack()

    print(f"The stack is empty: {stack.is_empty()}")

    for i in source:
        stack.push(i)
        # print(f"Stack after pushing objects: {stack._i}")

    while not stack.is_empty():
        print(f"Peek at the top object: {stack.peek()}")
        print(f"The popped object: {stack.pop()}")

    print(f"The stack is empty: {stack.is_empty()}")


    return 



def array_to_queue(queue, source):
    """
    -------------------------------------------------------
    Inserts contents of source into queue. At finish, source is empty.
    Last value in source is at rear of queue,
    first value in source is at front of queue.
    Use: array_to_queue(queue, source)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) != 0:
        val = source.pop(0)
        queue.insert(val)
    
    return

def queue_to_array(queue, target):
    """
    -------------------------------------------------------
    Removes contents of queue into target. At finish, queue is empty.
    Front value of queue is at front of target,
    rear value of queue is at end of target.
    Use: queue_to_array(queue, target)
    -------------------------------------------------------
    Parameters:
        queue - a Queue object (Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while not queue.is_empty():
        val = queue.remove()
        target.append(val)
        
    return 

def queue_test(a):
    """
    -------------------------------------------------------
    Tests queue implementation.
  Tests the methods of Queue are tested for both empty and
  non-empty queues using the data in a:
        is_empty, insert, remove, peek, len
    Use: queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    q = Queue()

    # tests for the queue methods go here
   
    # is empty
    queue_is_empty = q.is_empty()
    
    # insert
    value = input("Enter value to add to queue: ")
    q.insert(value)
    
    # remove
    value_removed = q.remove()
    
    # peek 
    value_peeked = q.peek()
    
    # length
    length_of_queue = len(q)
    
    # print the results of the method calls and verify by hand
    print(f"Is the queue is empty: {queue_is_empty}")
    
    print(f"The values in the queue: {q._values}")
    
    print(f"The value removed from the queue: {value_removed}")
    
    print(f"The value at index 0 of the queue: {value_peeked}")
    
    print(f"The number of values in the queue: {length_of_queue}")
    
    return


def array_to_pq(pq, source):
    """
    -------------------------------------------------------
    Inserts contents of source into pq. At finish, source is empty.
    Last value in source is at rear of pq,
    first value in source is at front of pq.
    Use: array_to_pq(pq, source)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while len(source) != 0:
        val = source.pop(0)
        pq.insert(val)
    
    return
        
        

def pq_to_array(pq, target):
    """
    -------------------------------------------------------
    Removes contents of pq into target. At finish, pq is empty.
    Highest priority value in pq is at front of target,
    lowest priority value in pq is at end of target.
    Use: pq_to_array(pq, target)
    -------------------------------------------------------
    Parameters:
        pq - a Priority_Queue object (Priority_Queue)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """

    while not pq.is_empty():
        val = pq.remove()
        target.append(val)
        
    return 

def priority_queue_test(a):
    """
    -------------------------------------------------------
    Tests priority queue implementation.
    Test the methods of Priority_Queue are tested for both empty and
    non-empty priority queues using the data in a:
        is_empty, insert, remove, peek
    Use: priority_queue_test(a)
    -------------------------------------------------------
    Parameters:
        a - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    
    a = []
    pq = Priority_Queue()
    
    # tests for the priority queue methods go here
    pq_is_empty = pq.is_empty()
    a.append(f"The priority queue is empty: {pq_is_empty}")
    
    value = input("Enter value to add to priority queue")
    pq.insert(value)
    a.append(f"The values inside the priority queue: {pq._values}")
    
    
    pq_value = pq.remove()
    a.append(f"The value removed from the priority queue: {pq_value}")
    
    
    pq_peek = pq.peek()
    a.append(f"The first value of the priority queue: {pq_peek}")
    
    
    # print the results of the method calls and verify by hand
    print(f"Is the priority empty: {pq_is_empty}")
    
    print(f"The values in the priority queue: {pq._values}")
    
    print(f"The value removed from the priority queue: {pq_value}")
    
    print(f"The first value of the priority queue is: {pq_peek}")
    
    return



def array_to_list(llist, source):
    """
    -------------------------------------------------------
    Appends contests of source to llist. At finish, source is empty.
    Last element in source is at rear of llist,
    first element in source is at front of llist.
    Use: array_to_list(llist, source)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        source - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    for value in source:
        llist.append(value)
    source.clear()
    
    return 

def list_to_array(llist, target):
    """
    -------------------------------------------------------
    Removes contents of llist into target. At finish, llist is empty.
    Front element of llist is at front of target,
    rear element of llist is at rear of target.
    Use: list_to_array(llist, target)
    -------------------------------------------------------
    Parameters:
        llist - a List object (List)
        target - a Python list (list)
    Returns:
        None
    -------------------------------------------------------
    """
    
    while len(llist) > 0:
        target.append(llist.pop(0))
    return


def list_test(source):
    """
    -------------------------------------------------------
    Tests List implementation.
    The methods of List are tested for both empty and
    non-empty lists using the data in source
    Use: list_test(source)
    -------------------------------------------------------
    Parameters:
        source - list of data (list of ?)
    Returns:
        None
    -------------------------------------------------------
    """
    lst = List()

    print("Test is_empty:")
    print("List is empty:", lst.is_empty())
    print("List is not empty:", not lst.is_empty())
    
    print("\nTest insert:")
    for value in source:
        lst.insert(value)
    print("List after inserts:", lst)
    
    print("\nTest index:")
    for i, value in enumerate(source):
        print("Index of", value, "is", lst.index(value))
    
    print("\nTest find:")
    for value in source:
        result = lst.find(value)
        print("Value", value, "was", "found" if result else "not found")
    
    print("\nTest min:")
    try:
        print("Minimum value is", lst.min())
    except Exception as e:
        print("Cannot find minimum of an empty list")
    
    print("\nTest max:")
    try:
        print("Maximum value is", lst.max())
    except Exception as e:
        print("Cannot find maximum of an empty list")