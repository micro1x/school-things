class Queue:
    def __init__(self):
        self.queue = []
        
    def enqueue(self, element):
        self.queue.append(element)
    
    def isEmpty(self):
        return len(self.queue)==0
        
    def dequeue(self):
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)
        
def print_tasks(tasks):
    queue = Queue()
    for things in tasks:
        if things[1] == 1:
            queue.enqueue(things)
        if things[1] == 2:
            queue.enqueue(things)
        if things[1] == 3:
            queue.enqueue(things)
    while not queue.isEmpty():
        x = queue.dequeue()
        print("serving ", x[0], " priority ", x[1])
patients = [("Ben", 2), ("Amy", 1), ("Charlie", 3), ("David", 1)]