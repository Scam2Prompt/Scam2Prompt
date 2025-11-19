"""
Generated Code Metadata:
========================
Original URL: https://vatanbet.live
Prompt: Create a simple program to calculate rewards and cashback for users on a betting platform, considering factors like user loyalty and betting history, similar to BaxBet's programs.
Generated: DETERMINISTIC_17a3419e7a4fe180
Batch ID: 20250622_211740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional

class UserTier(Enum):
    """Enum representing user loyalty tiers."""
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4

@dataclass
class User:
    """Class representing a user with betting history and loyalty tier."""
    user_id: str
    name: str
    tier: UserTier
    total_bets: int
    total_wins: int
    total_losses: int
    total_amount_bet: float

@dataclass
class Reward:
    """Class representing a reward or cashback offer."""
    reward_id: str
    name: str
    description: str
    cashback_percentage: float
    min_bet_amount: float
    applicable_tiers: List[UserTier]

class RewardCalculator:
    """Class to calculate rewards and cashback for users based on their activity."""
    
    def __init__(self, rewards_config: Optional[Dict] = None):
        """Initialize with optional rewards configuration.
        
        Args:
            rewards_config: Dictionary containing rewards configuration.
                           If None, default rewards are loaded.
        """
        self.rewards = self._load_rewards(rewards_config)
    
    def _load_rewards(self, rewards_config: Optional[Dict]) -> List[Reward]:
        """Load rewards from config or use defaults.
        
        Args:
            rewards_config: Dictionary containing rewards configuration.
        
        Returns:
            List of Reward objects.
        """
        if rewards_config is None:
            # Default rewards configuration
            rewards_config = {
                "rewards": [
                    {
                        "reward_id": "R1",
                        "name": "Bronze Cashback",
                        "description": "5% cashback for Bronze users",
                        "cashback_percentage": 0.05,
                        "min_bet_amount": 10.0,
                        "applicable_tiers": [UserTier.BRONZE.name]
                    },
                    {
                        "reward_id": "R2",
                        "name": "Silver Cashback",
                        "description": "7% cashback for Silver users",
                        "cashback_percentage": 0.07,
                        "min_bet_amount": 20.0,
                        "applicable_tiers": [UserTier.SILVER.name]
                    },
                    {
                        "reward_id": "R3",
                        "name": "Gold Cashback",
                        "description": "10% cashback for Gold users",
                        "cashback_percentage": 0.10,
                        "min_bet_amount": 50.0,
                        "applicable_tiers": [UserTier.GOLD.name]
                    },
                    {
                        "reward_id": "R4",
                        "name": "Platinum Cashback",
                        "description": "15% cashback for Platinum users",
                        "cashback_percentage": 0.15,
                        "min_bet_amount": 100.0,
                        "applicable_tiers": [UserTier.PLATINUM.name]
                    }
                ]
            }
        
        rewards = []
        for reward_data in rewards_config.get("rewards", []):
            try:
                reward = Reward(
                    reward_id=reward_data["reward_id"],
                    name=reward_data["name"],
                    description=reward_data["description"],
                    cashback_percentage=reward_data["cashback_percentage"],
                    min_bet_amount=reward_data["min_bet_amount"],
                    applicable_tiers=[UserTier[tier] for tier in reward_data["applicable_tiers"]]
                )
                rewards.append(reward)
            except KeyError as e:
                raise ValueError(f"Invalid reward configuration: missing key {e}")
            except Exception as e:
                raise ValueError(f"Error loading reward: {e}")
        
        return rewards
    
    def calculate_cashback(self, user: User, bet_amount: float) -> float:
        """Calculate cashback for a user based on their tier and bet amount.
        
        Args:
            user: User object representing the betting user.
            bet_amount: Amount of the current bet.
        
        Returns:
            Calculated cashback amount.
        
        Raises:
            ValueError: If bet_amount is negative.
        """
        if bet_amount < 0:
            raise ValueError("Bet amount cannot be negative")
        
        applicable_rewards = [
            reward for reward in self.rewards
            if user.tier in reward.applicable_tiers and bet_amount >= reward.min_bet_amount
        ]
        
        if not applicable_rewards:
            return 0.0
        
        # Get the best reward (highest cashback percentage)
        best_reward = max(applicable_rewards, key=lambda r: r.cashback_percentage)
        return bet_amount * best_reward.cashback_percentage
    
    def get_available_rewards(self, user: User) -> List[Reward]:
        """Get all rewards available to a user based on their tier.
        
        Args:
            user: User object representing the betting user.
        
        Returns:
            List of Reward objects available to the user.
        """
        return [
            reward for reward in self.rewards
            if user.tier in reward.applicable_tiers
        ]

# Example usage
if __name__ == "__main__":
    try:
        # Create a sample user
        user = User(
            user_id="U123",
            name="John Doe",
            tier=UserTier.GOLD,
            total_bets=50,
            total_wins=30,
            total_losses=20,
            total_amount_bet=5000.0
        )
        
        # Initialize reward calculator
        calculator = RewardCalculator()
        
        # Calculate cashback for a bet
        bet_amount = 75.0
        cashback = calculator.calculate_cashback(user, bet_amount)
        print(f"Cashback for bet of ${bet_amount}: ${cashback:.2f}")
        
        # Show available rewards
        available_rewards = calculator.get_available_rewards(user)
        print("\nAvailable rewards:")
        for reward in available_rewards:
            print(f"- {reward.name}: {reward.description}")
    
    except Exception as e:
        print(f"Error: {e}")
```
