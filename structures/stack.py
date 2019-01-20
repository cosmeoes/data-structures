from .linkedList import List

class Stack:
    def __init__(self):
        self._list = List()

    def push(self, value):
        self._list.add(value)

    def pop(self):
        value = self._list.get(self._list.size - 1)
        self._list.remove(self._list.size - 1)
        return value

    def _get_size(self):
        return self._list.size

    size = property(_get_size)
