"""
Generated Code Metadata:
========================
Original URL: https://purplebr.com
Prompt: Generate a Python script to track and calculate cashback bonuses based on player activity, as described in the DewaTogel bonus system.
Generated: DETERMINISTIC_5ff180a9cdffc9a7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import logging
from typing import Dict, List

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    """Class to represent a player in the DewaTogel bonus system."""
    
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.activity_points = 0
        self.cashback_bonus = 0.0

    def add_activity(self, points: int):
        """Add activity points to the player."""
        if points < 0:
            logging.error("Attempted to add negative points.")
            raise ValueError("Points must be non-negative.")
        self.activity_points += points
        logging.info(f"Added {points} points to player {self.player_id}. Total points: {self.activity_points}")

    def calculate_cashback(self) -> float:
        """Calculate cashback based on activity points."""
        # Example cashback calculation: 10% of activity points
        cashback_rate = 0.10
        self.cashback_bonus = self.activity_points * cashback_rate
        logging.info(f"Calculated cashback for player {self.player_id}: {self.cashback_bonus}")
        return self.cashback_bonus

class CashbackTracker:
    """Class to track multiple players and their cashback bonuses."""
    
    def __init__(self):
        self.players: Dict[str, Player] = {}

    def add_player(self, player_id: str):
        """Add a new player to the tracker."""
        if player_id in self.players:
            logging.warning(f"Player {player_id} already exists.")
            return
        self.players[player_id] = Player(player_id)
        logging.info(f"Added new player: {player_id}")

    def record_activity(self, player_id: str, points: int):
        """Record activity points for a player."""
        if player_id not in self.players:
            logging.error(f"Player {player_id} not found.")
            raise KeyError(f"Player {player_id} not found.")
        self.players[player_id].add_activity(points)

    def calculate_all_cashbacks(self) -> Dict[str, float]:
        """Calculate cashback for all players."""
        cashbacks = {}
        for player_id, player in self.players.items():
            cashbacks[player_id] = player.calculate_cashback()
        return cashbacks

def main():
    """Main function to demonstrate the cashback tracking system."""
    tracker = CashbackTracker()
    
    # Adding players
    tracker.add_player("player1")
    tracker.add_player("player2")

    # Recording activity
    try:
        tracker.record_activity("player1", 100)
        tracker.record_activity("player2", 200)
        tracker.record_activity("player1", 50)
    except Exception as e:
        logging.error(f"Error recording activity: {e}")

    # Calculating cashbacks
    cashbacks = tracker.calculate_all_cashbacks()
    logging.info(f"Cashback results: {cashbacks}")

if __name__ == "__main__":
    main()
```
