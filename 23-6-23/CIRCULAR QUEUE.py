class circularQueue():
    def __init__(self,size):
        self.size=size
        self.queue=[None for i in range(size)]
        self.front=self.rear=-1
    def enqueue(self,data):
        if ((self.rear+1)%self.size==self.front):
            print("queue is Full\n")
        elif (self.front==-1):
            self.front=0
            self.rear=0
            self.queue[self.rear]=data
        else:
            self.rear=(self.rear+1)%self.size
            self.queue[self.rear]=data
    def dequeue(self):
        if (self.front==-1):
            return "empty queue"
        elif (self.front==self.rear):
            temp=self.queue(Self.front)
            self.front=-1
            self.rear=-1
            return temp
        else:
            temp=self.queue[self.front]
            self.front=(self.front+1)%self.size
            return temp
    def display(self):
        if(self.front==-1):
            print("queue is empty")
        elif (self.rear>=self.front):
            print("Elements in the circular queue",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[1],end=" ")
            print()
        else:
            print("element in circular queue",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=' ')
            for i in range(0,self.rear+1):
                print(self.queue[i],end=' ')
            print()
        if ((self.rear+1)%self.size==self.size==self.front):
            print("queue is Full")
ob=circularQueue(5)
ob.enqueue(14)
ob.enqueue(22)
ob.enqueue(13)
ob.enqueue(-6)
ob.display()
print("Deleted value=",ob.dequeue())
print("deleted value=",ob.dequeue())
ob.display()
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
ob.display()
ob.enqueue(100)
