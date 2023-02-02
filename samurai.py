'''
This module implements the data and logic associated with the first role (e.i., samurai).
It determines the attributes and the challenges of the role.
'''

Strength = 2
Dexterity = 1
Intelligence = 0

def challenge_1():
    '''
    This function implements the first challenge.
    '''
    from random import randrange

    print("Your first challenge is to make your way to the castle and fight the guards that stand in your way. (This challenge is based on your Strength.)")
    display_result = input("Press Enter to display the result.")
    return randrange(2, 13)
