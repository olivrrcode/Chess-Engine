import random

king_scores = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 3, 2, 0, 0, 0, 2, 0],
               [0, 5, 4, 0, 0, 0, 5, 3]]

queen_scores = [[1, 1, 1, 3, 1, 1, 1, 1],
                [1, 2, 3, 3, 1, 1, 1, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 2, 3, 3, 3, 2, 2, 1],
                [1, 4, 3, 3, 3, 4, 2, 1],
                [1, 2, 3, 3, 1, 1, 1, 1],
                [1, 1, 1, 3, 1, 1, 1, 1]]

rook_scores = [[4, 3, 4, 4, 4, 4, 3, 4],
               [4, 4, 4, 4, 4, 4, 4, 4],
               [1, 1, 2, 3, 3, 2, 1, 1],
               [1, 2, 3, 4, 4, 3, 2, 1],
               [1, 2, 3, 4, 4, 3, 2, 1],
               [1, 2, 2, 3, 3, 2, 1, 1],
               [4, 4, 4, 4, 4, 4, 4, 4],
               [4, 3, 4, 4, 4, 4, 3, 4]]

bishop_scores = [[4, 3, 2, 1, 1, 2, 3, 4],
                 [4, 4, 3, 2, 2, 3, 4, 3],
                 [2, 3, 4, 3, 3, 4, 3, 2],
                 [1, 2, 3, 4, 4, 3, 2, 1],
                 [1, 2, 3, 4, 4, 3, 2, 1],
                 [2, 3, 6, 3, 3, 6, 3, 2],
                 [3, 7, 3, 2, 2, 3, 7, 3],
                 [4, 3, 2, 1, 1, 2, 3, 4]]

knight_scores = [[1, 1, 1, 1, 1, 1, 1, 1],
                 [1, 2, 2, 2, 2, 2, 2, 1],
                 [1, 2, 3, 3, 3, 3, 2, 1],
                 [1, 2, 3, 8, 8, 3, 2, 1],
                 [1, 2, 3, 7, 7, 3, 2, 1],
                 [1, 2, 5, 3, 3, 5, 2, 1],
                 [1, 2, 2, 2, 2, 2, 2, 1],
                 [1, 1, 1, 1, 1, 1, 1, 1]]

white_pawn_scores = [[8, 8, 8, 8, 8, 8, 8, 8],
                     [8, 8, 8, 8, 8, 8, 8, 8],
                     [5, 6, 6, 7, 7, 6, 6, 5],
                     [2, 3, 3, 5, 5, 3, 3, 2],
                     [1, 2, 3, 4, 4, 3, 2, 1],
                     [1, 1, 2, 3, 3, 2, 1, 1],
                     [1, 1, 1, 0, 0, 1, 1, 1],
                     [0, 0, 0, 0, 0, 0, 0, 0]]

black_pawn_scores = [[0, 0, 0, 0, 0, 0, 0, 0],
                     [1, 1, 1, 0, 0, 1, 1, 1],
                     [1, 1, 2, 3, 3, 2, 1, 1],
                     [1, 2, 3, 4, 4, 3, 2, 1],
                     [2, 3, 3, 5, 5, 3, 3, 2],
                     [5, 6, 6, 7, 7, 6, 6, 5],
                     [8, 8, 8, 8, 8, 8, 8, 8],
                     [8, 8, 8, 8, 8, 8, 8, 8]]

piece_score = {'K': 0,
               'Q': 9,
               'R': 5,
               'B': 3,
               'N': 3,
               'p': 1}

piece_position_scores = {'K': king_scores,
                         'Q': queen_scores,
                         'R': rook_scores,
                         'B': bishop_scores,
                         'N': knight_scores,
                         'wp': white_pawn_scores,
                         'bp': black_pawn_scores}

CHECKMATE = 1000
STALEMATE = 0
DEPTH = 3
global next_move


def find_random_move(valid_moves):
    return valid_moves[random.randint(0, len(valid_moves)-1)]


def find_best_move(gs, valid_moves):
    global next_move
    next_move = None
    find_move_negamax_alphabeta(gs, valid_moves, DEPTH, -CHECKMATE, CHECKMATE, 1 if gs.whiteToMove else -1)
    return next_move


def find_move_negamax_alphabeta(gs, valid_moves, depth, alpha, beta, turn_multiplier):
    global next_move
    if depth == 0:
        return turn_multiplier * score_board(gs)

    # move ordering - implement later
    max_score = -CHECKMATE
    for move in valid_moves:
        gs.make_move(move)
        next_moves = gs.get_valid_moves()
        score = -find_move_negamax_alphabeta(gs, next_moves, depth - 1, -beta, -alpha, -turn_multiplier)
        if score > max_score:
            max_score = score
            if depth == DEPTH:
                next_move = move
        gs.undo_move()
        if max_score > alpha:
            alpha = max_score
        if alpha >= beta:
            break
    return max_score


def score_board(gs):
    if gs.checkmate:
        if gs.whiteToMove:
            return -CHECKMATE
        else:
            return CHECKMATE
    elif gs.stalemate:
        return STALEMATE

    score = 0
    for row in range(len(gs.board)):
        for col in range(len(gs.board[row])):
            square = gs.board[row][col]
            if square != '--':
                piece_position_score = piece_position_scores[square if square[1] == 'p' else square[1]][row][col]
                if square[0] == 'w':
                    score += piece_score[square[1]] + piece_position_score * .17
                elif square[0] == 'b':
                    score -= piece_score[square[1]] + piece_position_score * .17
    return score


def score_material(board):
    score = 0
    for r in board:
        for sq in r:
            if sq[0] == 'w':
                score += piece_score[sq[1]]
            elif sq[0] == 'b':
                score -= piece_score[sq[1]]
    return score
