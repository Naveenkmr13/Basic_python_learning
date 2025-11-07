"""count=0
for i in range(1,100):
    if(i%3==0 and i%5==0):
        count=count+1
print(count)
----------------------------------------------------
# print sum of 1 to 5 natural numbers
sum=0
for i in range(1,6):
    sum=sum+i
print(sum)
------------------------------------------"""
a=[]# here list is used tol store the 10 values
sum=0
count=0
print("Enter the total 10 numers:")#to print 10 num... from the user and get the avg
for i in range(1,11):
    num=int(input("number"+str(i)+":"))
    a.append(num)#appen is used for send the num top last place in the list
    sum=sum+i
    count=count+1
print(count)
"""----------------------------------------
int (input("Enter the total numbers : "))#to display the cube of  numbers of and theri sums
for i in range(1,7):
    num=int(input(" The "+str(i)+" number is : "))
sum=0    
for i in range(1,7):
    sum=sum+i*i*i
    print("number is ",i," and cube of the "+str(i)+" is : ",i*i*i)
print("The Total sum is : ",sum)"""
    
