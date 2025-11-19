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


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)
        self.current_player = "X"
        self.board = [""] * 9  # 3x3 board initialized as empty
        self.init_ui()

    def init_ui(self):
        # Create a central widget and set a grid layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)
        
        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = [QPushButton("") for _ in range(9)]
        for i, button in enumerate(self.buttons):
            button.setFont(button.font() + button.font().setPointSize(24))
            button.clicked.connect(lambda checked, idx=i: self.make_move(idx))
            self.layout.addWidget(button, i // 3, i % 3)

    def make_move(self, idx):
        # Handle clicking on a button
        if self.board[idx] == "":
            self.board[idx] = self.current_player
            self.buttons[idx].setText(self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
            elif "" not in self.board:  # Check for draw
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != "":
                return True
        return False

    def show_winner(self, player):
        # Display a message box with the winner
        QMessageBox.information(self, "Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_draw(self):
        # Display a message box for a draw
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        # Reset the game state
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.setText("")

if __name__ == "__main__":
    # Entry point for the application
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
```
