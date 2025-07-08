def push(s,x,l):
 if l-1>=len(s):
  s.insert(0,x)
 else:
  print("queue is full")
  print("Overflow!!")
def pop(s):
 if len(s)>0:
  print("Deleted item is :",s[-1])
  s.pop()
 else:
  print("The list is empty")
  print("Underflow!!")
s=[]
l=int(input("Enter the size of the queue :- "))
while(1):
 print("1.Push")
 print("2.Pop")
 print("3.Display")
 print("4.Exit")
 print("Enter your choice?")
 c=int(input(""))
 if c==1:
  x=int(input("Enter your number : -"))
  push(s,x,l)
 elif c==2:
  pop(s)
 elif c==3:
  if len(s)!=0: 
   print("Queue = ",s)
  else:
   print("Queue is empty")
 elif c==4:
  exit(0)
 else:
  print("Wrong input!!") # type: ignore