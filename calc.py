#!/usr/bin/env python3

a = """              .__                     __                .__   
  ____ _____  |  |   ____           _/  |_  ____   ____ |  |  
_/ ___\\__  \ |  | _/ ___\   ______ \   __\/  _ \ /  _ \|  |  
\  \___ / __ \|  |_\  \___  /_____/  |  | (  <_> |  <_> )  |__
 \___  >____  /____/\___  >          |__|  \____/ \____/|____/
     \/     \/          \/                                    """

print(a)
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
