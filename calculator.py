print("\t\tThis program adds or subtracts two numbers that you give it as a user")
#Use of the Escape Sequences with Strings command "\t".
num1=int(input("Please input a number here:\t\t"))
num2=int(input("Please input a second number here:\t"))
#Users that use this program will be able to input any integer number for addition or subtraction.

choice=input("Would you like to add or subtract?\t")
# Use of If-statements for subtraction OR addition.
if choice=="add":
    sum= num1+num2
    print("The result is:\t"+ str(sum))
if choice=="subtract":
    sum= num1-num2
    print("The result is:\t"+ str(sum))
#Conversion of the int(sum) to str(sum) so it can be printed.
else:
    print("Please choose either 'add' or 'subtract'.")
#I used the "else" command just in case someone mispelled or typed in another word and expected a result.

    
