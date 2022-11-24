from pickle import NONE
from colorit import *
import cursor
import os
import WConio2

init_colorit()
os.system('cls')
cursor.hide()


character = "§"
yellow = color(character, Colors.yellow)
red = color(character, Colors.red)
blue = color(character, Colors.blue)
white = color(character, Colors.white)

class Player:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y

        self.matrizPlayer = [
            [yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, blue, blue, blue, blue, blue, blue, blue, None, None, None, None, blue, blue, blue, blue, blue, blue, blue, None, None, None],
            [None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, None, None, None, None, None, None, blue, blue, blue, blue, blue],
            [None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, white],
        ]




player = Player(0, 0)


counter = 0
WConio2.gotoxy(player.x, player.y)
for x in player.matrizPlayer:
    WConio2.gotoxy(player.x, player.y + counter)
    for y in x:
        if (y == None):
            print(' ', end="")
        else:
            print(y, end="")
    print('')
    counter +=1
    
