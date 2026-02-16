from tkinter import *
windowX = 750
windowY = 550
middle = windowX/2

Xturn = True
Oturn = False

game_end = False

tacGrid = ['N', 'N', 'N', 'N', 'N', 'N', 'N', 'N', 'N']
def tictacToe(pos, value):
    global Oturn
    global Xturn
    success = False
    if not game_end:
        if pos == 'a1' and tacGrid[0] == 'N':
            boxTopLeft.config(text=value)
            tacGrid[0] = value
            success = True
        elif pos == 'a2' and tacGrid[1] == 'N':
            boxTopMid.config(text=value)
            tacGrid[1] = value
            success = True
        elif pos == 'a3' and tacGrid[2] == 'N':
            boxTopRight.config(text=value)
            tacGrid[2] = value
            success = True
        elif pos == 'b1' and tacGrid[3] == 'N':
            boxMidLeft.config(text=value)
            tacGrid[3] = value
            success = True
        elif pos == 'b2' and tacGrid[4] == 'N':
            boxMid.config(text=value)
            tacGrid[4] = value
            success = True
        elif pos == 'b3' and tacGrid[5] == 'N':
            boxMidRight.config(text=value)
            tacGrid[5] = value
            success = True
        elif pos == 'c1' and tacGrid[6] == 'N':
            boxBotLeft.config(text=value)
            tacGrid[6] = value
            success = True
        elif pos == 'c2' and tacGrid[7] == 'N':
            boxBotMid.config(text=value)
            tacGrid[7] = value
            success = True
        elif pos == 'c3' and tacGrid[8] == 'N':
            boxBotRight.config(text=value)
            tacGrid[8] = value
            success = True
        
        if success:
            if value == 'O':
                turn_label.config(text="X's Turn")
                Xturn = True
                Oturn = False
            elif value == 'X':
                turn_label.config(text="O's Turn")
                Xturn = False
                Oturn = True
        check_winner()

def check_winner():
    global game_end
    winner = 'null'
    # O wins
    if ((tacGrid[0]=='O' and tacGrid[1]=='O' and tacGrid[2]=='O') or
        (tacGrid[0]=='O' and tacGrid[3]=='O' and tacGrid[6]=='O') or
        (tacGrid[3]=='O' and tacGrid[4]=='O' and tacGrid[5]=='O') or
        (tacGrid[6]=='O' and tacGrid[7]=='O' and tacGrid[8]=='O') or
        (tacGrid[1]=='O' and tacGrid[4]=='O' and tacGrid[7]=='O') or
        (tacGrid[2]=='O' and tacGrid[5]=='O' and tacGrid[8]=='O') or
        (tacGrid[0]=='O' and tacGrid[4]=='O' and tacGrid[8]=='O') or
        (tacGrid[6]=='O' and tacGrid[4]=='O' and tacGrid[2]=='O')):
        turn_label.config(text='O Wins!')

        if tacGrid[0] == 'O':
            boxTopLeft.config(bg='green')
        if tacGrid[1] == 'O':
            boxTopMid.config(bg='green')
        if tacGrid[2] == 'O':
            boxTopRight.config(bg='green')
        if tacGrid[3] == 'O':
            boxMidLeft.config(bg='green')
        if tacGrid[4] == 'O':
            boxMid.config(bg='green')
        if tacGrid[5] == 'O':
            boxMidRight.config(bg='green')
        if tacGrid[6] == 'O':
            boxBotLeft.config(bg='green')
        if tacGrid[7] == 'O':
            boxBotMid.config(bg='green')
        if tacGrid[8] == 'O':
            boxBotRight.config(bg='green')

        if tacGrid[0] == 'X':
            boxTopLeft.config(bg='red')
        if tacGrid[1] == 'X':
            boxTopMid.config(bg='red')
        if tacGrid[2] == 'X':
            boxTopRight.config(bg='red')
        if tacGrid[3] == 'X':
            boxMidLeft.config(bg='red')
        if tacGrid[4] == 'X':
            boxMid.config(bg='red')
        if tacGrid[5] == 'X':
            boxMidRight.config(bg='red')
        if tacGrid[6] == 'X':
            boxBotLeft.config(bg='red')
        if tacGrid[7] == 'X':
            boxBotMid.config(bg='red')
        if tacGrid[8] == 'X':
            boxBotRight.config(bg='red')

        game_end = True

    # X wins
    elif ((tacGrid[0]=='X' and tacGrid[1]=='X' and tacGrid[2]=='X') or
          (tacGrid[3]=='X' and tacGrid[4]=='X' and tacGrid[5]=='X') or
          (tacGrid[6]=='X' and tacGrid[7]=='X' and tacGrid[8]=='X') or
          (tacGrid[0]=='X' and tacGrid[3]=='X' and tacGrid[6]=='X') or
          (tacGrid[1]=='X' and tacGrid[4]=='X' and tacGrid[7]=='X') or
          (tacGrid[2]=='X' and tacGrid[5]=='X' and tacGrid[8]=='X') or
          (tacGrid[0]=='X' and tacGrid[4]=='X' and tacGrid[8]=='X') or
          (tacGrid[6]=='X' and tacGrid[4]=='X' and tacGrid[2]=='X')):
        turn_label.config(text='X Wins!')

        if tacGrid[0] == 'X':
            boxTopLeft.config(bg='green')
        if tacGrid[1] == 'X':
            boxTopMid.config(bg='green')
        if tacGrid[2] == 'X':
            boxTopRight.config(bg='green')
        if tacGrid[3] == 'X':
            boxMidLeft.config(bg='green')
        if tacGrid[4] == 'X':
            boxMid.config(bg='green')
        if tacGrid[5] == 'X':
            boxMidRight.config(bg='green')
        if tacGrid[6] == 'X':
            boxBotLeft.config(bg='green')
        if tacGrid[7] == 'X':
            boxBotMid.config(bg='green')
        if tacGrid[8] == 'X':
            boxBotRight.config(bg='green')

        if tacGrid[0] == 'O':
            boxTopLeft.config(bg='red')
        if tacGrid[1] == 'O':
            boxTopMid.config(bg='red')
        if tacGrid[2] == 'O':
            boxTopRight.config(bg='red')
        if tacGrid[3] == 'O':
            boxMidLeft.config(bg='red')
        if tacGrid[4] == 'O':
            boxMid.config(bg='red')
        if tacGrid[5] == 'O':
            boxMidRight.config(bg='red')
        if tacGrid[6] == 'O':
            boxBotLeft.config(bg='red')
        if tacGrid[7] == 'O':
            boxBotMid.config(bg='red')
        if tacGrid[8] == 'O':
            boxBotRight.config(bg='red')

        game_end = True

