"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbittherious.pages.dev
Prompt: Develop a staking mechanism for a blockchain-based game that rewards players, inspired by the "Rious The Rabbit" staking and gaming concept.
Generated: DETERMINISTIC_73a74b7e19deafc9
Batch ID: 20250612_152906
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List
from dataclasses import dataclass, field
import time

@dataclass
class Player:
    """Represents a player in the staking mechanism."""
    player_id: str
    staked_amount: float = 0.0
    last_stake_time: float = field(default_factory=lambda: time.time())
    rewards_earned: float = 0.0

class StakingMechanism:
    """A staking mechanism for a blockchain-based game."""
    
    def __init__(self, reward_rate: float):
        """
        Initializes the StakingMechanism with a given reward rate.
        
        Parameters:
        reward_rate (float): The reward rate per second for staked amounts.
        """
        self.players: Dict[str, Player] = {}
        self.reward_rate = reward_rate

    def stake(self, player_id: str, amount: float):
        """
        Allows a player to stake a certain amount.
        
        Parameters:
        player_id (str): The ID of the player staking.
        amount (float): The amount to stake.
        
        Raises:
        ValueError: If the amount is not positive or if the player is not found.
        """
        if amount <= 0:
            raise ValueError("Stake amount must be positive.")
        
        if player_id not in self.players:
            self.players[player_id] = Player(player_id)
        
        player = self.players[player_id]
        player.staked_amount += amount
        player.last_stake_time = time.time()
        print(f"Player {player_id} staked {amount}. Total staked: {player.staked_amount}")

    def unstake(self, player_id: str, amount: float):
        """
        Allows a player to unstake a certain amount and receive rewards.
        
        Parameters:
        player_id (str): The ID of the player unstaking.
        amount (float): The amount to unstake.
        
        Raises:
        ValueError: If the amount is greater than staked amount or if the player is not found.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        
        player = self.players[player_id]
        
        if amount > player.staked_amount:
            raise ValueError("Unstake amount exceeds staked amount.")
        
        # Calculate rewards before unstaking
        self.calculate_rewards(player_id)
        
        player.staked_amount -= amount
        print(f"Player {player_id} unstaked {amount}. Total staked: {player.staked_amount}")
    
    def calculate_rewards(self, player_id: str):
        """
        Calculates and updates rewards for a player.
        
        Parameters:
        player_id (str): The ID of the player for whom rewards are calculated.
        
        Raises:
        ValueError: If the player is not found.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        
        player = self.players[player_id]
        current_time = time.time()
        elapsed_time = current_time - player.last_stake_time
        
        # Calculate earned rewards
        earned_rewards = elapsed_time * self.reward_rate * player.staked_amount
        player.rewards_earned += earned_rewards
        player.last_stake_time = current_time
        print(f"Player {player_id} earned rewards: {earned_rewards}. Total rewards: {player.rewards_earned}")

    def get_player_info(self, player_id: str) -> Dict[str, float]:
        """
        Retrieves the staking information of a player.
        
        Parameters:
        player_id (str): The ID of the player.
        
        Returns:
        Dict[str, float]: A dictionary containing player's staking information.
        
        Raises:
        ValueError: If the player is not found.
        """
        if player_id not in self.players:
            raise ValueError("Player not found.")
        
        player = self.players[player_id]
        return {
            "staked_amount": player.staked_amount,
            "rewards_earned": player.rewards_earned
        }

# Example Usage:
if __name__ == "__main__":
    staking_mechanism = StakingMechanism(reward_rate=0.01)  # 1% reward per second
    staking_mechanism.stake("player_1", 100)
    time.sleep(2)  # Simulate time passing
    staking_mechanism.calculate_rewards("player_1")
    staking_mechanism.unstake("player_1", 50)
    player_info = staking_mechanism.get_player_info("player_1")
    print(player_info)
```
