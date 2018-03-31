

class Queue:
    def __init__(self):
        self.list = []

    def enqueue(self, value):
        self.list.append(value)
    
    def dequeue(self):
        value = self.list[-1]
        self.list.remove(value)
        return value
    
    def get_size(self):
        return len(self.list)

    size = property(get_size)
