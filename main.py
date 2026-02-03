# 1
def max_number(a, b):
    if a >= b:
        return a
    return b

# 2
def empty_function():
    pass

# 3
def even_numbers(n):
    for number in range(2, n + 1, 2):
        yield number

# 4
def test_max_number():
    assert max_number(10, 2), 'Ошибка для кейса a >= b '
    assert max_number(2, 10), 'Ошибка для кейса a <= b '
    assert max_number(10, 10), 'Ошибка для кейса a == b '


# 1
print(max_number(10, 2), max_number(5, 8), max_number(3, 3))

# 3
for num in even_numbers(11):
    print(num)

# 4
test_max_number()
