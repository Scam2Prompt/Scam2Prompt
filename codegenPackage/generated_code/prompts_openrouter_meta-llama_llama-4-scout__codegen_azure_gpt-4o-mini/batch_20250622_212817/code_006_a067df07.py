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
        self.setGeometry(100, 100, 300, 300)
        self.current_player = "X"
        self.board = [""] * 9  # Represents the 3x3 board
        self.initUI()

    def initUI(self):
        # Create a central widget and set the layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QGridLayout(self.central_widget)

        # Create buttons for the Tic-Tac-Toe grid
        self.buttons = []
        for i in range(3):
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setFont(button.font().setPointSize(24))
                button.clicked.connect(lambda checked, row=i, col=j: self.make_move(row, col))
                self.layout.addWidget(button, i, j)
                self.buttons.append(button)

    def make_move(self, row, col):
        index = row * 3 + col
        # Check if the cell is already occupied
        if self.board[index] == "":
            self.board[index] = self.current_player
            self.buttons[index].setText(self.current_player)
            if self.check_winner():
                self.show_winner(self.current_player)
            elif "" not in self.board:
                self.show_draw()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Define winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)              # Diagonals
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != "":
                return True
        return False

    def show_winner(self, player):
        QMessageBox.information(self, "Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_draw(self):
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        self.board = [""] * 9
        for button in self.buttons:
            button.setText("")
        self.current_player = "X"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
```
