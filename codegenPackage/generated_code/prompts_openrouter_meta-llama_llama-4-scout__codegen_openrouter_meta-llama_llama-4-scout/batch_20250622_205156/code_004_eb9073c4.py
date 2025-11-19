"""
Generated Code Metadata:
========================
Original URL: https://claim-taiko.cokiwe2297.workers.dev
Prompt: Design a simple magical chess game API with unique piece abilities inspired by Anichess.
Generated: DETERMINISTIC_eb9073c43b8bd3d5
Batch ID: 20250622_205156
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# magical_chess_game.py

from enum import Enum
from typing import List, Dict

class PieceType(Enum):
    """ Enum for piece types """
    KING = 1
    QUEEN = 2
    ROOK = 3
    BISHOP = 4
    KNIGHT = 5
    PAWN = 6
    WIZARD = 7  # Unique piece inspired by Anichess

class Piece:
    """ Base piece class """
    def __init__(self, piece_type: PieceType, color: str):
        self.piece_type = piece_type
        self.color = color

    def __str__(self):
        return f"{self.color} {self.piece_type.name}"

class MagicalChessGame:
    """ Magical chess game API """
    def __init__(self):
        self.board: Dict[tuple, Piece] = {}
        self.move_history: List[tuple] = []

    def add_piece(self, x: int, y: int, piece: Piece):
        """ Add a piece to the board """
        if (x, y) in self.board:
            raise ValueError("Position already occupied")
        self.board[(x, y)] = piece

    def remove_piece(self, x: int, y: int) -> Piece:
        """ Remove a piece from the board """
        if (x, y) not in self.board:
            raise ValueError("Position empty")
        piece = self.board.pop((x, y))
        return piece

    def move_piece(self, x1: int, y1: int, x2: int, y2: int):
        """ Move a piece on the board """
        if (x1, y1) not in self.board:
            raise ValueError("Starting position empty")
        if (x2, y2) in self.board:
            raise ValueError("Destination position occupied")
        piece = self.remove_piece(x1, y1)
        self.add_piece(x2, y2, piece)
        self.move_history.append((x1, y1, x2, y2))

    def get_piece_ability(self, piece: Piece) -> str:
        """ Get the ability of a piece """
        if isinstance(piece, Wizard):
            return "Can swap places with any other piece on the board"
        elif isinstance(piece, King):
            return "Can move one square in any direction"
        elif isinstance(piece, Queen):
            return "Can move any number of squares in any direction"
        elif isinstance(piece, Rook):
            return "Can move any number of squares horizontally or vertically"
        elif isinstance(piece, Bishop):
            return "Can move any number of squares diagonally"
        elif isinstance(piece, Knight):
            return "Can move in an L-shape"
        elif isinstance(piece, Pawn):
            return "Can move forward one square, but captures diagonally"
        else:
            raise ValueError("Unknown piece type")

class King(Piece):
    """ King piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.KING, color)

class Queen(Piece):
    """ Queen piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.QUEEN, color)

class Rook(Piece):
    """ Rook piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.ROOK, color)

class Bishop(Piece):
    """ Bishop piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.BISHOP, color)

class Knight(Piece):
    """ Knight piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.KNIGHT, color)

class Pawn(Piece):
    """ Pawn piece class """
    def __init__(self, color: str):
        super().__init__(PieceType.PAWN, color)

class Wizard(Piece):
    """ Wizard piece class with unique ability """
    def __init__(self, color: str):
        super().__init__(PieceType.WIZARD, color)

def main():
    game = MagicalChessGame()

    # Create pieces
    king = King("white")
    queen = Queen("black")
    wizard = Wizard("white")

    # Add pieces to the board
    game.add_piece(0, 0, king)
    game.add_piece(1, 1, queen)
    game.add_piece(2, 2, wizard)

    # Print piece abilities
    print(game.get_piece_ability(king))
    print(game.get_piece_ability(queen))
    print(game.get_piece_ability(wizard))

    # Move pieces
    game.move_piece(0, 0, 3, 3)
    print(game.move_history)

if __name__ == "__main__":
    main()
```
