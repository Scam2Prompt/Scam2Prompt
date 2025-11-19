"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Develop a Python variant of a Tic-Tac-Toe game using a GUI framework, similar to Tito Ngo's PyQt6 project.
Generated: DETERMINISTIC_a067df07ec74c592
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(300, 300)

        # Initialize game state
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        # Create the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout()
        self.central_widget.setLayout(self.grid_layout)

        # Create buttons for the grid
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(80, 80)
                button.setFont(button.font().setPointSize(20))
                button.clicked.connect(lambda _, r=row, c=col: self.handle_click(r, c))
                self.grid_layout.addWidget(button, row, col)

    def handle_click(self, row, col):
        # Check if the cell is already occupied
        if self.board[row][col] != "":
            return

        # Update the board and button text
        self.board[row][col] = self.current_player
        self.buttons[row][col].setText(self.current_player)

        # Check for a winner or a draw
        if self.check_winner():
            self.show_message(f"Player {self.current_player} wins!")
            self.reset_game()
        elif self.check_draw():
            self.show_message("It's a draw!")
            self.reset_game()
        else:
            # Switch to the other player
            self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        # Check if all cells are filled and there's no winner
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def show_message(self, message):
        # Display a message box with the given message
        msg_box = QMessageBox(self)
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()

    def reset_game(self):
        # Reset the game state for a new game
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())
```
