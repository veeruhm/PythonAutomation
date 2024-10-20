'''
to_seconds=24*60*60
name_unit='seconds'

print(f'20 days are {20*to_seconds} {name_unit}')
print(f'35 days are {35*to_seconds} {name_unit}')
print(f'50 days are {50*to_seconds} {name_unit}')
print(f'110 days are {110*to_seconds} {name_unit}')


la=['apple','orange',(1,2),'mango']
abc=list(la[2])
print(abc)
abc[1]=3
la[2]=tuple(abc)
print(la)

la=[(10, 20, 30), (40, 50), (60, 70)]
abc=list(la[2])
print(abc)
abc[1]=100
abc[0],abc[1]=abc[1],abc[0]
la[2]=tuple(abc)
print(la)

la=['cat', (2, 4, 6), 'dog']
abc=list(la[1])
abc.insert(2,5)
la[1]=tuple(abc)
print(la)

my_list = [(1, 2), (3, 4), (5, 6)]
temp_list=list(my_list[0])
temp_list[1]=10
my_list[0]=tuple(temp_list)
temp_list=list(my_list[1])
temp_list[1]=20
my_list[1]=tuple(temp_list)
print(my_list)


#list to tuple

my_list=[1,2,3,4]
tuple_list=tuple(my_list)
print(tuple_list)

#tuple to  list
my_tuple=(1,2,3,4)
my_list=list(my_tuple)
print(my_list)

#list to dict
my_list=[['a',1],['b',2],['c',3],['d',4]]
my_dict=dict(my_list)
print(my_dict)

#dict to list of tuples

my_dict={'a':1,'b':2,'c':3}
list_of_tuples=list(my_dict.items())
print(list_of_tuples)

#tuples to dict

my_tuple=(('a',1),('b',2),('c',3))
my_dict=dict(my_tuple)
print(my_dict)

#dictionary to tuple

my_dict={'a':1,'b':2,'c':3}
my_tuple=tuple(my_dict.items())
print(my_tuple)

# string to list
my_string='hello'
my_list=list(my_string)
print(my_list)
'''
#list to string
my_list=['h', 'e', 'l', 'l', 'o']
my_string=''.join(my_list)
print(my_string)

