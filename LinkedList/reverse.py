class LinkedList:
    def __init__(self, node):
        self.head = node

    def reverse(self):
        prev = None
        temp = self.head
        while (temp!=None):
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        self.head = prev #key point
    def display(self):
        temp = self.head
        while temp is not None:
            print (temp.data)
            temp = temp.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

a = Node('a')
b = Node('b')
c = Node('c')
b.next = c
a.next = b

ll = LinkedList(a)

ll.display()

ll.reverse()

ll.display()
