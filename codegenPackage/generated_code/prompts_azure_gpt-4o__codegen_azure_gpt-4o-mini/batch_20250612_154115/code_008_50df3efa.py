"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Provide a step-by-step guide to creating a Tic-Tac-Toe game GUI in PyQt6, similar to the project described on Tito Ngo's portfolio.
Generated: DETERMINISTIC_50df3efa19c742ce
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        
        self.current_player = "X"
        self.board = [None] * 9  # Represents the 3x3 board

        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setFont(button.font().setPointSize(24))
                button.clicked.connect(lambda _, x=i, y=j: self.make_move(x, y))
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, x, y):
        """Handles the player's move."""
        if self.board[x * 3 + y] is None:  # Check if the cell is empty
            self.board[x * 3 + y] = self.current_player
            self.buttons[x][y].setText(self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
            elif None not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Checks if the current player has won."""
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.current_player and \
               self.board[combo[1]] == self.current_player and \
               self.board[combo[2]] == self.current_player:
                return True
        return False

    def show_winner(self, player):
        """Displays a message box announcing the winner."""
        QMessageBox.information(self, "Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_draw(self):
        """Displays a message box announcing a draw."""
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        """Resets the game to its initial state."""
        self.current_player = "X"
        self.board = [None] * 9
        for row in self.buttons:
            for button in row:
                button.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
```
