"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: What are the steps to implement a rewards system for players in a game using the Pixels economy?
Generated: DETERMINISTIC_926064067924abb0
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Player:
    """Represents a player in the game with a unique ID and a reward balance."""
    
    def __init__(self, player_id):
        self.player_id = player_id
        self.reward_balance = 0 # Initial rewards are set to zero

    def add_rewards(self, amount):
        """Adds rewards to the player's balance.

        Args:
            amount (int): The amount of rewards to add.

        Raises:
            ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount of rewards to add must be non-negative.")
        self.reward_balance += amount

    def redeem_rewards(self, amount):
        """Redeems rewards from the player's balance.

        Args:
            amount (int): The amount of rewards to redeem.

        Raises:
            ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Amount of rewards to redeem must be non-negative.")
        if amount > self.reward_balance:
            raise ValueError("Insufficient rewards balance.")
        self.reward_balance -= amount

    def get_rewards_balance(self):
        """Returns the current rewards balance of the player.

        Returns:
            int: The current rewards balance.
        """
        return self.reward_balance


class RewardsSystem:
    """Manages the rewards system for players in the game."""

    def __init__(self):
        self.players = {}  # Dictionary to store players by their ID

    def add_player(self, player_id):
        """Adds a new player to the rewards system.

        Args:
            player_id (str): The unique ID of the player.

        Raises:
            ValueError: If the player already exists.
        """
        if player_id in self.players:
            raise ValueError("Player already exists.")
        self.players[player_id] = Player(player_id)

    def reward_player(self, player_id, amount):
        """Rewards a player with a specified amount.

        Args:
            player_id (str): The unique ID of the player.
            amount (int): The amount of rewards to add.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        self.players[player_id].add_rewards(amount)

    def redeem_rewards(self, player_id, amount):
        """Redeems a specified amount of rewards for a player.

        Args:
            player_id (str): The unique ID of the player.
            amount (int): The amount of rewards to redeem.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        self.players[player_id].redeem_rewards(amount)

    def get_player_balance(self, player_id):
        """Gets the current rewards balance of a player.

        Args:
            player_id (str): The unique ID of the player.

        Returns:
            int: The current rewards balance of the player.

        Raises:
            ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        return self.players[player_id].get_rewards_balance()


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Adding players
    rewards_system.add_player("player1")
    rewards_system.add_player("player2")

    # Rewarding players
    rewards_system.reward_player("player1", 50)
    rewards_system.reward_player("player2", 30)

    # Redeeming rewards
    try:
        rewards_system.redeem_rewards("player1", 20)
    except ValueError as e:
        print(f"Error: {e}")

    # Getting player balances
    print(f"Player 1 Balance: {rewards_system.get_player_balance('player1')}")
    print(f"Player 2 Balance: {rewards_system.get_player_balance('player2')}")
```
