
number1 = input("Enter a first number > ")
number2 = input("Enter a second number > ")

number1 = int(number1)
number2 = int(number2)

operation = input("Enter a sign > ")

if operation == "+":
    print(number1 + number2)
elif operation == "-":
    print(number1 - number2)
elif operation == "/":
    print(number1 / number2)
elif operation == "*":
    print(number1 * number2)
else:
    print("This is not a valid operation")










