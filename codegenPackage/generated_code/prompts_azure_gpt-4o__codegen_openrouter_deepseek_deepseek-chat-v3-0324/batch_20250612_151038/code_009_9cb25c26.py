"""
Generated Code Metadata:
========================
Original URL: https://pandas-dsp.pages.dev
Prompt: Write a program to simulate gamified staking in PandaVerse, including leveling up NFT Pandas and tracking rewards dynamically.
Generated: DETERMINISTIC_9cb25c261255708e
Batch ID: 20250612_151038
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from dataclasses import dataclass
from enum import Enum, auto
from typing import Dict, List, Optional

class PandaRarity(Enum):
    COMMON = auto()
    RARE = auto()
    EPIC = auto()
    LEGENDARY = auto()

@dataclass
class PandaNFT:
    token_id: int
    name: str
    rarity: PandaRarity
    level: int = 1
    xp: int = 0
    staked: bool = False
    last_claim_time: float = 0.0

    def __post_init__(self):
        self.last_claim_time = time.time()

    def add_xp(self, amount: int) -> None:
        """Add XP to the Panda and check for level up."""
        self.xp += amount
        while self.xp >= self.xp_needed_for_next_level():
            self.xp -= self.xp_needed_for_next_level()
            self.level_up()

    def level_up(self) -> None:
        """Increase the Panda's level by 1."""
        self.level += 1

    def xp_needed_for_next_level(self) -> int:
        """Calculate XP needed for next level based on current level and rarity."""
        base_xp = 100 * self.level
        rarity_multiplier = {
            PandaRarity.COMMON: 1.0,
            PandaRarity.RARE: 1.2,
            PandaRarity.EPIC: 1.5,
            PandaRarity.LEGENDARY: 2.0
        }
        return int(base_xp * rarity_multiplier[self.rarity])

    def claim_rewards(self) -> float:
        """Calculate and claim rewards based on staking duration and attributes."""
        if not self.staked:
            return 0.0
        
        current_time = time.time()
        duration = current_time - self.last_claim_time
        self.last_claim_time = current_time

        # Base rewards per hour
        base_reward = 1.0
        
        # Apply modifiers
        rarity_multiplier = {
            PandaRarity.COMMON: 1.0,
            PandaRarity.RARE: 1.5,
            PandaRarity.EPIC: 2.0,
            PandaRarity.LEGENDARY: 3.0
        }
        
        level_multiplier = 1 + (self.level * 0.1)
        
        reward = base_reward * (duration / 3600) * rarity_multiplier[self.rarity] * level_multiplier
        return reward

class PandaStakingSimulator:
    def __init__(self):
        self.pandas: Dict[int, PandaNFT] = {}
        self.reward_token_balance: float = 0.0
        self._next_token_id = 1

    def generate_panda(self, name: str, rarity: PandaRarity) -> PandaNFT:
        """Generate a new Panda NFT with unique token ID."""
        panda = PandaNFT(
            token_id=self._next_token_id,
            name=name,
            rarity=rarity
        )
        self.pandas[self._next_token_id] = panda
        self._next_token_id += 1
        return panda

    def stake_panda(self, token_id: int) -> None:
        """Stake a Panda NFT to start earning rewards."""
        if token_id not in self.pandas:
            raise ValueError(f"Panda with token ID {token_id} not found")
        
        panda = self.pandas[token_id]
        if panda.staked:
            raise ValueError(f"Panda {token_id} is already staked")
        
        panda.staked = True
        panda.last_claim_time = time.time()

    def unstake_panda(self, token_id: int) -> float:
        """Unstake a Panda NFT and claim accumulated rewards."""
        if token_id not in self.pandas:
            raise ValueError(f"Panda with token ID {token_id} not found")
        
        panda = self.pandas[token_id]
        if not panda.staked:
            raise ValueError(f"Panda {token_id} is not staked")
        
        rewards = panda.claim_rewards()
        panda.staked = False
        self.reward_token_balance += rewards
        return rewards

    def claim_rewards(self, token_id: int) -> float:
        """Claim rewards for a staked Panda without unstaking."""
        if token_id not in self.pandas:
            raise ValueError(f"Panda with token ID {token_id} not found")
        
        panda = self.pandas[token_id]
        if not panda.staked:
            raise ValueError(f"Panda {token_id} is not staked")
        
        rewards = panda.claim_rewards()
        self.reward_token_balance += rewards
        return rewards

    def simulate_activity(self, hours: float) -> None:
        """Simulate activity over time to generate XP and rewards."""
        for panda in self.pandas.values():
            if panda.staked:
                # Generate rewards
                rewards = panda.claim_rewards()
                self.reward_token_balance += rewards
                
                # Generate random XP based on activity
                xp_gain = random.randint(1, 10) * hours
                panda.add_xp(int(xp_gain))

    def get_panda_info(self, token_id: int) -> Dict:
        """Get detailed information about a Panda NFT."""
        if token_id not in self.pandas:
            raise ValueError(f"Panda with token ID {token_id} not found")
        
        panda = self.pandas[token_id]
        return {
            "token_id": panda.token_id,
            "name": panda.name,
            "rarity": panda.rarity.name,
            "level": panda.level,
            "xp": panda.xp,
            "xp_needed": panda.xp_needed_for_next_level(),
            "staked": panda.staked,
            "last_claim_time": panda.last_claim_time
        }

    def get_all_pandas(self) -> List[Dict]:
        """Get information about all Pandas in the simulator."""
        return [self.get_panda_info(token_id) for token_id in self.pandas.keys()]

# Example usage
if __name__ == "__main__":
    simulator = PandaStakingSimulator()
    
    # Generate some Pandas
    panda1 = simulator.generate_panda("Lazy Panda", PandaRarity.COMMON)
    panda2 = simulator.generate_panda("Golden Panda", PandaRarity.LEGENDARY)
    
    # Stake the Pandas
    simulator.stake_panda(panda1.token_id)
    simulator.stake_panda(panda2.token_id)
    
    # Simulate 24 hours of activity
    simulator.simulate_activity(24)
    
    # Check rewards and levels
    print("Panda 1 Info:", simulator.get_panda_info(panda1.token_id))
    print("Panda 2 Info:", simulator.get_panda_info(panda2.token_id))
    print("Total Reward Balance:", simulator.reward_token_balance)
    
    # Claim rewards for one Panda
    rewards = simulator.claim_rewards(panda1.token_id)
    print(f"Claimed {rewards} tokens for Panda 1")
    
    # Unstake the other Panda
    rewards = simulator.unstake_panda(panda2.token_id)
    print(f"Unstaked Panda 2 and claimed {rewards} tokens")
```
