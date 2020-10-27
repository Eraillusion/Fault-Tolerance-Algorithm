import numpy
import random
import csv
import sys
import timeit

selectMatrixToInject = input("Please inject an error: 1. To A.  2. To B.  3. To C   4. Nothing")

start = timeit.default_timer()

firstMatrix = []
csvfile1 = open("C:\\matrix1.csv","r",encoding='utf-8-sig')
reader1 = csv.reader(csvfile1)
for line in reader1:
    eachline = []
    for i in line:
        eachline.append(int(i))
    firstMatrix.append(eachline)

secondMatrix = []
csvfile2 = open("C:\\matrix2.csv","r",encoding='utf-8-sig')
reader2 = csv.reader(csvfile2)
for line in reader2:
    eachline = []
    for i in line:
        eachline.append(int(i))
    secondMatrix.append(eachline)

x = numpy.array(firstMatrix, dtype='int64')
y = numpy.array(secondMatrix, dtype='int64')



m = x.shape[0]  #image row size
n = x.shape[1]  #image column size

p = 4     #block row size
q = 4     #block column size

block_array = []
previous_row = 0
for row_block in range(256):
    previous_row = row_block * p
    previous_column = 0
    for column_block in range(256):
        previous_column = column_block * q
        block = x[previous_row:previous_row+p,previous_column:previous_column+q]
        block_array.append(block)

block_array = numpy.array(block_array)

#print(block_array)


block_array2 = []
previous_row = 0
for row_block in range(256):
    previous_row = row_block * p
    previous_column = 0
    for column_block in range(256):
        previous_column = column_block * q
        block = y[previous_row:previous_row+p,previous_column:previous_column+q]
        block_array2.append(block)

block_array2 = numpy.array(block_array2)

#print(block_array2)

fullMultiplication = []
for i in range(len(block_array)):
    fullMultiplication.append(numpy.dot(block_array[i], block_array2[i]))


print(fullMultiplication)

with open("D:\\matrix4.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(fullMultiplication)


faultRow = random.randint(0,1023)
faultColumn = random.randint(0,1023)

if selectMatrixToInject == "1":
    firstMatrix[faultRow][faultColumn] += 5
if selectMatrixToInject == "2":
    secondMatrix[faultRow][faultColumn] += 5
x = numpy.array(firstMatrix, dtype='int64')
y = numpy.array(secondMatrix, dtype='int64')
fullMultiplication2 = numpy.dot(x,y)



block_array = []
previous_row = 0
for row_block in range(256):
    previous_row = row_block * p
    previous_column = 0
    for column_block in range(256):
        previous_column = column_block * q
        block = x[previous_row:previous_row+p,previous_column:previous_column+q]
        block_array.append(block)

block_array = numpy.array(block_array)

#print(block_array)


block_array2 = []
previous_row = 0
for row_block in range(256):
    previous_row = row_block * p
    previous_column = 0
    for column_block in range(256):
        previous_column = column_block * q
        block = y[previous_row:previous_row+p,previous_column:previous_column+q]
        block_array2.append(block)

block_array2 = numpy.array(block_array2)

#print(block_array2)

fullMultiplication2 = []
for i in range(len(block_array)):
    fullMultiplication2.append(numpy.dot(block_array[i], block_array2[i]))

errorBlock = random.randint(0,65536)
if selectMatrixToInject == "3":
    print("Block : ")
    print(errorBlock)
    print(" of C matrix has been injected an Error !")
    fullMultiplication2[errorBlock][random.randint(0,3)][random.randint(0,3)] += 5

for i in range(len(fullMultiplication)):
    if ((fullMultiplication[i] == fullMultiplication2[i]).all()):
        continue
    else:
        print("There is an ERROR!!!! in ")
        print(i)
        print("th block")
        break

stop = timeit.default_timer()

print("Time: " , stop - start)
print("seconds.")