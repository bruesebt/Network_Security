#This function implements the ShiftRows step of the AES encryption algorithm.

# Description:
# shiftRows implements the shifting according to the AES encryption. The first row remains the same, the second row shifts to
# the right one place, the third row shifts all values to the right two places, and the fourth row shifts all values to the right 
# three places. All this shifting wraps when necessary (i.e. the first element goes the end of the row).
def shiftRows(matrix):
    #First row remains the same. Here is the shift for row 2:
    temp = matrix[0][1]
    matrix[0][1] = matrix[1][1]
    matrix[1][1] = matrix[2][1]
    matrix[2][1] = matrix[3][1]
    matrix[3][1] = temp

    #Shift for row 3:
    temp = matrix[0][2]
    matrix[0][2] = matrix[2][2]
    matrix[2][2] = temp

    temp = matrix[1][2]
    matrix[1][2] = matrix[3][2]
    matrix[3][2] = temp

    #Shift for row 4:
    temp = matrix[3][3]
    matrix[3][3] = matrix[2][3]
    matrix[2][3] = matrix[1][3]
    matrix[1][3] = matrix[0][3]
    matrix[0][3] = temp

    return matrix