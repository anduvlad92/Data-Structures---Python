from linked_list.Node import Node
class DoubleLinkedList:
    def __init__(self):
        self.counter = 0;
        self.head = Node(None,None,None);
        self.tail = Node(None,None,self.head);
        self.head.next = self.tail;

    def add(self,data):
        prev_node = self.tail.prev;
        prev_node.next = Node(data,self.tail,prev_node);
        self.tail.prev = prev_node.next;
        self.counter = self.counter + 1;



    def remove(self,index):
        if(index <0 or index >= self.counter):
            print("Remove: Index out of bounds");
        else:
            node =self.head;
            while(index >=0 ):
                node = node.next;
                index = index - 1;
            node.next.prev = node.prev;
            node.prev.next = node.next;
            self.counter = self.counter - 1;






    def display(self):
        aux = self.counter;
        node = self.head;
        while (aux != 0):
            node = node.next;
            print(node.data);
            aux = aux - 1;
