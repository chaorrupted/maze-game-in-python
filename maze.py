import random

def initboard(row,column):    
    board = [[0 for i in range(0,row)] for k in range(0,column)]
    
    #borders
    i = 0
    while(i<column):
        board[0][i] = 1
        i+=1
    
    i = 0
    while(i<column):
        board[column-1][i] = 1
        i+=1
 

    for each in board:
        each[0] = 1
        each[column-1] = 1
    
    return board

def drawboard(brod):
    for item in brod:
        for each in item:
            print(each, end="")
        print()

def startgame():
    board = initboard(13,13)
    
    player = [1 ,1]    
    board[player[0]][player[1]] = 7
    
    target = (8 ,8)
    board[target[0]][target[1]] = 8

    #add some walls

    walls = [(1, 3), (1, 4), (1, 8), (2, 6), (2, 10), (3, 2), (3, 3), (3, 4), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 7), (5, 2), (5, 5), (5, 6), (5, 7), (5, 9), (5, 10), (5, 11), (6, 2), (6, 3), (6, 5), (7, 5), (7, 8), (7, 9), (7, 10), (8, 2), (8, 4), (8, 7), (8, 10), (9, 2), (9, 6), (9, 10), (10, 2), (10, 3), (10, 6), (10, 10), (11, 4), (11, 5)]
    for block in walls:
        board[block[0]][block[1]] = 1 
    
    
    print("type \"d\" and hit enter to move left.")
    print("you know the deal with w, a and s.")

    while(1):
        drawboard(board)
        if(player[0] == target[0] and player[1] == target[1]):
            break
        

        inpi = str(input("where next?"))
        if(inpi == "s"):
            if(board[player[0]+1][player[1]] == 1):
                print("that's a WALL over there!")
                continue
            else:
                print()
            board[player[0]][player[1]] = 0
            player[0] += 1
            board[player[0]][player[1]] = 7
        if(inpi == "w"):
            if(board[player[0]-1][player[1]] == 1):
                print("thats a wall over there!")
                continue
            else:
                print()
            board[player[0]][player[1]] = 0
            player[0] -= 1
            board[player[0]][player[1]] = 7
        if(inpi == "d"):
            if(board[player[0]][player[1]+1] == 1):
                print("thats a wall over there!")
                continue
            else:
                print()
            board[player[0]][player[1]] = 0
            player[1] += 1
            board[player[0]][player[1]] = 7
        if(inpi == "a"):
            if(board[player[0]][player[1]-1] == 1):
                print("thats a wall over there!")
                continue
            else:
                print()
            board[player[0]][player[1]] = 0
            player[1] -= 1
            board[player[0]][player[1]] = 7

    while(1):
        yay = random.randint(0,200)

        if(yay % 2 == 0):
            print("CONGRATULATIONS")
        else:
            print("you did it")






#this is here so you can run the game from the terminal
startgame()
