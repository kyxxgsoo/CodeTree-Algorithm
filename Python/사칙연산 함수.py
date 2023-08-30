def addFunc(n1, n2):
    return n1 + n2

def subFunc(n1, n2):
    return n1 - n2

def mulFunc(n1, n2):
    return n1 * n2

def divFunc(n1, n2):
    return n1 // n2

n1, op, n2 = input().split()
result = 0

if op == '+':
    result = addFunc(int(n1), int(n2))
elif op == '-':
    result = subFunc(int(n1), int(n2))
elif op == '*':
    result = mulFunc(int(n1), int(n2))
elif op == '/':
    result = divFunc(int(n1), int(n2))

if op == '+' or op == '-' or op == '*' or op == '/':
    print(n1, op, n2, '=', result)
else:
    print(False)