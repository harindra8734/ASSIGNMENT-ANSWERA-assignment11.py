'''10. Write a python script to print the octal equivalent of a given decimal number. (do not
use oct() method)'''
n=int(input("enter octal number\n"))
oc=' '
while n!=0:
    oc=oc+str(n%8)
    n=n//8
print("decimal equal to octal is")
for i in range(len(oc)-1,-1,-1):
    print(oc[i],end=' ')
