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
from PyQt6 import QtWidgets, QtGui, QtCore

class TicTacToe(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)
        self.grid = QtWidgets.QGridLayout(self)
        self.buttons = {}
        self.current_player = "X"  # Start with player X
        self.initUI()

    def initUI(self):
        # Create grid buttons
        for row in range(3):
            for col in range(3):
                button = QtWidgets.QPushButton("")
                button.setFont(QtGui.QFont("Arial", 24))
                button.clicked.connect(lambda checked, r=row, c=col: self.player_move(r, c))
                self.grid.addWidget(button, row, col)
                self.buttons[(row, col)] = button

        self.reset_button = QtWidgets.QPushButton("Reset Game")
        self.reset_button.clicked.connect(self.reset_game)
        self.grid.addWidget(self.reset_button, 3, 0, 1, 3)

        self.show()

    def player_move(self, row, col):
        """Handle player's move and trigger computer's move if valid."""
        if self.buttons[(row, col)].text() == "" and self.check_winner() is None:
            self.buttons[(row, col)].setText(self.current_player)
            if self.check_winner() is None:
                self.current_player = "O"
                self.computer_move()
                if self.check_winner() is not None:
                    self.show_winner()

    def computer_move(self):
        """Randomly select an empty spot for the computer's move."""
        available_moves = [(r, c) for r in range(3) for c in range(3) if self.buttons[(r, c)].text() == ""]
        if available_moves:
            row, col = random.choice(available_moves)
            self.buttons[(row, col)].setText(self.current_player)
            if self.check_winner() is not None:
                self.show_winner()
            else:
                self.current_player = "X"

    def check_winner(self):
        """Check for a winner or a draw."""
        # Check rows, columns and diagonals
        for i in range(3):
            if self.buttons[(i, 0)].text() == self.buttons[(i, 1)].text() == self.buttons[(i, 2)].text() != "":
                return self.buttons[(i, 0)].text()
            if self.buttons[(0, i)].text() == self.buttons[(1, i)].text() == self.buttons[(2, i)].text() != "":
                return self.buttons[(0, i)].text()
        if self.buttons[(0, 0)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 2)].text() != "":
            return self.buttons[(0, 0)].text()
        if self.buttons[(0, 2)].text() == self.buttons[(1, 1)].text() == self.buttons[(2, 0)].text() != "":
            return self.buttons[(0, 2)].text()

        # Check for draw
        if all(self.buttons[(r, c)].text() != "" for r in range(3) for c in range(3)):
            return "Draw"
        return None

    def show_winner(self):
        """Display the winner in a message box."""
        winner = self.check_winner()
        if winner:
            QtWidgets.QMessageBox.information(self, "Game Over", f"{winner} wins!" if winner != "Draw" else "It's a draw!")
        self.reset_game()

    def reset_game(self):
        """Reset the game to the initial state."""
        for button in self.buttons.values():
            button.setText("")
        self.current_player = "X"  # Reset to player X

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    game = TicTacToe()
    sys.exit(app.exec())
```
