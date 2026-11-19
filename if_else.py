#Write a Python Program to find out in three numbers, which one is Greater
a=int(input("Enter 1st Number:"))
b=int(input("Enter 2nd Number:"))
c=int(input("Enter 3rd Number:"))
if a>b and a>c:
    print("The 1st Number is Greater")
elif b>a and b>c:
    print("The 2nd Number is Greater")
else:
    print("The 3rd Number is Greater")