# Singular value decomposition

# Let A* represent matrix A transpose

# SVD(A) = UEV*
# U --> eigan basis for AA*
# V --> eigan basis for A*A

# Characteristic eqn for eigan values

from copy import copy
from itertools import permutations

def permute(n):
	# For pattern product:
	# 	Each position in each row is the column
	# 	Each elem in each row is the row
	return list(permutations([i for i in range(n)]))


v = permute(3)
print(v)

## Determinant of nxn matrix
def det(A):
	# let p be a pattern of the matrix A
	# det = for all p in A --> sum( (sign of p)(prod p) )
	# pattern:
	#	the product of every element with every other element
	#	except when row or col is shared with previous operand
	# sign of p:
	#	number of inversions from I in pattern
	
	representatives = permute(len(A[0]))
	for index in range(len(A[0])):
		pass		
# Eigan vectors are in ker(A - dot(lambda, I))
# Using Gram-Shmidt for orthonormalization
# 	normalize v1 --> u1
#	[v2 - dot(u1, v2)u1] --> v2 perp
#	normalize v2 perp --> u2
#	[v3 - dot(v3, u2)u2 - dot(v3, u1)u1] - v3 perp
#	normalize v3 perp --> u3
