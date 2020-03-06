

loop.py

-while Loops
-for Loops

Condition it true, while loop execute a set of statements

x = 1
while x < 7:
		print(x)
		x += 1



While loop require variable ready.

x = 1
while x < 7:
		print(x)
		if x == 5:
			break
		x += 1

x = 50
while x < 100:
		print(x)
		if x == 5:
			break
		x += 1


For Loops

#for loops is iterating over a sequence

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)

#Looping in a string

for x in "pineapple":
	print(x)

#The break Statement

# stop after condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	print(x)
	if x == "pineapple":
		break

---------------

#stop before condition

fruits = ["apple", "banana", "orange", "pineapple", "coconut", "cucumber"]
for x in fruits:
	if x == "pineapple"
			break
	print(x)

#The continue Statement - stop the current iteration

for x in fruits:
	if x == "pineapple"
			continue
	print(x)

#The range() Function - a set of code a specified number of times
for x in range(10):
	print(x)

for x in range(10, 100):
	print(x)

for x in range(10, 100, 5):
	print(x)


#Nested Loops

numberA = [1, 2, 3, 4, 5]
numberB = [1, 2, 3, 4, 5]

for x in NumberA:
	for y in NumberB:
		print(x,y)

#Nested Loops

numberA = [1, 2, 3, 4, 5]
numberB = [1, 2, 3, 4, 5]
numberC = [1, 2, 3, 4, 5]

for x in NumberA:
	for y in NumberB:
		for z in numberC:
				print(x,y)
#pass

for x in [1, 2, 3, 4, 5]:
	pass

---------

words = ['cat', 'window', 'defenestrate']
for w in words:
	print(w, len(w))


------------

for n in range(2, 21):
	for x in range(2, n):
			if n % x == 0:
				print(n, 'equals', x, '*', n//x)
				break
			else:
				#loop fell through without finding a factor
				print(n, 'it a prime number')

-------------

for num in range(2, 10):
	if num % 2 == 0:
		print("Found an even number", num)
		continue
		print("Found a number", num)

---------------

>>> Finbonacci #module Folder














































































