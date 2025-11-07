for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
#--------------------------------------------
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
#----------------------------------------
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
for i in range(0,4):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(0,2*(4-i)-1):
        print("*",end="")
    print()
#------------------------------------------------
for i in range(0,5):
    for j in range(0,5-i-1):
        print(end=" ")
    for k in range(0,i+1):
        print("*",end=" ")
    print()
for i in range(0,4):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(0,4-i):
        print("*",end=" ")
    print()
#---------------------------------------------------
n=int(input("Enter the number 1 : "))
a=int(input("Enter the number 2 : "))

for i in range(0,n):
    for j in range(0,n-i-1):
        print(end=" ")
    for k in range(0,2*i+1):
        print("*",end="")
    print()
for i in range(0,a):
    for j in range(0,i+1):
        print(end=" ")
    for k in range(0,2*(a-i)-1):
        print("*",end="")
    print()

    
