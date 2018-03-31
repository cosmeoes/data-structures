
class Stack:
    def __init__(self):
        self._list = []
    
    def push(self, value):
        self._list.append(value)

    def pop(self):
        value = self._list[-1]
        self._list.remove(value)
        return value

    def _get_size(self):
        return len(self._list)

    size = property(_get_size)
