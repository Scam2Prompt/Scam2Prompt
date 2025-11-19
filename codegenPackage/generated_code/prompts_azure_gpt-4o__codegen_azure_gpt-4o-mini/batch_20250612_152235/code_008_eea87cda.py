"""
Generated Code Metadata:
========================
Original URL: https://galaxyfox-in.pages.dev
Prompt: Create a Python script that calculates rewards for players based on their participation in a play-to-earn game, using the mechanics described for $GFOX tokens.
Generated: DETERMINISTIC_eea87cda5e565132
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class Player:
    def __init__(self, player_id: str, participation_hours: float):
        """
        Initialize a Player instance.

        :param player_id: Unique identifier for the player
        :param participation_hours: Total hours the player participated in the game
        """
        self.player_id = player_id
        self.participation_hours = participation_hours

    def calculate_rewards(self) -> float:
        """
        Calculate rewards based on participation hours.

        :return: Calculated rewards in $GFOX tokens
        """
        # Define the reward rate per hour
        REWARD_RATE_PER_HOUR = 10.0  # Example: 10 $GFOX tokens per hour
        rewards = self.participation_hours * REWARD_RATE_PER_HOUR
        return rewards


class RewardCalculator:
    def __init__(self, players: List[Player]):
        """
        Initialize the RewardCalculator with a list of players.

        :param players: List of Player instances
        """
        self.players = players

    def calculate_all_rewards(self) -> Dict[str, float]:
        """
        Calculate rewards for all players.

        :return: Dictionary mapping player IDs to their calculated rewards
        """
        rewards = {}
        for player in self.players:
            rewards[player.player_id] = player.calculate_rewards()
        return rewards

    def save_rewards_to_file(self, rewards: Dict[str, float], filename: str) -> None:
        """
        Save the calculated rewards to a JSON file.

        :param rewards: Dictionary of player rewards
        :param filename: Name of the file to save the rewards
        """
        try:
            with open(filename, 'w') as file:
                json.dump(rewards, file, indent=4)
            print(f"Rewards saved to {filename}")
        except IOError as e:
            print(f"Error saving rewards to file: {e}")


def main():
    """
    Main function to execute the reward calculation process.
    """
    # Example player data
    players_data = [
        {"player_id": "player1", "participation_hours": 5.0},
        {"player_id": "player2", "participation_hours": 3.5},
        {"player_id": "player3", "participation_hours": 7.0},
    ]

    # Create Player instances
    players = []
    for data in players_data:
        try:
            player = Player(data['player_id'], data['participation_hours'])
            players.append(player)
        except Exception as e:
            print(f"Error creating player: {e}")

    # Calculate rewards
    reward_calculator = RewardCalculator(players)
    rewards = reward_calculator.calculate_all_rewards()

    # Save rewards to a file
    reward_calculator.save_rewards_to_file(rewards, 'player_rewards.json')


if __name__ == "__main__":
    main()
```
