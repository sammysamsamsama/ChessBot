from Piece import *
import copy


class Board:
    def __init__(self):
        self.board_pieces = []
        self.positions = []

        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(8):
            position_row = []
            for c in range(8):
                position_row.append(columns[c] + str(r + 1))
            self.positions.append(position_row)

    def threatened(self, r, c):
        for row in self.board_pieces:
            for piece in row:
                if piece is not None and (r, c) in piece.moves:
                    return True
        return False

    def set_moves(self, piece):
        if isinstance(piece, Piece):
            if isinstance(piece, Pawn):
                if piece.color is "b":
                    if not piece.has_moved and self.board_pieces[piece.r + 1][piece.c] is None and \
                            self.board_pieces[piece.r + 2][piece.c] is None:
                        piece.moves.append((piece.r + 2, piece.c))
                    if self.board_pieces[piece.r + 1][piece.c] is None:
                        piece.moves.append((piece.r + 1, piece.c))
                    if piece.c is not 0 and piece.c is not 7:
                        if isinstance(self.board_pieces[piece.r + 1][piece.c + 1], Piece) and \
                                self.board_pieces[piece.r + 1][piece.c + 1].color is not piece.color:
                            piece.moves.append((piece.r + 1, piece.c + 1))
                        if isinstance(self.board_pieces[piece.r + 1][piece.c - 1], Piece) and \
                                self.board_pieces[piece.r + 1][piece.c - 1].color is not piece.color:
                            piece.moves.append((piece.r + 1, piece.c - 1))
                    if piece.c is 0:
                        if isinstance(self.board_pieces[piece.r + 1][piece.c + 1], Piece) and \
                                self.board_pieces[piece.r + 1][piece.c + 1].color is not piece.color:
                            piece.moves.append((piece.r + 1, piece.c + 1))
                    if piece.c is 7:
                        if isinstance(self.board_pieces[piece.r + 1][piece.c - 1], Piece) and \
                                self.board_pieces[piece.r + 1][piece.c - 1].color is not piece.color:
                            piece.moves.append((piece.r + 1, piece.c - 1))

                elif piece.color is "w":
                    if not piece.has_moved and self.board_pieces[piece.r - 1][piece.c] is None and \
                            self.board_pieces[piece.r - 2][piece.c] is None:
                        piece.moves.append((piece.r - 2, piece.c))
                    if self.board_pieces[piece.r - 1][piece.c] is None:
                        piece.moves.append((piece.r - 1, piece.c))
                    if piece.c is not 0 and piece.c is not 7:
                        if isinstance(self.board_pieces[piece.r - 1][piece.c + 1], Piece) and \
                                self.board_pieces[piece.r - 1][piece.c + 1].color is not piece.color:
                            piece.moves.append((piece.r - 1, piece.c + 1))
                        if isinstance(self.board_pieces[piece.r - 1][piece.c - 1], Piece) and \
                                self.board_pieces[piece.r - 1][piece.c - 1].color is not piece.color:
                            piece.moves.append((piece.r - 1, piece.c - 1))
                    if piece.c is 0:
                        if isinstance(self.board_pieces[piece.r - 1][piece.c + 1], Piece) and \
                                self.board_pieces[piece.r - 1][piece.c + 1].color is not piece.color:
                            piece.moves.append((piece.r - 1, piece.c + 1))
                    if piece.c is 7:
                        if isinstance(self.board_pieces[piece.r - 1][piece.c - 1], Piece) and \
                                self.board_pieces[piece.r - 1][piece.c - 1].color is not piece.color:
                            piece.moves.append((piece.r - 1, piece.c - 1))
            elif isinstance(piece, Rook):
                for c in range(piece.c + 1, 8):
                    if self.board_pieces[piece.r][c] is None:
                        piece.moves.append((piece.r, c))
                    elif self.board_pieces[piece.r][c].color is not piece.color:
                        piece.moves.append((piece.r, c))
                        break
                    else:
                        break
                for c in range(piece.c - 1, 0, -1):
                    if self.board_pieces[piece.r][c] is None:
                        piece.moves.append((piece.r, c))
                    elif self.board_pieces[piece.r][c].color is not piece.color:
                        piece.moves.append((piece.r, c))
                        break
                    else:
                        break
                for r in range(piece.r, 8):
                    if self.board_pieces[r][piece.c] is None:
                        piece.moves.append((r, piece.c))
                    elif self.board_pieces[r][piece.c].color is not piece.color:
                        piece.moves.append((r, piece.c))
                    else:
                        break
                for r in range(piece.r, 0, -1):
                    if self.board_pieces[r][piece.c] is None:
                        piece.moves.append((r, piece.c))
                    elif self.board_pieces[r][piece.c].color is not piece.color:
                        piece.moves.append((r, piece.c))
                    else:
                        break
            elif isinstance(piece, Knight):
                piece.moves.append((piece.r - 1, piece.c + 2))
                piece.moves.append((piece.r - 1, piece.c - 2))
                piece.moves.append((piece.r - 2, piece.c + 1))
                piece.moves.append((piece.r - 2, piece.c - 1))
                piece.moves.append((piece.r + 1, piece.c + 2))
                piece.moves.append((piece.r + 1, piece.c - 2))
                piece.moves.append((piece.r + 2, piece.c + 1))
                piece.moves.append((piece.r + 2, piece.c - 1))
            elif isinstance(piece, Bishop):
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r + i][piece.c + i] is None:
                        piece.moves.append((piece.r + i, piece.c + i))
                    elif self.board_pieces[piece.r + i][piece.c + i].color is not piece.color:
                        piece.moves.append((piece.r + i, piece.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r + i][piece.c - i] is None:
                        piece.moves.append((piece.r + i, piece.c - i))
                    elif self.board_pieces[piece.r + i][piece.c - i].color is not piece.color:
                        piece.moves.append((piece.r + i, piece.c - i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r - i][piece.c + i] is None:
                        piece.moves.append((piece.r - i, piece.c + i))
                    elif self.board_pieces[piece.r - i][piece.c + i].color is not piece.color:
                        piece.moves.append((piece.r - i, piece.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r - i][piece.c - i] is None:
                        piece.moves.append((piece.r - i, piece.c - i))
                    elif self.board_pieces[piece.r - i][piece.c - i].color is not piece.color:
                        piece.moves.append((piece.r - i, piece.c - i))
                        break
                    else:
                        break
            elif isinstance(piece, Queen):
                for c in range(piece.c + 1, 8):
                    if self.board_pieces[piece.r][c] is None:
                        piece.moves.append((piece.r, c))
                    elif self.board_pieces[piece.r][c].color is not piece.color:
                        piece.moves.append((piece.r, c))
                        break
                    else:
                        break
                for c in range(piece.c - 1, 0, -1):
                    if self.board_pieces[piece.r][c] is None:
                        piece.moves.append((piece.r, c))
                    elif self.board_pieces[piece.r][c].color is not piece.color:
                        piece.moves.append((piece.r, c))
                        break
                    else:
                        break
                for r in range(piece.r, 8):
                    if self.board_pieces[r][piece.c] is None:
                        piece.moves.append((r, piece.c))
                    elif self.board_pieces[r][piece.c].color is not piece.color:
                        piece.moves.append((r, piece.c))
                    else:
                        break
                for r in range(piece.r, 0, -1):
                    if self.board_pieces[r][piece.c] is None:
                        piece.moves.append((r, piece.c))
                    elif self.board_pieces[r][piece.c].color is not piece.color:
                        piece.moves.append((r, piece.c))
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r + i][piece.c + i] is None:
                        piece.moves.append((piece.r + i, piece.c + i))
                    elif self.board_pieces[piece.r + i][piece.c + i].color is not piece.color:
                        piece.moves.append((piece.r + i, piece.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r + i][piece.c - i] is None:
                        piece.moves.append((piece.r + i, piece.c - i))
                    elif self.board_pieces[piece.r + i][piece.c - i].color is not piece.color:
                        piece.moves.append((piece.r + i, piece.c - i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r - i][piece.c + i] is None:
                        piece.moves.append((piece.r - i, piece.c + i))
                    elif self.board_pieces[piece.r - i][piece.c + i].color is not piece.color:
                        piece.moves.append((piece.r - i, piece.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - piece.r):
                    if self.board_pieces[piece.r - i][piece.c - i] is None:
                        piece.moves.append((piece.r - i, piece.c - i))
                    elif self.board_pieces[piece.r - i][piece.c - i].color is not piece.color:
                        piece.moves.append((piece.r - i, piece.c - i))
                        break
                    else:
                        break
            elif isinstance(piece, King):
                if not self.threatened(piece.r - 1, piece.c - 1):
                    piece.moves.append((piece.r - 1, piece.c - 1))
                if not self.threatened(piece.r - 1, piece.c):
                    piece.moves.append((piece.r - 1, piece.c))
                if not self.threatened(piece.r - 1, piece.c + 1):
                    piece.moves.append((piece.r - 1, piece.c + 1))
                if not self.threatened(piece.r, piece.c - 1):
                    piece.moves.append((piece.r, piece.c - 1))
                if not self.threatened(piece.r, piece.c + 1):
                    piece.moves.append((piece.r, piece.c + 1))
                if not self.threatened(piece.r + 1, piece.c - 1):
                    piece.moves.append((piece.r + 1, piece.c - 1))
                if not self.threatened(piece.r + 1, piece.c):
                    piece.moves.append((piece.r + 1, piece.c))
                if not self.threatened(piece.r + 1, piece.c + 1):
                    piece.moves.append((piece.r + 1, piece.c + 1))
                if not piece.has_moved and not self.threatened(piece.r, piece.c) and \
                        isinstance(self.board_pieces[piece.r][0], Rook) and \
                        self.board_pieces[piece.r][0].color is piece.color and not \
                        self.board_pieces[piece.r][0].has_moved and \
                        self.board_pieces[piece.r][1] is None and \
                        self.board_pieces[piece.r][2] is None and \
                        self.board_pieces[piece.r][3] is None:
                    piece.moves.append((piece.r, piece.c - 2))
                if not piece.has_moved and not self.threatened(piece.r, piece.c) and \
                        isinstance(self.board_pieces[piece.r][7], Rook) and \
                        self.board_pieces[piece.r][7].color is piece.color and not \
                        self.board_pieces[piece.r][7].has_moved and \
                        self.board_pieces[piece.r][6] is None and \
                        self.board_pieces[piece.r][5] is None and \
                        self.board_pieces[piece.r][4] is None:
                    piece.moves.append((piece.r, piece.c - 2))

            for position in list(piece.moves):
                r, c = position
                if r < 0 or c < 0 or r > 7 or c > 7:
                    piece.moves.remove(position)
                elif self.board_pieces[r][c] is not None and self.board_pieces[r][c].color is piece.color:
                    piece.moves.remove(position)
            return piece.moves
        return None

    def populate(self):
        back = []
        front = []
        empty = []

        back.append(Rook("b"))
        back.append(Knight("b"))
        back.append(Bishop("b"))
        back.append(Queen("b"))
        back.append(King("b"))
        back.append(Bishop("b"))
        back.append(Knight("b"))
        back.append(Rook("b"))

        for i in range(8):
            front.append(Pawn("b"))
            empty.append(None)

        self.board_pieces.append(copy.deepcopy(back))
        self.board_pieces.append(copy.deepcopy(front))

        for i in range(4):
            self.board_pieces.append(empty.copy())

        for piece in back:
            piece.color = "w"
        for piece in front:
            piece.color = "w"

        self.board_pieces.append(copy.deepcopy(front))
        self.board_pieces.append(copy.deepcopy(back))

        for r in range(8):
            for c in range(8):
                if self.board_pieces[r][c] is not None:
                    self.board_pieces[r][c].r = r
                    self.board_pieces[r][c].c = c

        for row in self.board_pieces:
            for piece in row:
                self.set_moves(piece)

    def __str__(self):
        str_board = ""
        for row in self.board_pieces:
            for piece in row:
                str_board += str(piece) + " "
            str_board += "\n"
        return str_board


if __name__ == "__main__":
    board = Board()
    board.populate()
    print(str(board))
    for row in board.board_pieces:
        for piece in row:
            if piece is not None:
                print(str(piece), piece.r, piece.c)
                print(str(piece.moves))
