from Piece import *
import copy


class Board:
    def __init__(self):
        self.pieces = []
        self.board_pieces = []
        self.positions = []

        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(8):
            position_row = []
            for c in range(8):
                position_row.append(columns[c] + str(r + 1))
            self.positions.append(position_row)

    def threatened(self, color, r, c):
        # is this position threatened by a piece of this color
        for rw in self.board_pieces:
            for p in rw:
                if p is not None and p.color is not color and (r, c) in p.moves:
                    return True
        return False

    def set_moves(self, p):
        """

        :rtype: list
        """
        if isinstance(p, Piece):
            if isinstance(p, Pawn):
                if p.color is "b":
                    if not p.has_moved and self.board_pieces[p.r + 1][p.c] is None and \
                            self.board_pieces[p.r + 2][p.c] is None:
                        p.moves.append((p.r + 2, p.c))
                    if self.board_pieces[p.r + 1][p.c] is None:
                        p.moves.append((p.r + 1, p.c))
                    if p.c is not 0 and p.c is not 7:
                        if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                                self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                            p.moves.append((p.r + 1, p.c + 1))
                        if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                                self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                            p.moves.append((p.r + 1, p.c - 1))
                    if p.c is 0:
                        if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                                self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                            p.moves.append((p.r + 1, p.c + 1))
                    if p.c is 7:
                        if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                                self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                            p.moves.append((p.r + 1, p.c - 1))

                elif p.color is "w":
                    if not p.has_moved and self.board_pieces[p.r - 1][p.c] is None and \
                            self.board_pieces[p.r - 2][p.c] is None:
                        p.moves.append((p.r - 2, p.c))
                    if self.board_pieces[p.r - 1][p.c] is None:
                        p.moves.append((p.r - 1, p.c))
                    if p.c is not 0 and p.c is not 7:
                        if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                                self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                            p.moves.append((p.r - 1, p.c + 1))
                        if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                                self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                            p.moves.append((p.r - 1, p.c - 1))
                    if p.c is 0:
                        if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                                self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                            p.moves.append((p.r - 1, p.c + 1))
                    if p.c is 7:
                        if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                                self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                            p.moves.append((p.r - 1, p.c - 1))
            elif isinstance(p, Rook):
                for c in range(p.c + 1, 8):
                    if self.board_pieces[p.r][c] is None:
                        p.moves.append((p.r, c))
                    elif self.board_pieces[p.r][c].color is not p.color:
                        p.moves.append((p.r, c))
                        break
                    else:
                        break
                for c in range(p.c - 1, 0, -1):
                    if self.board_pieces[p.r][c] is None:
                        p.moves.append((p.r, c))
                    elif self.board_pieces[p.r][c].color is not p.color:
                        p.moves.append((p.r, c))
                        break
                    else:
                        break
                for r in range(p.r, 8):
                    if self.board_pieces[r][p.c] is None:
                        p.moves.append((r, p.c))
                    elif self.board_pieces[r][p.c].color is not p.color:
                        p.moves.append((r, p.c))
                    else:
                        break
                for r in range(p.r, 0, -1):
                    if self.board_pieces[r][p.c] is None:
                        p.moves.append((r, p.c))
                    elif self.board_pieces[r][p.c].color is not p.color:
                        p.moves.append((r, p.c))
                    else:
                        break
            elif isinstance(p, Knight):
                p.moves.append((p.r - 1, p.c + 2))
                p.moves.append((p.r - 1, p.c - 2))
                p.moves.append((p.r - 2, p.c + 1))
                p.moves.append((p.r - 2, p.c - 1))
                p.moves.append((p.r + 1, p.c + 2))
                p.moves.append((p.r + 1, p.c - 2))
                p.moves.append((p.r + 2, p.c + 1))
                p.moves.append((p.r + 2, p.c - 1))
            elif isinstance(p, Bishop):
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r + i][p.c + i] is None:
                        p.moves.append((p.r + i, p.c + i))
                    elif self.board_pieces[p.r + i][p.c + i].color is not p.color:
                        p.moves.append((p.r + i, p.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r + i][p.c - i] is None:
                        p.moves.append((p.r + i, p.c - i))
                    elif self.board_pieces[p.r + i][p.c - i].color is not p.color:
                        p.moves.append((p.r + i, p.c - i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r - i][p.c + i] is None:
                        p.moves.append((p.r - i, p.c + i))
                    elif self.board_pieces[p.r - i][p.c + i].color is not p.color:
                        p.moves.append((p.r - i, p.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r - i][p.c - i] is None:
                        p.moves.append((p.r - i, p.c - i))
                    elif self.board_pieces[p.r - i][p.c - i].color is not p.color:
                        p.moves.append((p.r - i, p.c - i))
                        break
                    else:
                        break
            elif isinstance(p, Queen):
                for c in range(p.c + 1, 8):
                    if self.board_pieces[p.r][c] is None:
                        p.moves.append((p.r, c))
                    elif self.board_pieces[p.r][c].color is not p.color:
                        p.moves.append((p.r, c))
                        break
                    else:
                        break
                for c in range(p.c - 1, 0, -1):
                    if self.board_pieces[p.r][c] is None:
                        p.moves.append((p.r, c))
                    elif self.board_pieces[p.r][c].color is not p.color:
                        p.moves.append((p.r, c))
                        break
                    else:
                        break
                for r in range(p.r, 8):
                    if self.board_pieces[r][p.c] is None:
                        p.moves.append((r, p.c))
                    elif self.board_pieces[r][p.c].color is not p.color:
                        p.moves.append((r, p.c))
                    else:
                        break
                for r in range(p.r, 0, -1):
                    if self.board_pieces[r][p.c] is None:
                        p.moves.append((r, p.c))
                    elif self.board_pieces[r][p.c].color is not p.color:
                        p.moves.append((r, p.c))
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r + i][p.c + i] is None:
                        p.moves.append((p.r + i, p.c + i))
                    elif self.board_pieces[p.r + i][p.c + i].color is not p.color:
                        p.moves.append((p.r + i, p.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r + i][p.c - i] is None:
                        p.moves.append((p.r + i, p.c - i))
                    elif self.board_pieces[p.r + i][p.c - i].color is not p.color:
                        p.moves.append((p.r + i, p.c - i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r - i][p.c + i] is None:
                        p.moves.append((p.r - i, p.c + i))
                    elif self.board_pieces[p.r - i][p.c + i].color is not p.color:
                        p.moves.append((p.r - i, p.c + i))
                        break
                    else:
                        break
                for i in range(1, 8 - p.r):
                    if self.board_pieces[p.r - i][p.c - i] is None:
                        p.moves.append((p.r - i, p.c - i))
                    elif self.board_pieces[p.r - i][p.c - i].color is not p.color:
                        p.moves.append((p.r - i, p.c - i))
                        break
                    else:
                        break
            elif isinstance(p, King):
                if not self.threatened(p.color, p.r - 1, p.c - 1):
                    p.moves.append((p.r - 1, p.c - 1))
                if not self.threatened(p.color, p.r - 1, p.c):
                    p.moves.append((p.r - 1, p.c))
                if not self.threatened(p.color, p.r - 1, p.c + 1):
                    p.moves.append((p.r - 1, p.c + 1))
                if not self.threatened(p.color, p.r, p.c - 1):
                    p.moves.append((p.r, p.c - 1))
                if not self.threatened(p.color, p.r, p.c + 1):
                    p.moves.append((p.r, p.c + 1))
                if not self.threatened(p.color, p.r + 1, p.c - 1):
                    p.moves.append((p.r + 1, p.c - 1))
                if not self.threatened(p.color, p.r + 1, p.c):
                    p.moves.append((p.r + 1, p.c))
                if not self.threatened(p.color, p.r + 1, p.c + 1):
                    p.moves.append((p.r + 1, p.c + 1))
                if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                        isinstance(self.board_pieces[p.r][0], Rook) and \
                        self.board_pieces[p.r][0].color is p.color and not \
                        self.board_pieces[p.r][0].has_moved and \
                        self.board_pieces[p.r][1] is None and \
                        self.board_pieces[p.r][2] is None and \
                        self.board_pieces[p.r][3] is None:
                    p.moves.append((p.r, p.c - 2))
                if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                        isinstance(self.board_pieces[p.r][7], Rook) and \
                        self.board_pieces[p.r][7].color is p.color and not \
                        self.board_pieces[p.r][7].has_moved and \
                        self.board_pieces[p.r][6] is None and \
                        self.board_pieces[p.r][5] is None and \
                        self.board_pieces[p.r][4] is None:
                    p.moves.append((p.r, p.c - 2))
            for position in list(p.moves):
                r, c = position
                if r < 0 or c < 0 or r > 7 or c > 7:
                    p.moves.remove(position)
                elif self.board_pieces[r][c] is not None and self.board_pieces[r][c].color is p.color:
                    p.moves.remove(position)
            return p.moves
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

        for p in back:
            p.color = "w"
        for p in front:
            p.color = "w"

        self.board_pieces.append(copy.deepcopy(front))
        self.board_pieces.append(copy.deepcopy(back))

        for r in range(8):
            for c in range(8):
                if self.board_pieces[r][c] is not None:
                    self.board_pieces[r][c].r = r
                    self.board_pieces[r][c].c = c
                    self.pieces.append(self.board_pieces[r][c])

        for p in self.pieces:
            self.set_moves(p)

    def __str__(self):
        str_board = ""
        for r in self.board_pieces:
            for p in r:
                str_board += str(p) + " "
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
