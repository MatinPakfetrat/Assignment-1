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
But it will not be easy! There are three challenges ahead of you! And you need to win them all to succeed!''')

def choose_role():
    '''
    This function is for the player to pick their role and will not stop until the player has given the correct input.
    '''
    while True:   

        role_choice = input("Enter 1 for samurai or 2 for wizard:")   #This lets the player choose their role

        if role_choice == '1':
            print("You picked samurai are you sure of your choice?")
            deny = input("Enter 0 if you want to change your role:")   #This is for the player to confirm their choice or pick a different role
            if deny == '0':
                continue
            else:
                print("Great choice!")
                import samurai
                return samurai

        elif role_choice == '2':
            print("You picked wizard are you sure of your choice?")
            deny = input("Enter 0 if you want to change your role:")
            if deny == '0':
                continue
            else:
                print("Great choice!")
                import wizard
                return wizard
            
        print("Incorrect input!") 

def game():
    '''
    This function starts the game by calling all of the other functions and evaluates the result of the dice throw and prints win or loss.
    '''

    losses = 0  #This variable is used to determine if the game is won or not
    game_story()
    role = choose_role()
    start_challenges = input("Press Enter to start the challenges.")
    result = role.challenge_1()
    print("You got", result)

    if result < 3:
        print(f"Critical loss! The challenge is lost and Strength is decreased from {role.Strength} to {role.Strength-1}.")
        losses += 1
    elif result < 5:
        print("Loss! The challenge is lost, but there is no change to your Strength.")  
        losses += 1
    elif result < 8:
        print("Win! The challenge is won, but there is no change to your strength.")
    else:
        print(f"Critical win! The challenge is won, and your Strength is increased from {role.Strength} to {role.Strength+1}.")
    result = role.challenge_2()
    print("You got", result)

    if result < 4:
        print(f"Critical loss! The challenge is lost and Dexterity is decreased from {role.Dexterity} to {role.Dexterity-1}.")
        losses += 1
    elif result < 7:
        print("Loss! The challenge is lost, but there is no change to your Dexterity.")  
        losses += 1
    elif result < 9:
        print("Win! The challenge is won, but there is no change to your Dexterity.")
    else:
        print(f"Critical win! The challenge is won, and your Dexterity is increased from {role.Dexterity} to {role.Dexterity+1}.")              
    result = role.challenge_3()
    print("You got", result)

    if result < 4:
        print(f"Critical loss! The challenge is lost and Intelligence is decreased from {role.Intelligence} to {role.Intelligence-1}.")
        losses += 1
    elif result < 8:
        print("Loss! The challenge is lost, but there is no change to your Intelligence.")  
        losses += 1
    elif result < 11:
        print("Win! The challenge is won, but there is no change to your Intelligence.")
    else:
        print(f"Critical win! The challenge is won, and your Intelligence is increased from {role.Intelligence} to {role.Intelligence+1}.")    

    if losses > 0:
        print(f"Unfortunately you lost {losses} challenge(s)!\nGame Over")
        restart = input("Enter 1 if you want to play again:")
        if restart == '1':
            game()
    else:
        print("Congratulations! You won all of the challenges and beat the dragon! You truly are an amazing Dragon Slayer.\nGame Over")        
        restart = input("Enter 1 if you want to play again:")
        if restart == '1':
            game()
