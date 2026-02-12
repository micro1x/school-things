class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DLL: 
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        new_Node = Node(data)

        if not self.head:
            self.head = self.tail = new_Node
            return

        self.tail.next = new_Node
        new_Node.prev = self.tail
        self.tail = new_Node

    def insert_at_beginning(self, data):
        new_node = Node(data)

        # Case 1: list is empty
        if not self.head:
            self.head = self.tail = new_node
            return

        # Case 2: list has nodes
        new_node.next = self.head     # link new node forward
        self.head.prev = new_node     # link old head back
        self.head = new_node   

    def delete_head(self, data):
        if not self.head:
            return "list is empty"
        
        if self.head == self.tail:
            self.head = self.tail = None

        self.head = self.head.next
        self.head.prev = None
    
    def delete_tail(self, data):
        if not self.head:
            return "list is empty"
        if self.head == self.tail:
            self.head = self.tail = None
        
        self.tail = self.tail.prev
        self.tail.next = None
    
    def delete_value(self, value):
    # Case 1: empty list
        if self.head is None:
            return

        current = self.head

        while current:
            if current.data == value:

                # Case 2: deleting the head
                if current == self.head:
                    self.delete_head()
                    return

                # Case 3: deleting the tail
                if current == self.tail:
                    self.delete_tail()
                    return

                # Case 4: deleting from the middle
                current.prev.next = current.next
                current.next.prev = current.prev
                return

            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end = " <-> ")
            current = current.next
        print("None")

def insert(lst):
    Double = DLL()
    for nums in lst:
        if nums%2 == 0:
            Double.insert_at_beginning(nums)
        else:
            Double.insert_at_end(nums)
    Double.display()

print(insert([5,2,7,8,3]))