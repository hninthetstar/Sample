#sets

Sets.py

includes adata type for sets.
Curly braces or the set() function can be used to create sets.

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)           #unique that duplicates have been removed

'orange' in basket                   #fast membership testing
'crabgrass' in basket

Demostrate set operations on unique from two words

a = set ('abracadabra')
b = set ('alacazam')
a                                    #unique letters in a
									 #letters in a but not in b
a - b								 #letters in a or b or both
a |	b								 #letters in both a and b
a & b								 #letters in a or b but not both
a ^ b

a = b {x for in 'adracadabra' If x not in 'abc'}
a

-------

x = set {'23802348'}
y = set {'57839012'}
x - y
y - x
x * y
y | x
x & y
x

a = {x for x in 'adracadabra' if x not in 'abc'}

fruits = {'apple', 'banana', 'cherry', 'orange', 'kiwi', 'melon', 'mango'}
print('cherry' in fruits)

fruits.add('cucumber')
fruits
fruits.update('grapes')
fruits
fruits.remove('banana')
fruits
fruits.discard('kiwi')
fruits

>>>Dictionaries
#Dictionaries
#Another useful data type built into python is the dictionaries

tel = ('jack', 4098, 'sape', 4139)
tel['sape']
tel['guido']


dict([('sape', 4139),('guido', 4127),('jack', 4098)])
dict(sape=4139, guido=4127, jack=4098)

{x: x**2 for x in (2, 4, 6)}

1 : 1
4 : 16
6 : 36

>>>

{x: x**5 for x in (10, 20, 30, 50)}
{10: 100000, 20: 3200000, 30: 24300000, 50: 312500000}

When looping through dictionaries

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.item():
...     print(k,v)
...
gallahad the pure
robin the b


for i, v in enumerate(['tic', 'tac', 'toe']):
...     print(i,v)
...
0 tic
1 tac
2 toe