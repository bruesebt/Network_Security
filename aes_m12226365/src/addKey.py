#This function implements the AddKey step in the AES encryption algorithm

# Description:
# addKey takes an input matrix and a subkey matrix as inputs. For each value in each matrix, the values are XOR'd
# and stored in a list 'values[]'. For example, elements input[0][0] and subkey[0][0] are XOR'd and put into a list 
# to become a new matrix whose value at location [0][0] is the result from the XOR operation. This new matrix is the output.
def addKey(input, subkey):
    values = []
    
    for i, j in zip(input, subkey):
        for k, l in zip(i, j):
            val = int(k, 16) ^ int(l, 16) #this computes the bitwise XOR 
            values.append("{0:02x}".format(val, "x")) #adds the value to the list in hex
            
            
    #convert to list to matrix
    col_1 = values[:4] #first 4 elements
    col_2 = values[4:8] #second 4 elements
    col_3 = values[8:12] #third 4 elements
    col_4 = values[12:] #last 4 elements
    matrix = [col_1, col_2, col_3, col_4]
    return matrix
    