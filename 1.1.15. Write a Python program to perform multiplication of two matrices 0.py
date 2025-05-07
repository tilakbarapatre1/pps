def matmult(A,B):
	rowsA,rowsB=len(A),len(B)
	colsA,colsB=len(A[0]),len(B[0])
	if(colsA!=rowsB):
		print("Cannot multiply the two matrices. Incorrect dimensions.")
		return None
	result=[]
	for i in range(rowsA):
		row=[]
		for j in range(colsB):
			row.append(0)
		result.append(row)
	for i in range(rowsA):
		for j in range(colsB):
			for k in range(colsA):
				result[i][j]+=A[i][k]*B[k][j]
	return result
def readmatrix(name=''):
	matrix=[]
	row=[]
	print(f"Enter values for {name}")
	m=int(input("Number of rows, m = "))
	n=int(input("Number of columns, n = "))
	for i in range(m):
		row=[]
		for j in range(n):
			row.append(int(input(f"Entry in row: {i+1} column: {j+1}\n")))
		matrix.append(row)
		row=[]
	return matrix

matrixA=readmatrix('matrix - A')
matrixB=readmatrix('matrix - B')
print("Matrix - A =",matrixA)
print("Matrix - B =",matrixB)
print("Matrix - A * Matrix- B =",matmult(matrixA, matrixB))