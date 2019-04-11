board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
kloc=[0,0]
floc=[0,3]
ploc=[2,3]
hasflower=0
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
board[kloc[0]][kloc[1]]='k'
if floc[0]<5:
    board[floc[0]][floc[1]]='f'
for i in board:
    print(i)
print()
while hasflower!=2:
    if hasflower==1:
        kloc[0]+=1
        if kloc[0]==2:
            floc=kloc.copy()
            hasflower=2
    elif hasflower==0:
        if (floc[0]==kloc[0]) & (floc[1]==kloc[1]):
            hasflower=1
            floc=[5,5]
        elif kloc[1]<floc[1]:
            kloc[1]+=1
        elif kloc[0]<floc[0]:
            kloc[0]+=1
    board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board[kloc[0]][kloc[1]]='k'
    if floc[0]<5:
        board[floc[0]][floc[1]]='f'
        if (floc[0]==kloc[0]) & (floc[1]==kloc[1]):
            board[floc[0]][floc[1]]='kf'
    for i in board:
        print(i)
    print()
kloc[1]+=1
board=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
board[kloc[0]][kloc[1]]='k'
if floc[0]<5:
    board[floc[0]][floc[1]]='f'
    if (floc[0]==kloc[0]) & (floc[1]==kloc[1]):
        board[floc[0]][floc[1]]='kf'
for i in board:
    print(i)

            
