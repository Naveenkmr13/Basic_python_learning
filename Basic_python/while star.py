n=int(input("Enter the number : "))
for i in range(97,n):
    for j in range(97,i+1):
        print(chr(j),end="")
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
