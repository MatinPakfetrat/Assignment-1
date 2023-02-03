'''
This module implements the data and logic associated with the first role (e.i., wizard).
It determines the attributes and the challenges of the role.
'''

Strength = 0  #This is the wizard's Strength
Dexterity = 1  #This is the wizard's Dexterity
Intelligence = 2  #This is the wizard's Intelligence

def challenge_1():
    '''
    This function implements the first challenge.
    '''
    from random import randrange

    print("Your first challenge is to make your way to the castle and fight the guards that stand in your way. (This challenge is based on your Strength. Difficulty: Easy)")
    display_result = input("Press Enter to display the result.")
    return randrange(2, 13)

def challenge_2():
    '''
    This function implements the second challenge.
    '''
    from random import randrange

    print("A knight just appeared! Your second challenge is to defeat the knight defending the dragon. (This challenge is based on your Dexterity. Difficulty: Normal)")
    display_result = input("Press Enter to display the result.")
    return randrange(2, 13)

def challenge_3():
    '''
    This function implements the third challenge.
    '''
    from random import randrange

    print("Alright this is the third and final challenge. Beat the dragon and it is over! (This challenge is based on your Intelligence. Difficulty: Hard)")
    display_result = input("Press Enter to display the result.")
    return randrange(2, 13)
