# the fibonacci with generetor
def fibo(num):
    a = 0
    b = 1
    total = 0
    for item in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for i in fibo(20):
    print(i)


# fibonacci num in general
def fibo2(num):
    a = 0
    b = 1
    total = 0
    for item in range(num - 1):
        temp = a
        a = b
        b = temp + b
    return a


print(f'the fibo is  {fibo2(20)}')
