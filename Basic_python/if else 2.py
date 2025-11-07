'''x=int(input("ENTER THE NUMBER?"))#even and odd
if(x%2==0):
    print("even")
else:
    print("odd")
------------------------------------------------
score=100
if(score<35):
    print("poor student")
elif(score>35 and score<70):
    print("average student")
else:
    print("good student")
---------------------------------------------------
score=int(input("enter the score?"))
if(score<35):
    print("poor student")
if(score>35 and score<70): # there were n number of if we can use and with out else and also the  n number of elif we can use
    print("average student")
if(score>70):
    print("good student")
---------------------------------------------------'''
x=int(input("enter the 1st number"))
y=int(input("enter the 2nd number"))
operation=str(input("add,sub,mul,div"))
if(operation=="add"):
    print(x+y)
elif(operation=="sub"):
    print(x-y)
elif(operation=="multi"):
    print(x*y)
else:
    print(x/y)
