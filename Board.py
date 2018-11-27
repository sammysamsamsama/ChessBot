from Piece import *
import copy

# every position
a1 = (7, 0)
a2 = (6, 0)
a3 = (5, 0)
a4 = (4, 0)
a5 = (3, 0)
a6 = (2, 0)
a7 = (1, 0)
a8 = (0, 0)

b1 = (7, 1)
b2 = (6, 1)
b3 = (5, 1)
b4 = (4, 1)
b5 = (3, 1)
b6 = (2, 1)
b7 = (1, 1)
b8 = (0, 1)

c1 = (7, 2)
c2 = (6, 2)
c3 = (5, 2)
c4 = (4, 2)
c5 = (3, 2)
c6 = (2, 2)
c7 = (1, 2)
c8 = (0, 2)

d1 = (7, 3)
d2 = (6, 3)
d3 = (5, 3)
d4 = (4, 3)
d5 = (3, 3)
d6 = (2, 3)
d7 = (1, 3)
d8 = (0, 3)

e1 = (7, 4)
e2 = (6, 4)
e3 = (5, 4)
e4 = (4, 4)
e5 = (3, 4)
e6 = (2, 4)
e7 = (1, 4)
e8 = (0, 4)

f1 = (7, 5)
f2 = (6, 5)
f3 = (5, 5)
f4 = (4, 5)
f5 = (3, 5)
f6 = (2, 5)
f7 = (1, 5)
f8 = (0, 5)

g1 = (7, 6)
g2 = (6, 6)
g3 = (5, 6)
g4 = (4, 6)
g5 = (3, 6)
g6 = (2, 6)
g7 = (1, 6)
g8 = (0, 6)

h1 = (7, 7)
h2 = (6, 7)
h3 = (5, 7)
h4 = (4, 7)
h5 = (3, 7)
h6 = (2, 7)
h7 = (1, 7)
h8 = (0, 7)


