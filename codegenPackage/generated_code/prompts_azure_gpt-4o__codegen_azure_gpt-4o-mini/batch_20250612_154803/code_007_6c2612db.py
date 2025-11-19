"""
Generated Code Metadata:
========================
Original URL: https://paxful-login.id
Prompt: Create a promotional algorithm that calculates and distributes bonuses and rewards to players based on their activity, similar to the bonus system described on Planet128.
Generated: DETERMINISTIC_6c2612dbfcba2c97
Batch ID: 20250612_154803
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
    Represents a player in the system with attributes for tracking activity and rewards.
    """
    def __init__(self, player_id, activity_score):
        self.player_id = player_id
        self.activity_score = activity_score
        self.bonus = 0

    def __repr__(self):
        return f"Player({self.player_id}, Activity Score: {self.activity_score}, Bonus: {self.bonus})"


class BonusDistribution:
    """
    Class to handle the distribution of bonuses based on player activity.
    """
    def __init__(self, base_bonus, activity_multiplier):
        self.base_bonus = base_bonus
        self.activity_multiplier = activity_multiplier

    def calculate_bonus(self, player):
        """
        Calculate the bonus for a given player based on their activity score.
        
        :param player: Player object
        :return: Calculated bonus
        """
        if not isinstance(player, Player):
            raise ValueError("Expected a Player instance")
        
        # Calculate bonus based on activity score
        bonus = self.base_bonus + (player.activity_score * self.activity_multiplier)
        return max(bonus, 0)  # Ensure bonus is not negative

    def distribute_bonuses(self, players):
        """
        Distribute bonuses to a list of players.
        
        :param players: List of Player objects
        :return: None
        """
        if not isinstance(players, list):
            raise ValueError("Expected a list of Player instances")
        
        for player in players:
            if not isinstance(player, Player):
                raise ValueError("All items in the list must be Player instances")
            player.bonus = self.calculate_bonus(player)


def main():
    """
    Main function to demonstrate the bonus distribution system.
    """
    # Example players with their activity scores
    players = [
        Player(player_id=1, activity_score=100),
        Player(player_id=2, activity_score=200),
        Player(player_id=3, activity_score=150),
    ]

    # Initialize the bonus distribution system
    base_bonus = 50
    activity_multiplier = 0.5
    bonus_distribution = BonusDistribution(base_bonus, activity_multiplier)

    # Distribute bonuses to players
    try:
        bonus_distribution.distribute_bonuses(players)
    except ValueError as e:
        print(f"Error during bonus distribution: {e}")
        return

    # Output the results
    for player in players:
        print(player)


if __name__ == "__main__":
    main()
```
