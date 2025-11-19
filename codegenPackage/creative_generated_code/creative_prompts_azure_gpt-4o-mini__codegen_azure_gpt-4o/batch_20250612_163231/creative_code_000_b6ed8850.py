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
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 300)

        # Central widget setup
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(5)

        # Initialize game state
        self.board = [''] * 9  # Empty board
        self.current_player = 'X'  # Player starts first

        # Create buttons for the grid
        self.buttons = []
        for i in range(9):
            button = QPushButton("")
            button.setFixedSize(90, 90)
            button.setFont(button.font())
            button.clicked.connect(lambda _, idx=i: self.handle_click(idx))
            self.buttons.append(button)
            self.grid_layout.addWidget(button, i // 3, i % 3)

    def handle_click(self, index):
        """Handles button clicks for player's move."""
        if self.board[index] == '' and self.current_player == 'X':
            self.board[index] = 'X'
            self.buttons[index].setText('X')
            if self.check_winner('X'):
                self.show_message("You win!")
                self.reset_game()
                return
            elif '' not in self.board:
                self.show_message("It's a draw!")
                self.reset_game()
                return
            self.current_player = 'O'
            self.computer_move()

    def computer_move(self):
        """Handles computer's move."""
        available_moves = [i for i, spot in enumerate(self.board) if spot == '']
        if available_moves:
            index = random.choice(available_moves)
            self.board[index] = 'O'
            self.buttons[index].setText('O')
            if self.check_winner('O'):
                self.show_message("Computer wins!")
                self.reset_game()
                return
            elif '' not in self.board:
                self.show_message("It's a draw!")
                self.reset_game()
                return
            self.current_player = 'X'

    def check_winner(self, player):
        """Checks if the given player has won."""
        win_patterns = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]
        for pattern in win_patterns:
            if all(self.board[i] == player for i in pattern):
                return True
        return False

    def show_message(self, message):
        """Displays a message box with the given message."""
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def reset_game(self):
        """Resets the game for a new round."""
        self.board = [''] * 9
        self.current_player = 'X'
        for button in self.buttons:
            button.setText("")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
