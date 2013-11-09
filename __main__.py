#!/usr/bin/python  
# Hello World from Python
from ChessBoard import ChessBoard

def solveBoard(board):
    if(board.isSolved()):
        return True
    else:
        curr_Pos = board.curr_Pos()
        moves = board.nextMove()
        for move in moves:
            x = move[0]
            y = move[1]
            board.add_Move(x, y)
            if(solveBoard(board)):
                return True
            else:
                board.remove_Last()
                #print "Reversing"
        return False

for i in xrange(8):
    x = ChessBoard()
    x.add_Move(i, 0)
    solveBoard(x)
#next = x.nextMove()
#print next
    x.printGrid()
    print " "