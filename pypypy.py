#Задание 1 map filter
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 15, 35, 65, 99, 120]
print(list(filter(lambda elem: elem < 5, list1)))
print(list(map(lambda x: x/2, list1)))
print(list(map(lambda x: x/2, filter(lambda x: x > 17, list1))))
print(sum(list(map(lambda x: x**2, filter(lambda x: 9 < x < 100 and x%9 == 0, list1)))))
#Задание 2 generator
from math import factorial
def factorials(n):
    x = [factorial(i) for i in range(1, n+1)]
    yield x
print(*list(factorials(7)))
#Задание 3
def fibonacci(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
        yield f1**2
print(*fibonacci(7))
#Задание 4
def generator():
    for i in range(ord('а'), ord('я')+1):
        yield chr(i)
print(*generator())
#Задание 5
for i in range(ord('а'), ord('я')+1):
    print(chr(i), end=' ')
#Задание 6 function as object
def arithmetic_operation(operation):
    if operation == '+':
        return lambda x,y: x+y
    elif operation == '-':
        return lambda x,y: x-y
    elif operation == '*':
        return lambda x,y: x*y
    elif operation == '/':
        return lambda x,y: x/y
operation = arithmetic_operation('+')
print(operation(1, 4))
#Задание 7
def same_by(characteristic, objects):
    return len(set(map(characteristic, objects))) == 1 if objects else True
values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
#Задание 8
def print_operation_table(operation, num_rows=9, num_columns=9):
    for i in range(1, num_rows+1):
        for j in range(1, num_columns+1):
            print(f'{operation(i, j):<4}', end=' ')
            print()
print_operation_table(lambda x, y: x*y, 5)
#Задание 9

# я хз че сделать как потом сделаю

#Задание 10 standard features

#Задание 11
list2 = [3, 6, -8, 2, -78, 1, 23, -45, 9]
list2.sort()
print(list2)
#Задание 12
#Задание 13
#Задание 14
#Задание 15
#Задание 16
#Задание 17
#Задание 18
#Задание 19

