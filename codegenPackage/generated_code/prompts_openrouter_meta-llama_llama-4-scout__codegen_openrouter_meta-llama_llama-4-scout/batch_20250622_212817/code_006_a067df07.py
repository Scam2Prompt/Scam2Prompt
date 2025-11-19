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
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt

class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tic-Tac-Toe")
        self.setGeometry(100, 100, 300, 300)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.player_turn = "X"

        self.buttons = []
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
        return lambda: self.click(i, j)

    def click(self, i, j):
        if self.buttons[i][j].text() == "":
            self.buttons[i][j].setText(self.player_turn)
            if self.check_win():
                QMessageBox.information(self, "Game Over", f"Player {self.player_turn} wins!")
                self.reset_game()
            elif self.check_draw():
                QMessageBox.information(self, "Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        # Check rows and columns
        for i in range(3):
            if self.buttons[i][0].text() == self.buttons[i][1].text() == self.buttons[i][2].text() != "":
                return True
            if self.buttons[0][i].text() == self.buttons[1][i].text() == self.buttons[2][i].text() != "":
                return True

        # Check diagonals
        if self.buttons[0][0].text() == self.buttons[1][1].text() == self.buttons[2][2].text() != "":
            return True
        if self.buttons[0][2].text() == self.buttons[1][1].text() == self.buttons[2][0].text() != "":
            return True

        return False

    def check_draw(self):
        for row in self.buttons:
            for button in row:
                if button.text() == "":
                    return False
        return True

    def reset_game(self):
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button.setText("")

def main():
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
```
