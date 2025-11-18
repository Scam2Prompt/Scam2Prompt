"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://landing-jackpotcow.pages.dev
Prompt: Write code to implement a loyalty rewards system for an online casino, including free spins and exclusive perks for players, as highlighted in Jackpot Cow Casino's promotions.
Generated: DETERMINISTIC_9968ac25eea8e0bd
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# loyalty_rewards_system.py

from datetime import datetime
from typing import List, Dict, Optional

class Player:
    """
    Represents a player in the online casino.
    """
    def __init__(self, player_id: int, name: str, join_date: datetime):
        self.player_id = player_id
        self.name = name
        self.join_date = join_date
        self.loyalty_points = 0
        self.free_spins = 0
        self.perks = []

    def add_loyalty_points(self, points: int):
        """
        Add loyalty points to the player.
        """
        if points < 0:
            raise ValueError("Points cannot be negative.")
        self.loyalty_points += points

    def redeem_free_spins(self, num_spins: int):
        """
        Redeem free spins for the player.
        """
        if num_spins <= 0:
            raise ValueError("Number of spins must be positive.")
        if num_spins > self.free_spins:
            raise ValueError("Not enough free spins available.")
        self.free_spins -= num_spins

    def add_perks(self, perk: str):
        """
        Add exclusive perks to the player.
        """
        if perk not in self.perks:
            self.perks.append(perk)

    def __repr__(self):
        return f"Player({self.player_id}, {self.name}, Points: {self.loyalty_points}, Free Spins: {self.free_spins}, Perks: {self.perks})"


class LoyaltyRewardsSystem:
    """
    Manages the loyalty rewards system for the casino.
    """
    def __init__(self):
        self.players: Dict[int, Player] = {}

    def add_player(self, player_id: int, name: str, join_date: datetime):
        """
        Add a new player to the rewards system.
        """
        if player_id in self.players:
            raise ValueError(f"Player with ID {player_id} already exists.")
        self.players[player_id] = Player(player_id, name, join_date)

    def award_loyalty_points(self, player_id: int, points: int):
        """
        Award loyalty points to a player.
        """
        player = self.players.get(player_id)
        if not player:
            raise ValueError(f"Player with ID {player_id} not found.")
        player.add_loyalty_points(points)

    def grant_free_spins(self, player_id: int, num_spins: int):
        """
        Grant free spins to a player.
        """
        player = self.players.get(player_id)
        if not player:
            raise ValueError(f"Player with ID {player_id} not found.")
        if num_spins <= 0:
            raise ValueError("Number of spins must be positive.")
        player.free_spins += num_spins

    def award_exclusive_perks(self, player_id: int, perk: str):
        """
        Award exclusive perks to a player.
        """
        player = self.players.get(player_id)
        if not player:
            raise ValueError(f"Player with ID {player_id} not found.")
        player.add_perks(perk)

    def get_player_info(self, player_id: int) -> Optional[Player]:
        """
        Retrieve information about a specific player.
        """
        return self.players.get(player_id)

    def __repr__(self):
        return f"LoyaltyRewardsSystem({self.players})"


# Example usage of the system
if __name__ == "__main__":
    casino_rewards = LoyaltyRewardsSystem()

    # Add players
    casino_rewards.add_player(1, "Alice", datetime(2023, 1, 15))
    casino_rewards.add_player(2, "Bob", datetime(2023, 2, 10))

    # Award loyalty points
    casino_rewards.award_loyalty_points(1, 100)
    casino_rewards.award_loyalty_points(2, 50)

    # Grant free spins
    casino_rewards.grant_free_spins(1, 10)
    casino_rewards.grant_free_spins(2, 5)

    # Award exclusive perks
    casino_rewards.award_exclusive_perks(1, "VIP Lounge Access")
    casino_rewards.award_exclusive_perks(2, "Priority Support")

    # Print player info
    print(casino_rewards.get_player_info(1))
    print(casino_rewards.get_player_info(2))
```
