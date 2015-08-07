#!/usr/bin/env python
# HW04_ex00

# Create a program that does the following:
#     - creates a random integer from 1 - 25
#     - asks the user to guess what the number is
#     - validates input is a number
#     - tells the user if they guess correctly
#         - if not: tells them too high/low
#     - only lets the user guess five times
#         - then ends the program
################################################################################
# Imports
from random import randint

# Body

# I have nothing in the body... is this bad?


################################################################################
def main():

	#Generate random integer between 1 and 25
	answer = randint(1,25)
	print "I've generated a number between 1 and 25. You have five chances to guess it correctly."

	#Set number of guesses to 5
	n_guesses = 5

	while (n_guesses > 0):

		#Prompt for user inputted guess
		user_guess = raw_input("Guess an integer between 1 and 25: ")

		#Use try loop to confirm input can be cast as an integer
		try:
			user_guess_int = int(user_guess)

		#If input cannot be cast as an integer, let the user know (don't count as a guess)
		except:
			print "Try again please enter an integer! I'm nice so I won't count this as a guess."

		#If the input can be cast as an integer
		else:
			#Subtract one guess
			n_guesses -= 1

			#If the user is correct
			if user_guess_int == answer:

				#Block below is to ensure grammatically correct try/tries printed
				grammar = " tries."
				if n_guesses == 4:
					grammar = " try."
				#

				print "Correct! You got it in " + str(5-n_guesses) + grammar
				break

			#If the user's guess is less than the answer	
			elif user_guess_int < answer:
				print "Incorrect. Try higher."

			#If the user's guess is greater than the answer (only remaining case)	
			else:
				print "Incorrect. Try lower."

	#If number of guesses reaches 0 before user is correct, finish the loop
	else:
		print "Sorry, you've used up your five chances. Better luck next time!"


if __name__ == '__main__':
    main()