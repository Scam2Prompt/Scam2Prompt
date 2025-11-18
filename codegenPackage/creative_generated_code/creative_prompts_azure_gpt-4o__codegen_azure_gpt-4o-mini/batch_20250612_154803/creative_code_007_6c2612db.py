"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://paxful-login.id
Prompt: Create a promotional algorithm that calculates and distributes bonuses and rewards to players based on their activity, similar to the bonus system described on Planet128.
Generated: DETERMINISTIC_6c2612dbfcba2c97
Batch ID: 20250612_154803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class Player:
    """Class representing a player with an ID and activity metrics."""
    
    def __init__(self, player_id: int, activity_score: float):
        self.player_id = player_id
        self.activity_score = activity_score
        self.bonus = 0.0

    def __repr__(self):
        return f"Player({self.player_id}, Activity Score: {self.activity_score}, Bonus: {self.bonus})"

class BonusDistribution:
    """Class to handle bonus calculations and distributions for players."""
    
    def __init__(self, players: List[Player]):
        self.players = players

    def calculate_bonus(self) -> None:
        """Calculate bonuses based on players' activity scores."""
        total_activity = sum(player.activity_score for player in self.players)
        
        # Check for division by zero
        if total_activity == 0:
            raise ValueError("Total activity score is zero, cannot calculate bonuses.")
        
        for player in self.players:
            # Calculate bonus as a percentage of the total activity score
            player.bonus = (player.activity_score / total_activity) * 1000  # Example: 1000 is total bonus pool
    
    def distribute_bonus(self) -> None:
        """Distribute calculated bonuses to players."""
        for player in self.players:
            print(f"Distributing bonus of {player.bonus:.2f} to Player {player.player_id}")

def main():
    """Main function to execute the bonus distribution algorithm."""
    
    # Example player data (PlayerID, Activity Score)
    player_data = [
        (1, 150.0),
        (2, 300.0),
        (3, 450.0),
        (4, 100.0)
    ]
    
    # Create Player instances
    players = [Player(player_id, activity_score) for player_id, activity_score in player_data]

    # Initialize bonus distribution system
    bonus_system = BonusDistribution(players)

    try:
        # Calculate bonuses
        bonus_system.calculate_bonus()
        # Distribute bonuses
        bonus_system.distribute_bonus()
        
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
