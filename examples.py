from structures.linkedList import List
from structures.queue import Queue
from structures.stack import Stack

mylist = List()

for i in range(5):
    mylist.add(i)

mylist.add(5)
mylist.add(7,1)

for i in mylist:
    print(i)

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
for i in range(queue.size):
    print(queue.dequeue())

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
for i in range(stack.size):
    print(stack.pop())
