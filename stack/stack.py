class Stack:
    def __init__(self,maxSize):
        self.maxSize = maxSize;
        self.top = -1;
        self.stack = [None]*maxSize;


    def peek(self):
        if(self.top != -1):
            return self.stack[self.top];

    def isFull(self):
        if(self.top == self.maxSize-1):
            print("Stack is full");
            return True;
        else:
            return False;


    def isEmpty(self):
        if(self.top == -1):
            print("Stack is empty");
            return True;
        else:
            return False;


    def push(self,data):
        if(not self.isFull()):
            self.top = self.top+1;
            self.stack[self.top] = data;


    def pop(self):
        if(not self.isEmpty()):
            self.top = self.top - 1;
            return self.stack[self.top + 1];

