
print("---------hello in calc app---------")
print("-----------------------------------")

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
op = input("Enter the operation (+, -, /, *): ")

if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "/":
    if y != 0:
        print(x / y)
    else:
        print("Error: Division by zero")
elif op == "*":
    print(x * y)
else:
    print("Error: Invalid operation")

