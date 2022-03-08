from collections import deque


class Stack:

    def __init__(self):
        self.container=deque()

    def push(self,val):
        self.container.append(val)
    def peek(self):
        return self.container[-1]

    def pop(self):
        return self.container.pop()
    def is_empty(self):
       return len(self.container)==0

    def length(self):
        return len(self.container)

