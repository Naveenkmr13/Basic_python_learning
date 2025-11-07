#n=int(input("Enter the number : "))
"""i=10
while(i>0):
    print(i)
    i=i-1
n=int(input("Enter the number : "))
i=1
multy=1
sum=0
count=0
while(i<=n):
    print(i)
    multy=multy*i
    sum=sum+i
    count=count+1
    i=i+1
print("Total number of multiply is : "+str(multy))
print("Total number of sum is : "+str(sum))
print("Total number of count is : "+str(count))

n=int(input("Enter the number : "))
for i in range (0,n):
    for j in range(0,n-i-1):
        print(" ",end="")
    for k in range(0,i+1):
        print("* ",end="")
    print()"""


"""
n=int(input("Enter the number : "))
i=0
while(i<n):
    print(" " * (n-i-1) + "* " * (i+1))
    i=i+1
    
n=int(input("Enter the number : "))
a = b = n//2
for i in range (n-1):
    for j in range(n):
        if j==a or j==b:
            print("*",end=" ")
        else:
            print(" ",end="")
    a -= 1
    print("*",end=" ")
    print()
print("* "*n)


n=int(input("Enter the number : "))
for i in range (n-1):
    for j in range(0,n-i-1):
        print(" ",end="")
    print("* ",end="")
    for k in range(i+i-2):
        print(" ",end="")
    if i!=0:
        print("* ",end="")
    print()
print("* "*n)"""
n=5
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
    


