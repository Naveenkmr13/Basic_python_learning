for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
#----------------------------------
for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for  k in range(1,i+1):
        print("*",end="")
    print()
#----------------------------
for i in range(0,4):
    for j in range(0,i+1):
        print("*",end="")
    print()
for i in range(1,4):
    for j in range(1,5-i):
        print("*",end="")
    print()
#-------------------------------
for i in range(1,6):
    for j in range(1,6-i):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    for l in range(1,(6-i)*2):
        print(end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()
#---------------------------
for i in range(0,5):
    for j in range(0,4-i):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end="")
    for l in range(0,(4-i)*2):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
#x=int(input("Enter the number : ")
n=4
for i in range(0,n):
   # print("*",end="")
    for j in range(0,(n-2*i)+1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()
    
    
m=5
for i in range(0,m):
    for j in range(0,m-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("* ",end="")
    print()
for i in range(0,m):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(0,m-i-1):
        print("* ",end="")
    print()

n=int(input("Enter the number : "))
for i in range(65,n):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()
    
n=int(input("Enter the number 1 : "))
n=int(input("Enter the number 2 : "))
i=0
while(i<=n):
    print(" " * (n - i)+"* " * i)
    i=i+1
    
i=0
while(i<=n):
    print(" "*(i+1)+"* "*(n-i-1))
    i=i+1
    
n=int(input("Enter the number 1 : "))
for i in range(0,n):
    print(" " * (n - i-1)+"* " * (i+1))
    i=i+1




    


    

