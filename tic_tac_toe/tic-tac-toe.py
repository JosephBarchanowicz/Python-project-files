def game_board(m):
    print("")
    print("   |   |   ")
    print(f" {m[0]} | {m[1]} | {m[2]} ")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(f" {m[3]} | {m[4]} | {m[5]} ")
    print("   |   |   ")
    print("---+---+---")
    print("   |   |   ")
    print(f" {m[6]} | {m[7]} | {m[8]} ")
    print("   |   |   ")
    print("")

def new_game():
    blank_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return blank_board

def win_check(m, mark):
    return ((m[0] == mark and m[1] == mark and m[2] == mark) or
            (m[3] == mark and m[4] == mark and m[5] == mark) or
            (m[6] == mark and m[7] == mark and m[8] == mark) or
            (m[0] == mark and m[3] == mark and m[6] == mark) or
            (m[1] == mark and m[4] == mark and m[7] == mark) or
            (m[2] == mark and m[5] == mark and m[8] == mark) or
            (m[0] == mark and m[4] == mark and m[8] == mark) or
            (m[2] == mark and m[4] == mark and m[6] == mark))

next_game = True
while next_game == True:
    player1 = 'X'
    player2 = 'O'
    turn = 1
    win = 0
    played = new_game()
    game_board(played)
    check = False
    while check == False:
        if turn % 2 == 0:
            player = player2
        else:
            player = player1
        move_check = False
        while move_check == False:
            move = int(input("Enter position (1-9) player would like to move: "))
            if move < 1 or move > 9:
                print("The position must be a number 1-9, please choose again")
            elif played[move - 1] != ' ':
                print('This move has already been taken, please choose again.')
            else:
                played[move - 1] = player
                turn += 1
                move_check = True

        check = win_check(played, player)
        game_board(played)

        if turn == 10:
            win = 1
            break

    if win == 0:
        print('winner')
    else:
        print('The game ends in a tie')

    game = input('Would you like to play again (y/n): ')
    if game == 'n':
        next_game = False
    else:
        next_game = True
