from Piece import *


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

        self.pieces.append(back)
        self.pieces.append(front)

        for i in range(4):
            self.pieces.append(empty)

        for piece in back:
            piece.color = "w"
        for piece in front:
            piece.color = "w"

        self.pieces.append(front)
        self.pieces.append(back)

        for r in range(8):
            for c in range(8):
                if self.pieces[r][c] is not None:
                    self.pieces[r][c].position = self.positions[r][c]

    def __str__(self):
        str_board = ""
        for row in self.pieces:
            for piece in row:
                str_board += str(piece) + " "
            str_board += "\n"
        return str_board


if __name__ == "__main__":
    board = Board()
    print(str(board))
