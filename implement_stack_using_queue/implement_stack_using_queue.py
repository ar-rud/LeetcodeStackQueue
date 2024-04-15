"""
Implementation of stack using queue
"""

class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        if self.head is None:
            self.tail = Node(item)
            self.head = self.tail
        else:
            self.tail.next = Node(item)
            self.tail = self.tail.next

    def pop(self):
        if self.head:
            item = self.head
            self.head = self.head.next
            return item
        raise ValueError('Queue is empty.')

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def __str__(self):
        s = ''
        current = self.head
        while current is not None:
            s += str(current.item)+' '
            current = current.next
        return f'start -> {s}<- end'


class MyStack:

    def __init__(self):
        self._q1 = Queue()
        self._q2 = Queue()


    def push(self, x: int) -> None:
        if self._q2.is_empty():
            self._q1.add(x)
        else:
            self._q2.add(x)

    def pop(self) -> int:
        if not self._q1.is_empty():
            while not self._q1.is_empty():
                val = self._q1.pop()
                if not self._q1.is_empty():
                    self._q2.add(val.item)
            return val.item
        if not self._q2.is_empty():
            while not self._q2.is_empty():
                val = self._q2.pop()
                if not self._q2.is_empty():
                    self._q1.add(val.item)
            return val.item
        raise ValueError('Queue is empty.')


    def top(self) -> int:
        if not self._q1.is_empty():
            while not self._q1.is_empty():
                val = self._q1.pop()
                self._q2.add(val.item)
            return val.item
        if not self._q2.is_empty():
            while not self._q2.is_empty():
                val = self._q2.pop()
                self._q1.add(val.item)
            return val.item

    def empty(self) -> bool:
        return self._q1.is_empty() and self._q2.is_empty()
