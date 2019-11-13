from pythonds.basic.stack import Stack
global operandstack
global stackofoperates

operandstack = Stack()
stackofoperates = Stack()

def cal(Op):
    num1 = operandstack.pop()
    num2 = operandstack.pop()

    if Op == "+":
        return float(num2) + float(num1)
    elif Op == "-":
        return float(num2) - float(num1)
    elif Op == "*":
        return float(num2) * float(num1)
    elif Op == "/":
        return float(num2) / float(num1)
    else:
        return float(num2) ** float(num1)


def orderinfix():
    print('pls enter your infix operation seprated by spaces: ')
    calculation = input().split()

    priority = {"^": 4, "*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    for token in calculation:

        if token.isdigit():
            operandstack.push(token)
            

        elif token == "(":
            stackofoperates.push(token)

        elif token == ")":
            operation = stackofoperates.pop()
            while operation != "(":
                operandstack.push(cal(operation))
                operation = stackofoperates.pop()
            

        else:
            while (not stackofoperates.isEmpty()) and (priority[stackofoperates.peek()] >= priority[token]):

                operandstack.push(cal(stackofoperates.pop()))

            stackofoperates.push(token)

    while not stackofoperates.isEmpty():
        operandstack.push(cal(stackofoperates.pop()))

    print(operandstack.pop())
try:
    orderinfix()
except ZeroDivisionError:
    print('Divide by Zero is not Accepted') 