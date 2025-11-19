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
import random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.player_turn = True
        self.buttons = []
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def initUI(self):
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tic-Tac-Toe')
        layout = QGridLayout()

        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.clicked.connect(self.create_slot(i, j))
                layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        self.setLayout(layout)

    def create_slot(self, i, j):
        return lambda: self.click(i, j)

    def click(self, i, j):
        if self.board[i][j] == ' ':
            self.board[i][j] = 'X'
            self.buttons[i][j].setText('X')
            self.buttons[i][j].setEnabled(False)

            if self.check_win('X'):
                QMessageBox.information(self, 'Game Over', 'You win!')
                self.reset_game()
            elif self.check_draw():
                QMessageBox.information(self, 'Game Over', 'It\'s a draw!')
                self.reset_game()
            else:
                self.computer_move()

    def computer_move(self):
        move = self.get_computer_move()
        self.board[move[0]][move[1]] = 'O'
        self.buttons[move[0]][move[1]].setText('O')
        self.buttons[move[0]][move[1]].setEnabled(False)

        if self.check_win('O'):
            QMessageBox.information(self, 'Game Over', 'Computer wins!')
            self.reset_game()
        elif self.check_draw():
            QMessageBox.information(self, 'Game Over', 'It\'s a draw!')
            self.reset_game()

    def get_computer_move(self):
        # Simple AI: try to win, then block player, then move randomly
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'O'
                    if self.check_win('O'):
                        self.board[i][j] = ' '
                        return (i, j)
                    self.board[i][j] = ' '

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 'X'
                    if self.check_win('X'):
                        self.board[i][j] = ' '
                        return (i, j)
                    self.board[i][j] = ' '

        # Move randomly
        while True:
            i = random.randint(0, 2)
            j = random.randint(0, 2)
            if self.board[i][j] == ' ':
                return (i, j)

    def check_win(self, player):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] == player:
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] == player:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player:
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] == player:
            return True
        return False

    def check_draw(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    return False
        return True

    def reset_game(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for row in self.buttons:
            for button in row:
                button.setText('')
                button.setEnabled(True)

def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
```
