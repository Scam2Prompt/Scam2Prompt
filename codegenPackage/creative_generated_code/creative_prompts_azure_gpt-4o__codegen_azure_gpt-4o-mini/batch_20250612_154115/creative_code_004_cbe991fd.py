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
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)
        self.current_player = 'X'
        self.board = [None] * 9
        
        self.initUI()

    def initUI(self):
        # Create a central widget and set the layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        # Create buttons for the Tic Tac Toe grid
        for i in range(3):
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.clicked.connect(lambda checked, row=i, col=j: self.make_move(row, col))
                self.grid_layout.addWidget(button, i, j)

    def make_move(self, row, col):
        # Calculate index for the board list
        index = 3 * row + col

        # Check if the move is valid
        if self.board[index] is None:
            self.board[index] = self.current_player
            self.update_button(row, col)
            if self.check_winner():
                self.show_winner(self.current_player)
            elif None not in self.board:
                self.show_draw()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def update_button(self, row, col):
        # Update the button text based on the current player
        button = self.grid_layout.itemAtPosition(row, col).widget()
        button.setText(self.current_player)

    def check_winner(self):
        # Define winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)               # Diagonals
        ]

        # Check for a winner
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] != None:
                return True
        return False

    def show_winner(self, player):
        # Show a message box with the winner
        QMessageBox.information(self, "Game Over", f"Player {player} wins!")
        self.reset_game()

    def show_draw(self):
        # Show a message box indicating a draw
        QMessageBox.information(self, "Game Over", "It's a draw!")
        self.reset_game()

    def reset_game(self):
        # Reset the game state
        self.current_player = 'X'
        self.board = [None] * 9
        for i in range(3):
            for j in range(3):
                button = self.grid_layout.itemAtPosition(i, j).widget()
                button.setText("")

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        game = TicTacToe()
        game.show()
        sys.exit(app.exec())
    except Exception as e:
        print(f"An error occurred: {e}")
```
