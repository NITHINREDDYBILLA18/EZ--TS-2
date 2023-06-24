a=[] 
def func():
    print("Enter type of function")
    print("1.Insert\n2.Delete\n3.search\n4.sort")
    e=int(input())
    if e==1:
        insert()
    elif e==2:
        delete()
    elif e==3:
        search()
    elif e==4:
        sort()
    else:
        exit()
def insert():
    n=int(input("enter n value"))
    
    for i in range(0,n):
        n1=int(input("input"))
        a.append(n1)
    print(a)
    func()
def delete():
    print("enter the no to del")
    d=int(input())
    a.remove(d)
def search():
    print("enter the no to search")
    s=int(input())
    for i in a:
        if i==s:
            f=1
        else:
            f=0
    if f==1:
        print("found")
    if f==0:
        print("Not found")
    func()

def sort():
    a.sort()
    print(a)
    func()
func()
    



        

