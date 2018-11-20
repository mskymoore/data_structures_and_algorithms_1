class Stack():
    def __init__(self, *args, **kwargs):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(items) - 1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


def rev_string(a_str):
    s = Stack()
    for c in a_str:
        s.push(c)
    rev_str = list()
    while not s.is_empty():
        rev_str.append(s.pop())
    return ''.join(rev_str)


