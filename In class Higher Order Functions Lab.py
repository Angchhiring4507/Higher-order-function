#Angchhhiring Tamang
#200569497


from functools import reduce
from math import sqrt

# Higher Order Functions
def operate(func, x, y):
    return func(x, y)

# Test with a lambda function
print(operate(lambda a, b: a * b, 5, 3))  # Expected: 15

# Filtering Out Data
ages = [15, 22, 34, 40, 65, 18, 23, 30, 45, 50]

# Using filter
less_than_20 = list(filter(lambda age: age < 20, ages))
between_20_and_40 = list(filter(lambda age: 20 <= age <= 40, ages))
greater_than_40 = list(filter(lambda age: age > 40, ages))

print(less_than_20)
print(between_20_and_40)
print(greater_than_40)

# Transforming Data with map()
add_5_years = list(map(lambda age: age + 5, ages))
halve_age = list(map(lambda age: age / 2, ages))
sqrt_age = list(map(lambda age: sqrt(age), ages))

print(add_5_years)
print(halve_age)
print(sqrt_age)

# Complex Transformation with reduce
product_of_ages = reduce(lambda x, y: x * y, ages)
print(product_of_ages)

# Custom Higher-Order Function: napply
def napply(funcs, x):
    result = x
    for func in funcs:
        result = func(result)
    return result

f1 = lambda x: x + 2
f2 = lambda x: x * 2
f3 = lambda x: x - 3

print(napply([f1, f2, f3], 5))  # Expected: ((5+2)*2)-3 = 9

# Compose Functions
def compose(f, g):
    return lambda x: f(g(x))

f = lambda x: x + 2
g = lambda x: x * 3
h = compose(f, g)

print(h(3))  # Expected: (3*3)+2 = 11

# Custom Higher-Order Function: alternator
def alternator(f, g, lst):
    return [f(elem) if idx % 2 == 0 else g(elem) for idx, elem in enumerate(lst)]

f = lambda x: x * 2
g = lambda x: x - 2
lst = [1, 2, 3, 4, 5]

print(alternator(f, g, lst))  # Expected: [2, 0, 6, 2, 10]
