'''
35. Write a program to find the transpose of a matrix

'''

rows = int(input("Enter the Number of rows : " ))
column = int(input("Enter the Number of Columns: "))

print("Enter the elements of Matrix:")
matrix= [[int(input()) for i in range(column)] for i in range(rows)]
print("Matrix: ")
for n in matrix:
    print(n)

result =[[0 for i in range(rows)] for j in range(column)]

for r in range(rows):
   
   for c in range(column):
       result[c][r] = matrix[r][c]

print("Transpose: ")
for r in result:
    print(r)
