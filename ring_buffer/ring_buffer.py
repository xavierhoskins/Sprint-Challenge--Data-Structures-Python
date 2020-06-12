import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('./doubly_linked_list')


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # This import our storage
        self.storage = DoublyLinkedList()
        # This will be used to determine what node we are on accross the list
        self.z = None

    def append(self, item):
        # This will add to our tail
        if self.storage.length < self.capacity:
            # this adds the item to the tail
            self.storage.add_to_tail(item)
            # now our variable has been added and is z
            self.z = self.storage.tail
            return
        else:
            # if the variable is already there start back over at the beginning of the head
            if self.z == self.storage.tail:
                self.z = self.storage.head
            # otherwise the variable will be added to the next one
            else:
                self.z = self.z.next
            self.z.value = item

    def get(self):
        #This is the empty contents
        buffer_contents = []
        #This is the node that is stored at the head
        node = self.storage.head
        #When the node is something this continues adding to the next node as well as replacing if already full.
        while node is not None:
            buffer_contents.append(node.value)
            node = node.next
        #This returns all the contents of the array
        return buffer_contents