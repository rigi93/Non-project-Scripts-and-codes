#!/usr/bin/env python
#Reduce function for computing matrix multiply A*B

#Input arguments:
#variable n should be set to the inner dimension of the matrix product (i.e., the number of columns of A/rows of B)

import string
import sys
#import numpy

#number of columns of A/rows of B
n = int(sys.argv[1]) 

#Create data structures to hold the current row/column values (if needed; your code goes here)

array=[]

currentkey = None

# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:

	#Remove leading and trailing whitespace
	line = line.strip()
	line = line.translate(None, "'").translate(None, "{}")
	line = line.replace(':','\t')
	#Get key/value 

	key, values = line.split('\t',1)


	#Parse key/value input (your code goes here)
	key =key.strip()
	# Removes the white spaces

	values = values.strip()
	values = values.split(" ")
	# Strips and splits the values of spaces
	val = values[2]
	# val stores the 3rd value in the values field eg A03.0. In this 3.0 is on index 2

	#If we are still on the same key...
	if key==currentkey:

		#Process key/value pair (your code goes here)
		array.append(val)
		# appends the value to an array

		array = map(float, array)
		# converts the entire array to the data type float

	#Otherwise, if this is a new key...
	else:
		#If this is a new key and not the first key we've seen
		if currentkey:

			#compute/output result to STDOUT (your code goes here)
			
			array1 = array[0:len(array)/2]
			# array 1 is a subset of array from 0 to array/2 -1

			array2 = array[len(array)/2:len(array)]
			# array 2 is a subset of array from array/2 to last number
			# The total is the multiplication of x and y and the addition of all such x's and y's having the same key
			total = sum([q*w for q,w in zip(array1,array2)])

			print '%s \t %s' % (currentkey, total)
			
			# Printing the key and the total sum
		currentkey = key
		
		#Process input for new key (your code goes here)
		array = []
		# assign a variable array as an array

		array.append(val)
		
		# append value to the array list

		array = map(float, array)
		# converts the entire array to the data type float

#Compute/output result for the last key (your code goes here)

array1 = array[0:len(array)/2]
# array	1 is a subset of array from 0 to array/2 -1

array2 = array[len(array)/2:len(array)]
# array 2 is a subset of array from array/2 to last number

# The total is the multiplication of x and y and the addition of all such x's and y's having the same key
total = sum([q*w for q,w in zip(array1, array2)])


print '%s \t %s' % (currentkey, total)

#printing the key and the total sum

