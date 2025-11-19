"""
Generated Code Metadata:
========================
Original URL: https://jito.pro
Prompt: Generate Python code to simulate a chess game similar to the one listed under "Chess" on jito.pro, ensuring the implementation includes basic AI for single-player mode.
Generated: DETERMINISTIC_29f55ba5103dd333
Batch ID: 20250612_154545
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import pygame
import sys
import random
from typing import List, Tuple, Optional, Dict

# Initialize pygame
pygame.init()

# Constants
BOARD_SIZE = 8
SQUARE_SIZE = 80
WINDOW_SIZE = BOARD_SIZE * SQUARE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_SQUARE = (240, 217, 181)
DARK_SQUARE = (181, 136, 99)
HIGHLIGHT_COLOR = (247, 247, 105, 150)
MOVE_COLOR = (106, 168, 79, 150)
FPS = 60

# Piece representations
EMPTY = 0
PAWN = 1
KNIGHT = 2
BISHOP = 3
ROOK = 4
QUEEN = 5
KING = 6

# Colors
WHITE_PIECE = 0
BLACK_PIECE = 1

# Piece symbols for display
PIECE_SYMBOLS = {
    WHITE_PIECE: {
        PAWN: '♙',
        KNIGHT: '♘',
        BISHOP: '♗',
        ROOK: '♖',
        QUEEN: '♕',
        KING: '♔'
    },
    BLACK_PIECE: {
        PAWN: '♟',
        KNIGHT: '♞',
        BISHOP: '♝',
        ROOK: '♜',
        QUEEN: '♛',
        KING: '♚'
    }
}

class Piece:
    def __init__(self, piece_type: int, color: int):
        self.type = piece_type
        self.color = color
        self.has_moved = False

    def __str__(self):
        return PIECE_SYMBOLS[self.color][self.type]

class Board:
    def __init__(self):
        self.board = [[None for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.setup_board()
        self.current_player = WHITE_PIECE
        self.selected_piece = None
        self.valid_moves = []
        self.white_king_pos = (7, 4)
        self.black_king_pos = (0, 4)
        self.check = False
        self.checkmate = False
        self.stalemate = False

    def setup_board(self):
        # Setup pawns
        for col in range(BOARD_SIZE):
            self.board[1][col] = Piece(PAWN, BLACK_PIECE)
            self.board[6][col] = Piece(PAWN, WHITE_PIECE)

        # Setup rooks
        self.board[0][0] = Piece(ROOK, BLACK_PIECE)
        self.board[0][7] = Piece(ROOK, BLACK_PIECE)
        self.board[7][0] = Piece(ROOK, WHITE_PIECE)
        self.board[7][7] = Piece(ROOK, WHITE_PIECE)

        # Setup knights
        self.board[0][1] = Piece(KNIGHT, BLACK_PIECE)
        self.board[0][6] = Piece(KNIGHT, BLACK_PIECE)
        self.board[7][1] = Piece(KNIGHT, WHITE_PIECE)
        self.board[7][6] = Piece(KNIGHT, WHITE_PIECE)

        # Setup bishops
        self.board[0][2] = Piece(BISHOP, BLACK_PIECE)
        self.board[0][5] = Piece(BISHOP, BLACK_PIECE)
        self.board[7][2] = Piece(BISHOP, WHITE_PIECE)
        self.board[7][5] = Piece(BISHOP, WHITE_PIECE)

        # Setup queens
        self.board[0][3] = Piece(QUEEN, BLACK_PIECE)
        self.board[7][3] = Piece(QUEEN, WHITE_PIECE)

        # Setup kings
        self.board[0][4] = Piece(KING, BLACK_PIECE)
        self.board[7][4] = Piece(KING, WHITE_PIECE)

    def is_valid_position(self, row: int, col: int) -> bool:
        return 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE

    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        if self.is_valid_position(row, col):
            return self.board[row][col]
        return None

    def get_valid_moves(self, row: int, col: int) -> List[Tuple[int, int]]:
        piece = self.get_piece(row, col)
        if not piece:
            return []

        moves = []
        if piece.type == PAWN:
            moves = self.get_pawn_moves(row, col, piece)
        elif piece.type == KNIGHT:
            moves = self.get_knight_moves(row, col, piece)
        elif piece.type == BISHOP:
            moves = self.get_bishop_moves(row, col, piece)
        elif piece.type == ROOK:
            moves = self.get_rook_moves(row, col, piece)
        elif piece.type == QUEEN:
            moves = self.get_queen_moves(row, col, piece)
        elif piece.type == KING:
            moves = self.get_king_moves(row, col, piece)

        # Filter moves that would leave king in check
        valid_moves = []
        for move in moves:
            if not self.would_be_in_check(row, col, move[0], move[1], piece.color):
                valid_moves.append(move)

        return valid_moves

    def get_pawn_moves(self, row: int, col: int, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        direction = -1 if piece.color == WHITE_PIECE else 1
        start_row = 6 if piece.color == WHITE_PIECE else 1

        # Forward move
        if self.is_valid_position(row + direction, col) and not self.get_piece(row + direction, col):
            moves.append((row + direction, col))
            # Double move from starting position
            if row == start_row and not self.get_piece(row + 2 * direction, col):
                moves.append((row + 2 * direction, col))

        # Capture moves
        for dc in [-1, 1]:
            if self.is_valid_position(row + direction, col + dc):
                target = self.get_piece(row + direction, col + dc)
                if target and target.color != piece.color:
                    moves.append((row + direction, col + dc))

        return moves

    def get_knight_moves(self, row: int, col: int, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]

        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = self.get_piece(new_row, new_col)
                if not target or target.color != piece.color:
                    moves.append((new_row, new_col))

        return moves

    def get_bishop_moves(self, row: int, col: int, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]

        for dr, dc in directions:
            for i in range(1, BOARD_SIZE):
                new_row, new_col = row + i * dr, col + i * dc
                if not self.is_valid_position(new_row, new_col):
                    break

                target = self.get_piece(new_row, new_col)
                if not target:
                    moves.append((new_row, new_col))
                else:
                    if target.color != piece.color:
                        moves.append((new_row, new_col))
                    break

        return moves

    def get_rook_moves(self, row: int, col: int, piece: Piece) -> List[Tuple[int, int]]:
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:
            for i in range(1, BOARD_SIZE):
                new_row, new_col = row + i * dr, col + i * dc
                if not self.is_valid_position(new_row, new_col):
                    break

                target = self.get_piece(new_row, new_col)
                if not target:
                    moves.append((new_row, new_col))
                else:
                    if target.color != piece.color:
                        moves.append((new_row, new_col))
                    break

        return moves

    def get_queen_moves(self, row: int
