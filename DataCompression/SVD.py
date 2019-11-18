# Singular value decomposition

# Let A* represent matrix A transpose

# SVD(A) = UEV*
# U --> eigan basis for AA*
# V --> eigan basis for A*A

# Characteristic eqn for eigan values
# Eigan vectors are in ker(A - dot(lambda, I))
# Using Gram-Shmidt for orthonormalization
# 	normalize v1 --> u1
#	[v2 - dot(u1, v2)u1] --> v2 perp
#	normalize v2 perp --> u2
#	[v3 - dot(v3, u2)u2 - dot(v3, u1)u1] - v3 perp
#	normalize v3 perp --> u3
