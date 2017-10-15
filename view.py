#Deming Hao
# project 4
#game_logic module.

from othello import status


def number_of_row():
    '''get how many row will this board will have'''
    number_of_row = int(input())
    return number_of_row


def number_of_column():
    '''get how many columns this board will have'''

    number_of_column = int(input())
    return number_of_column
          

def move_first():
    '''decide who drop first'''
    turn = input()
    return turn            


def decide_top_left():
    '''choose whose disc on left top'''
    top = input()
    return top      


def win_condition():
    '''choose win by more disc or less disc by enter > or <'''
    win = input()
    return win    
    
     
def print_board(board):
    '''print the board'''
    for row in range(number_of_row):
        row_str = ''
        for col in range(number_of_column):            
            if board[row][col]== 0:
                row_str += '.' +' '
            elif board[row][col]== 1:
                row_str += 'B' +' '
            elif board[row][col]==2:
                row_str += 'W' +' '
        print(row_str)


def drop_position():
    '''drop the row and column by enter their numbers '''
    move = input()
    move = move.split(' ')   
    row = int(move[0])-1
    column = int(move[1])-1
    return row,column
            
def show_turn(turn):
    '''show whose turn is now'''
    if turn =='W':
        print('TURN: W')
    elif turn =='B':
        print('TURN: B')


if __name__ =='__main__':
    print('FULL')
    number_of_row = number_of_row()
    number_of_column = number_of_column()   
    turn= move_first()
    top = decide_top_left()
    win = win_condition()
    game=status(number_of_row, number_of_column) 
    board=game.position_on_board(number_of_row, number_of_column,top)
    
    while True:
        print('B: ' + str(game.black) + '  W: '+str(game.white))
        print_board(board)
        if game.is_gameover== True:
            print('WINNER: '+ game.winner)
        show_turn(turn)
                            
        while True:
            try:
                row,column = drop_position()    
                if game.make_a_move(board,row,column,turn):
                    print('VALID')
                    break
            except:
                print('INVALID')
        game.update_score(board,win)
        turn=game.change_turns(turn,board,win)

        


        
        
            

