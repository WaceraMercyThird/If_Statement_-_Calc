

#  if statements the comparision
def max_num(num1, num2, num3):
    if num1>= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >=num3:
        return num2
    else: 
        return num3

print(max_num(9,3,0))
# Building a better calculater
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter seconf number: "))
if op == "+":
    print(num1 +num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid opertor")

