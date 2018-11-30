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
    # constructor
    def __init__(self):
        # list of pieces
        self.pieces = []
        # matrix of board
        self.board_pieces = []
        # positions of board
        self.positions = []

        # fill out positions
        columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
        for r in range(7, -1, -1):
            position_row = []
            for c in range(8):
                position_row.append(columns[c] + str(r + 1))
            self.positions.append(position_row)

    # would a piece of this color be threatened at this position
    def threatened(self, color, r, c):
        for rw in self.board_pieces:
            for p in rw:
                if p is not None and p.color is not color and (r, c) in p.moves:
                    return True
        return False

    # clear pieces and board
    def clear(self):
        self.pieces.clear()
        self.board_pieces.clear()
        for r in range(8):
            row = []
            for c in range(8):
                row.append(None)
            self.board_pieces.append(row)
            del row

    # set moves for all pieces
    def set_all_moves(self):
        for p in self.pieces:
            self.set_moves(p)

    # set pawn moves
    def set_pawn(self, p):
        # for black pawn
        if p.color is "b":
            # can it move twice
            if not p.has_moved and self.board_pieces[p.r + 1][p.c] is None and \
                    self.board_pieces[p.r + 2][p.c] is None:
                p.moves.add((p.r + 2, p.c))
            # can it move forward 1
            if self.board_pieces[p.r + 1][p.c] is None:
                p.moves.add((p.r + 1, p.c))
            # if not at edge of board, can it capture diagonally forward 1
            if p.c is not 0 and p.c is not 7:
                if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c + 1))
                if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c - 1))
            # at the edge, can it capture diagonally forward 1
            if p.c is 0:
                if isinstance(self.board_pieces[p.r + 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c + 1))
            if p.c is 7:
                if isinstance(self.board_pieces[p.r + 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r + 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r + 1, p.c - 1))
        # for white pawn
        elif p.color is "w":
            # can it move twice
            if not p.has_moved and self.board_pieces[p.r - 1][p.c] is None and \
                    self.board_pieces[p.r - 2][p.c] is None:
                p.moves.add((p.r - 2, p.c))
            # can it move forward 1
            if self.board_pieces[p.r - 1][p.c] is None:
                p.moves.add((p.r - 1, p.c))
            # if not at edge of board, can it capture diagonally forward 1
            if p.c is not 0 and p.c is not 7:
                if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c + 1))
                if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c - 1))
            # at the edge, can it capture diagonally forward 1
            if p.c is 0:
                if isinstance(self.board_pieces[p.r - 1][p.c + 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c + 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c + 1))
            if p.c is 7:
                if isinstance(self.board_pieces[p.r - 1][p.c - 1], Piece) and \
                        self.board_pieces[p.r - 1][p.c - 1].color is not p.color:
                    p.moves.add((p.r - 1, p.c - 1))

    # set rook moves
    def set_rook(self, p):
        # how far can it move right
        for i in range(1, 8):
            # until it hits the edge
            if p.c + i > 7:
                break
            if self.board_pieces[p.r][p.c + i] is None:
                p.moves.add((p.r, p.c + i))
            # until it finds an enemy
            elif self.board_pieces[p.r][p.c + i].color is not p.color:
                p.moves.add((p.r, p.c + i))
                break
            else:
                break
        # how far can it move left
        for i in range(1, 8):
            # until it hits the edge
            if p.c - i < 0:
                break
            if self.board_pieces[p.r][p.c - i] is None:
                p.moves.add((p.r, p.c + i))
            # until it finds an enemy
            elif self.board_pieces[p.r][p.c - i].color is not p.color:
                p.moves.add((p.r, p.c - i))
                break
            else:
                break
        # how far can it move down
        for i in range(1, 8):
            # before it hits the bottom
            if p.r + i > 7:
                break
            if self.board_pieces[p.r + i][p.c] is None:
                p.moves.add((p.r + i, p.c))
            # until it finds an enemy
            elif self.board_pieces[p.r + i][p.c].color is not p.color:
                p.moves.add((p.r + i, p.c))
                break
            else:
                break
        # how far can it move up
        for i in range(1, 8):
            # before it hits the top
            if p.r - i < 0:
                break
            if self.board_pieces[p.r - i][p.c] is None:
                p.moves.add((p.r - i, p.c))
            # until it finds an enemy
            elif self.board_pieces[p.r - i][p.c].color is not p.color:
                p.moves.add((p.r - i, p.c))
                break
            else:
                break

    # set knight moves
    def set_knight(self, p):
        # all illegal moves checked and removed in set_moves()
        # add all combinations of 2 and 1 away from p.position
        p.moves.add((p.r - 1, p.c + 2))
        p.moves.add((p.r - 1, p.c - 2))
        p.moves.add((p.r - 2, p.c + 1))
        p.moves.add((p.r - 2, p.c - 1))
        p.moves.add((p.r + 1, p.c + 2))
        p.moves.add((p.r + 1, p.c - 2))
        p.moves.add((p.r + 2, p.c + 1))
        p.moves.add((p.r + 2, p.c - 1))

    # set bishop moves
    def set_bishop(self, p):
        # how far can it move down and right
        for i in range(1, 8):
            # before it hits an edge
            if p.r + i > 7 or p.c + i > 7:
                break
            if self.board_pieces[p.r + i][p.c + i] is None:
                p.moves.add((p.r + i, p.c + i))
            # until it finds an enemy
            elif self.board_pieces[p.r + i][p.c + i].color is not p.color:
                p.moves.add((p.r + i, p.c + i))
                break
            else:
                break
        # how far can it move up and right
        for i in range(1, 8):
            # before it hits an edge
            if p.r - i < 0 or p.c + i > 7:
                break
            if self.board_pieces[p.r - i][p.c + i] is None:
                p.moves.add((p.r - i, p.c + i))
            # until it finds an enemy
            elif self.board_pieces[p.r - i][p.c + i].color is not p.color:
                p.moves.add((p.r - i, p.c + i))
                break
            else:
                break
        # how far can it move up and left
        for i in range(1, 8):
            # before it hits an edge
            if p.r - i < 0 or p.c - i < 0:
                break
            if self.board_pieces[p.r - i][p.c - i] is None:
                p.moves.add((p.r - i, p.c - i))
            # until it finds an enemy
            elif self.board_pieces[p.r - i][p.c - i].color is not p.color:
                p.moves.add((p.r - i, p.c - i))
                break
            else:
                break
        # how far can it move down and left
        for i in range(1, 8):
            # before it hits an edge
            if p.r + i > 7 or p.c - i < 0:
                break
            if self.board_pieces[p.r + i][p.c - i] is None:
                p.moves.add((p.r + i, p.c - i))
            # until it finds an enemy
            elif self.board_pieces[p.r + i][p.c - i].color is not p.color:
                p.moves.add((p.r + i, p.c - i))
                break
            else:
                break

    # set king moves
    def set_king(self, p):
        # all illegal moves checked and removed in set_moves()
        # add 8 closest positions
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
        # can it castle left
        if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                isinstance(self.board_pieces[p.r][0], Rook) and \
                self.board_pieces[p.r][0].color is p.color and not \
                self.board_pieces[p.r][0].has_moved and \
                self.board_pieces[p.r][1] is None and \
                self.board_pieces[p.r][2] is None and \
                self.board_pieces[p.r][3] is None:
            p.moves.add((p.r, p.c - 2))
        # can it castle right
        if not p.has_moved and not self.threatened(p.color, p.r, p.c) and \
                isinstance(self.board_pieces[p.r][7], Rook) and \
                self.board_pieces[p.r][7].color is p.color and not \
                self.board_pieces[p.r][7].has_moved and \
                self.board_pieces[p.r][6] is None and \
                self.board_pieces[p.r][5] is None and \
                self.board_pieces[p.r][4] is None:
            p.moves.add((p.r, p.c - 2))

    def set_moves(self, p):
        # clear current moves
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
            # check illegal moves
            for position in list(p.moves):
                r, c = position
                # if r or c lay outside the board, remove position from moves
                if r < 0 or c < 0 or r > 7 or c > 7:
                    p.moves.remove(position)
                # if the piece color at [r][c] is p.color, remove position from moves
                elif self.board_pieces[r][c] is not None and self.board_pieces[r][c].color is p.color:
                    p.moves.remove(position)
            return p.moves
        return None

    # set the board
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

        # assign the first moves
        self.set_all_moves()

    # move a to b
    def move(self, a, b):
        # extract position coordinates
        r1, c1 = a
        r2, c2 = b

        # add pointer to piece p at a
        p = self.board_pieces[r1][c1]

        # check if p is really a piece
        if p is None:
            raise Exception("There is no piece at " + self.positions[r1][c1])

        # check if p can move to b
        if b not in p.moves:
            raise Exception(self.positions[r1][c1] + " cannot move to " + self.positions[r2][c2])

        # p will move
        p.has_moved = True

        # reassign position variables for p
        p.r, p.c = b
        p.position = b

        # print( a to b )
        print(self.positions[r1][c1] + " to " + self.positions[r2][c2])

        # check if capture takes place
        if self.board_pieces[r2][c2] is not None:
            print(str(p) + " takes " + str(board.board_pieces[r2][c2]))
            self.pieces.remove(self.board_pieces[r2][c2])
            self.board_pieces[r2][c2] = None

        # clear a on board, set b on board to p
        self.board_pieces[r1][c1] = None
        self.board_pieces[r2][c2] = p

        # recheck all movement possibilities
        self.set_all_moves()

        # print board
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
    # for row in board.board_pieces:
    #     for piece in row:
    #         if piece is not None:
    #             print(str(piece), piece.r, piece.c)
    #             print(str(piece.moves))
