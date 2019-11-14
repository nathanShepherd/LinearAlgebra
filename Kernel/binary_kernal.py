
def dot(lhs, rhs, viz=False):
	result = ""
	for row in lhs:
		if viz:
			print(row, rhs)

		summ = 0
		for i in range(len(row)):
			if row[i] == '1' and rhs[i] == '1':
				summ += 1
		result += str(summ % 2) #summ to binary

	print("dot_prod(lhs,",rhs +") =", result)
	return result

v_ham = '''0000000
1001101
0101011
1100110
0010111
1011010
0111100
1110001'''.split("\n")

h_ham = [] # Kernel of V hamming

for i in range(128):
	binary = bin(i).replace("0b", "").rjust(7, '0')
	res = dot(v_ham, binary)
	if int(res, 2) == 0:
		h_ham.append(binary)

print("H hamming, the kernel of V hamming")
for row in h_ham:
	print(str(row))

for row in v_ham:	
	print(dot(h_ham, row))
	
