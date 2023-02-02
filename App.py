
'''
This is the only module that interacts with the player. It starts off with the player confirming to start the game,
then prints the story and the roles and lets the player choose their role,
finally starts the challenges and prints a win or loss game over message.
'''

import Game

start = input("Press enter to start the game.")  #Once the player presses Enter the game will start

Game.game_story()

role = Game.choose_role()
