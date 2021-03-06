"""
PEDAC
P- 
find the sum of diagonal numbers from left to right and right to left
and subtract them to find the difference and return the difference 

E-
sqaure matrix = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]

diagonal_difference(squarematrix) == 3

D-
input = nested array
output = integer

A-
start at the first array to the last array 
store the indexes that start at the last of the array and go up the last array 
the first array will store the first and last index 
the second will

"""
def diagonal_difference(matrix):
    ltr, rtl = 0, 0
    for i in range(len(matrix)):
        ltr += matrix[i][i]
        rtl += matrix[i][ len(matrix) -1 -i]
        
    return abs(ltr - rtl)
    
squarematrix = [[2, 3, 4, 5],
                [5, 5, 5,10],
                [0, 7, 13, 10],
                [9, 9, 9, 9]]

print(diagonal_difference(squarematrix) == 3)