class Board:
    def __init__(self):
        self.pieces = []
        self.board_pieces = []
        self.positions = []

        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(7, -1, -1):
            position_row = []
            for c in range(8):
                position_row.append(columns[c] + str(r + 1))
            self.positions.append(position_row)

    def threatened(self, color, r, c):
        # is this position threatened by a piece not this color
        for rw in self.board_pieces:
            for p in rw:
                if p is not None and p.color is not color and (r, c) in p.moves:
                    return True
        return False

    def clear(self):
        self.pieces.clear()
        self.board_pieces.clear()
        for r in range(8):
            row = []
            for c in range(8):
                row.append(None)
            self.board_pieces.append(row)
            del row

    def set_all_moves(self):
        for p in self.pieces:
            self.set_moves(p)

    def set_pawn(self, p):
        if p.color is "b":
            if not p.has_moved and self.board_pieces[p.r + 1][p.c] is None and \
                    self.board_pieces[p.r + 2][p.c] is None:
                p.moves.add((p.r + 2, p.c))
            if self.board_pieces[p.r + 1][p.c] is None:
                p.moves.add((p.r + 1, p.c))
            if p.c is not 0 and p.c is not 7:
                if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c + 1))
                if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c - 1))
            if p.c is 0:
                if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c + 1))
            if p.c is 7:
                if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c - 1))
        elif p.color is "w":
            if not p.has_moved and self.board_pieces[p.r - 1][p.c] is None and \
                    self.board_pieces[p.r - 2][p.c] is None:
                p.moves.add((p.r - 2, p.c))
            if self.board_pieces[p.r - 1][p.c] is None:
                p.moves.add((p.r - 1, p.c))
            if p.c is not 0 and p.c is not 7:
                if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c + 1))
                if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c - 1))
            if p.c is 0:
                if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c + 1))
            if p.c is 7:
                if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c - 1))

    def set_rook(self, p):
        for i in range(1, 8):
            if p.c + i > 7:
                break
            if self.board_pieces[p.r][p.c + i] is None:
                p.moves.add((p.r, p.c + i))
            elif self.board_pieces[p.r][p.c + i].color is not p.color:
                p.moves.add((p.r, p.c + i))
                break
            else:
                break
        for i in range(1, 8):
            if p.c - i < 0:
                break
            if self.board_pieces[p.r][p.c - i] is None:
                p.moves.add((p.r, p.c + i))
            elif self.board_pieces[p.r][p.c - i].color is not p.color:
                p.moves.add((p.r, p.c - i))
                break
            else:
                break
        for i in range(1, 8):
            if p.r + i > 7:
                break
            if self.board_pieces[p.r + i][p.c] is None:
                p.moves.add((p.r + i, p.c))
            elif self.board_pieces[p.r + i][p.c].color is not p.color:
                p.moves.add((p.r + i, p.c))
                break
            else:
                break
        for i in range(1, 8):
            if p.r - i < 0:
                break
            if self.board_pieces[p.r - i][p.c] is None:
                p.moves.add((p.r - i, p.c))
            elif self.board_pieces[p.r - i][p.c].color is not p.color:
                p.moves.add((p.r - i, p.c))
                break
            else:
                break

    def set_knight(self, p):
        # all illegal moves removed at the end
        p.moves.add((p.r - 1, p.c + 2))
        p.moves.add((p.r - 1, p.c - 2))
        p.moves.add((p.r - 2, p.c + 1))
        p.moves.add((p.r - 2, p.c - 1))
        p.moves.add((p.r + 1, p.c + 2))
        p.moves.add((p.r + 1, p.c - 2))
        p.moves.add((p.r + 2, p.c + 1))
        p.moves.add((p.r + 2, p.c - 1))

    def set_bishop(self, p):
        for i in range(1, 8):
            if p.r + i > 7 or p.c + i > 7:
                break
            if self.board_pieces[p.r + i][p.c + i] is None:
                p.moves.add((p.r + i, p.c + i))
            elif self.board_pieces[p.r + i][p.c + i].color is not p.color:
                p.moves.add((p.r + i, p.c + i))
                break
            else:
                break
        for i in range(1, 8):
            if p.r + i > 7 or p.c - i < 0:
                break
            if self.board_pieces[p.r + i][p.c - i] is None:
                p.moves.add((p.r + i, p.c - i))
            elif self.board_pieces[p.r + i][p.c - i].color is not p.color:
                p.moves.add((p.r + i, p.c - i))
                break
            else:
                break
        for i in range(1, 8):
            if p.r - i < 0 or p.c + i > 7:
                break
            if self.board_pieces[p.r - i][p.c + i] is None:
                p.moves.add((p.r - i, p.c + i))
            elif self.board_pieces[p.r - i][p.c + i].color is not p.color:
                p.moves.add((p.r - i, p.c + i))
                break
            else:
                break
        for i in range(1, 8):
            if p.r - i < 0 or p.c - i < 0:
                break
            if self.board_pieces[p.r - i][p.c - i] is None:
                p.moves.add((p.r - i, p.c - i))
            elif self.board_pieces[p.r - i][p.c - i].color is not p.color:
                p.moves.add((p.r - i, p.c - i))
                break
            else:
                break

    def set_king(self, p):
        if not self.threatened(p.color, p.r - 1, p.c - 1):
            p.moves.add((p.r - 1, p.c - 1))
        if not self.threatened(p.color, p.r - 1, p.c):
            p.moves.add((p.r - 1, p.c))
        if not self.threatened(p.color, p.r - 1, p.c + 1):
            p.moves.add((p.r - 1, p.c + 1))
        if not self.threatened(p.color, p.r, p.c - 1):
            p.moves.add((p.r, p.c - 1))
        if not self.threatened(p.color, p.r, p.c + 1):
            p.moves.add((p.r, p.c + 1))
        if not self.threatened(p.color, p.r + 1, p.c - 1):
            p.moves.add((p.r + 1, p.c - 1))
        if not self.threatened(p.color, p.r + 1, p.c):
            p.moves.add((p.r + 1, p.c))
        if not self.threatened(p.color, p.r + 1, p.c + 1):
            p.moves.add((p.r + 1, p.c + 1))
        if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                isinstance(self.board_pieces[p.r][0], Rook) and \
                self.board_pieces[p.r][0].color is p.color and not \
                self.board_pieces[p.r][0].has_moved and \
                self.board_pieces[p.r][1] is None and \
                self.board_pieces[p.r][2] is None and \
                self.board_pieces[p.r][3] is None and not \
                self.threatened(p.color, p.r, 2) and not \
                self.threatened(p.color, p.r, 3):
            p.moves.add((p.r, p.c - 2))
            # self.board_pieces[p.r][0].moves.add(p.r, 2)
        if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                isinstance(self.board_pieces[p.r][7], Rook) and \
                self.board_pieces[p.r][7].color is p.color and not \
                self.board_pieces[p.r][7].has_moved and \
                self.board_pieces[p.r][6] is None and \
                self.board_pieces[p.r][5] is None and \
                self.board_pieces[p.r][4] is None and not \
                self.threatened(p.color, p.r, 6) and not \
                self.threatened(p.color, p.r, 5):
            p.moves.add((p.r, p.c - 2))
            # self.board_pieces[p.r][7].moves.add(p.r, 5)

    def set_moves(self, p):
        p.moves.clear()
        """

        :rtype: list
        """
        if isinstance(p, Piece):
            if isinstance(p, Pawn):
                self.set_pawn(p)
            elif isinstance(p, Rook):
                self.set_rook(p)
            elif isinstance(p, Knight):
                self.set_knight(p)
            elif isinstance(p, Bishop):
                self.set_bishop(p)
            elif isinstance(p, Queen):
                self.set_rook(p)
                self.set_bishop(p)
            elif isinstance(p, King):
                self.set_king(p)
            for position in list(p.moves):
                r, c = position
                if r < 0 or c < 0 or r > 7 or c > 7:
                    p.moves.remove(position)
                elif self.board_pieces[r][c] is not None and self.board_pieces[r][c].color is p.color:
                    p.moves.remove(position)
            return p.moves
        return None

    def populate(self):
        # clear board
        self.pieces.clear()
        self.board_pieces.clear()

        # back row, front row, empty row
        back = []
        front = []
        empty = []

        # populate back row
        back.append(Rook("b"))
        back.append(Knight("b"))
        back.append(Bishop("b"))
        back.append(Queen("b"))
        back.append(King("b"))
        back.append(Bishop("b"))
        back.append(Knight("b"))
        back.append(Rook("b"))

        # populate front and empty rows
        for i in range(8):
            front.append(Pawn("b"))
            empty.append(None)

        # add black set to board
        self.board_pieces.append(copy.deepcopy(back))
        self.board_pieces.append(copy.deepcopy(front))

        # add empty middle ground
        for i in range(4):
            self.board_pieces.append(empty.copy())

        # create white set
        for p in back:
            p.color = "w"
        for p in front:
            p.color = "w"

        # add white set to board
        self.board_pieces.append(copy.deepcopy(front))
        self.board_pieces.append(copy.deepcopy(back))

        # add every piece on the board to the list of pieces
        for r in range(8):
            for c in range(8):
                if self.board_pieces[r][c] is not None:
                    p = self.board_pieces[r][c]
                    # set piece coordinates
                    p.r = r
                    p.c = c
                    p.position = (r, c)
                    self.pieces.append(p)

        self.set_all_moves()

    def move(self, a, b):
        r1, c1 = a
        r2, c2 = b
        if self.board_pieces[r1][c1] is None:
            raise Exception("There is no piece at " + self.positions[r1][c1])
        p = self.board_pieces[r1][c1]
        if b not in p.moves:
            raise Exception(self.positions[r1][c1] + " cannot move to " + self.positions[r2][c2])
        if isinstance(p, King) and not p.has_moved and abs(c2 - c1) > 1:
            if c2 is 2 and isinstance(self.board_pieces[p.r][0], Rook) and not \
                    self.board_pieces[p.r][0].has_moved:
                self.board_pieces[p.r][0].has_moved = True
                self.board_pieces[p.r][0].c = 3
                self.board_pieces[p.r][0].position = (p.r, 3)
                print("O-O-O")
            elif c2 is 6 and isinstance(self.board_pieces[p.r][7], Rook) and not \
                    self.board_pieces[p.r][7].has_moved:
                self.board_pieces[p.r][0].has_moved = True
                self.board_pieces[p.r][0].c = 5
                self.board_pieces[p.r][0].position = (p.r, 5)
                print("O-O")
        p.has_moved = True
        p.r, p.c = b
        p.position = b
        print(self.positions[r1][c1] + " to " + self.positions[r2][c2])
        if self.board_pieces[r2][c2] is not None:
            print(str(p) + " takes " + str(board.board_pieces[r2][c2]))
            self.board_pieces[r2][c2] = None
        self.board_pieces[r1][c1] = None
        self.board_pieces[r2][c2] = p
        self.set_all_moves()
        print(str(self))

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
    board.move(e2, e4)
    board.move(d7, d5)
    board.move(e4, d5)
    #board.move(a1, a2)
    # for row in board.board_pieces:
    #     for piece in row:
    #         if piece is not None:
    #             print(str(piece), piece.r, piece.c)
    #             print(str(piece.moves))
