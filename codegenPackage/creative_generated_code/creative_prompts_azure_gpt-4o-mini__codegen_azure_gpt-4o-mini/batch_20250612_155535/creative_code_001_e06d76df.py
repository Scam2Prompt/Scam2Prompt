"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galagames-rewards.com
Prompt: Write a Python script that implements the 2048 game logic, including tile merging and movement.
Generated: DETERMINISTIC_e06d76dfc7fe92c9
Batch ID: 20250612_155535
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random

class Game2048:
    def __init__(self):
        """Initialize a new game with a 4x4 board and two starting tiles."""
        self.size = 4
        self.board = [[0] * self.size for _ in range(self.size)]
        self.add_new_tile()
        self.add_new_tile()

    def add_new_tile(self):
        """Add a new tile (2 or 4) to a random empty position on the board."""
        empty_positions = [(r, c) for r in range(self.size) for c in range(self.size) if self.board[r][c] == 0]
        
        if not empty_positions:
            return  # No empty positions left
        
        row, col = random.choice(empty_positions)
        self.board[row][col] = 4 if random.random() < 0.1 else 2

    def compress(self, row):
        """Compress the tiles in the row to the left."""
        new_row = [num for num in row if num != 0]
        new_row += [0] * (self.size - len(new_row))
        return new_row

    def merge(self, row):
        """Merge tiles in the row to the left and return the new row after merging."""
        new_row = self.compress(row)
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1] and new_row[i] != 0:
                new_row[i] *= 2
                new_row[i + 1] = 0
        return self.compress(new_row)

    def move_left(self):
        """Move tiles to the left and merge them."""
        moved = False
        for i in range(self.size):
            original_row = self.board[i][:]
            self.board[i] = self.merge(self.board[i])
            if self.board[i] != original_row:
                moved = True
        if moved:
            self.add_new_tile()

    def move_right(self):
        """Move tiles to the right and merge them."""
        self.board = [row[::-1] for row in self.board]
        self.move_left()
        self.board = [row[::-1] for row in self.board]

    def move_up(self):
        """Move tiles up and merge them."""
        self.board = [list(row) for row in zip(*self.board)]  # Transpose board
        self.move_left()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose back

    def move_down(self):
        """Move tiles down and merge them."""
        self.board = [list(row) for row in zip(*self.board)]  # Transpose board
        self.move_right()
        self.board = [list(row) for row in zip(*self.board)]  # Transpose back

    def is_game_over(self):
        """Check if there are no moves left."""
        for row in self.board:
            if 0 in row:
                return False
            for i in range(self.size - 1):
                if row[i] == row[i + 1]:
                    return False
        for col in range(self.size):
            if self.board[0][col] == self.board[1][col] or self.board[1][col] == self.board[2][col] or self.board[2][col] == self.board[3][col]:
                return False
        return True

    def get_board(self):
        """Return the current state of the board."""
        return self.board

if __name__ == "__main__":
    game = Game2048()
    
    # Main game loop (simple representation, can be replaced with a UI for full game experience)
    while not game.is_game_over():
        print("Current Board:")
        for row in game.get_board():
            print(row)
        
        move = input("Enter move (w/a/s/d for up/left/down/right): ")
        if move == 'a':
            game.move_left()
        elif move == 'd':
            game.move_right()
        elif move == 'w':
            game.move_up()
        elif move == 's':
            game.move_down()
        else:
            print("Invalid move. Please use 'w', 'a', 's', or 'd'.")
    
    print("Game Over!")
    print("Final Board:")
    for row in game.get_board():
        print(row)
```
