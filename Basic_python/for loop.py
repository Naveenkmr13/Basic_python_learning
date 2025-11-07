'''for i in range(1,21):#2 table
    print(str(i)+"*2="+str(i*2))
----------------------------------
for i in range(9,15):
    print(i)
    #or

x=int(input("enter the value:"))#inputformat  if 8 and 15
y=int(input("enter the  2nd numer:"))
for i in range(x+1,y):
    print(i)
-------------------------------------
for i in range(1,10):
    if(i%2==1):   #print even numer from 1 to 10
        print(i)

--------------------------------------------------------'''
#count the no of even num from 1 to 10
even_count=int(input("enter the nubmer"))
odd_count=int(input('enter the 2nd number'))
for i in range(1,11):
    if (i%2==0):
        even_count=even_count+1
    else:
        odd_count=odd_count+1
print(even_count+odd_count)


