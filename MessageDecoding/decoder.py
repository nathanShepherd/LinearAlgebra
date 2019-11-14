import csv

msg = []
with open('message.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
     
    for row in csv_reader:
    	msg.append([int(num) for num in row])


gBig =  '''1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 1 0 0 1
1 1 1 0 0
1 0 1 1 0
1 0 0 1 1'''

g = gBig.replace(" ", "").split("\n")

'''
Convert alphabet to binary representation
Associate conversion in dictionary {binary: letter}
Encode each letter using gBig
Compare encrypted message to encrypted alphabet
Recover letter codes in message changed during transmission
  (msg letter codes differ from encypted letters by <= 1 bit)
'''


alpha_orig = [bin(num).replace("0b","").rjust(5, '0') for num in range(27)]
#print(alpha_orig)

letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(" ")
letters = [" "] + letters #space is a letter
alpha = {}

def dot(lhs, rhs):
	result = ""
	for row in lhs:
		print(row, rhs)

		summ = 0
		for i in range(len(row)):
			if row[i] == '1' and rhs[i] == '1':
				summ += 1
		result += str(summ % 2) #summ to binary

	print("dot_prod(gBig,",rhs +") =", result)
	return result

#Encode each letter using gBig
prod = []
for i in range(len(alpha_orig)):
	prod.append( dot(g, alpha_orig[i]))

#Associate alphabet encoding to each letter
alpha = dict(zip(prod, letters))

print('\n',len(alpha), alpha)

decoded = "" #;print(msg)

for char in msg:
	#cast char into binary string from array representation
	char = str(char)[1:-1].replace(", ", "")

	for i in range(len(char)):
		temp = char
		if temp not in alpha:					
			if temp[i] == '0':
				temp = temp[:i]+ '1' +temp[i + 1:]
			else:
				temp = temp[:i]+ '0' +temp[i + 1:]
		
		if temp in alpha:
			decoded += alpha[temp]
			break

print("\nDecoded message with len",len(decoded),":", decoded)
