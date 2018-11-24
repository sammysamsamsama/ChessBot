from Piece import *
import copy


class Board:
    def __init__(self):
        self.pieces = []
        self.positions = []

        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(8):
            position_row = []
            for c in range(8):
                position_row.append(columns[c] + str(r + 1))
            self.positions.append(position_row)

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

        self.pieces.append(copy.deepcopy(back))
        self.pieces.append(copy.deepcopy(front))

        for i in range(4):
            self.pieces.append(empty.copy())

        for piece in back:
            piece.color = "w"
        for piece in front:
            piece.color = "w"

        self.pieces.append(copy.deepcopy(front))
        self.pieces.append(copy.deepcopy(back))

        for r in range(8):
            for c in range(8):
                if self.pieces[r][c] is not None:
                    self.pieces[r][c].r = r
                    self.pieces[r][c].c = c

    def threatened(self, r, c):
        for piece in self.pieces:
            if piece.moves.contains((r, c)):
                return True
        return False

    def set_moves(self, piece):
        if piece is Pawn:
            if piece.color is "b":
                if self.pieces[piece.r + 1][piece.c] is None:
                    piece.moves.append((piece.r + 1, piece.c))
                if piece.c is not 0 or 7:
                    if self.pieces[piece.r + 1][piece.c + 1].color is not piece.color:
                        piece.moves.append((piece.r + 1, piece.c + 1))
                    if self.pieces[piece.r + 1][piece.c - 1].color is not piece.color:
                        piece.moves.append((piece.r + 1, piece.c - 1))
                if piece.c is 0:
                    if self.pieces[piece.r + 1][piece.c + 1].color is not piece.color:
                        piece.moves.append((piece.r + 1, piece.c + 1))
                if piece.c is 7:
                    if self.pieces[piece.r + 1][piece.c - 1].color is not piece.color:
                        piece.moves.append((piece.r + 1, piece.c - 1))

            elif piece.color is "w":
                if self.pieces[piece.r - 1][piece.c] is None:
                    piece.moves.append((piece.r - 1, piece.c))
                if piece.c is not 0 or 7:
                    if self.pieces[piece.r - 1][piece.c + 1].color is not piece.color:
                        piece.moves.append((piece.r - 1, piece.c + 1))
                    if self.pieces[piece.r - 1][piece.c - 1].color is not piece.color:
                        piece.moves.append((piece.r - 1, piece.c - 1))
                if piece.c is 0:
                    if self.pieces[piece.r - 1][piece.c + 1].color is not piece.color:
                        piece.moves.append((piece.r - 1, piece.c + 1))
                if piece.c is 7:
                    if self.pieces[piece.r - 1][piece.c - 1].color is not piece.color:
                        piece.moves.append((piece.r - 1, piece.c - 1))
        elif piece is Rook:
            for c in range(piece.c + 1, 8):
                if self.pieces[piece.r][c] is None:
                    piece.moves.append((piece.r, c))
                elif self.pieces[piece.r][c].color is not piece.color:
                    piece.moves.append((piece.r, c))
                    break
                else:
                    break
            for c in range(piece.c - 1, 0, -1):
                if self.pieces[piece.r][c] is None:
                    piece.moves.append((piece.r, c))
                elif self.pieces[piece.r][c].color is not piece.color:
                    piece.moves.append((piece.r, c))
                    break
                else:
                    break
            for r in range(piece.r, 8):
                if self.pieces[r][piece.c] is None:
                    piece.moves.append((r, piece.c))
                elif self.pieces[r][piece.c].color is not piece.color:
                    piece.moves.append((r, piece.c))
                else:
                    break
            for r in range(piece.r, 0, -1):
                if self.pieces[r][piece.c] is None:
                    piece.moves.append((r, piece.c))
                elif self.pieces[r][piece.c].color is not piece.color:
                    piece.moves.append((r, piece.c))
                else:
                    break
        elif piece is Knight:
            if self.pieces[piece.r + 1][piece.c + 2].color is not piece.color:
                piece.moves.append((piece.r + 1, piece.c + 2))
            if self.pieces[piece.r + 1][piece.c - 2].color is not piece.color:
                piece.moves.append((piece.r + 1, piece.c - 2))

            if self.pieces[piece.r + 2][piece.c + 1].color is not piece.color:
                piece.moves.append((piece.r + 2, piece.c + 1))
            if self.pieces[piece.r + 2][piece.c - 1].color is not piece.color:
                piece.moves.append((piece.r + 2, piece.c - 1))

            if self.pieces[piece.r - 1][piece.c + 2].color is not piece.color:
                piece.moves.append((piece.r - 1, piece.c + 2))
            if self.pieces[piece.r - 1][piece.c - 2].color is not piece.color:
                piece.moves.append((piece.r - 1, piece.c - 2))

            if self.pieces[piece.r - 2][piece.c + 1].color is not piece.color:
                piece.moves.append((piece.r - 2, piece.c + 1))
            if self.pieces[piece.r - 2][piece.c - 1].color is not piece.color:
                piece.moves.append((piece.r - 2, piece.c - 1))
        elif piece is Bishop:
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r + i][piece.c + i] is None:
                    piece.moves.append((piece.r + i, piece.c + i))
                elif self.pieces[piece.r + i][piece.c + i].color is not piece.color:
                    piece.moves.append((piece.r + i, piece.c + i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r + i][piece.c - i] is None:
                    piece.moves.append((piece.r + i, piece.c - i))
                elif self.pieces[piece.r + i][piece.c - i].color is not piece.color:
                    piece.moves.append((piece.r + i, piece.c - i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r - i][piece.c + i] is None:
                    piece.moves.append((piece.r - i, piece.c + i))
                elif self.pieces[piece.r - i][piece.c + i].color is not piece.color:
                    piece.moves.append((piece.r - i, piece.c + i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r - i][piece.c - i] is None:
                    piece.moves.append((piece.r - i, piece.c - i))
                elif self.pieces[piece.r - i][piece.c - i].color is not piece.color:
                    piece.moves.append((piece.r - i, piece.c - i))
                    break
                else:
                    break
        elif piece is Queen:
            for c in range(piece.c + 1, 8):
                if self.pieces[piece.r][c] is None:
                    piece.moves.append((piece.r, c))
                elif self.pieces[piece.r][c].color is not piece.color:
                    piece.moves.append((piece.r, c))
                    break
                else:
                    break
            for c in range(piece.c - 1, 0, -1):
                if self.pieces[piece.r][c] is None:
                    piece.moves.append((piece.r, c))
                elif self.pieces[piece.r][c].color is not piece.color:
                    piece.moves.append((piece.r, c))
                    break
                else:
                    break
            for r in range(piece.r, 8):
                if self.pieces[r][piece.c] is None:
                    piece.moves.append((r, piece.c))
                elif self.pieces[r][piece.c].color is not piece.color:
                    piece.moves.append((r, piece.c))
                else:
                    break
            for r in range(piece.r, 0, -1):
                if self.pieces[r][piece.c] is None:
                    piece.moves.append((r, piece.c))
                elif self.pieces[r][piece.c].color is not piece.color:
                    piece.moves.append((r, piece.c))
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r + i][piece.c + i] is None:
                    piece.moves.append((piece.r + i, piece.c + i))
                elif self.pieces[piece.r + i][piece.c + i].color is not piece.color:
                    piece.moves.append((piece.r + i, piece.c + i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r + i][piece.c - i] is None:
                    piece.moves.append((piece.r + i, piece.c - i))
                elif self.pieces[piece.r + i][piece.c - i].color is not piece.color:
                    piece.moves.append((piece.r + i, piece.c - i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r - i][piece.c + i] is None:
                    piece.moves.append((piece.r - i, piece.c + i))
                elif self.pieces[piece.r - i][piece.c + i].color is not piece.color:
                    piece.moves.append((piece.r - i, piece.c + i))
                    break
                else:
                    break
            for i in range(1, 8 - piece.r):
                if self.pieces[piece.r - i][piece.c - i] is None:
                    piece.moves.append((piece.r - i, piece.c - i))
                elif self.pieces[piece.r - i][piece.c - i].color is not piece.color:
                    piece.moves.append((piece.r - i, piece.c - i))
                    break
                else:
                    break
        elif piece is King:
            if not self.threatened(piece.r - 1, piece.c - 1):
                piece.moves.append((piece.r - 1, piece.c -1))
            if not self.threatened(piece.r - 1, piece.c):
                piece.moves.append((piece.r - 1, piece.c))
            if not self.threatened(piece.r -1, piece.c + 1):
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

    def __str__(self):
        str_board = ""
        for row in self.pieces:
            for piece in row:
                str_board += str(piece) + " "
            str_board += "\n"
        return str_board


if __name__ == "__main__":
    board = Board()
    board.populate()
    print(str(board))
    print(board.set_moves(board.pieces[1][0]))
