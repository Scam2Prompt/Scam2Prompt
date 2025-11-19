"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Provide a step-by-step guide to creating a Tic-Tac-Toe game GUI in PyQt6, similar to the project described on Tito Ngo's portfolio.
Generated: DETERMINISTIC_50df3efa19c742ce
Batch ID: 20250612_154115
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QMessageBox, QGridLayout
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(400, 500)
        
        # Game state variables
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        self.init_ui()
    
    def init_ui(self):
        """Initialize the main UI components."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Title label
        self.title_label = QLabel("Tic-Tac-Toe")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setFont(QFont("Arial", 24))
        main_layout.addWidget(self.title_label)
        
        # Current player label
        self.player_label = QLabel(f"Current Player: {self.current_player}")
        self.player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.player_label.setFont(QFont("Arial", 16))
        main_layout.addWidget(self.player_label)
        
        # Game board
        self.board_layout = QGridLayout()
        self.board_layout.setSpacing(5)
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        
        for row in range(3):
            for col in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.setFont(QFont("Arial", 40))
                button.clicked.connect(lambda _, r=row, c=col: self.on_button_click(r, c))
                self.buttons[row][col] = button
                self.board_layout.addWidget(button, row, col)
        
        main_layout.addLayout(self.board_layout)
        
        # Reset button
        reset_button = QPushButton("Reset Game")
        reset_button.setFont(QFont("Arial", 14))
        reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(reset_button)
    
    def on_button_click(self, row, col):
        """Handle button clicks on the game board."""
        if self.game_over or self.board[row][col] != "":
            return
        
        self.board[row][col] = self.current_player
        self.buttons[row][col].setText(self.current_player)
        
        if self.check_winner():
            self.game_over = True
            QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
            return
        
        if self.check_draw():
            self.game_over = True
            QMessageBox.information(self, "Game Over", "It's a draw!")
            return
        
        self.switch_player()
    
    def check_winner(self):
        """Check if the current player has won."""
        # Check rows
        for row in range(3):
            if all(self.board[row][col] == self.current_player for col in range(3)):
                return True
        
        # Check columns
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(3)):
            return True
        if all(self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        
        return False
    
    def check_draw(self):
        """Check if the game is a draw."""
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))
    
    def switch_player(self):
        """Switch to the other player."""
        self.current_player = "O" if self.current_player == "X" else "X"
        self.player_label.setText(f"Current Player: {self.current_player}")
    
    def reset_game(self):
        """Reset the game state."""
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.game_over = False
        
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
        
        self.player_label.setText(f"Current Player: {self.current_player}")


def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
```
