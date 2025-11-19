"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mint.alphadogs.run
Prompt: Create a function that allows users to earn rewards in the Alphadogs blockchain game based on their racing performance.
Generated: DETERMINISTIC_c915d1ef55b01c95
Batch ID: 20250612_163909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_system.py

import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class AlphadogsRewards:
    """
    A class to manage the rewards system for the Alphadogs blockchain game.
    """

    def __init__(self):
        """
        Initializes the rewards system with predefined reward tiers.
        """
        self.reward_tiers = {
            "gold": 100,  # Points for players who finish in the top position
            "silver": 50, # Points for players who finish in second position
            "bronze": 25, # Points for players who finish in third position
            "participation": 10 # Points for simply participating in the race
        }

    def calculate_rewards(self, player_position):
        """
        Calculates rewards based on the player's race performance.

        Parameters:
        player_position (int): The position the player finished in the race (1 for first place, 2 for second, etc.).

        Returns:
        int: The reward points earned based on performance.

        Raises:
        ValueError: If player_position is not a positive integer.
        """
        try:
            # Validate player_position
            if not isinstance(player_position, int) or player_position <= 0:
                raise ValueError("player_position must be a positive integer.")
            
            # Determine rewards based on position
            if player_position == 1:
                return self.reward_tiers["gold"]
            elif player_position == 2:
                return self.reward_tiers["silver"]
            elif player_position == 3:
                return self.reward_tiers["bronze"]
            else:
                return self.reward_tiers["participation"]  # For all other participants
        except ValueError as e:
            logging.error(f"Invalid player_position: {e}")
            raise

    def award_rewards(self, player_id, player_position):
        """
        Assigns rewards to a player based on their race performance.

        Parameters:
        player_id (str): Unique identifier for the player.
        player_position (int): The position the player finished in the race.

        Returns:
        dict: A dictionary containing the player's ID and earned reward points.

        Raises:
        ValueError: If player_id is empty or player_position is invalid.
        """
        try:
            # Validate player_id
            if not player_id or not isinstance(player_id, str):
                raise ValueError("player_id must be a non-empty string.")

            # Calculate rewards
            rewards = self.calculate_rewards(player_position)

            # Return a structured response
            return {
                "player_id": player_id,
                "reward_points": rewards
            }
        except ValueError as e:
            logging.error(f"Error awarding rewards: {e}")
            raise


# Example usage
if __name__ == "__main__":
    # Initialize rewards system
    rewards_system = AlphadogsRewards()

    try:
        # Award rewards to a player
        player_rewards = rewards_system.award_rewards(player_id="player123", player_position=1)
        logging.info(f"Rewards awarded: {player_rewards}")
    except Exception as e:
        logging.error(f"Failed to award rewards: {e}")
```
