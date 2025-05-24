HUMAN, AI, EMPTY = 'O', 'X', ' '

def print_board(b):
    for row in b: print(' | '.join(row)); print('-' * 5)

def winner(b, p):
    return any(all(b[i][j] == p for j in range(3)) or all(b[j][i] == p for j in range(3)) for i in range(3)) or all(b[i][i] == p for i in range(3)) or all(b[i][2-i] == p for i in range(3))

def moves_left(b):
    return any(c == EMPTY for row in b for c in row)

def minimax(b, is_ai):
    if winner(b, AI): return 1
    if winner(b, HUMAN): return -1
    if not moves_left(b): return 0
    best = -2 if is_ai else 2
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI if is_ai else HUMAN
                score = minimax(b, not is_ai)
                b[i][j] = EMPTY
                best = max(best, score) if is_ai else min(best, score)
    return best

def best_move(b):
    move, best = None, -2
    for i in range(3):
        for j in range(3):
            if b[i][j] == EMPTY:
                b[i][j] = AI
                score = minimax(b, False)
                b[i][j] = EMPTY
                if score > best:
                    best, move = score, (i, j)
    return move

def play():
    b = [[EMPTY]*3 for _ in range(3)]
    print_board(b)
    while True:
        r, c = map(int, input("Your move (row col): ").split())
        if b[r][c] != EMPTY:
            print("Invalid!")
            continue
        b[r][c] = HUMAN
        print_board(b)
        if winner(b, HUMAN): print("You win!"); break
        if not moves_left(b): print("Draw!"); break
        ai = best_move(b)
        b[ai[0]][ai[1]] = AI
        print("AI move:")
        print_board(b)
        if winner(b, AI): print("AI wins!"); break
        if not moves_left(b): print("Draw!"); break

play()

                   
        

        
