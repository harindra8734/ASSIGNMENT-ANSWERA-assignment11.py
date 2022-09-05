#7. Write a python script to count digits in a given number



n=int(input("enter a number"))
count=0
if n<0:
    count=-1*n
if n==0:
    count=1
while n!=0:
    n=n//10
    count+=1
print("count of the number",count)