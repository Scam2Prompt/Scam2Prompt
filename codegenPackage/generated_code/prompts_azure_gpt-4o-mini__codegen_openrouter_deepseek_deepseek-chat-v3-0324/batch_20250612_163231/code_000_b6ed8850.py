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
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QGridLayout, QPushButton, QWidget, QLabel, QVBoxLayout, QMessageBox
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
import random


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 350)
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        self.init_ui()

    def init_ui(self):
        """Initialize the UI components."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # Title label
        self.title_label = QLabel("Tic-Tac-Toe")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Arial", 16))
        layout.addWidget(self.title_label)

        # Game board
        self.grid_layout = QGridLayout()
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(QSize(80, 80))
                button.setFont(QFont("Arial", 24))
                button.clicked.connect(lambda _, pos=i * 3 + j: self.handle_click(pos))
                self.grid_layout.addWidget(button, i, j)
                self.buttons.append(button)
        layout.addLayout(self.grid_layout)

        # Reset button
        self.reset_button = QPushButton("Reset Game")
        self.reset_button.clicked.connect(self.reset_game)
        layout.addWidget(self.reset_button)

    def handle_click(self, pos):
        """Handle button clicks from the player."""
        if not self.game_over and self.board[pos] == "":
            self.buttons[pos].setText(self.current_player)
            self.board[pos] = self.current_player
            if self.check_winner():
                self.game_over = True
                QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
                return
            elif self.check_draw():
                self.game_over = True
                QMessageBox.information(self, "Game Over", "It's a draw!")
                return
            self.current_player = "O" if self.current_player == "X" else "X"
            if self.current_player == "O":
                self.computer_move()

    def computer_move(self):
        """Handle the computer's move."""
        available_positions = [i for i, val in enumerate(self.board) if val == ""]
        if available_positions:
            pos = random.choice(available_positions)
            self.buttons[pos].setText("O")
            self.board[pos] = "O"
            if self.check_winner():
                self.game_over = True
                QMessageBox.information(self, "Game Over", "Computer wins!")
                return
            elif self.check_draw():
                self.game_over = True
                QMessageBox.information(self, "Game Over", "It's a draw!")
                return
            self.current_player = "X"

    def check_winner(self):
        """Check if there is a winning combination."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for combo in winning_combinations:
            a, b, c = combo
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def check_draw(self):
        """Check if the game is a draw."""
        return "" not in self.board

    def reset_game(self):
        """Reset the game state."""
        self.current_player = "X"
        self.board = [""] * 9
        self.game_over = False
        for button in self.buttons:
            button.setText("")


if __name__ == "__main__":
    app = QApplication([])
    game = TicTacToe()
    game.show()
    app.exec()
```
