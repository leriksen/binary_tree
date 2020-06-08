import unittest

from binary_tree import BinaryTree

class TestBinaryTree(unittest.TestCase):
    def test_find_min_empty(self):
        self.assertEqual(BinaryTree().find_min(), None)

    def test_find_min_simple(self):
        tree = BinaryTree()
        tree.value = 1
        value = tree.find_min()
        self.assertEqual(value, 1)

    def test_find_min_complex(self):
        tree = BinaryTree()
        tree.value = 5
        tree.left = BinaryTree()
        tree.left.value = 3
        value = tree.find_min()
        self.assertEqual(value, 3)

    def test_find_min_complex2(self):
        tree = BinaryTree()
        tree.value = 5
        tree.right = BinaryTree()
        tree.right.value = 8
        value = tree.find_min()
        self.assertEqual(value, 5)


    def test_find_max_empty(self):
        self.assertEqual(BinaryTree().find_max(), None)

    def test_find_max_simple(self):
        tree = BinaryTree()
        tree.value = 1
        value = tree.find_max()
        self.assertEqual(value, 1)


    def test_find_max_complex(self):
        tree = BinaryTree()
        tree.value = 3
        tree.right = BinaryTree()
        tree.right.value = 5
        value = tree.find_max()
        self.assertEqual(value, 5)


    def test_find_max_complex2(self):
        tree = BinaryTree()
        tree.value = 5
        tree.left = BinaryTree()
        tree.left.value = 3
        value = tree.find_max()
        self.assertEqual(value, 5)

    def test_contains_empty(self):
        self.assertEqual(BinaryTree().__contains__(1), False)

    def test_contains_simple_pass(self):
        tree = BinaryTree()
        tree.value = 1
        self.assertEqual(tree.__contains__(1), True)

    def test_contains_simple_fail(self):
        tree = BinaryTree()
        tree.value = 1
        self.assertEqual(tree.__contains__(0), False)

    def test_contains_complex_pass(self):
        tree = BinaryTree()
        tree.value = 3
        tree.left = BinaryTree()
        tree.left.value = 1
        self.assertEqual(tree.__contains__(1), True)

    def test_contains_complex2_pass(self):
        tree = BinaryTree()
        tree.value = 3
        tree.left = BinaryTree()
        tree.left.value = 1
        tree.right = BinaryTree()
        tree.right.value = 5
        self.assertEqual(tree.__contains__(5), True)


    def test_contains_complex_fail(self):
        tree = BinaryTree()
        tree.value = 3
        tree.left = BinaryTree()
        tree.left.value = 1
        self.assertEqual(tree.__contains__(0), False)


    def test_contains_complex2_fail(self):
        tree = BinaryTree()
        tree.value = 3
        tree.left = BinaryTree()
        tree.left.value = 1
        tree.right = BinaryTree()
        tree.right.value = 5
        self.assertEqual(tree.__contains__(7), False)

if __name__ == '__main__':
    unittest.main()