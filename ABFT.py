import numpy
import random
import csv
import sys
import timeit


generateFault = input("Please select a matrix to generate a fault : 1. A matrix; 2. B matrix. 3. C matrix (The product of the first two matrix) 4. Any matrix 5. Nothing")
if generateFault == "4":
    generateFault = str(random.randint(1,4))

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

print ("The product of matrices is : ")
fullMultiplication = numpy.dot(x,y)
print (fullMultiplication)

with open("D:\\matrix3.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(fullMultiplication)

# Calculate the checkSum for each rows and columns of C matrix

checkSumRow = []
for i in range(0,1024):
    sum = 0
    for j in range(0,1024):
        sum += fullMultiplication[i][j]
    checkSumRow.append(sum)

checkSumColumn = []
for i in range(0,1024):
    sum = 0
    for j in range(0,1024):
        sum += fullMultiplication[j][i]
    checkSumColumn.append(sum)

# Gernerate a fault in C matrix

faultRow = random.randint(0,1023)
faultColumn = random.randint(0,1023)

if generateFault != "5":
    print("Injecting an error in row: ")
    print(faultRow)
    print("Injecting an error in column: ")
    print(faultColumn)

if generateFault == "3":
    fullMultiplication[faultRow][faultColumn] += 5


if generateFault == "1":
    firstMatrix[faultRow][faultColumn] += 5

if generateFault == "2":
    secondMatrix[faultRow][faultColumn] += 5

x = numpy.array(firstMatrix, dtype='int64')
y = numpy.array(secondMatrix, dtype='int64')
fullMultiplication2 = numpy.dot(x,y)



# Detect a fault in C matrix

for i in range(0,1024):
    sum = 0
    for j in range(0,1024):
        sum += fullMultiplication[i][j]
    if sum != checkSumRow[i]:
        print("The error is from matrix C, The error row is : ")
        print(i)


for i in range(0,1024):
    sum = 0
    for j in range(0,1024):
        sum += fullMultiplication[j][i]
    if sum != checkSumColumn[i]:
        print("The error is from matrix C, The error column is : ")
        print(i)
        stop = timeit.default_timer()
        print("Time: " , stop - start)
        print("seconds.")
        sys.exit()


for i in range(0,1024):
    sum = 0
    for j in range(0,1024):
        sum += fullMultiplication2[i][j]
    if sum != checkSumRow[i]:
        print("\nThere is an ERROR !!!!! \nThe error is from matrix A or B")
        break

stop = timeit.default_timer()

print("Time: " , stop - start)
print("seconds.")