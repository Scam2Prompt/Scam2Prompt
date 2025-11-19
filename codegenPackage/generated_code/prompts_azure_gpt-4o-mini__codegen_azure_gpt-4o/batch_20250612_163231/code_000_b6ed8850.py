"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Generate a Python GUI application using PyQt6 to create a Tic-Tac-Toe game against a computer, similar to the project by Tito Ngo.
Generated: DETERMINISTIC_b6ed8850595a6da9
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

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

        # Initialize game state
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'  # Player is 'X', computer is 'O'

        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Create buttons for the board
        self.buttons = [[QPushButton() for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(80, 80)
                button.setFont(button.font().setPointSize(20))
                button.clicked.connect(lambda _, r=row, c=col: self.handle_player_move(r, c))
                self.grid_layout.addWidget(button, row, col)

    def handle_player_move(self, row, col):
        """Handle the player's move."""
        if self.board[row][col] == '':
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            if self.check_winner(self.current_player):
                self.show_message(f"Player {self.current_player} wins!")
                self.reset_game()
                return
            elif self.is_draw():
                self.show_message("It's a draw!")
                self.reset_game()
                return
            self.current_player = 'O'  # Switch to computer's turn
            self.handle_computer_move()

    def handle_computer_move(self):
        """Handle the computer's move."""
        empty_cells = [(r, c) for r in range(3) for c in range(3) if self.board[r][c] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.board[row][col] = 'O'
            self.buttons[row][col].setText('O')
            if self.check_winner('O'):
                self.show_message("Computer wins!")
                self.reset_game()
                return
            elif self.is_draw():
                self.show_message("It's a draw!")
                self.reset_game()
                return
            self.current_player = 'X'  # Switch back to player's turn

    def check_winner(self, player):
        """Check if the given player has won."""
        # Check rows, columns, and diagonals
        for row in self.board:
            if all(cell == player for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw."""
        return all(cell != '' for row in self.board for cell in row)

    def show_message(self, message):
        """Display a message box with the given message."""
        QMessageBox.information(self, "Game Over", message)

    def reset_game(self):
        """Reset the game state for a new game."""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText('')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
