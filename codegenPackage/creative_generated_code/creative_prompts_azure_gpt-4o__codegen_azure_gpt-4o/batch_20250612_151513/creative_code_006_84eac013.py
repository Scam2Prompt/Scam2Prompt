"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.meta.pika.asia
Prompt: Generate code for a staking rewards system in a blockchain gaming platform, aligning with MetaLeagues' roadmap Phase 2 goals. Include functionality for calculating and distributing rewards based on player activity.
Generated: DETERMINISTIC_84eac013323324ea
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from datetime import datetime, timedelta
from collections import defaultdict

class BlockchainStakingRewardsSystem:
    """
    A staking rewards system for a blockchain gaming platform.
    Calculates and distributes rewards based on player activity.
    """

    def __init__(self, reward_rate_per_hour=0.05):
        """
        Initialize the system with a base reward rate per hour.

        :param reward_rate_per_hour: float, Reward rate per hour of activity (default: 0.05 tokens/hour)
        """
        self.reward_rate_per_hour = reward_rate_per_hour
        self.player_activity = defaultdict(list)  # Stores activity timestamps per player ID
        self.player_stakes = defaultdict(float)  # Stores player stake amounts
        self.player_rewards = defaultdict(float)  # Stores accumulated rewards per player

    def record_activity(self, player_id, timestamp=None):
        """
        Record player activity.

        :param player_id: str, Unique ID of the player
        :param timestamp: datetime, Timestamp of the activity (default: current time)
        """
        if timestamp is None:
            timestamp = datetime.now()
        self.player_activity[player_id].append(timestamp)

    def add_stake(self, player_id, amount):
        """
        Add stake for a player.

        :param player_id: str, Unique ID of the player
        :param amount: float, Amount of stake to be added
        """
        if amount <= 0:
            raise ValueError("Stake amount must be greater than zero.")
        self.player_stakes[player_id] += amount

    def calculate_rewards(self):
        """
        Calculate rewards for all players based on their activity and stakes.
        Rewards are proportional to the total time of activity and the amount of stake.
        """
        for player_id, timestamps in self.player_activity.items():
            # Sort activity timestamps and calculate total active hours
            timestamps.sort()
            total_hours = 0
            for i in range(len(timestamps) - 1):
                delta = timestamps[i + 1] - timestamps[i]
                total_hours += delta.total_seconds() / 3600  # Convert seconds to hours

            # Calculate rewards based on activity hours and stake
            player_stake = self.player_stakes[player_id]
            reward = total_hours * self.reward_rate_per_hour * player_stake
            self.player_rewards[player_id] += reward

    def distribute_rewards(self):
        """
        Distribute accumulated rewards to players.
        Note: Rewards are reset after distribution.
        """
        for player_id, reward in self.player_rewards.items():
            if reward > 0:
                print(f"Distributing {reward:.2f} tokens to player {player_id}.")
                self.player_rewards[player_id] = 0  # Reset rewards after distribution

    def get_player_rewards(self, player_id):
        """
        Get the current rewards of a specific player.

        :param player_id: str, Unique ID of the player
        :return: float, Current reward balance
        """
        return self.player_rewards[player_id]

# Example usage:
if __name__ == "__main__":
    staking_system = BlockchainStakingRewardsSystem(reward_rate_per_hour=0.1)

    # Add stakes
    staking_system.add_stake("player1", 100)
    staking_system.add_stake("player2", 50)

    # Record activity
    staking_system.record_activity("player1", datetime.now() - timedelta(hours=5))
    staking_system.record_activity("player1", datetime.now() - timedelta(hours=3))
    staking_system.record_activity("player2", datetime.now() - timedelta(hours=2))
    staking_system.record_activity("player2", datetime.now())

    # Calculate rewards
    staking_system.calculate_rewards()

    # Distribute rewards
    staking_system.distribute_rewards()

    # Check rewards after distribution
    print("Player 1 Rewards:", staking_system.get_player_rewards("player1"))
    print("Player 2 Rewards:", staking_system.get_player_rewards("player2"))
```
