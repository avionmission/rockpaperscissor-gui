import random
import os
import sys
from io import StringIO

user_score = 0
ai_score = 0

class PlayGame():

    def update_score(self, u, ai):
        global user_score
        global ai_score

        if u == ai:
            ai_score += 0
        if u.isspace() or u not in ['r', 'p', 's']:
            quit()
        elif u == 'p' and ai == 'p':
            user_score += 0
        elif u == 'r' and ai == 'r':
            user_score += 0
        elif u == 's' and ai == 's':
            user_score += 0
        elif u == 'p' and ai == 'r':
            user_score += 1
        elif u == 'r' and ai == 's':
            user_score += 1
        elif u == 'p' and ai == 'r':
            user_score += 1
        elif u == 's' and ai == 'p':
            user_score += 1
        else:
            ai_score += 1
        self.print_screen()

    def print_screen(self):
        global user_score
        global ai_score

        for i in range(len("Play stone paper scissor with your AI!")): print("-", end='')
        print("\nPlay stone paper scissor with your AI!")
        print("\nEnter r for rock, p for paper and s for scissor and q to quit the game.\n")

        print ("Score - You: " + str(user_score) + " AI: " + str(ai_score) )

        if (user_score > 1) and (ai_score > 1) and user_score != ai_score:
            if user_score > ai_score:
                print(f'You are winning by {user_score-ai_score} points\n')
            else:
                print(f'AI is winning by {ai_score-user_score} points\n')

        # take input from user
        x = input("You: ")
        sys.stdout.write("\033[K") #clear line

        # make a random move
        y = random.choice(['r', 'p', 's'])
        print("AI: "+y)

        self.update_score(x, y)

gameplay = PlayGame()
gameplay.print_screen()