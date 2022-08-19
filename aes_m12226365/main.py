#This program implements the first round of AES encryption. 

#import statements to grab from other modules
from src.initializeData import *
from src.addKey import *
from src.subBytes import *
from src.shiftRows import *
from src.mixColumns import *

############################# Getting the input and subkeys #############################
#open and read the conents of the file 'plaintext.txt' into the string 'message'
with open('data/plaintext.txt') as f:
    message = f.read()
with open('data/subkey_example.txt') as f:
    lines = f.read()
    line0 = lines.split('\n', 1)[0]
    line1 = lines.split('\n', 1)[1]
#our initial input will be formatted using the function initializeData()  
#our subkeys will be formatted using the function initializeSubkeys()
input = initializeData(message)
subkey0 = initializeSubkeys(line0)
subkey1= initializeSubkeys(line1)





############################# Initial AddKey #############################
#Step 0: Technically this occurs before Round 1, so we will include it in its own category. Call addKey() with subkey0.
step_zero = addKey(input, subkey0)
print("After initial AddKey:")
counter = 0
for r in step_zero:
    print(f"Column {counter}:")
    counter += 1
    print(r)
print('\n')




############################# Round 1 #############################
#Step 1: Call subBytes().
step_one = subBytes(step_zero)

#Step 2: Call shiftRows().
step_two = shiftRows(step_one)

#Step 3: Call mixColumns().
step_three = mixColumns(step_two)

#Step 4: Call addKey() again, but this time with subkey1.
step_four = addKey(step_three, subkey1)




############################# Display the Output #############################
#Now that we have finished our round of encryption, print the results.

### Step 1 ###
print("First step:")
counter = 0
for r in step_one:
    print(f"Column {counter}:")
    counter += 1
    print(r)
print('\n')

### Step 2 ###
print("Second step:")
counter = 0
for r in step_two:
    print(f"Column {counter}:")
    counter += 1
    print(r)
print('\n')

### Step 3 ###
print("Third step:")
counter = 0
for r in step_three:
    print(f"Column {counter}:")
    counter += 1
    print(r)
print('\n')

### Step 4 ###
print("Fourth Step:")
counter = 0
for r in step_four:
    print(f"Column {counter}:")
    counter += 1
    print(r)
print('\n')

##### Final Output as a string #####
list = [] #holds a list of bytes
for c in step_four:
    byte = ''
    for r in c:
        byte += r
    list.append(byte)

print(f'The output from round 1 of AES is:\n0x{list[0]} {list[1]} {list[2]} {list[3]}\n') #prints each byte

#### Write the output to file named result.txt ####
file = open('data/result.txt', 'w+') #open file in write mode, create the file if it does not exist.
file.write(list[0] + list[1] + list[2] + list[3]) #write the string to the file
file.close()
