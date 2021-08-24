import random
import os
import sys
from io import StringIO

user_score = 0
ai_score = 0


class PlayGame:

    def update_score(self, u, ai):
        global user_score
        global ai_score

        if u == ai:
            ai_score += 0
        if u == 'q':
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

    def print_screen(self):
        global user_score
        global ai_score

        print("------------------------------------")
        print("Play stone paper scissor with your AI!")
        print("\nEnter r for rock, p for paper and s for scissor and q to quit the game.\n")

        print("Score - AI-1: " + str(user_score) + " AI-2: " + str(ai_score))
        if (user_score > 1) and (ai_score > 1):
            if user_score > ai_score:
                print(f'Player-1 is winning by {user_score - ai_score} points\n')
            else:
                print(f'Player-2 is winning by {ai_score - user_score} points\n')
        # take input from user
        x = random.choice(['r', 'p', 's'])
        print(f"Player-1: {x}")

        # make a random move
        y = random.choice(['r', 'p', 's'])
        print("Player-2: " + y)

        self.update_score(x, y)


gameplay = PlayGame()
for num in range(10000):
    gameplay.print_screen()
