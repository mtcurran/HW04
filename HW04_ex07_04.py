#!/usr/bin/env python
# HW04_ex07_04

# The built-in function eval takes a string and evaluates it using the Python
# interpreter.
# For example:
    
#     >>> eval('1 + 2 * 3')
#     7
#     >>> import math
#     >>> eval('math.sqrt(5)')
#     2.2360679774997898
#     >>> eval('type(math.pi)')
#     <type 'float'>

# Write a function called eval_loop that iteratively prompts the user, takes the
# resulting input and evaluates it using eval, and prints the result.

# It should continue until the user enters 'done', and then return the value of
# the last expression it evaluated.

################################################################################
# Imports
import math

# Body

def eval_loop():

		user_input = raw_input("Input here: ")

		while user_input != "done":
			print eval(user_input)
			eval_loop()
			return



################################################################################
def main():
	# Remove this line and uncomment below once eval_loop is defined.
	try:
		eval_loop()
   	except:
   		print "Invalid entry."
    

if __name__ == '__main__':
    main()