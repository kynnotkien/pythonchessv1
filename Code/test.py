for i in range(32):
    test = i // 4
    print(test)





            x_selection = event.pos[0] // 50
            y_selection = event.pos[1] // 50
            click = (x_selection, y_selection)
            if turn_step <= 1:
                if click in w_cord:
                    selection = w_cord.index(click)
                    if turn_step == 0:
                        turn_step = 1
                if click in valid_moves and selection != 100:
                    w_cord[selection] = click
                    if click in b_cord:
                        b_piece = b_cord.index(click)
                        captured_pieces_white.append(b_pieces[b_piece])
                        b_pieces.pop(b_piece)
                        b_cord.pop(b_pieces)
                    b_option = check_options(b_pieces, b_cord)
                    w_option = check_options(w_pieces, w_cord)
                    turn_step = 2
                    selection = 100
                    valid_moves = []
            if turn_step > 1:
                if click in b_cord:
                    selection = b_cord.index(click)
                    if turn_step == 2:
                        turn_step = 3
                if click in valid_moves and selection != 100:
                    b_cord[selection] = click
                    if click in b_cord:
                        w_piece = w_cord.index(click)
                        captured_pieces_black.append(w_pieces[w_piece])
                        w_pieces.pop(w_piece)
                        b_cord.pop(b_pieces)
                    b_option = check_options(b_pieces, b_cord)
                    w_option = check_options(w_pieces, w_cord)
                    turn_step = 0
                    selection = 100
                    valid_moves = []