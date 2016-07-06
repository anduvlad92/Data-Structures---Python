class Queue:
    def __init__(self,maxSize):
        self.rear = 0;
        self.front = -1;
        self.maxSize = maxSize;
        self.queue = [None]*maxSize;
        print ("Queue created with size of: "+str(maxSize));



    def isFull(self):
        if(self.rear == self.front or self.maxSize <=0):
            print("Queue is full");
            return True;
        else:
            return False;

    def isEmpty(self):
        if(self.front == -1):
            print("Queue is empty");
            return True;
        else:
            return False;

    def peek(self):
        if(self.front != -1):
            return self.queue[self.front];
        else:
            print("Can't return peek. The queue is empty");

    def enqueue(self,data):
        if(not self.isFull()):
            if(self.front == -1):
                self.front = self.front+1;
            self.queue[self.rear] = data;
            self.rear = (self.rear+1)%self.maxSize;

    def dequeue(self):
        if(not self.isEmpty()):
            data = self.queue[self.front];
            self.front = (self.front+1)%self.maxSize;

            if(self.rear == self.front):
                self.rear = 0;
                self.front = -1;
            return data;

