from pythonds.basic.stack import Stack
global operandstack
global stackofoperates
# This function separate the infix FOR EXAPMLE (2+3) will be [ '(', '2', '+', '3', ')' ]
def separation(operation):
    lis = []
    x = ''
    for i in range(len(operation)):
       if operation[i] not in "+-*/^)(" :
            x += operation[i]
       if (operation[i] in "+-*/^)(") :
           if x=='':
                lis += operation[i]
           else:
            lis += [x]
            lis += operation[i]
            x = ''
       if  i == len(operation) - 1:
           lis += [x]
        
    return lis
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
    print('pls enter your infix operation: ')
    c = input()
    calculation=separation(c)
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
    print('Divide by Zero is not Accepted..pls Try Again')
    while not stackofoperates.isEmpty():
        stackofoperates.pop()
    while not operandstack.isEmpty():
        operandstack.pop()
    orderinfix()
    