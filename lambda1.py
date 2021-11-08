import os

clear = lambda: os.system("cls")
clear()

remainder = lambda num: num %2

print(remainder(5))

product = lambda x,y: x*y

print(product(2,3))

def test_func(num):
    print(num)
    return lambda x: x*num

result10 =test_func(10)
result10 = lambda x: x *10

result100 = test_func(100)
result100 = lambda x: x * 100

print(result10(9))
print(result100(9))

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(5))

numbers_list = [2,6,8,19,11,14,4,2,5,6]

filtered_list = list(filter(lambda num: (num>7),numbers_list))
print(filtered_list)

mapped_list = list(map(lambda num: num % 2, numbers_list))
print(mapped_list)

def addition(n):
    return n + n 

numbers = [1,2,3,4]
result = list(map(addition, numbers))
print(result)
result = list(map(lambda num: num + num, numbers))
print(result)