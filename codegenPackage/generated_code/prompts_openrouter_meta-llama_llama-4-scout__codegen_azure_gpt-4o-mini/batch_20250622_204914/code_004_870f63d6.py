"""
Generated Code Metadata:
========================
Original URL: https://luckyblock-5bs.pages.dev
Prompt: Design a system for a crypto casino to offer regular bonuses, free spins, and exclusive promotions to its players, using a combination of cryptocurrency and loyalty programs.
Generated: DETERMINISTIC_870f63d6139f821b
Batch ID: 20250622_204914
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from datetime import datetime, timedelta
from typing import List, Dict, Optional

class Player:
    """Represents a player in the crypto casino."""
    
    def __init__(self, player_id: str, username: str):
        self.player_id = player_id
        self.username = username
        self.balance = 0.0
        self.loyalty_points = 0
        self.bonuses: List[Bonus] = []

    def add_balance(self, amount: float):
        """Add funds to the player's balance."""
        if amount < 0:
            raise ValueError("Amount must be positive.")
        self.balance += amount

    def redeem_bonus(self, bonus: 'Bonus'):
        """Redeem a bonus for the player."""
        if bonus in self.bonuses:
            self.bonuses.remove(bonus)
            self.balance += bonus.value
            print(f"{self.username} redeemed bonus: {bonus.description} worth {bonus.value}.")

class Bonus:
    """Represents a bonus that can be awarded to players."""
    
    def __init__(self, description: str, value: float, expiry_date: datetime):
        self.description = description
        self.value = value
        self.expiry_date = expiry_date

    def is_valid(self) -> bool:
        """Check if the bonus is still valid."""
        return datetime.now() < self.expiry_date

class Casino:
    """Represents the crypto casino that manages players and promotions."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}
        self.promotions: List[Bonus] = []

    def add_player(self, player_id: str, username: str):
        """Add a new player to the casino."""
        if player_id in self.players:
            raise ValueError("Player ID already exists.")
        self.players[player_id] = Player(player_id, username)

    def award_bonus(self, player_id: str, description: str, value: float, days_valid: int):
        """Award a bonus to a player."""
        if player_id not in self.players:
            raise ValueError("Player not found.")
        expiry_date = datetime.now() + timedelta(days=days_valid)
        bonus = Bonus(description, value, expiry_date)
        self.players[player_id].bonuses.append(bonus)
        print(f"Awarded bonus to {self.players[player_id].username}: {description} worth {value}.")

    def get_active_promotions(self) -> List[Bonus]:
        """Retrieve all active promotions."""
        return [promo for promo in self.promotions if promo.is_valid()]

    def add_promotion(self, description: str, value: float, days_valid: int):
        """Add a new promotion to the casino."""
        expiry_date = datetime.now() + timedelta(days=days_valid)
        self.promotions.append(Bonus(description, value, expiry_date))
        print(f"Added promotion: {description} worth {value}.")

# Example usage
if __name__ == "__main__":
    try:
        casino = Casino()
        casino.add_player("1", "PlayerOne")
        casino.add_player("2", "PlayerTwo")

        casino.award_bonus("1", "Welcome Bonus", 50.0, 30)
        casino.award_bonus("2", "Loyalty Bonus", 20.0, 15)

        # Redeem a bonus
        player_one = casino.players["1"]
        if player_one.bonuses:
            player_one.redeem_bonus(player_one.bonuses[0])

        # Add and list promotions
        casino.add_promotion("Weekend Special", 10.0, 7)
        active_promotions = casino.get_active_promotions()
        print(f"Active Promotions: {[promo.description for promo in active_promotions]}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
