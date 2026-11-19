

#Write a python script to find the Area and circumference of a circle and convert the area into integer
x=float(input("Enter the Radius of the Circle:"))
Area=3.142*x**2
Circumference=2*3.142*x

print("Area of the circle is :",Area)
print("Circumference of the circle is:",Circumference)
area_int=int(Area)
circumference_int=int(Circumference)
print("the converted area into the integer is:",area_int)
print("the converted circumference into the integer is:",circumference_int)

