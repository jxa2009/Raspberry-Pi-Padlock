#Queue Class that takes a max size as a parameter and will only enqueue items up to that max size indicated
class Queue:

    def __init__(self, MAX_SIZE):
        self.queue = []
        self.MAX_SIZE = MAX_SIZE

    # create an empty queue
    def create_queue(self):
        return []

    # return the size of the list added as a parameter
    def size(self):
        return len(self.queue)
    def maxsize(self):
        return self.MAX_SIZE
    # add an input to the end of the list
    # returns list
    def enqueue(self,input):
        if self.size() < self.maxsize():
            self.queue.append(input)
        return self.queue

    # pops off the first item of the list
    def dequeue(self):
        return self.queue.pop(0)
    def printQueue(self):
        print("this is the whole queue: ")
        print(self.queue)
    def getQueue(self):
        return self.queue

def testQueue():
    q1 = Queue(4)#make a queue of size 4
    q1.printQueue()
    q1.enqueue(1)
    q1.printQueue()
    q1.dequeue()
    q1.printQueue()
    q1.enqueue(3)
    q1.enqueue(4)
    q1.enqueue(2)
    q1.enqueue(2)
    q1.printQueue()
    q1.enqueue(1)
    q1.printQueue()
    print("Item dequeued: " + str(q1.dequeue()))
#testQueue()