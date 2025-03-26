operator = input("Enter an operator (+ - * /):")
num1 = float(input("Enter a Number :"))
num2 = float(input("Enter a Number :"))

if operator == "+":
    Answer = num1 + num2
    print(round(Answer,3))
elif operator == "-":
    Answer = num1 - num2
    print(round(Answer, 3))
elif operator == "*":
    Answer = num1 * num2
    print(round(Answer, 3))
elif operator == "/":
    Answer = num1 * num2
    print(round(Answer, 3))
else:
    print(f"{operator} is not a valid operator")