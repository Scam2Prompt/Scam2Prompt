"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ooi-ev8.pages.dev
Prompt: Create a Python program to track trading competitions on Bitunix and calculate potential rewards based on the prize pool distribution.
Generated: DETERMINISTIC_1420e71d1daabc1c
Batch ID: 20250612_151705
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import sys
from typing import List, Dict


class TradingCompetition:
    """
    A class to represent trading competitions.
    Tracks participants and calculates rewards based on their rankings.
    """

    def __init__(self, prize_pool: float, distribution: List[float]):
        """
        Initializes the competition with a prize pool and distribution percentages.

        :param prize_pool: Total prize money for the competition.
        :param distribution: List of distribution percentages for the top participants.
                             e.g., [50, 30, 20] means 50% for 1st, 30% for 2nd, 20% for 3rd.
        """
        if not distribution or not isinstance(distribution, list):
            raise ValueError("Distribution must be a non-empty list of percentages.")
        if sum(distribution) != 100:
            raise ValueError("Distribution percentages must sum to 100.")
        self.prize_pool = prize_pool
        self.distribution = distribution
        self.participants = {}

    def add_participant(self, username: str, trading_volume: float):
        """
        Adds a participant with their trading volume.

        :param username: Unique username of the participant.
        :param trading_volume: Trading volume of the participant.
        """
        if username in self.participants:
            raise ValueError(f"Participant '{username}' already exists.")
        if trading_volume < 0:
            raise ValueError("Trading volume must be a non-negative number.")
        self.participants[username] = trading_volume

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculates rewards for participants based on their rankings and prize pool distribution.

        :return: A dictionary where keys are usernames and values are rewards.
        """
        if not self.participants:
            raise ValueError("No participants available to calculate rewards.")

        # Sort participants by trading volume in descending order
        ranked_participants = sorted(self.participants.items(), key=lambda x: x[1], reverse=True)
        rewards = {}
        for i, (username, _) in enumerate(ranked_participants):
            if i < len(self.distribution):
                # Allocate reward based on the distribution
                percentage = self.distribution[i]
                reward = (percentage / 100) * self.prize_pool
                rewards[username] = reward
            else:
                # If ranking exceeds distribution percentages, no reward is given
                rewards[username] = 0.0
        return rewards

    def export_rewards_to_json(self, file_path: str):
        """
        Exports the calculated rewards to a JSON file.

        :param file_path: Path to the output JSON file.
        """
        rewards = self.calculate_rewards()
        try:
            with open(file_path, "w") as file:
                json.dump(rewards, file, indent=4)
        except IOError as e:
            print(f"Error writing to file: {e}", file=sys.stderr)
            raise


# Example usage
if __name__ == "__main__":
    try:
        # Initialize competition with a $1000 prize pool and distribution percentages
        competition = TradingCompetition(prize_pool=1000, distribution=[50, 30, 20])

        # Add participants and their trading volumes
        competition.add_participant("Alice", 50000)
        competition.add_participant("Bob", 30000)
        competition.add_participant("Charlie", 20000)

        # Calculate and display rewards
        rewards = competition.calculate_rewards()
        print("Rewards:", rewards)

        # Export rewards to a JSON file
        competition.export_rewards_to_json("rewards.json")
        print("Rewards exported to 'rewards.json'.")
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
```