window = Tk()
window.geometry(f"{windowX}x{windowY}")
window.title("Tic-Tac-Toe")
window.config(bg="#a17899")

turn_label = Label(window, text="X's Turn", font=('Arial', 20))

#Boxes
boxTopLeft = Button(window,activebackground='gray', bg="white",font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('a1', 'X' if Xturn else 'O'))
boxTopMid = Button(window,activebackground='gray', bg="white", font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('a2', 'X' if Xturn else 'O'))
boxTopRight = Button(window,activebackground='gray', bg="white", font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('a3', 'X' if Xturn else 'O'))
boxMidLeft = Button(window,activebackground='gray', bg="white", font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('b1', 'X' if Xturn else 'O'))
boxMid = Button(window,activebackground='gray', bg="white",font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('b2', 'X' if Xturn else 'O'))
boxMidRight = Button(window,activebackground='gray', bg="white",font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('b3', 'X' if Xturn else 'O'))
boxBotLeft = Button(window,activebackground='gray', bg="white",font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('c1', 'X' if Xturn else 'O'))
boxBotMid = Button(window,activebackground='gray', bg="white", font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('c2', 'X' if Xturn else 'O'))
boxBotRight = Button(window,activebackground='gray', bg="white", font=('Arial', 50), width=3, height=1, command=lambda: tictacToe('c3', 'X' if Xturn else 'O'))


boxTopLeft.place(x=middle - 150, y=100, anchor='center')
boxTopMid.place(x=middle, y=100, anchor='center')
boxTopRight.place(x=middle + 150, y=100, anchor='center')

boxMidLeft.place(x=middle - 150, y=250, anchor='center')
boxMid.place(x=middle, y=250, anchor='center')
boxMidRight.place(x=middle +150, y=250, anchor='center')

boxBotLeft.place(x=middle - 150, y=400, anchor='center')
boxBotMid.place(x=middle, y=400, anchor='center')
boxBotRight.place(x=middle + 150, y=400, anchor='center')

turn_label.place(anchor='center', x= middle, y=500)


window.mainloop()
