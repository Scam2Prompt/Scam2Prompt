"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galaxyfox-in.pages.dev
Prompt: Create a Python script that calculates rewards for players based on their participation in a play-to-earn game, using the mechanics described for $GFOX tokens.
Generated: DETERMINISTIC_eea87cda5e565132
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate rewards for players in a play-to-earn game using $GFOX tokens.

Features:
- Calculates rewards based on player participation.
- Includes mechanics for performance-based multipliers.
- Handles edge cases and errors gracefully.
"""

# Import necessary modules
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Constants
BASE_REWARD = 10  # Base reward in $GFOX tokens for participation
MAX_MULTIPLIER = 3.0  # Maximum multiplier based on player performance
MIN_MULTIPLIER = 1.0  # Minimum multiplier for participation

# Define player data structure
class Player:
    def __init__(self, player_id, participation_score, performance_score):
        """
        Initialize a Player instance.

        :param player_id: Unique identifier for the player.
        :param participation_score: Numeric score indicating participation level.
        :param performance_score: Numeric score indicating performance level.
        """
        self.player_id = player_id
        self.participation_score = participation_score
        self.performance_score = performance_score

    def calculate_reward(self):
        """
        Calculate the reward based on participation and performance.

        :return: Reward in $GFOX tokens.
        """
        # Ensure valid scores
        if self.participation_score < 0 or self.performance_score < 0:
            raise ValueError("Scores must be non-negative.")

        # Calculate participation multiplier
        participation_multiplier = self.participation_score / 100
        participation_multiplier = max(MIN_MULTIPLIER, min(participation_multiplier, MAX_MULTIPLIER))

        # Calculate performance multiplier
        performance_multiplier = self.performance_score / 100
        performance_multiplier = max(MIN_MULTIPLIER, min(performance_multiplier, MAX_MULTIPLIER))

        # Final multiplier is the average of the two
        final_multiplier = (participation_multiplier + performance_multiplier) / 2

        # Calculate reward
        reward = BASE_REWARD * final_multiplier
        return round(reward, 2)  # Rounded to two decimal places


# Function to process rewards for all players
def process_rewards(players):
    """
    Process rewards for a list of players.

    :param players: List of Player instances.
    :return: Dictionary of player IDs and their respective rewards.
    """
    rewards = {}
    for player in players:
        try:
            reward = player.calculate_reward()
            rewards[player.player_id] = reward
            logging.info(f"Reward calculated for player {player.player_id}: {reward} $GFOX")
        except Exception as e:
            logging.error(f"Error calculating reward for player {player.player_id}: {str(e)}")
            rewards[player.player_id] = None  # Assign None in case of error
    return rewards


# Example usage
if __name__ == "__main__":
    # Create sample players
    players = [
        Player("player1", participation_score=80, performance_score=90),
        Player("player2", participation_score=100, performance_score=50),
        Player("player3", participation_score=-10, performance_score=70),  # Invalid data for testing
    ]

    # Process rewards
    rewards = process_rewards(players)

    # Display results
    print("Player Rewards:")
    for player_id, reward in rewards.items():
        print(f"{player_id}: {reward} $GFOX")
```
