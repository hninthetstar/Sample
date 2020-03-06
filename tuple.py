tuple

Tuple - ()
t = 12345, 54321, 'Hello!'
t[0]

t

#tuples may be nested
u = t,(1, 2, 3, 4, 5)
u

#Tuples are immutable.
t[0] = 88888

#but they can contain mutable objects:
v = ([1, 2, 3],[3, 2, 1])
v

fruits = ('apple', 'banana', 'orange', 'kiwi', 'melon', 'mango')
print(fruits[2:5])

#change Tuples value