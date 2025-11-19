"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Generate a Python GUI application using PyQt6 to create a Tic-Tac-Toe game against a computer, similar to the project by Tito Ngo.
Generated: DETERMINISTIC_b6ed8850595a6da9
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
import random
from PyQt6 import QtWidgets, QtGui, QtCore

class TicTacToe(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)
        self.grid_layout = QtWidgets.QGridLayout()
        self.setLayout(self.grid_layout)

        # Initialize the game board and current player
        self.board = [None] * 9
        self.current_player = 'X'
        self.game_active = True
        
        # Create buttons for the game board
        self.buttons = []
        for i in range(9):
            button = QtWidgets.QPushButton("")
            button.setFont(QtGui.QFont("Arial", 24))
            button.clicked.connect(lambda _, idx=i: self.player_move(idx))
            self.buttons.append(button)
            self.grid_layout.addWidget(button, i // 3, i % 3)

        self.reset_button = QtWidgets.QPushButton("Restart Game")
        self.reset_button.clicked.connect(self.reset_game)
        self.grid_layout.addWidget(self.reset_button, 3, 0, 1, 3)

    def player_move(self, idx):
        """Handle player's move."""
        if self.game_active and self.board[idx] is None:
            self.board[idx] = self.current_player
            self.buttons[idx].setText(self.current_player)
            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif None not in self.board:
                self.end_game("It's a tie!")
            else:
                self.current_player = 'O'  # Switch to computer player
                self.computer_move()

    def computer_move(self):
        """Make a random move for the computer."""
        available_moves = [i for i in range(9) if self.board[i] is None]
        if available_moves:
            idx = random.choice(available_moves)
            self.board[idx] = self.current_player
            self.buttons[idx].setText(self.current_player)
            if self.check_winner(self.current_player):
                self.end_game("Player O wins!")
            elif None not in self.board:
                self.end_game("It's a tie!")
            else:
                self.current_player = 'X'  # Switch back to player

    def check_winner(self, player):
        """Check if the current player has won."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        return any(all(self.board[i] == player for i in combo) for combo in winning_combinations)

    def end_game(self, message):
        """End the game and show a message."""
        self.game_active = False
        QtWidgets.QMessageBox.information(self, "Game Over", message)

    def reset_game(self):
        """Reset the game to the initial state."""
        self.board = [None] * 9
        for button in self.buttons:
            button.setText("")
        self.current_player = 'X'
        self.game_active = True

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
