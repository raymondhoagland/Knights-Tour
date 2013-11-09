class ChessBoard:
    def __init__(self):
        self.grid = [[0 for x in xrange(8)] for x in xrange(8)]
        self.moves = []
    def add_Move(self, x, y):
        self.moves.append([x,y])
        self.grid[x][y] = len(self.moves)  
    def printGrid(self):
        for i in self.grid:
            string = ""
            for k in i:
                string = string + str(k) + " "
                if(k < 10):
                    string = string + " "
            print string
    def remove_Last(self):
        move = self.moves.pop()
        self.grid[move[0]][move[1]] = 0
        return move
    def curr_Pos(self):
        return self.moves[len(self.moves)-1]
    def getCols(self):
        return len(self.grid[0])
    def getRows(self):
        return len(self.grid)
    def isValidPos(self, x, y):
        if(x>=0 and x<=7):
            if(y>=0 and y<=7):
                if(self.grid[x][y] == 0):
                    return True
        return False
    def isSolved(self):
        for i in self.grid:
            for k in i:
                if(k == 0):
                    return False
        return True
    def possibMove(self, **keyword_parameters):
        if('move' in keyword_parameters):
            move = keyword_parameters['move']
        else:
            move = self.curr_Pos()
        row = move[0]
        col = move[1]
        one = [row-2, col-1]
        two = [row+2, col-1]
        tre = [row-1, col-2]
        fou = [row+1, col-2]
        fiv = [row-2, col+1]
        six = [row+2, col+1]
        sev = [row-1, col+2]
        eit = [row+1, col+2]
        trial = [one, two, tre, fou, fiv, six, sev, eit]
        poss = []
        for pos in trial:
            if(self.isValidPos(pos[0], pos[1])):
                poss.append(pos)
        return poss
        
    def nextMove(self):
        '''
        min = 500
        minindex = -1
        moves = self.possibMove()
        for k in range(0, len(moves)):
            self.add_Move(moves[k][0], moves[k][1])
            moves_sec = self.possibMove()
            if(len(moves_sec) < min):
                min = len(moves_sec)
                minindex = k
            self.remove_Last()
        if(minindex == -1):
            return []
        return moves[minindex]
        '''
        moves = self.possibMove()
        lens = []
        for movee in moves:
            lens.append(len(self.possibMove(move = movee)))
        return [x for (y, x) in sorted(zip(lens, moves))]