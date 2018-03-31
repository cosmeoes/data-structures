
class List():

    def __init__(self):
        self._head = None
        self.size = 0

    def __iter__(self):
        values = []
        aux = self._head
        while aux:
            values.append(aux.value)
            aux = aux.next_node
        return iter(values)


    def add(self, value, index=-1):
        "Adds a node to the list"
        node = Node(value=value)
        if index == -1:
            if self._head:
                p = self._head
                while p.next_node:
                    p = p.next_node
                p.next_node = node
            else:
                self._head = node
        else:
            if index == 0:
                node.next_node = self._head
                self._head = node
            else:
                prev = self._get_node_at(index-1)
                node.next_node = prev.next_node
                prev.next_node = node
        self.size += 1
 
    def get(self, index):
        return self._get_node_at(index).value

    def remove(self, index):
        node = self._get_node_at(index-1)
        node_to_remove = node.next_node
        if node_to_remove.next_node:
            node.next_node = node.next_node.next_node
        else:
            node.next_node = None
        self.size -= 1

    def _get_node_at(self, index):
        if index < self.size: 
            node = self._head
            for i in range(index):
                node = node.next_node 
            return node
        
    def print(self):
       self._head.print()

class Node():
    "The node class for the List object"
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next_node = next_node

    def set_value(self, value):
        self._value = value

    def get_value(self):
        return self._value

    value = property(get_value, set_value)
    
    def set_next(self, next_node):
        self._next_node = next_node

    def get_next(self):
        return self._next_node

    next_node = property(get_next, set_next)

    def print(self):
        print(self.value) 
        if self.next_node:
            self.next_node.print()

