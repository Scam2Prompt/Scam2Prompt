"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Write a Python script to emulate a Tic-Tac-Toe game using PyQt6, ensuring the GUI design aligns with the example project described on Tito Ngo's portfolio.
Generated: DETERMINISTIC_cbe991fd1dd2caf9
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
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox, QGridLayout, QWidget
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 300)

        # Initialize game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"

        # Create main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Create buttons for the grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = QPushButton("")
                button.setFixedSize(80, 80)
                button.setFont(button.font().setPointSize(20))
                button.clicked.connect(lambda _, r=row, c=col: self.make_move(r, c))
                self.grid_layout.addWidget(button, row, col)
                self.buttons[row][col] = button

    def make_move(self, row, col):
        # Check if the selected cell is empty
        if self.board[row][col] == "":
            # Update game state
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)

            # Check for win or draw
            if self.check_winner(self.current_player):
                self.show_message(f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_draw():
                self.show_message("It's a draw!")
                self.reset_game()
            else:
                # Switch to next player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
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
        # If all cells are filled and no winner, it's a draw
        return all(cell != "" for row in self.board for cell in row)

    def reset_game(self):
        # Reset the game state
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.current_player = "X"
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")

    def show_message(self, message):
        # Display a message box
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

def main():
    # Entry point for the program
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
