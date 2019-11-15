
top = []
for i in range(3):
	for j in range(3):
		top.append([i % 3, j % 3])
print(top)
left = top

res = []
for col in top:
	rrr = ""
	for row in left:
		lhs = (col[0] * row[0]) % 3
		rhs = (col[1] * row[1]) % 3
		if col[1] == row[1]:
			rhs = 0
			lhs = (lhs - 1) % 3
		rrr += str(lhs) + " + " +str(rhs) + "i\t"
	res.append(rrr)

for r in res:
	print(r)
		
