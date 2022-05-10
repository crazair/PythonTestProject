import math


def print_s(text):
    print(text)

print_s('привет!')


t = ['d', 's', 'l']

def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

#Генераторы списков
def capitalize_all2(t):
    return [s.capitalize() for s in t]
def only_upper(t):
    return [s for s in t if s.isupper()]

#Синтаксический сахар
x = 1
y = math.log(x) if x > 0 else float('nan')

#Выражения-генераторы
g = (x**2 for x in range(5))
print(next(g))
print(next(g))
print(next(g))

s = sum(x ** 2 for x in range(100))
print(s)

any([False, False, True])
any(letter == 'т' for letter in 'монти')
all([False, False, True])

def has_duplicates(t):
    return len(set(t)) < len(t)

l = [1, 2, 4]
l.insert(2, 3)
print(l)

stack = [3]
stack.append(42) # [3, 42]
stack.pop() # 42 (stack: [3])
print(stack)
stack.pop() # 3 (stack: [])


## Данные
txt = ['lambda functions are anonymous functions.',
 'anonymous functions dont have a name.',
 'functions are objects in Python.']
## Однострочник
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)
## Результаты
print(list(mark))

## Данные (ежедневные котировки акций ($))
price = [[9.9, 9.8, 9.8, 9.4, 9.5, 9.7],
 [9.5, 9.4, 9.4, 9.3, 9.2, 9.1],
 [8.4, 7.9, 7.9, 8.1, 8.0, 8.0],
 [7.1, 5.9, 4.8, 4.8, 4.7, 3.9]]
## Однострочник
sample = [line[::2] for line in price]
## Результат
print(sample)


## Данные
companies = {
 'CoolCompany' : {'Alice' : 33, 'Bob' : 28, 'Frank' : 29},
 'CheapCompany' : {'Ann' : 4, 'Lee' : 9, 'Chrisi' : 7},
 'SosoCompany' : {'Esther' : 38, 'Cole' : 8, 'Paris' : 18}}
## Однострочник
illegal = [x for x in companies if any(y<9 for y in companies[x].values())]

print(illegal)

## Однострочник
is_palindrome1 = lambda phrase: phrase == phrase[::-1]
def is_palindrome(phrase): return phrase == phrase[::-1]
## Результат
print(is_palindrome("anna"))
print(is_palindrome("kdljfasjf"))

print('12345'[::-1])


def practicum():
    args = {
        0: 'Практикум',
        1: 'Яндекс',
    }
    args[0] = 'Яндекс'
    args[1] = 'Практикум'
    return [a for a in args]

print(practicum())