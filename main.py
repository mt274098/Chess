class ChessPiece:
    def __init__(self, color, x, y):
        self.color = color
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x = x
        self.y = y

class Pawn(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, x, y):
        if self.color == "white":
            if y == self.y + 1 and (x == self.x + 1 or x == self.x - 1):
                super().move(x, y)
            elif y == self.y + 1 and x == self.x:
                super().move(x, y)
        else:
            if y == self.y - 1 and (x == self.x + 1 or x == self.x - 1):
                super().move(x, y)
            elif y == self.y - 1 and x == self.x:
                super().move(x, y)

class Knight(ChessPiece):
    def __init__(self, color, x, y):
        super().__init__(color, x, y)

    def move(self, x, y):
        if (x == self.x + 2 or x == self.x - 2) and (y == self.y + 1 or y == self.y - 1):
            super().move(x, y)
        elif (x == self.x + 1 or x == self.x - 1) and (y == self.y + 2 or y == self.y - 2):
            super().move(x, y)

class ChessBoard:
    def __init__(self):
        self.board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(None)
            self.board.append(row)

    def add_piece(self, piece, x, y):
        self.board[x][y] = piece

    def move_piece(self, piece, x, y):
        piece.move(x, y)
        self.board[piece.x][piece.y] = piece
        self.board[x][y] = None

board = ChessBoard()
pawn = Pawn("white", 1, 1)
board.add_piece(pawn, 1, 1)
board.move_piece(pawn, 2, 2)
print(pawn.x, pawn.y)

knight = Knight("black", 0, 0)
board.add_piece(knight, 0, 0)
board.move_piece(knight, 2, 1)
print(knight.x, knight.y)
