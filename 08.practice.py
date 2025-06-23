#Q1.Write a python program to input your name and age,
'''name=input("Enter your name : ")
age=int(input("Enter your age : "))
print(f"my name is {name} and i am {age} years old.")
#Q2.Take two inputs from the user as strings, convert them into integers, add them, and print the result.
num1=input("Enter youre first number : ")
num2=input("Enter youre second number : ")
sum=int(num1)+int(num2)
print("sum is :",sum)'''
#Q3.: Take any input from the user and print which data type it is after converting it (e.g., int, float, str).
value=input("Enter any value : ")
# check type befor and after typecasting
print("orginal type:",type(value))
if value.isdigit():
    value=int(value)
    print("convert to int.Type now:",type(value))
else:
    try:
        value=float(value)
        print("convert to float. Type now:",type(value))
    except:
      print("kept as string Type:",type(value))
#Q4.Arethmatic operator
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Modulus:", a % b)
#Q5: Input the marks of 3 subjects from the user and calculate:


sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total = sub1 + sub2 + sub3
average = total / 3
percentage = (total / 300) * 100

print("Total Marks:", total)
print("Average Marks:", average)
print("Percentage:", percentage, "%")
