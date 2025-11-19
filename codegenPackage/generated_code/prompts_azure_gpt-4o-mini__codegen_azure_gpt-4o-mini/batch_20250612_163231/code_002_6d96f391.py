"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: How can I create a basic Tic-Tac-Toe game in Python using PyQt6, referencing Tito Ngo's approach in his portfolio?
Generated: DETERMINISTIC_6d96f3918c74e358
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
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox

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
                button.clicked.connect(lambda checked, row=i, col=j: self.make_move(row, col))
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self, row, col):
        """Handles a player's move."""
        index = row * 3 + col
        if self.board[index] is None:  # Check if the cell is empty
            self.board[index] = self.current_player
            self.buttons[row][col].setText(self.current_player)
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
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] is not None:
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
