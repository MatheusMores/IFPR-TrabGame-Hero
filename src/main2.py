import os
import cursor
import WConio2
from colorit import *

from modules.player2 import Player2


def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()
    blue = color('#', (0, 106, 255))

    player_x = 20
    player_y = 10
    counterX, counterY = 0, 0
    count = 0


    player = Player2(player_x, player_y)
    
    while True:
        WConio2.gotoxy(0, 0)
    
        # Bordas de cima
        print(blue * 200)

        counterY = 0
        for j in range(50):
            print(blue,end="")
            
            counterX = 0

            for k in range(198):
                char = " "

                player.controll(count)

                if (k < 22 + player.x and j < 19 + player.y):
                    if k == player.x + counterX and j == player.y + counterY:
                        if player.matrizPlayer[counterY][counterX] != None:
                            char = player.matrizPlayer[counterY][counterX]
                        
                        counterX+=1
                        
                
                print(char, end="")
            
            if j >= player.y:
                counterY += 1
            
            print(blue)

        # Bordas de baixo 
        print(blue * 200)

        count += 1

    
        

iniciarJogo()