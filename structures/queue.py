from .linkedList import List

class Queue:
    def __init__(self):
        self._list = List()

    def enqueue(self, value):
        self._list.add(value)

    def dequeue(self):
        value = self._list.get(0)
        self._list.remove(0)
        return value

    def _get_size(self):
        return self._list.size

    size = property(_get_size)
