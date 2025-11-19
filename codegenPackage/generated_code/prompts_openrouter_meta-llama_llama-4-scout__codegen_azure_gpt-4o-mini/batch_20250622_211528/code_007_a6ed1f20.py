"""
Generated Code Metadata:
========================
Original URL: https://btfdbull.pages.dev
Prompt: Provide a detailed explanation of the BTFD Bull Run game and how players can collect and claim BTFD coins.
Generated: DETERMINISTIC_a6ed1f203f3fdc9b
Batch ID: 20250622_211528
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
BTFD Bull Run Game

This script simulates a simple game where players can collect and claim BTFD coins.
Players can earn coins by participating in the game, and they can claim their coins
once they reach a certain threshold.

Game Features:
- Players can join the game and start collecting BTFD coins.
- Players can claim their coins once they reach a specified amount.
- The game includes error handling for invalid operations.

Usage:
- Create a game instance.
- Players can join the game and collect coins.
- Players can claim their coins when they have enough.

"""

class BTFDBullRunGame:
    def __init__(self):
        """Initialize the game with an empty player list and coin threshold."""
        self.players = {}
        self.coin_threshold = 100  # Minimum coins required to claim

    def join_game(self, player_name):
        """Allow a player to join the game.

        Args:
            player_name (str): The name of the player.

        Raises:
            ValueError: If the player name is empty or already exists.
        """
        if not player_name:
            raise ValueError("Player name cannot be empty.")
        if player_name in self.players:
            raise ValueError(f"Player '{player_name}' already exists.")
        
        self.players[player_name] = 0  # Initialize player's coins to 0
        print(f"Player '{player_name}' has joined the game.")

    def collect_coins(self, player_name, amount):
        """Allow a player to collect a specified amount of coins.

        Args:
            player_name (str): The name of the player.
            amount (int): The amount of coins to collect.

        Raises:
            ValueError: If the player does not exist or the amount is invalid.
        """
        if player_name not in self.players:
            raise ValueError(f"Player '{player_name}' does not exist.")
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")
        
        self.players[player_name] += amount
        print(f"Player '{player_name}' collected {amount} coins. Total: {self.players[player_name]} coins.")

    def claim_coins(self, player_name):
        """Allow a player to claim their coins if they meet the threshold.

        Args:
            player_name (str): The name of the player.

        Raises:
            ValueError: If the player does not exist or does not have enough coins.
        """
        if player_name not in self.players:
            raise ValueError(f"Player '{player_name}' does not exist.")
        
        current_coins = self.players[player_name]
        if current_coins < self.coin_threshold:
            raise ValueError(f"Player '{player_name}' does not have enough coins to claim. Current: {current_coins}, Required: {self.coin_threshold}.")
        
        # Reset player's coins after claiming
        self.players[player_name] = 0
        print(f"Player '{player_name}' has claimed their coins. Total claimed: {current_coins} coins.")

# Example usage
if __name__ == "__main__":
    game = BTFDBullRunGame()
    
    try:
        game.join_game("Alice")
        game.collect_coins("Alice", 50)
        game.collect_coins("Alice", 60)  # This will exceed the threshold
        game.claim_coins("Alice")  # This will raise an error due to insufficient coins
    except ValueError as e:
        print(f"Error: {e}")

    try:
        game.collect_coins("Bob", 10)  # This will raise an error since Bob hasn't joined
    except ValueError as e:
        print(f"Error: {e}")

    try:
        game.join_game("Alice")  # This will raise an error since Alice already exists
    except ValueError as e:
        print(f"Error: {e}")
```
