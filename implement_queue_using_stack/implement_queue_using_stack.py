"""
Implementation of queue using stack
"""
class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next

class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count
    def __str__(self):
        s = ''
        cur = self.head
        while cur is not None:
            s = str(cur.item) + ' ' +s
            cur = cur.next
        return 'bottom -> '+ s+'<- top'

class MyQueue:

    def __init__(self):
        self._stack_in = Stack()
        self._stack_out = Stack()


    def push(self, x: int) -> None:

        while not self._stack_out.is_empty():
            self._stack_in.push(self._stack_out.pop())
        self._stack_in.push(x)

    def pop(self) -> int:
        while not self._stack_in.is_empty():
            self._stack_out.push(self._stack_in.pop())
        return self._stack_out.pop()


    def peek(self) -> int:
        while not self._stack_in.is_empty():
            self._stack_out.push(self._stack_in.pop())
        return self._stack_out.peek


    def empty(self) -> bool:
        return not (self._stack_in or self._stack_out)
