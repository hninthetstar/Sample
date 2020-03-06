import student
import mary

x = student.a["code"]
y = student.b["code"]
z = student.a["student"]
print(x, ' ', y, ' ', z)

e = student.a["age"]
f = student.a["mother"]
g = student.b["student"]
h = student.b["father"]
print(e, ' ', f, ' ', g, ' ', h) 

for i in range(len(mary.a)):
	print(i, mary.a[i])
