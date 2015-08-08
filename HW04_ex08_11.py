#!/usr/bin/env python
# HW04_ex08_11

# The following functions are all intended to check whether a string contains 
# any lowercase letters, but at least some of them are wrong. For each function, 
# describe what the function actually does (assuming that the parameter is a
# string).

# Do not merely paste the output as a counterexample into the documentation 
# string, explain what is wrong.

################################################################################
# Body

def any_lowercase1(s):
    """Explain what is wrong, if anything, here.
    This function will return a result only for the first letter checked. If the
    case of the first letter of the string is different from the case of any other
    letters, like in "Dog", the return will be incorrect.
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False

def any_lowercase2(s):
    """Explain what is wrong, if anything, here.
    This function does not evaluate a letter in the word, but rather checks a
    lowercase "c" only, thus the return will always be true, even for a string
    that is in all capital letters like NASA.
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

def any_lowercase3(s):
    """Explain what is wrong, if anything, here.
    This function returns the result of only the last letter in a string. If the
    case of the last letter is different from the case of any other letters, like
    in "palm treE", the return will be incorrect.
    """
    for c in s:
        flag = c.islower()
    return flag

def any_lowercase4(s):
    """Explain what is wrong, if anything, here.
    I think this function works properly in all cases.
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

def any_lowercase5(s):
    """Explain what is wrong, if anything, here.
    This function doesn't check for any lowercase letters, but rather checks if all
    letters are lowercase. For a word like "Absolutely", it fails because at least one
    letter is capital.
    """
    for c in s:
        if not c.islower():
            return False
    return True

################################################################################
def main():

    # Remove print("Hello World!") and for each function above that is wrong, 
    # call that function with a string for which the function returns
    # incorrectly.
    # ex.: any_lowercase_("thisstringmessesupthefunction")

    print any_lowercase1("Dog")
    print any_lowercase2("NASA")
    print any_lowercase3("palm treE")
    print any_lowercase5("Absolutely")


    

if __name__ == '__main__':
    main()