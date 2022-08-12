# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14tDX6AFgCFAYD

def express_convert(data):
    stack = []
    res = ''
    for x in data:
        if x.isdecimal():
            res += x
        else:
            if x == '(':
                stack.append(x)
            elif x == '*' or x == '/':
                while stack and (stack[-1] == '*' or stack[-1] == '/'):
                    res += stack.pop()
                stack.append(x)
            elif x == '+' or x == '-':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.append(x)
            elif x == ')':
                while stack and stack[-1] != '(':
                    res += stack.pop()
                stack.pop()
    while stack:
        res += stack.pop()

    return res

def calc_data(data):
    stack = []
    for x in data:
        if x.isdecimal():
            stack.append(x)
        else:
            if x == '+':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a + b)
            elif x == '-':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a - b)
            if x == '*':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a * b)
            elif x == '/':
                b = int(stack.pop())
                a = int(stack.pop())
                stack.append(a // b)

    return stack.pop()
            

for tc in range(1, 11):
    input()
    result = calc_data(express_convert(input()))
    print('#{} {}'.format(tc, result))
