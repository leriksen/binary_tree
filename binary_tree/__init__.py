class BinaryTree:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

    def find_min(self):
        if self.left is not None:
            return self.left.find_min()
        return self.value

    def find_max(self):
        if self.right is not None:
            return self.right.find_max()
        return self.value

    def __contains__(self, item):
        if self.value is item:
            return True
        if self.left is None and self.right is None:
            return False
        if self.value > item:
            return False if self.left is None else self.left.__contains__(item)
        return False if self.left is None else self.right.__contains__(item)