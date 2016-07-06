from linked_list.Node import Node


class LinkedList:
    def __init__(self):
        self.counter = 0;
        self.tail = Node(None,None);
        self.head = Node(None,self.tail);

    def add(self,data):
        node = self.head;
        aux = self.counter;
        while(aux != 0):
            node = node.next;
            aux = aux - 1;
        node.next = Node(data,self.tail);
        self.counter = self.counter + 1;



    def display(self):
        aux = self.counter;
        node = self.head;
        while(aux != 0):
            node = node.next;
            print(node.data);
            aux = aux - 1;


    def remove(self,index):
        prev = self.head;
        if(index >= self.counter or index < 0):
            print("Remove :  index out of bounds");
            return ;
        else:
            while(index-1 >=0):
                prev = prev.next;
                index = index - 1;
            prev.next = prev.next.next;
            self.counter = self.counter - 1;