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
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QMessageBox
from PyQt6.QtCore import pyqtSlot

class TicTacToe(QWidget):
    """
    A simple implementation of a Tic-Tac-Toe game using PyQt6.
    """

    def __init__(self):
        super().__init__()

        self.initUI()
        self.player_turn = "X"

    def initUI(self):
        """
        Initializes the UI components.
        """
        self.setGeometry(300, 300, 300, 300)
        self.setWindowTitle('Tic-Tac-Toe')

        layout = QGridLayout()
        self.setLayout(layout)

        self.buttons = []
        for i in range(3):
            row = []
            for j in range(3):
                button = QPushButton()
                button.setFixedSize(100, 100)
                button.clicked.connect(self.create_slot(i, j))
                layout.addWidget(button, i, j)
                row.append(button)
            self.buttons.append(row)

        self.show()

    def create_slot(self, i, j):
        """
        Creates a slot for a button click event.

        Args:
            i (int): The row index of the button.
            j (int): The column index of the button.

        Returns:
            A slot function that handles the button click event.
        """
        @pyqtSlot()
        def slot():
            self.button_clicked(i, j)
        return slot

    def button_clicked(self, i, j):
        """
        Handles a button click event.

        Args:
            i (int): The row index of the button.
            j (int): The column index of the button.
        """
        if self.buttons[i][j].text() == "":
            self.buttons[i][j].setText(self.player_turn)
            if self.check_win():
                QMessageBox.information(self, "Game Over", f"Player {self.player_turn} wins!")
                self.reset_game()
            else:
                self.player_turn = "O" if self.player_turn == "X" else "X"

    def check_win(self):
        """
        Checks if there is a winner.

        Returns:
            bool: True if there is a winner, False otherwise.
        """
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

    def reset_game(self):
        """
        Resets the game.
        """
        self.player_turn = "X"
        for row in self.buttons:
            for button in row:
                button.setText("")

def main():
    app = QApplication(sys.argv)
    ex = TicTacToe()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
```
