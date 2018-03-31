

class Queue:
    def __init__(self):
        self._list = []

    def enqueue(self, value):
        self._list.append(value)
    
    def dequeue(self):
        value = self._list[0]
        self._list.remove(value)
        return value
    
    def _get_size(self):
        return len(self._list)

    size = property(_get_size)
