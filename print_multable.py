#Write a program to read an integer and print the multiplication table of the same number
Number=int(input("Enter a Number:"))
for i in range(1, 11):
    print(f"{Number} x {i} = {Number*i}")
pos=neg=zero=0

while (n!=-1):
    n=int(input("Enter a number:"))
    if n>0:
        pos=pos+n
        print("The sum of positive numbers is:",pos)
    elif n<0:
        neg=neg+n
        print("The sum of negative numbers is:",neg)
    else:
        zero=zero+n
        print("The sum of zero numbers is:",zero)
        