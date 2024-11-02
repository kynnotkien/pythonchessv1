# -----------------------
#  Made by KynNotKien <3 
# -----------------------
# Images from chess.com

# Before we begin, you need to install the Pygame library.
# Open a terminal (or command prompt) and run the following command:
# pip install pygame

import pygame
import funtion

# Color pattle

DARK_GREEN = (118,150,86)
LIGHT_GREEN = (238,238,210)
GREEN = (186,202,68)
BLACK = (0,0,0)
WHITE = (255,255,255)

# window create

pygame.init()
WIDTH = 400
HEGHT = 500
screen = pygame.display.set_mode([WIDTH, HEGHT])
pygame.display.set_caption("Chess")
fps = 60
 
# Drawing the board_drawing

def board_drawing():
    for i in range(32):
        column = i % 4
        row = i // 4
        if row % 2 == 0:
            pygame.draw.rect(screen,DARK_GREEN,(350 - (column * 100), row * 50, 50, 50 ))
        else:
            pygame.draw.rect(screen,DARK_GREEN,(300 - (column * 100), row * 50, 50, 50 ))

    pygame.draw.rect(screen, BLACK, (0, 400, 400, 10))


# pieces info
# k = king / q = queen / rook = r / bigshop = b / knight = n / pawn = p

# white pieces

w_pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
            'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',]

w_cord = [(0, 7), (1, 7), (2, 7), (3, 7), (4, 7), (5, 7), (6, 7), (7, 7),
          (0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (5, 6), (6, 6), (7, 6)]

# black pieces

b_pieces = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r',
            'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p',]

b_cord = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
          (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1)]

valid_moves = []

# white pieces images

wk = pygame.image.load('Images/wk.png') 
wk = pygame.transform.scale(wk, (50, 50))

wq = pygame.image.load('Images/wq.png') 
wq = pygame.transform.scale(wq, (50, 50))

wb = pygame.image.load('Images/wb.png') 
wb = pygame.transform.scale(wb, (50, 50))

wr = pygame.image.load('Images/wr.png') 
wr = pygame.transform.scale(wr, (50, 50))

wn = pygame.image.load('Images/wn.png') 
wn = pygame.transform.scale(wn, (50, 50))

wp = pygame.image.load('Images/wp.png') 
wp = pygame.transform.scale(wp, (50, 50))

w_images = [wr, wn, wb, wq, wk, wp]

# black pieces image

bk = pygame.image.load('Images/bk.png') 
bk = pygame.transform.scale(bk, (50, 50))

bq = pygame.image.load('Images/bq.png') 
bq = pygame.transform.scale(bq, (50, 50))

bb = pygame.image.load('Images/bb.png') 
bb = pygame.transform.scale(bb, (50, 50))

br = pygame.image.load('Images/br.png') 
br = pygame.transform.scale(br, (50, 50))

bn = pygame.image.load('Images/bn.png') 
bn = pygame.transform.scale(bn, (50, 50))

bp = pygame.image.load('Images/bp.png') 
bp = pygame.transform.scale(bp, (50, 50))

b_images = [br, bn, bb, bq, bk, bp]

pieces_type = ['r', 'n', 'b', 'q', 'k', 'p']


turn_step = 0
selection = 100

# load image for pieces

def pieces_load():

    for i in range(len(w_pieces)):
        image = pieces_type.index(w_pieces[i])
        if w_pieces[i] == 'p':
            screen.blit(wp, (w_cord[i][0] * 50, w_cord[i][1] * 50))
        else:
            screen.blit(w_images[image], (w_cord[i][0] * 50, w_cord[i][1] * 50 ))
        if turn_step <= 1:
            if selection == i:
                pygame.draw.rect(screen, BLACK, (w_cord[i][0] * 50, w_cord[i][1] * 50, 50, 50), 2)

    for i in range(len(b_pieces)):
        image = pieces_type.index(b_pieces[i])
        if b_pieces[i] == 'p':
            screen.blit(bp, (b_cord[i][0] * 50, b_cord[i][1] * 50 ))
        else:
            screen.blit(b_images[image], (b_cord[i][0] * 50, b_cord[i][1] * 50 ))
        if turn_step > 1:
            if selection == i:
                pygame.draw.rect(screen, BLACK, (b_cord[i][0] * 50, b_cord[i][1] * 50, 50, 50), 2)

# check pieces moves, possible moves

def check_options(pieces, locations, turn):
    moves = []
    possible_moves = []
    
    for i in range((len(pieces))):
        location = locations[i]
        piece = pieces[i]
        if piece == 'p':
            moves = pos_p(location, turn)
            #print(moves)
        if piece == 'r':
            #print('check')
            moves = pos_r(location, turn)
        if piece == 'n':
            moves = pos_n(location, turn)
        if piece == 'b':
            moves = pos_b(location, turn)
        if piece == 'k':
            moves = pos_k(location, turn)
        if piece == 'q':
            moves = pos_q(location, turn)

    #print(moves)        
        possible_moves.append(moves)
    return possible_moves

# check valid pawn moves

