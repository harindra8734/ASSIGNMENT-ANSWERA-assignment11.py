#5. Write a python script to calculate sum of first N even natural numbers

n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    if i%2==0:
        s+=i
print("even number is ",s)
