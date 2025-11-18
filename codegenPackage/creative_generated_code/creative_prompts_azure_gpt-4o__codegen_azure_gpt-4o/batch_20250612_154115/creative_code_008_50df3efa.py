"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://symbioticsnake.github.io
Prompt: Provide a step-by-step guide to creating a Tic-Tac-Toe game GUI in PyQt6, similar to the project described on Tito Ngo's portfolio.
Generated: DETERMINISTIC_50df3efa19c742ce
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules from PyQt6
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(200, 200, 300, 300)

        # Initialize game variables
        self.current_player = "X"  # First player starts as "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]  # 3x3 board

        # Create the main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        # Create buttons for the board
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                btn = self.buttons[row][col]
                btn.setFixedSize(80, 80)  # Set button size
                btn.setFont(btn.font().setPointSize(16))  # Adjust font size
                btn.clicked.connect(lambda _, r=row, c=col: self.handle_button_click(r, c))
                self.grid_layout.addWidget(btn, row, col)

    def handle_button_click(self, row, col):
        """Handle button click events."""
        # Check if the cell is already occupied
        if self.board[row][col] != "":
            return  # Do nothing if the cell is already filled

        # Update the board and button text
        self.board[row][col] = self.current_player
        self.buttons[row][col].setText(self.current_player)

        # Check if this move leads to a win or a draw
        if self.check_winner():
            self.end_game(f"Player {self.current_player} wins!")
        elif self.check_draw():
            self.end_game("It's a draw!")
        else:
            # Switch to the other player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if the current player has won."""
        # Check rows, columns, and diagonals for a win condition
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == self.current_player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == self.current_player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == self.current_player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == self.current_player:
            return True
        return False

    def check_draw(self):
        """Check if the game is a draw."""
        for row in self.board:
            if "" in row:
                return False  # At least one empty cell exists
        return True  # No empty cells, the game is a draw

    def end_game(self, message):
        """End the game and show a message."""
        QMessageBox.information(self, "Game Over", message)
        self.reset_board()

    def reset_board(self):
        """Reset the board for a new game."""
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")

# Main entry point of the program
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
