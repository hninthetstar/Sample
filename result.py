import studentx
import maryi

x = studentx.a["code"]
y = studentx.b["code"]
z = studentx.a["student"]
print(x, ' ', y, ' ', z)

e = studentx.a["age"]
f = studentx.a["mother"]
g = studentx.b["student"]
h = studentx.b["father"]
print(e, ' ', f, ' ', g, ' ', h)

for i in range(len(maryi.a)):
	print(i, maryi.a[i])
