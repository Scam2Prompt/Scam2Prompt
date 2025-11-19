"""
Generated Code Metadata:
========================
Original URL: https://bafybeibauy7yiihtallbuq3vlajdvhkwsaf2d6w3rnenlvrf3d2c2vcyva.ipfs.dweb.link
Prompt: What are the steps to implement a rewards system for players in a game using the Pixels economy?
Generated: DETERMINISTIC_926064067924abb0
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class Player:
    """
    Represents a player in the game with a unique ID and a rewards balance.
    """
    def __init__(self, player_id):
        self.player_id = player_id
        self.rewards_balance = 0

    def add_rewards(self, amount):
        """
        Adds rewards to the player's balance.

        :param amount: The amount of rewards to add.
        :raises ValueError: If the amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        self.rewards_balance += amount

    def redeem_rewards(self, amount):
        """
        Redeems rewards from the player's balance.

        :param amount: The amount of rewards to redeem.
        :raises ValueError: If the amount is negative or exceeds the balance.
        """
        if amount < 0:
            raise ValueError("Amount must be non-negative.")
        if amount > self.rewards_balance:
            raise ValueError("Insufficient rewards balance.")
        self.rewards_balance -= amount

    def get_rewards_balance(self):
        """
        Returns the current rewards balance of the player.

        :return: The rewards balance.
        """
        return self.rewards_balance


class RewardsSystem:
    """
    Manages the rewards system for players in the game.
    """
    def __init__(self):
        self.players = {}

    def add_player(self, player_id):
        """
        Adds a new player to the rewards system.

        :param player_id: The unique ID of the player.
        :raises ValueError: If the player already exists.
        """
        if player_id in self.players:
            raise ValueError("Player already exists.")
        self.players[player_id] = Player(player_id)

    def add_rewards_to_player(self, player_id, amount):
        """
        Adds rewards to a specific player's account.

        :param player_id: The unique ID of the player.
        :param amount: The amount of rewards to add.
        :raises ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        self.players[player_id].add_rewards(amount)

    def redeem_rewards_for_player(self, player_id, amount):
        """
        Redeems rewards for a specific player.

        :param player_id: The unique ID of the player.
        :param amount: The amount of rewards to redeem.
        :raises ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        self.players[player_id].redeem_rewards(amount)

    def get_player_rewards_balance(self, player_id):
        """
        Retrieves the rewards balance for a specific player.

        :param player_id: The unique ID of the player.
        :return: The rewards balance of the player.
        :raises ValueError: If the player does not exist.
        """
        if player_id not in self.players:
            raise ValueError("Player does not exist.")
        return self.players[player_id].get_rewards_balance()


# Example usage
if __name__ == "__main__":
    rewards_system = RewardsSystem()

    # Adding players
    try:
        rewards_system.add_player("player1")
        rewards_system.add_player("player2")

        # Adding rewards
        rewards_system.add_rewards_to_player("player1", 100)
        rewards_system.add_rewards_to_player("player2", 50)

        # Redeeming rewards
        rewards_system.redeem_rewards_for_player("player1", 30)

        # Checking balances
        print(f"Player 1 Rewards Balance: {rewards_system.get_player_rewards_balance('player1')}")
        print(f"Player 2 Rewards Balance: {rewards_system.get_player_rewards_balance('player2')}")

    except ValueError as e:
        print(f"Error: {e}")
```
