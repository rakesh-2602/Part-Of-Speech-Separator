import math

list1=[]
list2=[]

n=int(input("enter the number of elements : "))
print("enter the elements : ")
for i in range(0,n):
    x=int(input())
    list1.append(x)
print("list 1 elements are : ",list1)

print("enter the elements : ")
for i in range(0,n):
    y=int(input())
    list2.append(y)
print("list 2 elements are : ",list2)

num=sum(x*y for x,y in zip(list1,list2))
print("numerator is : ",num)

normx=sum(x**2 for x in list1)
normy=sum(y**2 for y in list2)

den = math.sqrt(normx) * math.sqrt(normy)
sum=num/den
print("cosine similarity is : ",sum)