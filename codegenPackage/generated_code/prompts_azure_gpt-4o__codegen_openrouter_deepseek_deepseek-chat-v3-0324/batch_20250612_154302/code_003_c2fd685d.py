"""
Generated Code Metadata:
========================
Original URL: https://daos-world-wl.pages.dev
Prompt: Provide a step-by-step guide to implement a rewards system for users participating in AI hedge funds, inspired by the daos.world platform.
Generated: DETERMINISTIC_c2fd685d31cfcb7e
Batch ID: 20250612_154302
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_system.py
import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass
import hashlib
import uuid
from enum import Enum

class RewardType(Enum):
    """Enum representing different types of rewards"""
    PARTICIPATION = "participation"
    PERFORMANCE = "performance"
    REFERRAL = "referral"
    STAKING = "staking"

@dataclass
class User:
    """Class representing a user in the system"""
    user_id: str
    wallet_address: str
    join_date: datetime
    total_points: float = 0.0
    rewards_earned: float = 0.0

@dataclass
class Reward:
    """Class representing a reward"""
    reward_id: str
    user_id: str
    reward_type: RewardType
    amount: float
    timestamp: datetime
    description: str
    is_claimed: bool = False

class RewardSystem:
    """Main class implementing the rewards system"""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.rewards: Dict[str, Reward] = {}
        self.reward_rules = {
            RewardType.PARTICIPATION: 10.0,
            RewardType.PERFORMANCE: 50.0,
            RewardType.REFERRAL: 25.0,
            RewardType.STAKING: 5.0
        }
    
    def register_user(self, wallet_address: str) -> User:
        """Register a new user in the system"""
        if not self._validate_wallet_address(wallet_address):
            raise ValueError("Invalid wallet address")
            
        user_id = str(uuid.uuid4())
        new_user = User(
            user_id=user_id,
            wallet_address=wallet_address,
            join_date=datetime.now()
        )
        self.users[user_id] = new_user
        return new_user
    
    def _validate_wallet_address(self, address: str) -> bool:
        """Validate cryptocurrency wallet address"""
        # Basic validation - in production would use proper crypto address validation
        return len(address) >= 26 and len(address) <= 42
    
    def add_reward(self, user_id: str, reward_type: RewardType, description: str = "") -> Reward:
        """Add a reward for a user"""
        if user_id not in self.users:
            raise ValueError("User not found")
            
        reward_amount = self.reward_rules.get(reward_type, 0.0)
        reward_id = hashlib.sha256(f"{user_id}{datetime.now().timestamp()}".encode()).hexdigest()
        
        new_reward = Reward(
            reward_id=reward_id,
            user_id=user_id,
            reward_type=reward_type,
            amount=reward_amount,
            timestamp=datetime.now(),
            description=description
        )
        
        self.rewards[reward_id] = new_reward
        self.users[user_id].total_points += reward_amount
        return new_reward
    
    def claim_reward(self, reward_id: str) -> bool:
        """Mark a reward as claimed and transfer tokens"""
        if reward_id not in self.rewards:
            raise ValueError("Reward not found")
            
        reward = self.rewards[reward_id]
        if reward.is_claimed:
            raise ValueError("Reward already claimed")
            
        reward.is_claimed = True
        self.users[reward.user_id].rewards_earned += reward.amount
        return True
    
    def get_user_rewards(self, user_id: str, claimed_only: bool = False) -> List[Reward]:
        """Get all rewards for a user, optionally filtered by claimed status"""
        if user_id not in self.users:
            raise ValueError("User not found")
            
        return [
            reward for reward in self.rewards.values() 
            if reward.user_id == user_id and (not claimed_only or reward.is_claimed)
        ]
    
    def get_user_balance(self, user_id: str) -> Dict[str, float]:
        """Get a user's total points and earned rewards"""
        if user_id not in self.users:
            raise ValueError("User not found")
            
        user = self.users[user_id]
        return {
            "total_points": user.total_points,
            "rewards_earned": user.rewards_earned,
            "unclaimed_rewards": user.total_points - user.rewards_earned
        }
    
    def calculate_performance_reward(self, user_id: str, performance_score: float) -> Reward:
        """Calculate performance-based reward"""
        if performance_score < 0 or performance_score > 1:
            raise ValueError("Performance score must be between 0 and 1")
            
        base_reward = self.reward_rules[RewardType.PERFORMANCE]
        reward_amount = base_reward * performance_score
        return self.add_reward(
            user_id=user_id,
            reward_type=RewardType.PERFORMANCE,
            description=f"Performance reward with score {performance_score:.2f}"
        )
    
    def export_rewards_to_json(self, file_path: str) -> bool:
        """Export all rewards to a JSON file"""
        try:
            with open(file_path, 'w') as f:
                json.dump({
                    "rewards": [
                        {
                            "reward_id": r.reward_id,
                            "user_id": r.user_id,
                            "type": r.reward_type.value,
                            "amount": r.amount,
                            "timestamp": r.timestamp.isoformat(),
                            "description": r.description,
                            "claimed": r.is_claimed
                        }
                        for r in self.rewards.values()
                    ]
                }, f, indent=2)
            return True
        except Exception as e:
            print(f"Error exporting rewards: {e}")
            return False

# Example usage
if __name__ == "__main__":
    system = RewardSystem()
    
    # Register users
    user1 = system.register_user("0x71C7656EC7ab88b098defB751B7401B5f6d8976F")
    user2 = system.register_user("0xAb5801a7D398351b8bE11C439e05C5B3259aeC9B")
    
    # Add rewards
    system.add_reward(user1.user_id, RewardType.PARTICIPATION, "Initial participation")
    system.add_reward(user1.user_id, RewardType.REFERRAL, "Referred user2")
    system.calculate_performance_reward(user1.user_id, 0.85)
    
    # Claim a reward
    rewards = system.get_user_rewards(user1.user_id)
    if rewards:
        system.claim_reward(rewards[0].reward_id)
    
    # Check balances
    print(f"User1 balance: {system.get_user_balance(user1.user_id)}")
    
    # Export rewards
    system.export_rewards_to_json("rewards_export.json")
```
