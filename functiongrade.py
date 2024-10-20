'''
def abc(perc):
    if perc<35:
        grade='fail'
    elif perc>=35 and perc<=50:
        grade='third class'
    elif perc>50 and perc>60:
        grade='second class'
    else:
        grade='first class'
    return grade
perc=input('enter the percantage')
print('the grade is:',abc(int(perc))


def abc(set1,set2):
    set3=set1&set2
    return set3
set1={1,2,3,4}
set2={1,6,5,3,2}
ans=abc(set1,set2)
print('common elements from two sets are:',ans)


#s1='veeranna'
#for ab in s1:
 #   print(ab)

s1='veeranna'
length=len(s1)
#print('the lenthee is:',length)
for id in range(length):
    print(id,':',s1[id])


s='python'
length=len(s)
for id in range(length-1,-1,-1):
    print(id,':',s[id])

s='programing'
vowels='aeiou'
count=0
for char in s:
    if char in vowels:
        count +=1
print('the number of vowels:',count)

for num in range(2,6):
    for div in range(2,num):
        if num % div == 0:
            print(f'{num} is not prime')
            break
        else:
            print(f'{num} is prime')

for i in range(1,4):
    for j in range(1,4):
        print(f'i={i} and j={j}')

for num in range(1,6):
    if num ==3:
        continue
        print(num)

num=[1,2,3,4,5,6,7,8,9,10]
for nu in num:
    if nu % 2==0:
        print(f'{nu} is even')
    else:
        print(f'{nu} is odd')

for i in range(1,11):
    for j in range(1,11):
        print(f'{i}*{j}={i*j}',end='\t')
    print()

for num in range(2, 10):  # Loop through numbers from 2 to 9
    is_prime = True  # Assume num is prime
    for divisor in range(2, num):  # Check divisors from 2 up to num-1
        if num % divisor == 0:  # If num is divisible by any divisor
            is_prime = False  # Set flag to False, meaning num is not prime
            break  # Exit the inner loop once we find a divisor
    if is_prime:  # After checking all divisors, if still prime
        print(f'{num} is prime')
    else:
        print(f'{num} is not prime')

for i in range(1,7):
    print(i)

for i in range(2,11,2):
    print(i)

fruits=['apple','banana','chery']
for fruit in fruits:
    print(fruit)

for i in range(1,4):
    for j in range(1,4):
        print(f'({i},{j})')


for i in range(1,8):
    if i == 3:
        break
    print(i)

for i in range(1,8):
    if i == 4:
        continue
    print(i)

word='python'
for char in word:
    print(char)

numbers=[1,2,3,4,5]
total=0
for num in numbers:
    total +=num
print('total sum is : ',total)

for i in range(1,4):
    print(i)
else:
    print('loop successfully completed')

student_grades={'veeru':90,'ravi':90,'ambi':92}
for student,grade in student_grades.items():
    print(f'{student}:{grade}')

numbers=[10,12,27,35,46,88]
max_num=numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
print('max number is:',max_num)

colors=['red','green','blue']
for index,color in enumerate(colors):
    print(f'index {index}: {color}')

for i in range(5,0,-1):
    print(i)

names=['veeru','chetu','vaidu','varnu']
age=[37,30,7,2]
for names,age in zip(names,age):
    print(f'{names} is {age} years old')
'''