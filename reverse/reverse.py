# CANNOT USE DOUBLY LINKED LIST WHICH MEANS WE DO NOT KNOW THE PREVIOUS SO CANNOT USE TAIL
class Node:
    # These are our blue prints for th node and how they work
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        self.head = None

    # Blue Print for adding to head
    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    # Blue Print for what the current node is at
    def contains(self, value):
        if not self.head:
            return False

        current = self.head
        # Our conditional statement that will only return if we have a real node
        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()
        # otherwise it will be done and break
        return False

    
    def reverse_list(self, node, prev):
        #if the node is None we will return None
        if node is None:
            return
        #get_next() returns a nested structure that will represent the NEXT element
        if node.get_next() is None:
            #sets the head to node
            self.head = node
            #sets the next node to the previous
            self.head.next_node = prev
            return
        #implements recursion (Calling itself inside the function)
        self.reverse_list(node.get_next(), node)
        #This will set the next node to the previous node
        #Basically redrawing the points
        node.next_node = prev