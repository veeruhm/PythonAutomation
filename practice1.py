#Sum of Even Numbers in a Range
'''
total=0
for i in range(1,11):
    if i % 2 ==0:
        total+=i
print('total sum of even number is :',total)


#Product of All Numbers in a List
numbers=[1,2,3,4,5]
product=1
for num in numbers:
    product *= num
print(f'the product is :',product)

#Find the Largest Number in a List
numbers=[10,23,45,28,9,234]
max_num=numbers[0]
for num in numbers:
    if num>max_num:
        max_num=num
print(f'the maximum number is :',num)

#Sum of List Elements
numbers=[1,2,3,4,5]
total=0
for num in numbers:
    total +=num
print(f'the total sum is :',total)

#Sum of Squares of Numbers
total=0
for i in range(1,6):
    total += i **2
print(f'sum of squared number is :',total)

#Count the Number of Even Numbers in a List

a=[1,2,3,4,5,6,7,8,9,10]
even_count=0
for num in a:
    if num % 2==0:
        even_count +=1
print(f'the even number count is :',even_count)

#Find the Average of Numbers in a List

numbers=[10,20,30,40,50]
total=0
for num in numbers:
    total+=num
average=total/len(numbers)
print(f'the average numbers :',average)

word='python'
reversed_word=''
for char in word:
    reversed_word=char+reversed_word
print('reversed string :',reversed_word)

# sum of odd numbers
numbers=[1,2,3,4,5,6,7,8,9,10]
odd_sum=0
for num in numbers:
    if num % 2!=0:
        odd_sum +=num
print(f'the sum of odd numbers are :',odd_sum)

s='i am veeranna melmuri working as etl test engineer'
cap=s.title()
print(cap)

list=[1,2,3,4,5,6,7,8]
a=[]
for num in list:
    if num % 2 !=0:
        a.append(num)
print(f'even numbers:',a)
'''

