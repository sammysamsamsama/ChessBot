class Piece:
    def __init__(self, color):
        self.color = color
        self.r = None
        self.c = None
        self.position = None
        self.moves = set()
        self.has_moved = False

    def __str__(self):
        return self.color


class Pawn(Piece):
    def __init__(self, color):
        super(Pawn, self).__init__(color)

    def __str__(self):
        return self.color + ".pn"


class Rook(Piece):
    def __init__(self, color):
        super(Rook, self).__init__(color)

    def __str__(self):
        return self.color + ".rk"


class Knight(Piece):
    def __init__(self, color):
        super(Knight, self).__init__(color)

    def __str__(self):
        return self.color + ".kt"


class Bishop(Piece):
    def __init__(self, color):
        super(Bishop, self).__init__(color)

    def __str__(self):
        return self.color + ".bp"


class Queen(Piece):
    def __init__(self, color):
        super(Queen, self).__init__(color)

    def __str__(self):
        return self.color + ".qn"


class King(Piece):
    def __init__(self, color):
        super(King, self).__init__(color)

    def __str__(self):
        return self.color + ".kg"
