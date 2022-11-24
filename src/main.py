import os
import cursor
import WConio2
from colorit import *

from modules.player import Player
#from initFunctions.setFont import setFontSize

def iniciarJogo():
    init_colorit()
    os.system('cls')
    cursor.hide()
    #setFontSize(6)

    cont = 0
    player_x = 10
    player_y = 10

    player1 = Player(player_x, player_y)


    while True:
        player1.controll()
        
        player1.printPlayer()





        
        



iniciarJogo()