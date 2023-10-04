#print("Hello world!")

"""
Write a calculator program that supports the +, -, *, / for (natural) numbers. exit the program by typing exit

<number> <op> <number> ...
<op> is one of {+, -, *, /}
"""

def calculate(x: int, y: int, symbol: str)  -> float:
    if symbol == "+":
        return x+y
    elif symbol == "-":
        return x-y
    elif symbol == "*":
        return x*y
    elif symbol == "/":
        return x/y
    else:
        raise ValueError("Unknown operation")

operations ="+-*/"
print("Welcome to calculator, type exit to quit.")

while True:
    command = input(">>>")
    command = command.strip()

    if command == "exit":
        break


    index = 0
    symbol =''

    for oper in operations:
        index += command.count(oper)
        if index  == 1 and symbol == '':
            symbol=oper

    if index != 1:
        print("Invalid expression")
        break

    tokens = command.split(symbol)
    oper_left = int(tokens[0].strip())
    oper_right = int(tokens[1].strip())

    print("Result: ",calculate(oper_left, oper_right, symbol))

print("Goodbye!!")