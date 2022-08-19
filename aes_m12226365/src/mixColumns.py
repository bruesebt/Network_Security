#This function implements the MixColumns step of the AES encryption algorithm.


#Predetermined matrix that we multiply against the input. Each list within the list is a column.
mix_matrix = [['02', '01', '01', '03'], 
             ['03', '02', '01', '01'], 
             ['01', '03', '02', '01'], 
             ['01', '01', '03', '02']]


# Description: 
# multiply_bytes takes two bytes, byte1 being the byte from the input matrix in mixColumns, and byte2 being the byte
# from 'mix_matrix'. Since mix_matrix only contains values '01', '02', '03', the if statements within the function
# handle all three possibilities seperately for efficiency purposes. 
# In byte multiplication in GF(2^8), if the leading bit in byte1 is a '1', we must left shift first (fx * x), but also
# bitwise XOR this byte with 00011011, which in hexidecimal is '1b'. This can be seen in lines 24 and 35.
def multiply_bytes(byte1, byte2):  
    #fx * (x + 1) 
    if byte2 == '03':
        product = int(byte1, 16) << 1 & 255 #left shift the byte, same as fx * x

        #if the first bit is a 1, we need to XOR with 00011011
        if int(byte1, 16) >> 7 == 1:
            product = product ^ int('1b', 16) #XOR with 00011011

        new_product = product ^ int(byte1, 16) #(fx * x) + fx
        return "{0:02x}".format(new_product, 'x') #returns the value in hex

    #fx * x
    elif byte2 == '02':
        product = int(byte1, 16) << 1 & 255 #left shift the byte, same as fx * x

        #if the first bit is a 1, we need to XOR with 00011011
        if int(byte1, 16) >> 7 == 1:
            product = product ^ int('1b', 16) #XOR with 00011011

        return "{0:02x}".format(product, 'x') #returns the product in hex

    #same as fx * 1 = fx
    elif byte2 == '01':
        return byte1
    
def add_bytes(byte1, byte2):
    sum = int(byte1, 16) ^ int(byte2, 16) #bitwise XOR
    return "{0:02x}".format(sum, 'x') #returns the value in hex


# Description: 
# mixColumns takes a matrix as an input, and uses the predetermined matrix 'mix_matrix' as a multiplicator.
# The function uses helper functions 'add_bytes' to perform bitwise XOR operations for addition, as well as
# 'multiply_bytes' to perform the byte multiplication in GF(2^8). 
def mixColumns(input):
    result = [['00' for x in range(4)] for y in range(4)] #creates a blank matrix for us to insert our values into
    
    for i in range(len(mix_matrix)):
        for j in range(len(input[0])):
            for k in range(len(input)):
 
                # resulted matrix
                val = multiply_bytes(input[i][k], mix_matrix[k][j]) #multiplies the input value by the given matrix value
                result[i][j] = add_bytes(str(result[i][j]), val) #the product value 'val' is added to the existing value in the matrix
                

    return result  



