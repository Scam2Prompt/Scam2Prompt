"""
Generated Code Metadata:
========================
Original URL: https://staylloud.io
Prompt: Explain how the Loud experiment on staylloud.io incentivizes social engagement through perpetual rewards, focusing on the distribution of SOL rewards.
Generated: DETERMINISTIC_5bdb4e00f0574b73
Batch ID: 20250622_212817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
This script simulates the Loud experiment on staylloud.io, which incentivizes social engagement 
through perpetual rewards. It focuses on the distribution of SOL rewards to participants based 
on their engagement levels. The code is designed to be clean, efficient, and production-ready.
"""

import time
import random
from typing import List, Dict

# Constants
SOL_REWARD_POOL = 1000  # Total SOL reward pool available for distribution
ENGAGEMENT_MULTIPLIER = 0.1  # Multiplier to calculate rewards based on engagement
REWARD_INTERVAL = 60  # Time interval (in seconds) for distributing rewards

# Error classes
class RewardDistributionError(Exception):
    """Custom exception for errors during reward distribution."""
    pass

# Participant class
class Participant:
    """
    Represents a participant in the Loud experiment.
    Attributes:
        username (str): The username of the participant.
        engagement_score (float): The engagement score of the participant.
    """
    def __init__(self, username: str, engagement_score: float):
        self.username = username
        self.engagement_score = engagement_score
        self.sol_rewards = 0.0  # Initial SOL rewards

    def add_rewards(self, rewards: float):
        """Adds SOL rewards to the participant."""
        self.sol_rewards += rewards

# Reward distribution function
def distribute_rewards(participants: List[Participant], total_rewards: float) -> None:
    """
    Distributes SOL rewards among participants based on their engagement scores.
    Args:
        participants (List[Participant]): List of participants.
        total_rewards (float): Total SOL rewards to distribute.
    Raises:
        RewardDistributionError: If total_rewards is less than or equal to zero.
    """
    if total_rewards <= 0:
        raise RewardDistributionError("Total rewards must be greater than zero.")

    # Calculate total engagement score
    total_engagement = sum(p.engagement_score for p in participants)
    if total_engagement == 0:
        raise RewardDistributionError("Total engagement score must be greater than zero.")

    # Distribute rewards proportionally
    for participant in participants:
        reward_share = (participant.engagement_score / total_engagement) * total_rewards
        participant.add_rewards(reward_share)

# Simulate engagement
def simulate_engagement(participants: List[Participant]) -> None:
    """
    Simulates engagement by randomly updating participants' engagement scores.
    Args:
        participants (List[Participant]): List of participants.
    """
    for participant in participants:
        # Randomly increase engagement score
        participant.engagement_score += random.uniform(0, ENGAGEMENT_MULTIPLIER)

# Main function
def main():
    """
    Main function to run the Loud experiment simulation.
    """
    # Initialize participants
    participants = [
        Participant("Alice", 10.0),
        Participant("Bob", 20.0),
        Participant("Charlie", 15.0),
    ]

    try:
        while True:
            print("Simulating engagement...")
            simulate_engagement(participants)

            print("Distributing rewards...")
            distribute_rewards(participants, SOL_REWARD_POOL)

            # Display participant rewards
            for participant in participants:
                print(f"{participant.username}: {participant.sol_rewards:.2f} SOL")

            # Wait for the next reward interval
            time.sleep(REWARD_INTERVAL)

    except KeyboardInterrupt:
        print("\nSimulation stopped by user.")
    except RewardDistributionError as e:
        print(f"Error during reward distribution: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Entry point
if __name__ == "__main__":
    main()
```
