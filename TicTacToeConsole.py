a1 = ' '
a2 = ' '
a3 = ' '
b1 = ' '
b2 = ' '
b3 = ' '
c1 = ' '
c2 = ' '
c3 = ' '


valid_positions = ['a1','a2','a3','b1','b2','b3','c1','c2','c3']


marked_list = []
game_end = False


def print_board():
    print(f'a |{a1}|{a2}|{a3}|')
    print(f'b |{b1}|{b2}|{b3}|')
    print(f'c |{c1}|{c2}|{c3}|')
    print('   1 2 3')


print_board()


xturn = True
oturn = False


def xchange_board(m):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,xturn,oturn
    
    if m not in valid_positions:
        print("Invalid position")
        return

    if m in marked_list:
        print("Position taken, try again.")
        return

    if m == 'a1':
        a1 = 'X'
    elif m == 'a2':
        a2 = 'X'
    elif m == 'a3':
        a3 = 'X'
    elif m == 'b1':
        b1 = 'X'
    elif m == 'b2':
        b2 = 'X'
    elif m == 'b3':
        b3 = 'X'
    elif m == 'c1':
        c1 = 'X'
    elif m == 'c2':
        c2 = 'X'
    elif m == 'c3':
        c3 = 'X'
    else:
        print("Invalid position")
        return

    xturn = False
    oturn = True

    marked_list.append(m)
    check_draw()


def ochange_board(m):
    global a1,a2,a3,b1,b2,b3,c1,c2,c3,xturn,oturn
    
    if m not in valid_positions:
        print("Invalid position")
        return
    
    if m in marked_list:
        print("Position taken, try again.")
        return
    
    if m == 'a1':
        a1 = 'O'
    elif m == 'a2':
        a2 = 'O'
    elif m == 'a3':
        a3 = 'O'
    elif m == 'b1':
        b1 = 'O'
    elif m == 'b2':
        b2 = 'O'
    elif m == 'b3':
        b3 = 'O'
    elif m == 'c1':
        c1 = 'O'
    elif m == 'c2':
        c2 = 'O'
    elif m == 'c3':
        c3 = 'O'
    else:
        print("Invalid position")
        return

    oturn = False
    xturn = True

    marked_list.append(m)
    check_draw()


def check_winner():
    global game_end

    # O wins
    if ((a1=='O' and a2=='O' and a3=='O') or
        (b1=='O' and b2=='O' and b3=='O') or
        (c1=='O' and c2=='O' and c3=='O') or
        (a1=='O' and b1=='O' and c1=='O') or
        (a2=='O' and b2=='O' and c2=='O') or
        (a3=='O' and b3=='O' and c3=='O') or
        (a1=='O' and b2=='O' and c3=='O') or
        (a3=='O' and b2=='O' and c1=='O')):
        print("O wins!")
        game_end = True

    # X wins
    elif ((a1=='X' and a2=='X' and a3=='X') or
          (b1=='X' and b2=='X' and b3=='X') or
          (c1=='X' and c2=='X' and c3=='X') or
          (a1=='X' and b1=='X' and c1=='X') or
          (a2=='X' and b2=='X' and c2=='X') or
          (a3=='X' and b3=='X' and c3=='X') or
          (a1=='X' and b2=='X' and c3=='X') or
          (a3=='X' and b2=='X' and c1=='X')):
        print("X wins!")
        game_end = True


def check_draw():
    global game_end
    if len(marked_list) == 9 and not game_end:
        print("Draw!")
        game_end = True


while not game_end:
    if xturn:
        move = input("X turn:")
        xchange_board(move)
        print_board()
        check_winner()

    if oturn and not game_end:
        move = input("O turn:")
        ochange_board(move)
        print_board()
        check_winner()
