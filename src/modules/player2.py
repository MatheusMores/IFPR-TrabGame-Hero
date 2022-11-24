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

class Player2:
    def __init__(self, player_x, player_y):
        self.x = player_x
        self.y = player_y

        self.matrizPlayer = [
            [None, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, None, None, None, None],
            [None, None, None, None, yellow, yellow, yellow, yellow, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, None, None, None, None, None, None, None],
            [None, None, None, None, red, red, red, red, None, None, None, None, red, red, red, red, red, red, red, red, red, red],
            [None, None, None, None, red, red, red, red, None, None, None, None, None, None, None, red, red, red, red, red, red, red],
            [None, None, blue, blue, blue, blue, blue, blue, None, None, None, None, blue, blue, blue, blue, blue, blue, blue, None, None, None],
            [None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue, blue],
            [None, None, None, None, blue, blue, blue, blue, None, None, None, None, None, None, None, None, None, blue, blue, blue, blue, blue],
            [None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, None, None, None, None],
            [None, None, None, None, None, None, None, None, None, None, white, white, white, white, white, white, white, white, white, white, white, white],
        ]
    
    def controll(self, count):
        if WConio2.kbhit():
            (key, symbol) = WConio2.getch()
    
            if symbol == 'a':
                if count%3 == 0:
                    self.x-=1
    
            if symbol == 'd':
                if count%3 == 0:
                    self.x+=1
    

    