num1 = float(input("Wprowadź pierwszą cyfrę:"))
op= input("Wprowadź operator:")
num2 = float(input("Wprowadź drugą cyfrę:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("ERROR")
