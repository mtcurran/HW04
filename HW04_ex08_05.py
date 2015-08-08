#!/usr/bin/env python
# HW04_ex08_05

# The following program counts the number of times the letter a appears in a 
# string:

#     word = 'banana'
#     count = 0
#     for letter in word:
#         if letter == 'a':
#             count = count + 1
#     print count

# Encapsulate this code in a function named "count", and generalize it so that 
# it accepts the string and the letter as arguments.

################################################################################
# Imports


# Body

def count_letters(w, l):
	result = 0
	for let in w:
		if let == l:
			result += 1

	report = "There are " + str(result) + " " + str(l) + "'s in the word " + str(w)

	return report


################################################################################
def main():

    # Remove print("Hello World!") and add several functions calls to count()
    # below, passing various strings and letters
    
    print count_letters("python", "y")
    print count_letters("mercury", "r")
    print count_letters("mississippi", "s")
    print count_letters("antidisestablishmentarianism", "i")

    

if __name__ == '__main__':
    main()