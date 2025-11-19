"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purplebr.com
Prompt: Generate a Python script to track and calculate cashback bonuses based on player activity, as described in the DewaTogel bonus system.
Generated: DETERMINISTIC_5ff180a9cdffc9a7
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import logging

# Configure logging to output debug messages to a file
logging.basicConfig(level=logging.DEBUG, filename='cashback_tracker.log', 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    """Class to represent a player in the cashback system."""
    
    def __init__(self, player_id, name):
        """Initialize a Player with an ID and a name."""
        self.player_id = player_id
        self.name = name
        self.activity_points = 0
        self.cashback_rate = 0.01  # Default cashback rate of 1%
        self.cashback_bonus = 0.0

    def update_activity(self, points):
        """Update the player's activity points and calculate cashback bonus."""
        if points < 0:
            logging.error(f"Negative points error for player {self.name}: {points}")
            raise ValueError("Points cannot be negative.")
        
        self.activity_points += points
        logging.info(f"Updated activity points for {self.name}: {self.activity_points}")
        
        self.calculate_cashback()

    def calculate_cashback(self):
        """Calculate the cashback bonus based on the activity points."""
        self.cashback_bonus = self.activity_points * self.cashback_rate
        logging.debug(f"Calculated cashback for {self.name}: {self.cashback_bonus}")

    def reset_activity(self):
        """Reset the player's activity points and cashback bonus for the new period."""
        logging.info(f"Resetting activity for player {self.name}.")
        self.activity_points = 0
        self.cashback_bonus = 0.0

    def get_cashback_bonus(self):
        """Return the current cashback bonus."""
        return self.cashback_bonus

class CashbackSystem:
    """Class to manage the cashback system for multiple players."""
    
    def __init__(self):
        """Initialize an empty player list."""
        self.players = {}

    def add_player(self, player_id, name):
        """Add a new player to the cashback system."""
        if player_id in self.players:
            logging.warning(f"Player {player_id} already exists.")
            raise ValueError("Player ID already exists.")
        
        self.players[player_id] = Player(player_id, name)
        logging.info(f"Added new player: {name} with ID: {player_id}")

    def update_player_activity(self, player_id, points):
        """Update activity points for a specific player."""
        if player_id not in self.players:
            logging.error(f"Player ID {player_id} not found for activity update.")
            raise KeyError("Player ID not found.")

        self.players[player_id].update_activity(points)

    def get_player_cashback(self, player_id):
        """Get the current cashback bonus of a given player."""
        if player_id not in self.players:
            logging.error(f"Player ID {player_id} not found when retrieving cashback.")
            raise KeyError("Player ID not found.")

        return self.players[player_id].get_cashback_bonus()

    def reset_all_activities(self):
        """Reset activities for all players at the end of the cashback period."""
        for player in self.players.values():
            player.reset_activity()

# Example usage of the CashbackSystem
if __name__ == "__main__":
    try:
        cashback_system = CashbackSystem()
        cashback_system.add_player("P001", "Alice")
        cashback_system.add_player("P002", "Bob")

        cashback_system.update_player_activity("P001", 100)
        cashback_system.update_player_activity("P002", 200)

        print(f"Alice's cashback: {cashback_system.get_player_cashback('P001')}")
        print(f"Bob's cashback: {cashback_system.get_player_cashback('P002')}")

        # Reset cashback activities at the end of the period
        cashback_system.reset_all_activities()

    except Exception as e:
        logging.exception("An error occurred in the cashback system: %s", str(e))
```
