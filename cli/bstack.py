class BoundedStack:
    """Implements a stack with a bounded capacity to hold items."""

    def __init__(self, capacity: int):
        """
        Initializes a new Bounded Stack that is empty.

        Args:
            capacity (int): The maximum number of items the stack can hold.
        """
        self.items = []
        self.capacity = capacity

    def push(self, item):
        """
        Adds a new item on top of the stack if there is space.

        Args:
            item: The item to be added to the stack.

        Raises:
            Exception: If the stack is already at its maximum capacity.
        """
        if len(self.items) < self.capacity:
            self.items.append(item)
        else:
            raise Exception("Stack is at maximum capacity.")

    def pop(self):
        """
        Removes the top item from the stack and returns it.

        Returns:
            The item that was removed from the top of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.isEmpty():
            raise Exception("Cannot pop from an empty stack.")
        return self.items.pop()

    def peek(self):
        """
        Returns the top item from the stack without removing it.

        Returns:
            The top item of the stack.

        Raises:
            Exception: If the stack is empty.
        """
        if self.isEmpty():
            raise Exception("Cannot peek in an empty stack.")
        return self.items[-1]

    def isEmpty(self):
        """
        Tests to see whether the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def isFull(self):
        """
        Tests to see whether the stack is full.

        Returns:
            bool: True if the stack is full, False otherwise.
        """
        return len(self.items) == self.capacity

    def size(self):
        """
        Returns the number of items in the stack.

        Returns:
            int: The number of items in the stack.
        """
        return len(self.items)

    def clear(self):
        """
        Empties the stack of all its items.
        """
        self.items.clear()

    def __str__(self):
        """
        Returns a string representation of the stack.

        Returns:
            str: The string representation of the stack's items in the format of a list.
        """
        # This shows the top of the stack at the end of the list
        return str([str(item) for item in self.items])
