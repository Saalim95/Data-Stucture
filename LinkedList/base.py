class LinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        temp = self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next

    def push(self, data):
        node = Node(data)
        temp = self.head
        if self.head ==  None:
            self.head = node
        else:
            while temp.next != None:
                temp = temp.next
            temp.next = node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.display()
