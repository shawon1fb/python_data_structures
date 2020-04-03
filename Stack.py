class Stack():
    def __init__(self):
        self._items = []

    def push(self, *args):
        for item in args:
            self._items.append(item)

    def pop(self):
        return self._items.pop()

    def clear(self):
        self._items.clear()

    def get_stacks(self):
        return self._items

    def is_empty(self):
        return self._items == []

    def top(self):
        if not self.is_empty():
            return self._items[-1]

    def __str__(self):
        return f"{self._items[:]}"
