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

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)
        self.current_player = "X"
        self.board = [""] * 9
        self.initUI()

    def initUI(self):
        # Create a central widget and set the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.clicked.connect(lambda _, x=i, y=j: self.player_move(x, y))
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def player_move(self, x, y):
        # Handle player's move
        if self.board[x * 3 + y] == "":
            self.board[x * 3 + y] = self.current_player
            self.buttons[x][y].setText(self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            else:
                self.current_player = "O"
                self.computer_move()

    def computer_move(self):
        # Handle computer's move
        available_moves = [i for i in range(9) if self.board[i] == ""]
        if available_moves:
            move = random.choice(available_moves)
            self.board[move] = self.current_player
            self.buttons[move // 3][move % 3].setText(self.current_player)
            if self.check_winner(self.current_player):
                self.show_winner(self.current_player)
            else:
                self.current_player = "X"

    def check_winner(self, player):
        # Check if the given player has won
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def show_winner(self, player):
        # Show a message box with the winner
        QMessageBox.information(self, "Game Over", f"Player {player} wins!")
        self.reset_game()

    def reset_game(self):
        # Reset the game state
        self.board = [""] * 9
        self.current_player = "X"
        for row in self.buttons:
            for button in row:
                button.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
```
