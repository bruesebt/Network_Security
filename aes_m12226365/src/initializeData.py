#This function reads the plaintext message, turns it into ASCII, and returns a matrix as the initial state.

# This function takes each character in the message, formats the character into its hex value, and then
# appends the hex to a list. This list is then converted into a matrix.
def initializeData(message):
    ascii_values = []
    for c in message:
        ascii_values.append("{0:02x}".format(ord(c), "x"))
    #instead of just the list, now we make it into a matrix
    col_1 = ascii_values[:4] #first 4 elements
    col_2 = ascii_values[4:8] #second 4 elements
    col_3 = ascii_values[8:12] #third 4 elements
    col_4 = ascii_values[12:] #last 4 elements
    matrix = [col_1, col_2, col_3, col_4]
    return matrix

# This function takes a subkey (a string of characters) and converts it to a matrix of bytes.
def initializeSubkeys(subkey):
    values = []
    for i, j in zip(subkey[0::2], subkey[1::2]): #since the subkey is in hex, we really want every two characters as an element
        values.append(i+j)

    #instead of just the list, now we make it into a matrix
    col_1 = values[:4] #first 4 elements
    col_2 = values[4:8] #second 4 elements
    col_3 = values[8:12] #third 4 elements
    col_4 = values[12:] #last 4 elements
    matrix = [col_1, col_2, col_3, col_4]
    return matrix


