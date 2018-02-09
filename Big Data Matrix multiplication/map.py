#!/usr/bin/env python
# map function for matrix multiply
#Input file assumed to have lines of the form "A,i,j,x", where i is the row index, j is the column index, and x is the value in row i, column j of A. Entries of A are followed by lines of the form "B,i,j,x" for the matrix B. 
#It is assumed that the matrix dimensions are such that the product A*B exists. 

#Input arguments:
#m should be set to the number of rows in A, p should be set to the number of columns in B.
 
import sys
import string
#import numpy

#number of rows in A
m = int(sys.argv[1]) 

#number of columns in B
p = int(sys.argv[2])


# input comes from STDIN (stream data that goes to the program)
for line in sys.stdin:
    
	#Remove leading and trailing whitespace
	line = line.strip()

	#Split line into array of entry data
	entry = line.split(",")
    
	# Set row, column, and value for this entry
	row = int(entry[1])
	col = int(entry[2])
	value = float(entry[3])

	#If this is an entry in matrix A...
	if (entry[0] == "A"):
		
		#Generate the necessary key-value pairs
 		#(your code goes here)
		for q in range(0,p):
		# For an element in matrix A the outputs it provides value to are = columns in B
			info = dict()

			# enables info (information) to be in the form of key, value
			info[str(row)+str(q)] = "A " + str(col) + " "+ str(value)

			# Left side of the code creates key incrementing the Columns portion in B
                        # Right side gives the value pair eg: A  0  2.0

			print(info) 
			# prints the info stored.

	#Otherwise, if this is an entry in matrix B...
	else:
		
		#Generate the necessary key-value pairs
 		#(your code goes here)
		for w in range(0,m):
		# For an element in matrix B the outputs it provides value to are = rows in A 
			info=dict()
			# enables info (information) to be in the form of key, value
			info[str(w)+str(col)] = "B " + str(row) + " " + str(value)
			
			# Left side of the code creates key incrementing the rows portion in A
			# Right side gives the value pair eg: B  0  2.0
			
			print(info) 
			# prints the info stored.
        
