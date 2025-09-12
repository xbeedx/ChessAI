from const import *
from piece import *
from square import Square
class Board:

    def __init__(self):
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        self.squares = [[Square(row, col) for row in range(ROWS)] for col in range(COLS)]

    def _add_pieces(self,color):
        row_pawn, row_other = (ROWS-2,ROWS-1) if color == 'white' else  (1,0)

        # Pawns
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))

        # Knights
        self.squares[row_other][1] = Square(row_pawn, 1, Knight(color))
        self.squares[row_other][6] = Square(row_pawn, 6, Knight(color))

        # Bishops
        self.squares[row_other][2] = Square(row_pawn, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_pawn, 5, Bishop(color))

        # Rooks
        self.squares[row_other][0] = Square(row_pawn, 0, Rook(color))
        self.squares[row_other][7] = Square(row_pawn, 7, Rook(color))

        # Queen
        self.squares[row_other][3] = Square(row_pawn, 3, Queen(color))

        # King
        self.squares[row_other][4] = Square(row_pawn, 4, King(color))