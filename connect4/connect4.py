#include <iostream>
#include <iomanip>
#include <string>
#include <vector>

from tkinter import *


class Game():
    def __init__(self):
        
        #constructor for making the main window 
        # instead of using lambda. I defined some small call back functions called clicked for each slot
       
        window = Tk()
        window.title('M O J G A N  C  O  N  N  E  C  T  4')
        window.geometry('600x600')

        self.board = []

        self.boardFrame = Frame(window, width=400, borderwidth=60) # for drawing the actual game board
                                                                   # It should be packed from the bottom
        self.boardFrame.pack(side = BOTTOM)

        self.outputText = Label()

        self.outputFrame = Frame(window, width=250, borderwidth=5) # for creating the label that should be packed on Top
        self.outputFrame.pack(side = TOP)

        self.clearBoard()
        # for reseting the game and starting it all oevragain
        self.resetFrame = Frame(window, width=100, borderwidth=5) # diemsions of the reset label 
        self.resetFrame.pack(side = TOP)
        reset = Button(self.resetFrame, borderwidth=1, text = 'Play Again', command=self.clearBoard).grid(row = 0, column = 0)
        # Slot buttons
        slotButtonFrame = Frame(window, width=400, borderwidth=20)
        slotButtonFrame.pack(side = TOP)
        slot1 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 1', command=self.clicked1)
        slot1.pack(side = LEFT)
        slot2 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 2', command=self.clicked2)
        slot2.pack(side = LEFT)
        slot3 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 3', command=self.clicked3)
        slot3.pack(side = LEFT)
        slot4 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 4', command=self.clicked4)
        slot4.pack(side = LEFT)
        slot5 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 5', command=self.clicked5)
        slot5.pack(side = LEFT)
        slot6 = Button(slotButtonFrame, borderwidth=8, text = 'Slot 6', command=self.clicked6)
        slot6.pack(side = LEFT)

        window.mainloop()
        
    def clicked1(self):
        self.play(1)

    def clicked2(self):
        self.play(2)

    def clicked3(self):
        self.play(3)

    def clicked4(self):
        self.play(4)

    def clicked5(self):
        self.play(5)

    def clicked6(self):
        self.play(6)
    # function for placing a chip to a slot, and also deciding if a move is valid or anybody has won
    def play(self, slotChoice):
        if self.isValidChoice(slotChoice, self.board): # mking sure if the column is not full
            self.playMove(len(self.board) - 1, int(slotChoice) - 1, self.player, self.board, ) #placing a chip to a slot
            won = self.hasWon(self.board)
            stalemate = self.isStalemate(self.board, 0)

            if won or stalemate:
                if stalemate:
                    self.message = str('****** Game Over. Nobody wins. :) ******')
                    self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
                    with open("Output.txt", "w") as text_file:
                        text_file.write("You're both equal. Nobody wins! :)")
                    return
                else:
                    self.message = str('** Congratulations! Player %s won! **' % self.player)
                    self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
                    with open("Output.txt","w") as text_file:
                        text_file.write("The Winner is Player: %s" % self.player)
                    return
            if self.player == 'XX':
                self.player = 'OO'
            else:
                self.player = 'XX'

            self.message = str('***** Player %s, choose a slot. *****' % self.player)
            outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
            

            

    def clearBoard(self):

        self.board = [['  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  '],
                      ['  ', '  ', '  ', '  ', '  ', '  ']]

        self.player = 'XX'
        # reading from a two diemnsional array and creating lebels for players
        b00 = Label(self.boardFrame, borderwidth=18, text=self.board[0][0]).grid(row = 0, column = 0)
        b01 = Label(self.boardFrame, borderwidth=18, text=self.board[0][1]).grid(row = 0, column = 1)
        b02 = Label(self.boardFrame, borderwidth=18, text=self.board[0][2]).grid(row = 0, column = 2)
        b03 = Label(self.boardFrame, borderwidth=18, text=self.board[0][3]).grid(row = 0, column = 3)
        b04 = Label(self.boardFrame, borderwidth=18, text=self.board[0][4]).grid(row = 0, column = 4)
        b05 = Label(self.boardFrame, borderwidth=18, text=self.board[0][5]).grid(row = 0, column = 5)
        b10 = Label(self.boardFrame, borderwidth=18, text=self.board[1][0]).grid(row = 1, column = 0)
        b11 = Label(self.boardFrame, borderwidth=18, text=self.board[1][1]).grid(row = 1, column = 1)
        b12 = Label(self.boardFrame, borderwidth=18, text=self.board[1][2]).grid(row = 1, column = 2)
        b13 = Label(self.boardFrame, borderwidth=18, text=self.board[1][3]).grid(row = 1, column = 3)
        b14 = Label(self.boardFrame, borderwidth=18, text=self.board[1][4]).grid(row = 1, column = 4)
        b15 = Label(self.boardFrame, borderwidth=18, text=self.board[1][5]).grid(row = 1, column = 5)
        b20 = Label(self.boardFrame, borderwidth=18, text=self.board[2][0]).grid(row = 2, column = 0)
        b21 = Label(self.boardFrame, borderwidth=18, text=self.board[2][1]).grid(row = 2, column = 1)
        b22 = Label(self.boardFrame, borderwidth=18, text=self.board[2][2]).grid(row = 2, column = 2)
        b23 = Label(self.boardFrame, borderwidth=18, text=self.board[2][3]).grid(row = 2, column = 3)
        b24 = Label(self.boardFrame, borderwidth=18, text=self.board[2][4]).grid(row = 2, column = 4)
        b25 = Label(self.boardFrame, borderwidth=18, text=self.board[2][5]).grid(row = 2, column = 5)
        b30 = Label(self.boardFrame, borderwidth=18, text=self.board[3][0]).grid(row = 3, column = 0)
        b31 = Label(self.boardFrame, borderwidth=18, text=self.board[3][1]).grid(row = 3, column = 1)
        b32 = Label(self.boardFrame, borderwidth=18, text=self.board[3][2]).grid(row = 3, column = 2)
        b33 = Label(self.boardFrame, borderwidth=18, text=self.board[3][3]).grid(row = 3, column = 3)
        b34 = Label(self.boardFrame, borderwidth=18, text=self.board[3][4]).grid(row = 3, column = 4)
        b35 = Label(self.boardFrame, borderwidth=18, text=self.board[3][5]).grid(row = 3, column = 5)
        b40 = Label(self.boardFrame, borderwidth=18, text=self.board[4][0]).grid(row = 4, column = 0)
        b41 = Label(self.boardFrame, borderwidth=18, text=self.board[4][1]).grid(row = 4, column = 1)
        b42 = Label(self.boardFrame, borderwidth=18, text=self.board[4][2]).grid(row = 4, column = 2)
        b43 = Label(self.boardFrame, borderwidth=18, text=self.board[4][3]).grid(row = 4, column = 3)
        b44 = Label(self.boardFrame, borderwidth=18, text=self.board[4][4]).grid(row = 4, column = 4)
        b45 = Label(self.boardFrame, borderwidth=18, text=self.board[4][5]).grid(row = 4, column = 5)
        b50 = Label(self.boardFrame, borderwidth=18, text=self.board[5][0]).grid(row = 5, column = 0)
        b51 = Label(self.boardFrame, borderwidth=18, text=self.board[5][1]).grid(row = 5, column = 1)
        b52 = Label(self.boardFrame, borderwidth=18, text=self.board[5][2]).grid(row = 5, column = 2)
        b53 = Label(self.boardFrame, borderwidth=18, text=self.board[5][3]).grid(row = 5, column = 3)
        b54 = Label(self.boardFrame, borderwidth=18, text=self.board[5][4]).grid(row = 5, column = 4)
        b55 = Label(self.boardFrame, borderwidth=18, text=self.board[5][5]).grid(row = 5, column = 5)

        self.message = str('***** Player %s, choose a slot. *****' % self.player)
        self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)


    def drawBoard(self, b):
        print('M O J G A N   C   O   N   N   E   C   T   4 ')
        print()
        print('     S    L    O    T    S     ')
        print('  1    2    3    4    5    6   ')
        print('                               ')
        print('| %s | %s | %s | %s | %s | %s |' % (b[0][0], b[0][1], b[0][2], b[0][3], b[0][4], b[0][5]))
        print('|----|----|----|----|----|----|')
        print('| %s | %s | %s | %s | %s | %s |' % (b[1][0], b[1][1], b[1][2], b[1][3], b[1][4], b[1][5]))
        print('|----|----|----|----|----|----|')
        print('| %s | %s | %s | %s | %s | %s |' % (b[2][0], b[2][1], b[2][2], b[2][3], b[2][4], b[2][5]))
        print('|----|----|----|----|----|----|')
        print('| %s | %s | %s | %s | %s | %s |' % (b[3][0], b[3][1], b[3][2], b[3][3], b[3][4], b[3][5]))
        print('|----|----|----|----|----|----|')
        print('| %s | %s | %s | %s | %s | %s |' % (b[4][0], b[4][1], b[4][2], b[4][3], b[4][4], b[4][5]))
        print('|----|----|----|----|----|----|')
        print('| %s | %s | %s | %s | %s | %s |' % (b[5][0], b[5][1], b[5][2], b[5][3], b[5][4], b[5][5]))
        print('|====|====|====|====|====|====|')
        print()


    def isValidChoice(self, slotChoice, board):
        try:
            col = int(slotChoice) - 1
            if col < 0 or col > 5:
                self.message = str('*** Term entered is out of range. ***')
                self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
                return False
        except ValueError:
            self.message = str('Column is full. Try again, player %s.')
            self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
            return False

        if board[0][col]  == '  ':
            return True

        self.message = str('Column is full. Try again player %s: ' % self.player)
        self.outputText = Label(self.outputFrame, text = self.message).grid(row = 0, column = 0)
        return False


    def playMove(self, row, col, player, board):
        if board[row][col] == '  ':
            board[row][col] = player
        elif row >= 0:
            self.playMove(row - 1, col, player, board)

        b00 = Label(self.boardFrame, borderwidth=18, text=self.board[0][0]).grid(row = 0, column = 0)
        b01 = Label(self.boardFrame, borderwidth=18, text=self.board[0][1]).grid(row = 0, column = 1)
        b02 = Label(self.boardFrame, borderwidth=18, text=self.board[0][2]).grid(row = 0, column = 2)
        b03 = Label(self.boardFrame, borderwidth=18, text=self.board[0][3]).grid(row = 0, column = 3)
        b04 = Label(self.boardFrame, borderwidth=18, text=self.board[0][4]).grid(row = 0, column = 4)
        b05 = Label(self.boardFrame, borderwidth=18, text=self.board[0][5]).grid(row = 0, column = 5)
        b10 = Label(self.boardFrame, borderwidth=18, text=self.board[1][0]).grid(row = 1, column = 0)
        b11 = Label(self.boardFrame, borderwidth=18, text=self.board[1][1]).grid(row = 1, column = 1)
        b12 = Label(self.boardFrame, borderwidth=18, text=self.board[1][2]).grid(row = 1, column = 2)
        b13 = Label(self.boardFrame, borderwidth=18, text=self.board[1][3]).grid(row = 1, column = 3)
        b14 = Label(self.boardFrame, borderwidth=18, text=self.board[1][4]).grid(row = 1, column = 4)
        b15 = Label(self.boardFrame, borderwidth=18, text=self.board[1][5]).grid(row = 1, column = 5)
        b20 = Label(self.boardFrame, borderwidth=18, text=self.board[2][0]).grid(row = 2, column = 0)
        b21 = Label(self.boardFrame, borderwidth=18, text=self.board[2][1]).grid(row = 2, column = 1)
        b22 = Label(self.boardFrame, borderwidth=18, text=self.board[2][2]).grid(row = 2, column = 2)
        b23 = Label(self.boardFrame, borderwidth=18, text=self.board[2][3]).grid(row = 2, column = 3)
        b24 = Label(self.boardFrame, borderwidth=18, text=self.board[2][4]).grid(row = 2, column = 4)
        b25 = Label(self.boardFrame, borderwidth=18, text=self.board[2][5]).grid(row = 2, column = 5)
        b30 = Label(self.boardFrame, borderwidth=18, text=self.board[3][0]).grid(row = 3, column = 0)
        b31 = Label(self.boardFrame, borderwidth=18, text=self.board[3][1]).grid(row = 3, column = 1)
        b32 = Label(self.boardFrame, borderwidth=18, text=self.board[3][2]).grid(row = 3, column = 2)
        b33 = Label(self.boardFrame, borderwidth=18, text=self.board[3][3]).grid(row = 3, column = 3)
        b34 = Label(self.boardFrame, borderwidth=18, text=self.board[3][4]).grid(row = 3, column = 4)
        b35 = Label(self.boardFrame, borderwidth=18, text=self.board[3][5]).grid(row = 3, column = 5)
        b40 = Label(self.boardFrame, borderwidth=18, text=self.board[4][0]).grid(row = 4, column = 0)
        b41 = Label(self.boardFrame, borderwidth=18, text=self.board[4][1]).grid(row = 4, column = 1)
        b42 = Label(self.boardFrame, borderwidth=18, text=self.board[4][2]).grid(row = 4, column = 2)
        b43 = Label(self.boardFrame, borderwidth=18, text=self.board[4][3]).grid(row = 4, column = 3)
        b44 = Label(self.boardFrame, borderwidth=18, text=self.board[4][4]).grid(row = 4, column = 4)
        b45 = Label(self.boardFrame, borderwidth=18, text=self.board[4][5]).grid(row = 4, column = 5)
        b50 = Label(self.boardFrame, borderwidth=18, text=self.board[5][0]).grid(row = 5, column = 0)
        b51 = Label(self.boardFrame, borderwidth=18, text=self.board[5][1]).grid(row = 5, column = 1)
        b52 = Label(self.boardFrame, borderwidth=18, text=self.board[5][2]).grid(row = 5, column = 2)
        b53 = Label(self.boardFrame, borderwidth=18, text=self.board[5][3]).grid(row = 5, column = 3)
        b54 = Label(self.boardFrame, borderwidth=18, text=self.board[5][4]).grid(row = 5, column = 4)
        b55 = Label(self.boardFrame, borderwidth=18, text=self.board[5][5]).grid(row = 5, column = 5)


    def isStalemate(self, board, j):
        if j == len(board):
            return True
        if board[0][j] == '  ':
            return False

        return self.isStalemate(board, j + 1)


    def hasWon(self, board):
        if self.checkVertical(board):
            return True

        if self.checkHorizontal(board):
            return True
    
        if self.checkUpRightDiagonal(board):
            return True

        if self.checkDownRightDiagonal(board):
            return True

        return False


    def checkVertical(self, board): # Check if the 4 chips are aligned vertically 
        count = 1
        for cols in range(len(board)):
            for rows in range(len(board) - 3):
                for k in range(1,4):
                    if board[rows][cols] == board[rows+k][cols] and board[rows][cols] != '  ':
                        count = count + 1
                    if count == 4:
                        return True
                count = 1

        return False


    def checkHorizontal(self, board): # Check if the 4 chips are aligned horizontally
        count = 1
        for rows in range(len(board)):
            for cols in range(len(board) - 3):
                for k in range(1,4):
                    if board[rows][cols] == board[rows][cols+k] and board[rows][cols] != '  ':
                        count = count + 1
                    if count == 4:
                        return True
                count = 1

        return False


    def checkUpRightDiagonal(self, board): #Check if the 4 chips are aligned diagonally from down to up right
        count = 1
        for rows in range(len(board)-1, 2, -1):
            for cols in range(len(board) - 3):
                for k in range(1,4):
                    if board[rows][cols] == board[rows-k][cols+k] and board[rows][cols] != '  ':
                        count = count + 1
                    if count == 4:
                        return True
                count = 1

        return False


    def checkDownRightDiagonal(self, board): # Check if the 4 chips are aligned diagoanlly from up to down right.
        count = 1
        for cols in range(len(board)-3):
            for rows in range(len(board) - 3):
                for k in range(1,4):
                    if board[rows][cols] == board[rows+k][cols+k] and board[rows][cols] != '  ':
                        count = count + 1
                    if count == 4:
                        return True
                count = 1

        return False


Game()
