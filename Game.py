'''
This module implements the game data and logic and determines if the game was won or lost.
'''

def game_story():
    '''
    This function prints the story of the game.
    '''
    print("The Dragon Slayer")

    print('''Welcome slayer! We've been waiting so long for you! Thank you so much for coming!
You see that castle up there? That is where the dragon is.
This village has not seen peace since it took over it!
If you kill the dragon, peace will return, and we will pay you handsomely!
But it will not be easy! There are three challenges ahead of you!''')

def choose_role():
    '''
    This function is for the player to pick their role and will not stop until the player has given the correct input.
    '''
    while True:   

        role_choice = input("Enter 1 for samurai or 2 for wizard:")   #This lets the player choose their role

        if role_choice == '1':
            print("You picked samurai are you sure of your choice?")
            deny = input("Enter 0 if you want to change your role:")
            if deny == '0':
                continue
            else:
                import samurai
                return samurai

        elif role_choice == '2':
            print("You picked wizard are you sure of your choice?")
            deny = input("Enter 0 if you want to change your role:")
            if deny == '0':
                continue
            else:
                import wizard
                return wizard
            
        print("Incorrect input!") 
