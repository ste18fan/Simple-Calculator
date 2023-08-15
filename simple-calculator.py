import math


print("                  Python Calculator")
print(" ")
print(" ")


print("1. Addition\n")
print("2. Subtraction\n")
print("3. Multiplication\n")
print("4. Division\n")
print("5. Exponent\n")

select = int(input("Choose between the following operations: 1, 2, 3, 4, 5, 6: /"))
print(" ")


number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

def addition(number_1, number_2):
  return (number_1 + number_2)


def subtraction(num1, num2):
  return (num1 - num2)

def multiplication(num1, num2):
  return num1 * num2


def division(num1, num2):
  return num1 / num2

# New Function

def exponent(num1, num2):
  return  num1 ** num2

# New Function
def squareroot (num1, num2):
  return math.sqrt(num1, num2)

if select == 1: 
  print(number_1, "+" ,number_2, "=",
  addition(number_1, number_2))

elif select == 2:
  print(number_1, "-", number_2, "=", 
  subtraction(number_1, number_2))

elif select == 3:
  print(number_1, "*" ,number_2, "=", 
    multiplication(number_1, number_2))

elif select == 4:
  print(number_1, "/" ,number_2, "=", 
  division(number_1, number_2))

# New Function

elif select == 5:
  print(number_1, "**",number_2, "=",
  exponent(number_1, number_2))

# New Function

elif select == 6:
  print("The square root of the two numbers you chose are: ")
  print(" ")
  print(math.sqrt(number_1))
  print("and")
  print(math.sqrt(number_2))
  

else:
  print("Invalid Input.")




