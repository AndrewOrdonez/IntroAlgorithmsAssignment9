 
#battleship
from random import randint
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
randx= int(randint(0, len(board)-1))
randy= int(randint(0, len(board)-1))
j=4
while j>0:
    j-=1
    for i in board:
        print(i)
    userx = int(input("What column do you want to attack?"))
    usery = int(input("what row do you want ot attack?"))
    board[usery][userx]='X'
    if userx==randx:
        if usery==randy:
            print("HIT you sunk my battleship")
            break
        print("Miss")
    else:
        print("MISS")
if j==0:
    print("out of turns, GAME OVER")



