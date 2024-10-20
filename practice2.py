'''
i = 1
while i <= 5:
    print(i)
    i += 1

n = 10
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print('sum:',sum)

n=3
factorial=1
i=1

while i<=n:
    factorial *= i
    i +=1
print(f'the factorial {n} is {factorial}')

c=25
a,b = 0,1
while a <= c:
    print(a,end=' ')
    a,b = b,a+b
'''

def is_prime(n):
    if n<2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(is_prime(29))




