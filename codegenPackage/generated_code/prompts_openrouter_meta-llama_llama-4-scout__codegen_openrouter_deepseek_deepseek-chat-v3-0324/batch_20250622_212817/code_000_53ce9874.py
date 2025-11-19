"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a Python GUI program using PyQt6 to emulate a Tic-Tac-Toe game against a computer, similar to Tito Ngo's project.
Generated: DETERMINISTIC_53ce98745fa53a6d
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
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QMessageBox, QGridLayout
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont
import random


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.setFixedSize(400, 500)
        
        # Game state variables
        self.board = [""] * 9
        self.current_player = "X"  # Human is X, computer is O
        self.game_over = False
        
        # Initialize UI
        self.init_ui()
        
    def init_ui(self):
        """Initialize the user interface."""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)
        
        # Title label
        self.title_label = QLabel("Tic-Tac-Toe")
        self.title_label.setFont(QFont("Arial", 24))
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.title_label)
        
        # Status label
        self.status_label = QLabel("Your turn (X)")
        self.status_label.setFont(QFont("Arial", 14))
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(self.status_label)
        
        # Game board
        self.board_layout = QGridLayout()
        self.board_layout.setSpacing(5)
        self.buttons = []
        
        for i in range(9):
            button = QPushButton()
            button.setFixedSize(100, 100)
            button.setFont(QFont("Arial", 40))
            button.clicked.connect(lambda _, pos=i: self.handle_click(pos))
            self.buttons.append(button)
            self.board_layout.addWidget(button, i // 3, i % 3)
        
        main_layout.addLayout(self.board_layout)
        
        # Reset button
        reset_button = QPushButton("Reset Game")
        reset_button.setFont(QFont("Arial", 14))
        reset_button.clicked.connect(self.reset_game)
        main_layout.addWidget(reset_button)
        
    def handle_click(self, position):
        """Handle button click events."""
        if self.game_over or self.board[position] != "":
            return
            
        # Human move
        self.make_move(position, "X")
        
        if not self.game_over:
            # Computer move
            self.computer_move()
            
    def make_move(self, position, player):
        """Make a move on the board."""
        self.board[position] = player
        self.buttons[position].setText(player)
        
        if self.check_winner(player):
            self.game_over = True
            winner = "You" if player == "X" else "Computer"
            self.status_label.setText(f"{winner} win!")
            self.show_game_over_message(f"{winner} wins!")
        elif "" not in self.board:
            self.game_over = True
            self.status_label.setText("It's a draw!")
            self.show_game_over_message("It's a draw!")
        else:
            self.current_player = "O" if player == "X" else "X"
            self.status_label.setText(
                "Your turn (X)" if self.current_player == "X" 
                else "Computer's turn (O)"
            )
    
    def computer_move(self):
        """Computer makes a move."""
        available_moves = [i for i, spot in enumerate(self.board) if spot == ""]
        
        if not available_moves:
            return
            
        # Check for winning move
        for move in available_moves:
            temp_board = self.board.copy()
            temp_board[move] = "O"
            if self.check_winner("O", temp_board):
                self.make_move(move, "O")
                return
                
        # Block human's winning move
        for move in available_moves:
            temp_board = self.board.copy()
            temp_board[move] = "X"
            if self.check_winner("X", temp_board):
                self.make_move(move, "O")
                return
                
        # Choose center if available
        if 4 in available_moves:
            self.make_move(4, "O")
            return
            
        # Choose a random corner
        corners = [0, 2, 6, 8]
        available_corners = [c for c in corners if c in available_moves]
        if available_corners:
            self.make_move(random.choice(available_corners), "O")
            return
            
        # Choose a random edge
        edges = [1, 3, 5, 7]
        available_edges = [e for e in edges if e in available_moves]
        if available_edges:
            self.make_move(random.choice(available_edges), "O")
            return
            
        # Fallback to random move
        self.make_move(random.choice(available_moves), "O")
    
    def check_winner(self, player, board=None):
        """Check if the specified player has won."""
        if board is None:
            board = self.board
            
        # Check rows
        for i in range(0, 9, 3):
            if board[i] == board[i+1] == board[i+2] == player:
                return True
                
        # Check columns
        for i in range(3):
            if board[i] == board[i+3] == board[i+6] == player:
                return True
                
        # Check diagonals
        if board[0] == board[4] == board[8] == player:
            return True
        if board[2] == board[4] == board[6] == player:
            return True
            
        return False
    
    def show_game_over_message(self, message):
        """Show a message box when the game ends."""
        msg_box = QMessageBox()
        msg_box.setWindowTitle("Game Over")
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
        
    def reset_game(self):
        """Reset the game state."""
        self.board = [""] * 9
        self.current_player = "X"
        self.game_over = False
        
        for button in self.buttons:
            button.setText("")
            
        self.status_label.setText("Your turn (X)")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
```
