import numpy as np
import random

# pieces is a list of all possible Tetris pieces and rotations

# 0's are empty
# 1's are filled
pieces = {
    0:[[1,1,1,1]], # I's
    1:[[1],
    [1],
    [1],
    [1]], 

    2:[[1,1],[1,1]], # O's

    3:[[0,1,0],[1,1,1]], # T's
    4:[[1,0],
    [1,1],
    [1,0]],
    5:[[1,1,1],[0,1,0]],
    6:[[0,1],
    [1,1],
    [0,1]],

    7:[[1,0], # L's
    [1,0],
    [1,1]],
    8:[[0,0,1],
    [1,1,1]],
    9:[[1,1],
    [0,1],
    [0,1]],
    10:[[1,1,1],
    [1,0,0]],

    11:[[0,1], # J's
    [0,1],
    [1,1]],
    12:[[1,1,1],
    [0,0,1]],
    13:[[1,1],
    [1,0],
    [1,0]],
    14:[[1,0,0],
    [1,1,1]],

    15:[[0,1,1], # S's
    [1,1,0]],
    16:[[1,0],
    [1,1],
    [0,1]],

    17:[[1,1,0], # Z's
    [0,1,1]],
    18:[[0,1],
    [1,1],
    [1,0]]
}

board = [] # empty that will be filled with our Tetris game board 

# creates empty array of 0's
def gen_empty_board(cords):
    row, col = cords
    global board
    board = np.zeros((row, col), dtype=int)
    return 1

# takes piece, and a piece id num, and column and spawns them at the top of the board
def spawn_piece(piece_num, piece, col_input):
    if (len(piece[0]) + col_input > len(board[0])):
        return -1

    for row in range(len(piece)):
        for col in range(len(piece[0])):
            if piece[row][col] != 0:
                board[row][col + col_input] = piece_num

    return 1


# drop down function (could be optimized)
# returns 1 if moved returns 0 if stuck
def move_down(piece_num):
    locs = []

    # finds all blocks with piece_num
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == piece_num:
                locs.append((row,col))

    for loc in locs:
        # checks all block in piece to see if can move
        row, col = loc

        if (row + 1 >= len(board)):
            return 0

        if (board[row + 1][col] != piece_num) and (board[row + 1][col] != 0):
            return 0 

        
    #moves down 1
    for loc in locs:
        row, col = loc
        board[row][col] = 0
    
    for loc in locs:
        row, col = loc
        board[row + 1][col] = piece_num 
    return 1



# returns a copy of the board with the piece dropped in a position 
def hard_drop(piece_num):
    iterations = 0

    while move_down(piece_num):
        iterations += 1
        if iterations > len(board) + 20: # just a safety/sanity check
            return -1
    
    return 0 


# returns 0 if no holes, returns 1 if holes
def hole_detector():
    for col in range(len(board[0])):
        top = 0
        for row in range(len(board)):
            if board[row][col] != 0:
                top += 1
            if board[row][col] == 0 and top:
                return 1
        
    return 0

# makes all columns about equal in height. It looks nice when this is taken into account
def roughness_detector():
    threshold = 2 # these could be changed, but this yielded good results for me

    heights = array = np.full(len(board[0]), len(board)).tolist()
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] != 0:
                heights[col] = row
                break
            
    for i in range(1, len(heights) - 1):
        if abs(heights[i] - heights[i+1]) > threshold:
            return 1
        if abs(heights[i] - heights[i-1]) > threshold:
            return 1

    if abs(heights[0] - heights[1]) > threshold:
        return 1


    if abs(heights[-1] - heights[-2]) > threshold:
        return 1

    
    return 0
                

# delete piece:
def delete_piece(piece_num):
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == piece_num:
                board[row][col] = 0

# prints the piece. Just for debugging really
def print_piece(piece):
    print(piece)
    for row in range(len(piece)):
        for col in range(len(piece[row])):
            if (piece[row][col]!= 0):
                print(piece[row][col], end="")
            else:
                print(" ", end="") 
        print("\n", end="")


# places num_of_pieces while trying to minimize roughness and holes. If it increases those values it deletes the piece
def main_run(num_of_pieces):
    for piece_id_num in range(num_of_pieces):
        piece_shape_num = random.randint(0, len(pieces) - 1)
        piece = pieces[piece_shape_num]

        col = random.randint(0, len(board[0]) - len(piece[0]))

        spawn_piece(piece_id_num, piece, col)
        hard_drop(piece_id_num)

        if(hole_detector() or roughness_detector()):
            delete_piece(piece_id_num)

    return(board)
