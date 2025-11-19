"""
Generated Code Metadata:
========================
Original URL: https://symbioticsnake.github.io
Prompt: Write a Python program using PyQt6 to create a Tic-Tac-Toe GUI that allows a user to play against a computer, as described on Tito Ngo's portfolio website.
Generated: DETERMINISTIC_071efaf5dc54d0b4
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
import random
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import pyqtSlot

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.buttons = []
        self.player_turn = True
        self.game_over = False

        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.clicked.connect(self.create_slot(i, j))
                self.layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

    def create_slot(self, i, j):
        @pyqtSlot()
        def slot():
            self.click(i, j)
        return slot

    def click(self, i, j):
        if self.game_over:
            return

        if self.buttons[i][j].text() == "":
            self.buttons[i][j].setText("X")
            if self.check_win("X"):
                self.game_over = True
                self.show_win_message("Player")
            elif self.check_draw():
                self.game_over = True
                self.show_draw_message()
            else:
                self.computer_move()

    def computer_move(self):
        empty_buttons = [(i, j) for i in range(3) for j in range(3) if self.buttons[i][j].text() == ""]
        if empty_buttons:
            i, j = self.best_move(empty_buttons)
            self.buttons[i][j].setText("O")
            if self.check_win("O"):
                self.game_over = True
                self.show_win_message("Computer")
            elif self.check_draw():
                self.game_over = True
                self.show_draw_message()

    def best_move(self, empty_buttons):
        # Simple AI: try to win, then block player, then move randomly
        for i, j in empty_buttons:
            self.buttons[i][j].setText("O")
            if self.check_win("O"):
                self.buttons[i][j].setText("")
                return i, j
            self.buttons[i][j].setText("")
        for i, j in empty_buttons:
            self.buttons[i][j].setText("X")
            if self.check_win("X"):
                self.buttons[i][j].setText("")
                return i, j
            self.buttons[i][j].setText("")
        return random.choice(empty_buttons)

    def check_win(self, player):
        for row in self.buttons:
            if all(button.text() == player for button in row):
                return True
        for col in range(3):
            if all(self.buttons[row][col].text() == player for row in range(3)):
                return True
        if all(self.buttons[i][i].text() == player for i in range(3)):
            return True
        if all(self.buttons[i][2-i].text() == player for i in range(3)):
            return True
        return False

    def check_draw(self):
        return all(button.text() != "" for row in self.buttons for button in row)

    def show_win_message(self, winner):
        QMessageBox.information(self, "Game Over", f"{winner} wins!")

    def show_draw_message(self):
        QMessageBox.information(self, "Game Over", "It's a draw!")

def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
