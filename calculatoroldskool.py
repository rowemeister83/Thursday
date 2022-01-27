#trying the old prelearning calculator, from memory!

def calculator(a, b, operator):

    if (operator == "+"):
        output = a + b
    elif operator == '-':
        output = a - b
    elif operator == '*':
        output = a * b
    elif operator == '/':
        output = a / b


    else:
        output = 0

    return output


print(calculator(2000, 456, "+"))
print(calculator(2000, 456, "-"))
print(calculator(2000, 5656565656565656444, "-"))
print(calculator(2000, 5656568989524245574, "*"))