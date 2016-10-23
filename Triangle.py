import math
#I am importing the math module so i can use the math.hypot command.
print("\t\tFind out the area and the hypotenuse of a triangle.")
print("\n--------------------------------------------------------------------------------\n")

#Here i decided to make use of some of the Escape Sequences with Strings that we talked about in our lecture.

print("\t\tHypotenuse of a right angled triangle triangle.")
#Here we will be able to find the hypotenuse of a triangle using the math.hypot command.
a =(int(input("Enter a number for side a:\t")))
b =(int(input("Enter a number for side b:\t")))
print ("The hypotenuse of your triangle is:\t"+(str(math.hypot(a, b))))
    
    
print("\t\tArea of the triangle.")
#Here we will be be able to find out the area of a trangle
a=(int(input("Enter a number for side a:\t")))
b=(int(input("Enter a number for side b:\t")))
c=(int(input("Enter a number for side c:\t")))
s=(a+b+c)/2
#The formula for finding the area of a trangle.
area=((s*(s-a)*(s-b))*(s-c)) ** 0.5
print("The area of the triangle is:\t"+(str(area)))

#Here I am converting the are into a string.

     






    




        
