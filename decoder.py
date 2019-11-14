import csv
import numpy as np

msg = []
with open('message.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
     
    for row in csv_reader:
    	msg.append([int(num) for num in row])

msg = np.array(msg)

gBig =  '''1 0 0 0 0
0 1 0 0 0
0 0 1 0 0
0 0 0 1 0
0 0 0 0 1
1 1 0 0 1
1 1 1 0 0
1 0 1 1 0
1 0 0 1 1'''

g = []
for elem in gBig.split("\n"):
	g.append([int(num) for num in elem.split(" ")])

g = np.array(g)

#print(np.dot(g, [0, 0, 0, 0, 1]))
alpha_orig = np.array([bin(num)[2:].ljust(5, '0') for num in range(27)])

letters = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split(" ")
alpha = {}
for i, l in enumerate(letters):
	arr = []
	for j in range(len(alpha_orig[i])):
		arr.append(int(alpha_orig[i][j]))
	
	######## TODO: this dot product in binary
	encoded = np.dot(g, np.array(arr))
	alpha[str(encoded)] = l

print(alpha)

decoded = ""
print(msg)
for char in msg:
	char = str(char)	
	for i in range(len(char)):
		temp = char
		if temp[i] == '0':
			temp = temp[:i]+ '1' +temp[i + 1:]
		else:
			temp = temp[:i]+ '0' +temp[i + 1:]
		if temp in alpha:
			decoded += alpha[temp]
print(decoded)

