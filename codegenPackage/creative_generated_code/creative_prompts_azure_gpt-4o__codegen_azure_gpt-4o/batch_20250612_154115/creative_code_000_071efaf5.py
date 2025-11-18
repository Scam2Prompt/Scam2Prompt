"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Write a Python program using PyQt6 to create a Tic-Tac-Toe GUI that allows a user to play against a computer, as described on Tito Ngo's portfolio website.
Generated: DETERMINISTIC_071efaf5dc54d0b4
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 300)

        # Create the game board (3x3 grid of buttons)
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Human player starts with "X"

        # Central widget setup
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        self.initialize_board()

    def initialize_board(self):
        """Initialize the Tic-Tac-Toe board with buttons."""
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(lambda _, r=row, c=col: self.make_move(r, c))
                self.grid_layout.addWidget(button, row, col)
                self.board[row][col] = button

    def make_move(self, row, col):
        """Handle a player's move."""
        button = self.board[row][col]
        if button.text() != "":
            return  # Ignore clicks on already occupied cells

        button.setText(self.current_player)

        # Check if the current player has won
        if self.check_winner(self.current_player):
            self.display_winner(self.current_player)
            return

        # Check for a tie
        if self.board_is_full():
            self.display_tie()
            return

        # Switch to the computer's turn
        self.current_player = "O"
        self.computer_move()

    def computer_move(self):
        """Handle the computer's move."""
        possible_moves = [(row, col) for row in range(3) for col in range(3) if self.board[row][col].text() == ""]
        if not possible_moves:
            return  # No moves available (should not happen)

        # Select a random move
        row, col = random.choice(possible_moves)
        self.board[row][col].setText(self.current_player)

        # Check if the computer has won
        if self.check_winner(self.current_player):
            self.display_winner(self.current_player)
            return

        # Check for a tie
        if self.board_is_full():
            self.display_tie()
            return

        # Switch back to the human player's turn
        self.current_player = "X"

    def check_winner(self, player):
        """Check if the given player has won."""
        # Check rows, columns, and diagonals
        for row in range(3):
            if all(self.board[row][col].text() == player for col in range(3)):
                return True
        for col in range(3):
            if all(self.board[row][col].text() == player for row in range(3)):
                return True
        if all(self.board[i][i].text() == player for i in range(3)):
            return True
        if all(self.board[i][2 - i].text() == player for i in range(3)):
            return True
        return False

    def board_is_full(self):
        """Check if the board is full (tie condition)."""
        return all(self.board[row][col].text() != "" for row in range(3) for col in range(3))

    def display_winner(self, player):
        """Display a message box showing the winner."""
        QMessageBox.information(self, "Game Over", f"{player} wins!")
        self.reset_game()

    def display_tie(self):
        """Display a message box showing a tie."""
        QMessageBox.information(self, "Game Over", "It's a tie!")
        self.reset_game()

    def reset_game(self):
        """Reset the game board for a new round."""
        for row in range(3):
            for col in range(3):
                self.board[row][col].setText("")
        self.current_player = "X"  # Reset to human player


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
