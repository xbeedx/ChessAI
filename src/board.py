from const import *
from square import Square
class Board:

    def __init__(self):
        self._create()

    def _create(self):
        self.squares = [[Square(row, col) for row in range(ROWS)] for col in range(COLS)]

    def _add_pieces(self,color):
        pass
