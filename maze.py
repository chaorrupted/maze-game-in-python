from random import randint, choice

hero = 'ğ'
path = 'o'
dest = 'ü'
wall = ['(',')','?']
congrats=[
        "ŞĞÜÜÜ",
        "FFFRRRRPPPP",
        "*ÖPÜCÜK SESLERİ*",
        "SERPİL YALVARIRIM GERİ DÖN!!!!!",
        "ğ(",
        "şğ.",
        "şğüü",
        "şbommm",
        "mmmhhhhççççç"
        ]
error_wall=[
        "şğbom ğü(",
        "ğ?",
        "frrrp.",
        "rröööÖÖÖÖÖÖÖÖ!",
        "aaaaaaaaaaaaa!",
        "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA!!!!"
        ]
error_input=[
        "ulan",
        "UlAnn",
        "Ulan .d",
        "u l a nnnnnnn !!@!!",
        "u LAN",
        '?',
        '?',
        '?',
        '?',
        '?',
        '?',
        ]

def initboard(row,column):    
    board = [[path for i in range(0,row)] for k in range(0,column)]
    
    #borders
    i = 0
    while(i<column):
        board[0][i] = choice(wall)
        i+=1
    
    i = 0
    while(i<column):
        board[-1][i] = choice(wall)
        i+=1
 

    for each in board:
        each[0] = choice(wall)
        each[-1] = choice(wall)
    
    return board

def drawboard(brod):
    for item in brod:
        for each in item:
            print(each, end=" ")
        print()

def move(player, board, direction):
    def can_move(player, board, deltax, deltay):
        if board[player[0]+deltax][player[1]+deltay] in wall:
            return False
        else:
            return True
    deltax,deltay = 0,0
    if direction == 'k':
        deltax = -1
    elif direction == 'h':
        deltay = -1
    elif direction == 'j':
        deltax = 1
    elif direction == 'l':
        deltay = 1
    else:
        print(choice(error_input))
        return

    if can_move(player, board, deltax, deltay):
        board[player[0]][player[1]] = path
        player[0] += deltax
        player[1] += deltay
        board[player[0]][player[1]] = hero

    else:
        print(choice(error_wall))
            

def startgame():
    board = initboard(13,13)
    
    player = [1 ,1]    
    board[player[0]][player[1]] = hero
    
    target = (8 ,8)
    board[target[0]][target[1]] = dest

    #add some walls

    walls = [(1, 3), (1, 4), (1, 8), (2, 6), (2, 10), (3, 2), (3, 3), (3, 4), (3, 7), (3, 8), (3, 9), (3, 10), (4, 1), (4, 7), (5, 2), (5, 5), (5, 6), (5, 7), (5, 9), (5, 10), (5, 11), (6, 2), (6, 3), (6, 5), (7, 5), (7, 8), (7, 9), (7, 10), (8, 2), (8, 4), (8, 7), (8, 10), (9, 2), (9, 6), (9, 10), (10, 2), (10, 3), (10, 6), (10, 10), (11, 4), (11, 5)]
    for block in walls:
        board[block[0]][block[1]] = choice(wall)
    
    
    print("type \"d\" and hit enter to move right.")
    print("you know the deal with w, a and s.")
    print(*wall, sep=", ", end="")
    print("'s are walls. ", hero," is you.", sep='')
    print(dest,"is the exit.")
    
    while(1):
        drawboard(board)
        if(player[0] == target[0] and player[1] == target[1]):
            break
        

        sibel_canin_sari_kedisi = str(input('ğü? '))
        move(player, board, sibel_canin_sari_kedisi)
    while("MERHABA ARKADASLAR KANALIMA HOSGELDINIZ"):
        print(choice(congrats))


#this is here so you can run the game from the terminal
startgame()
