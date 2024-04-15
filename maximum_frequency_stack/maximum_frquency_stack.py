"""
Implementation of maximum frequency stack
"""
from collections import deque

class Node():
    """node class"""
    def __init__(self, val, freq=1) -> None:
        self.val = val
        self.freq = freq

class FreqStack:

    def __init__(self):
        self.stack = deque()


    def push(self, val: int) -> None:
        for el in reversed(self.stack):
            if el.val == val:
                self.stack.append(Node(val, freq= el.freq + 1))
                return
        self.stack.append(Node(val))


    def pop(self) -> int:
        max_freq = 0
        node = None
        for nd in reversed(self.stack):
            if nd.freq > max_freq:
                max_freq = nd.freq
                node = nd
        self.stack.remove(node)
        return node.val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
