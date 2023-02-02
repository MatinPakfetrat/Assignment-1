'''
This is the only module that interacts with the player. It starts off with the player confirming to start the game,
then prints the story and the roles and lets the player choose their role,
finally starts the challenges and prints a win or loss game over message.
'''
import Game

start = input("Press enter to start the game.")  #Once the player presses Enter the game will start

print("The Dragon Slayer")

print('''Welcome slayer! We've been waiting so long for you! Thank you so much for coming!
You see that castle up there? That is where the dragon is.
This village has not seen peace since it took over it!
If you kill the dragon, peace will return, and we will pay you handsomely!
But it will not be easy! There are three challenges ahead of you!''')

while True:   #This loop is for the player to pick their role and will not stop until the player has given the correct input

    role_choice = input("Enter 1 for samurai or 2 for wizard:")   #This lets the player choose their role

    if role_choice == '1':
        print("You picked samurai are you sure of your choice?")
        deny = input("Enter 0 if you want to change your role:")
        if deny == '0':
            continue
        else:
            import samurai
            role = samurai
            break

    elif role_choice == '2':
        print("You picked wizard are you sure of your choice?")
        deny = input("Enter 0 if you want to change your role:")
        if deny == '0':
            continue
        else:
            import wizard
            role = wizard
            break
        
    print("Incorrect input!") 
