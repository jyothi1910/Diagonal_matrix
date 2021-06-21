# sum of diagonals

def printDiagonaldiff(mat, n):

	r_diag = 0
	l_diag = 0
	for i in range(n):
		r_diag += mat[i][i]
		l_diag += mat[i][n - i - 1]
		
	print("right Diagonal:", r_diag)
	print("left Diagonal:", l_diag)
	diag = r_diag - l_diag
	print("difference between diagonal is:",(diag) )

# Driver code
matrix = [[12,15,17,17],
          [16,18,91,78],
          [45,86,98,90],
          [67,87,35,89]]

printDiagonaldiff(matrix, 4)


