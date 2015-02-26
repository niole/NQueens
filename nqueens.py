def issafe(board,row,n):
    if board[n][row] == 0:
#        print 'row: '+str(row)+', n: '+str(n)
        return True
    return False

# (int, int, board) -> board
def place(row,n,board):
    newBoard = [[0 for _ in range(len(board))] for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            newBoard[i][j] = board[i][j]
#            print newBoard
    newBoard[n][row] = 'q'
#    print board
    for i in range(len(board)):#cross out row
        if newBoard[i][row] != 'q':
            newBoard[i][row] = '-'
#    print board
    for i in range(len(board)):#cross out column
        if newBoard[n][i] != 'q':
            newBoard[n][i] = '-'
#    print board
    for i in range(len(board)):#cross out diagonals
        if n+i < len(board) and row+i < len(board) and newBoard[n+i][row+i] != 'q':
            newBoard[n+i][row+i] = '-'
#            print board
        if n+i < len(board) and row-i > -1 and newBoard[n+i][row-i] != 'q':
            newBoard[n+i][row-i] = '-'
#            print board
#    print printBoard(newBoard)
    return newBoard

def printBoard(board):
    print '-'*20
    for row in board:
        print row

def placecol(n,board):
#    print 'placecol top: n: '+str(n)
    if n == len(board):
        print printBoard(board)
        return board
    for row in range(len(board)):
#        print 'placecol mid: n: '+str(n)+', row: '+str(row)
        if issafe(board,row,n):
            newboard = place(row,n,board)
            placecol(n+1,newboard)

#e = [0 for x in range(3)]
#b = [e for x in range(3)]
#print 'b: '+str(b)
N = [[0 for _ in range(4)] for _ in range(4)]
print placecol(0,N)
