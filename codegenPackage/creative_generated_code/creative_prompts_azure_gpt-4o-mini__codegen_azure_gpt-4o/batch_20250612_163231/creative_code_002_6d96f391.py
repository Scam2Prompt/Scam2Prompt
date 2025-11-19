"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: How can I create a basic Tic-Tac-Toe game in Python using PyQt6, referencing Tito Ngo's approach in his portfolio?
Generated: DETERMINISTIC_6d96f3918c74e358
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToeGame(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 300)

        # Initialize the board state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"  # Start with player X

        # Set up the UI
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.grid_layout = QGridLayout()
        self.main_widget.setLayout(self.grid_layout)

        # Create buttons for the board
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(80, 80)
                button.setStyleSheet("font-size: 20px;")
                button.clicked.connect(lambda _, r=row, c=col: self.handle_button_click(r, c))
                self.grid_layout.addWidget(button, row, col)

    def handle_button_click(self, row, col):
        """Handles button clicks, updates board state, and checks for game status."""
        # Check if the cell is already taken
        if self.board[row][col] != "":
            return  # Do nothing if the cell is already occupied

        # Update the board state and button text
        self.board[row][col] = self.current_player
        self.buttons[row][col].setText(self.current_player)

        # Check for win or draw conditions
        if self.check_winner():
            QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
            self.reset_game()
        elif self.check_draw():
            QMessageBox.information(self, "Game Over", "It's a draw!")
            self.reset_game()
        else:
            # Switch to the next player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Checks if the current player has won the game."""
        # Check rows, columns, and diagonals for a winning condition
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)):  # Check rows
                return True
            if all(self.board[j][i] == self.current_player for j in range(3)):  # Check columns
                return True
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False

    def check_draw(self):
        """Checks if the game is a draw."""
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        """Resets the game for a new round."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
        self.current_player = "X"  # Reset to player X

if __name__ == "__main__":
    # Start the application
    app = QApplication(sys.argv)
    window = TicTacToeGame()
    window.show()
    sys.exit(app.exec())
```
