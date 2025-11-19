"""
Generated Code Metadata:
========================
Original URL: https://claimcompound.net
Prompt: Design a basic algorithm for Agar.io game AI, allowing a computer-controlled cell to effectively hunt and eat player-controlled cells.
Generated: DETERMINISTIC_1acf99dee16c76d1
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
import random

class Cell:
    """Represents a cell in the Agar.io game."""
    
    def __init__(self, x, y, mass):
        """
        Initializes a cell.

        Args:
            x (float): The x-coordinate of the cell.
            y (float): The y-coordinate of the cell.
            mass (float): The mass of the cell.
        """
        self.x = x
        self.y = y
        self.mass = mass

class PlayerCell(Cell):
    """Represents a player-controlled cell."""
    
    def __init__(self, x, y, mass):
        super().__init__(x, y, mass)

class BotCell(Cell):
    """Represents a computer-controlled cell."""
    
    def __init__(self, x, y, mass):
        super().__init__(x, y, mass)

class AgarGame:
    """Simulates the Agar.io game."""
    
    def __init__(self):
        self.player_cells = []
        self.bot_cells = []

    def add_player_cell(self, cell):
        """Adds a player-controlled cell to the game."""
        self.player_cells.append(cell)

    def add_bot_cell(self, cell):
        """Adds a computer-controlled cell to the game."""
        self.bot_cells.append(cell)

    def distance(self, cell1, cell2):
        """
        Calculates the Euclidean distance between two cells.

        Args:
            cell1 (Cell): The first cell.
            cell2 (Cell): The second cell.

        Returns:
            float: The distance between the two cells.
        """
        return math.sqrt((cell1.x - cell2.x) ** 2 + (cell1.y - cell2.y) ** 2)

    def can_eat(self, bot_cell, player_cell):
        """
        Checks if a bot cell can eat a player cell.

        Args:
            bot_cell (BotCell): The bot cell.
            player_cell (PlayerCell): The player cell.

        Returns:
            bool: True if the bot cell can eat the player cell, False otherwise.
        """
        return bot_cell.mass > player_cell.mass

    def get_closest_player(self, bot_cell):
        """
        Finds the closest player cell to a bot cell.

        Args:
            bot_cell (BotCell): The bot cell.

        Returns:
            PlayerCell: The closest player cell, or None if no player cells exist.
        """
        closest_player = None
        min_distance = float('inf')
        for player in self.player_cells:
            distance = self.distance(bot_cell, player)
            if distance < min_distance:
                min_distance = distance
                closest_player = player
        return closest_player

    def update_bot(self, bot_cell):
        """
        Updates the position of a bot cell.

        Args:
            bot_cell (BotCell): The bot cell.
        """
        closest_player = self.get_closest_player(bot_cell)
        if closest_player and self.can_eat(bot_cell, closest_player):
            # Move towards the closest player cell
            dx = closest_player.x - bot_cell.x
            dy = closest_player.y - bot_cell.y
            angle = math.atan2(dy, dx)
            speed = 1.0  # adjust this value to change the bot's speed
            bot_cell.x += math.cos(angle) * speed
            bot_cell.y += math.sin(angle) * speed
        else:
            # Randomly move if no player cell can be eaten
            angle = random.uniform(0, 2 * math.pi)
            speed = 0.1  # adjust this value to change the bot's speed
            bot_cell.x += math.cos(angle) * speed
            bot_cell.y += math.sin(angle) * speed

    def update(self):
        """Updates the game state."""
        for bot in self.bot_cells:
            self.update_bot(bot)

    def eat_player(self, bot_cell, player_cell):
        """
        Removes a player cell if it can be eaten by a bot cell.

        Args:
            bot_cell (BotCell): The bot cell.
            player_cell (PlayerCell): The player cell.
        """
        if self.can_eat(bot_cell, player_cell):
            self.player_cells.remove(player_cell)
            bot_cell.mass += player_cell.mass

def main():
    game = AgarGame()

    # Create player cells
    player1 = PlayerCell(10, 10, 10)
    player2 = PlayerCell(20, 20, 20)
    game.add_player_cell(player1)
    game.add_player_cell(player2)

    # Create bot cells
    bot1 = BotCell(15, 15, 30)
    game.add_bot_cell(bot1)

    # Game loop
    for _ in range(100):
        game.update()
        print(f"Bot position: ({bot1.x:.2f}, {bot1.y:.2f}), Mass: {bot1.mass:.2f}")
        if player1 in game.player_cells:
            print(f"Player 1 position: ({player1.x:.2f}, {player1.y:.2f}), Mass: {player1.mass:.2f}")
        if player2 in game.player_cells:
            print(f"Player 2 position: ({player2.x:.2f}, {player2.y:.2f}), Mass: {player2.mass:.2f}")
        if bot1 in game.bot_cells:
            closest_player = game.get_closest_player(bot1)
            if closest_player:
                game.eat_player(bot1, closest_player)

if __name__ == "__main__":
    main()
```
