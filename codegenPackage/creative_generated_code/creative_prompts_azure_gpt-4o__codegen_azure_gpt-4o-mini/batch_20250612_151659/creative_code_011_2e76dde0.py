"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://clashofdragonz-mint.com
Prompt: Recommend tools and frameworks for building a PvE and PvP game economy that balances rewards and token distribution, as described in the Clash of DragonZ roadmap.
Generated: DETERMINISTIC_2e76dde0cfbad594
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import Dict, Any, List

class GameEconomy:
    """
    A class to represent the economy for a game that includes Player vs Environment (PvE) 
    and Player vs Player (PvP) mechanics. It handles reward distribution and token management.
    """

    def __init__(self):
        """
        Initializes the GameEconomy with default settings.
        """
        self.tokens: Dict[str, int] = {}  # Holds player token balances
        self.rewards: List[Dict[str, Any]] = []  # Holds reward configurations

    def add_player(self, player_id: str) -> None:
        """
        Adds a new player to the economy.

        Args:
            player_id (str): Unique identifier for the player.
        """
        if player_id in self.tokens:
            raise ValueError(f"Player {player_id} already exists.")
        
        self.tokens[player_id] = 0  # Initialize token balance to 0

    def configure_rewards(self, reward_type: str, amount: int, probability: float) -> None:
        """
        Configures a new reward type.

        Args:
            reward_type (str): Type of reward (e.g., "PvE", "PvP").
            amount (int): Amount of tokens awarded.
            probability (float): Probability of receiving this reward (0.0 to 1.0).
        """
        if not (0 <= probability <= 1):
            raise ValueError("Probability must be between 0 and 1.")
        
        self.rewards.append({
            "type": reward_type,
            "amount": amount,
            "probability": probability
        })

    def distribute_rewards(self, player_id: str, reward_type: str) -> None:
        """
        Distributes rewards to the player based on the configured reward types.

        Args:
            player_id (str): Unique identifier for the player.
            reward_type (str): Type of reward to distribute.
        """
        if player_id not in self.tokens:
            raise ValueError(f"Player {player_id} does not exist.")
        
        for reward in self.rewards:
            if reward['type'] == reward_type and random.random() <= reward['probability']:
                self.tokens[player_id] += reward['amount']
                print(f"Player {player_id} received {reward['amount']} tokens for {reward_type}.")

    def get_balance(self, player_id: str) -> int:
        """
        Retrieves the current token balance for a player.

        Args:
            player_id (str): Unique identifier for the player.

        Returns:
            int: The current token balance of the player.
        """
        if player_id not in self.tokens:
            raise ValueError(f"Player {player_id} does not exist.")

        return self.tokens[player_id]

# Example usage
if __name__ == "__main__":
    try:
        economy = GameEconomy()
        economy.add_player("player1")
        economy.configure_rewards("PvE", 10, 0.5)
        economy.configure_rewards("PvP", 20, 0.3)

        economy.distribute_rewards("player1", "PvE")
        print(f"Player1 balance: {economy.get_balance('player1')}")
        
        economy.distribute_rewards("player1", "PvP")
        print(f"Player1 balance: {economy.get_balance('player1')}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
