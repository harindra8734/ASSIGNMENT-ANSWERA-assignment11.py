#3. Write a python script to calculate sum of cubes of first N natural numbers

n=int(input("enter a number"))
s=0
for i in range(1,n+1):
    s=s+pow(i,3)
print(s)