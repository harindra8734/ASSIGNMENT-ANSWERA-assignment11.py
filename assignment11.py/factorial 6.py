#6. Write a python script to calculate factorial of a given number

n=int(input("enter a number"))
f=1
for i in range(n,0,-1):
    f=f*i
print(f)