"""
Generated Code Metadata:
========================
Original URL: https://www.meta.pika.asia
Prompt: Generate code for a staking rewards system in a blockchain gaming platform, aligning with MetaLeagues' roadmap Phase 2 goals. Include functionality for calculating and distributing rewards based on player activity.
Generated: DETERMINISTIC_84eac013323324ea
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards.py

from datetime import datetime, timedelta
from decimal import Decimal
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Player:
    """Class representing a player in the staking rewards system."""
    
    def __init__(self, player_id: str):
        self.player_id = player_id
        self.staked_amount = Decimal('0.0')
        self.last_staked_time = None
        self.total_rewards = Decimal('0.0')

    def stake(self, amount: Decimal):
        """Stake a certain amount of tokens."""
        if amount <= 0:
            logging.error("Stake amount must be greater than zero.")
            raise ValueError("Stake amount must be greater than zero.")
        
        self.staked_amount += amount
        self.last_staked_time = datetime.now()
        logging.info(f"Player {self.player_id} staked {amount} tokens.")

    def calculate_rewards(self, current_time: datetime) -> Decimal:
        """Calculate rewards based on the time staked and the amount staked."""
        if self.last_staked_time is None:
            return Decimal('0.0')

        time_staked = (current_time - self.last_staked_time).total_seconds() / 3600  # in hours
        reward_rate = Decimal('0.05')  # Example: 5% reward rate per hour
        rewards = self.staked_amount * reward_rate * time_staked
        logging.info(f"Player {self.player_id} calculated rewards: {rewards}.")
        return rewards

    def distribute_rewards(self, current_time: datetime):
        """Distribute rewards to the player."""
        rewards = self.calculate_rewards(current_time)
        self.total_rewards += rewards
        self.last_staked_time = current_time  # Reset last staked time
        logging.info(f"Player {self.player_id} distributed rewards: {rewards}. Total rewards: {self.total_rewards}.")

class StakingRewardsSystem:
    """Class to manage the staking rewards system for multiple players."""
    
    def __init__(self):
        self.players = {}

    def add_player(self, player_id: str):
        """Add a new player to the system."""
        if player_id in self.players:
            logging.error(f"Player {player_id} already exists.")
            raise ValueError(f"Player {player_id} already exists.")
        
        self.players[player_id] = Player(player_id)
        logging.info(f"Added player {player_id} to the staking rewards system.")

    def stake_tokens(self, player_id: str, amount: Decimal):
        """Stake tokens for a player."""
        if player_id not in self.players:
            logging.error(f"Player {player_id} not found.")
            raise ValueError(f"Player {player_id} not found.")
        
        self.players[player_id].stake(amount)

    def distribute_rewards(self):
        """Distribute rewards to all players based on their activity."""
        current_time = datetime.now()
        for player in self.players.values():
            player.distribute_rewards(current_time)

# Example usage
if __name__ == "__main__":
    try:
        staking_system = StakingRewardsSystem()
        staking_system.add_player("player1")
        staking_system.stake_tokens("player1", Decimal('100.0'))
        
        # Simulate waiting for some time before distributing rewards
        # In a real application, this would be triggered by an event or a scheduled task
        staking_system.distribute_rewards()
        
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
