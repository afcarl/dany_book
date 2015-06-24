class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
    def __str__(self):
        return repr(self.data)

if __name__ == '__main__':
    head = Node(0)
    print head
        
    #list generation
    cur = head
    for i in xrange(100):
        new_node = Node(i)
        cur.next = new_node
        cur = cur.next
	
    #list observation
    cur = head
    while cur:
        print cur
        cur = cur.next
