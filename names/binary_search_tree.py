#My Binary Tree from my data project. Only parts I need

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if self.value > value:
            if self.left:
                return self.left.insert(value)
            # check if dot right exists.
            else:
                self.left = new_node
        else:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True


        elif target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
                return self.right.contains(target)
            else:
                return False