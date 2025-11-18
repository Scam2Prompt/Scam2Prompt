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
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic Tac Toe")
        self.setGeometry(100, 100, 300, 300)
        
        # Initialize the game state
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        
        # Set up the main widget and layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)
        
        # Create buttons for the Tic Tac Toe grid
        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton("")
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 24px;")
                button.clicked.connect(self.make_move)
                self.grid_layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def make_move(self):
        """Handles the button click event and updates the game state."""
        button = self.sender()  # Get the button that was clicked
        if button.text() == "":  # Check if the cell is empty
            button.setText(self.current_player)
            index = self.get_button_index(button)
            self.board[index] = self.current_player
            
            if self.check_winner():
                QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif '' not in self.board:
                QMessageBox.information(self, "Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player

    def get_button_index(self, button):
        """Returns the index of the button in the board."""
        for i in range(3):
            for j in range(3):
                if self.buttons[i][j] == button:
                    return i * 3 + j
        return -1  # Should never happen

    def check_winner(self):
        """Checks if the current player has won the game."""
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]               # Diagonals
        ]
        for combo in winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def reset_game(self):
        """Resets the game to the initial state."""
        self.current_player = 'X'
        self.board = ['' for _ in range(9)]
        for row in self.buttons:
            for button in row:
                button.setText("")  # Clear the button text

def main():
    """Initializes the application and starts the Tic Tac Toe game."""
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