def pos_p(position, color):
    moves = []
    
    if color == 'white':

        # straight 1 or 2 squares at frist time and 1 for the rest 
        # if there are any piece in font of the pawn, they cant move

        if (position[0], position[1] - 1) not in w_cord and (position[0], position[1] - 1) not in b_cord and position[1] > 0:
            moves.append((position[0], position[1] - 1))
            if (position[0], position[1] - 2) not in w_cord and (position[0], position[1] - 2) not in b_cord and position[1] == 6:
                moves.append((position[0], position[1] - 2))

        # check if pawns can eat enemy or not

        if (position[0] + 1, position[1] - 1) in b_cord:
            moves.append((position[0] + 1, position[1] - 1))
        if (position[0] - 1, position[1] - 1) in b_cord:
            moves.append((position[0] - 1, position[1] - 1))
    else:

        # straight 1 or 2 squares at frist time and 1 for the rest 
        # if there are any piece in font of the pawn, they cant move

        if (position[0], position[1] + 1) not in w_cord and (position[0], position[1] + 1) not in b_cord and position[1] < 7:
            moves.append((position[0], position[1] + 1))
            if (position[0], position[1] + 2) not in w_cord and (position[0], position[1] + 2) not in b_cord and position[1] == 1:
                moves.append((position[0], position[1] + 2))
        
        # check if pawns can eat enemy or not

        if (position[0] + 1, position[1] + 1) in w_cord:
            moves.append((position[0] + 1, position[1] + 1))
        if (position[0] - 1, position[1] + 1) in w_cord:
            moves.append((position[0] - 1, position[1] + 1))
    return moves

# check valid rook moves

def pos_r(position, color):
    #print('def run')
    moves = []

    if color == 'white':
        enemy = b_cord
        ally = w_cord
    else:
        ally = b_cord
        enemy = w_cord
    for i in range(4):
        path = True
        chain = 1
        if i == 0:
            x = 0
            y = 1
        elif i == 1:
            x = 0
            y = -1
        elif i == 2:
            x = 1
            y = 0
        else:
            x = -1
            y = 0
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in ally and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemy:
                    path = False
                chain += 1

                #print(moves)    
            else:
                path = False

    return moves

# check valid knight moves

def pos_n(position, color):
    moves = []
    if color == 'white':
        enemy = b_cord
        ally = w_cord
    else:
        ally = b_cord
        enemy = w_cord
    # 8 squares to check for knights, they can go two squares in one direction and one in another
    targets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in ally and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves.append(target)
    return moves



def pos_b(position, color):
    moves_list = []
    if color == 'white':
        enemy = b_cord
        ally = w_cord
    else:
        ally = b_cord
        enemy = w_cord
    for i in range(4):  # up-right, up-left, down-right, down-left
        path = True
        chain = 1
        if i == 0:
            x = 1
            y = -1
        elif i == 1:
            x = -1
            y = -1
        elif i == 2:
            x = 1
            y = 1
        else:
            x = -1
            y = 1
        while path:
            if (position[0] + (chain * x), position[1] + (chain * y)) not in ally and 0 <= position[0] + (chain * x) <= 7 and 0 <= position[1] + (chain * y) <= 7:
                moves_list.append((position[0] + (chain * x), position[1] + (chain * y)))
                if (position[0] + (chain * x), position[1] + (chain * y)) in enemy:
                    path = False
                chain += 1
            else:
                path = False
    return moves_list




def pos_k(position, color):
    moves_list = []
    if color == 'white':
        enemy = b_cord
        ally = w_cord
    else:
        ally = b_cord
        enemy = w_cord
    # 8 squares to check for kings, they can go one square any direction
    targets = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
    for i in range(8):
        target = (position[0] + targets[i][0], position[1] + targets[i][1])
        if target not in ally and 0 <= target[0] <= 7 and 0 <= target[1] <= 7:
            moves_list.append(target)
    return moves_list


def pos_q(position, color):
    moves_list = pos_b(position, color)
    second_list = pos_r(position, color)
    for i in range(len(second_list)):
        moves_list.append(second_list[i])
    return moves_list


def check_valid_moves():
    if turn_step < 2:
        options_list = w_option
    else:
        options_list = b_option
    valid_options = options_list[selection]
    return valid_options

def draw_valid(draw_moves):
    for i in range(len(draw_moves)):
        pygame.draw.circle(screen, BLACK, (draw_moves[i][0] * 50 + 25, draw_moves[i][1] * 50 +25), 8)

b_option = check_options(b_pieces, b_cord, 'black')
w_option = check_options(w_pieces, w_cord, 'white')


running = True

while running:    
    screen.fill(LIGHT_GREEN)
    board_drawing()
    pieces_load()
    if selection != 100:
        valid_moves = check_valid_moves()   
        draw_valid(valid_moves)

    if 'k' not in w_pieces:
        print('ok')
    if 'k' not in b_pieces:
        print('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x_selection = event.pos[0] // 50
            y_selection = event.pos[1] // 50
            click = (x_selection, y_selection)

            # white selection

            if turn_step <= 1:
                if click in w_cord:
                    selection = w_cord.index(click)
                    if turn_step == 0:
                        turn_step = 1
                if click in valid_moves and selection != 100:
                    w_cord[selection] = click
                    if click in b_cord: 
                        b_piece = b_cord.index(click)
                        #print(b_piece)
                        b_pieces.pop(b_piece)
                        b_cord.pop(b_piece)
                    b_option = check_options(b_pieces, b_cord, 'black')
                    w_option = check_options(w_pieces, w_cord, 'white')
                    #print(w_option)
                    turn_step = 2
                    selection = 100
                    valid_moves = []

            # black selection 

            if turn_step > 1:
                if click in b_cord:
                    selection = b_cord.index(click)
                    if turn_step == 2:
                        turn_step = 3
                if click in valid_moves and selection != 100:
                    b_cord[selection] = click
                    if click in w_cord:
                        w_piece = w_cord.index(click)
                        w_pieces.pop(w_piece)
                        w_cord.pop(w_piece)
                    b_option = check_options(b_pieces, b_cord, 'black')
                    w_option = check_options(w_pieces, w_cord, 'white')
                    turn_step = 0
                    selection = 100
                    valid_moves = []
            
    pygame.display.flip()
pygame.quit()

        