from .boundedstack import BoundedStack
import unittest
from clii import BoundedStack

class TestBoundedStack(unittest.TestCase):
    def test_push_and_pop(self):
        stack = BoundedStack(2)
        stack.push("first")
        stack.push("second")

        self.assertEqual(stack.pop(), "second")
        self.assertEqual(stack.pop(), "first")

    def test_push_full_stack(self):
        stack = BoundedStack(1)
        stack.push("item")

        self.assertRaises(Exception, lambda: stack.push("another"))

    def test_pop_empty_stack(self):
        stack = BoundedStack(1)
        self.assertRaises(Exception, stack.pop)

    def test_peek(self):
        stack = BoundedStack(2)
        stack.push("first")
        stack.push("second")

        self.assertEqual(stack.peek(), "second")
        self.assertEqual(stack.pop(), "second")

    def test_is_empty(self):
        stack = BoundedStack(3)
        self.assertTrue(stack.isEmpty())

        stack.push("item")
        self.assertFalse(stack.isEmpty())

    def test_is_full(self):
        stack = BoundedStack(1)
        self.assertFalse(stack.isFull())

        stack.push("item")
        self.assertTrue(stack.isFull())

    def test_size(self):
        stack = BoundedStack(3)
        self.assertEqual(stack.size(), 0)

        stack.push("item")
        stack.push("another")
        self.assertEqual(stack.size(), 2)

    def test_clear(self):
        stack = BoundedStack(2)
        stack.push("item")
        stack.push("another")
        stack.clear()

        self.assertTrue(stack.isEmpty())


if __name__ == '__main__':
    unittest.main()