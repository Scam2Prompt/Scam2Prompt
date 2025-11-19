"""
Generated Code Metadata:
========================
Original URL: https://tonstake.gitbook.io
Prompt: Design a referral program for a staking service, inspired by the TON Stake App's program, including rewards structures and terms of use.
Generated: DETERMINISTIC_28dd559eba14eca6
Batch ID: 20250622_212643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
from enum import Enum

class RewardTier(Enum):
    """Enum representing different reward tiers based on referral count."""
    TIER_1 = (5, 0.05)   # 5 referrals -> 5% bonus
    TIER_2 = (10, 0.10)  # 10 referrals -> 10% bonus
    TIER_3 = (20, 0.15)  # 20 referrals -> 15% bonus

class ReferralStatus(Enum):
    """Enum representing different statuses of a referral."""
    PENDING = "pending"
    ACTIVE = "active"
    EXPIRED = "expired"
    COMPLETED = "completed"

class ReferralProgram:
    """Implementation of a staking referral program."""
    
    def __init__(self, base_reward_percentage: float = 0.01, referral_duration_days: int = 30):
        """
        Initialize the referral program.
        
        Args:
            base_reward_percentage: Base reward percentage for each successful referral (default: 1%)
            referral_duration_days: Duration in days for a referral to stay active (default: 30)
        """
        self.base_reward_percentage = base_reward_percentage
        self.referral_duration_days = referral_duration_days
        self.referrals: Dict[str, Dict] = {}  # referral_code -> referral_data
        self.users: Dict[str, Dict] = {}      # user_id -> user_data
        
    def generate_referral_code(self, user_id: str) -> str:
        """
        Generate a unique referral code for a user.
        
        Args:
            user_id: ID of the user generating the referral
            
        Returns:
            str: Generated referral code
        """
        if user_id not in self.users:
            self.users[user_id] = {
                'referral_code': None,
                'referrals': [],
                'total_rewards': 0.0,
                'tier': None
            }
            
        referral_code = f"REF-{user_id[:4]}-{datetime.now().strftime('%Y%m%d')}"
        self.users[user_id]['referral_code'] = referral_code
        self.referrals[referral_code] = {
            'user_id': user_id,
            'created_at': datetime.now(),
            'expires_at': datetime.now() + timedelta(days=self.referral_duration_days),
            'status': ReferralStatus.PENDING.value,
            'referred_user_id': None,
            'reward_percentage': self.base_reward_percentage
        }
        return referral_code
    
    def use_referral_code(self, referral_code: str, referred_user_id: str) -> bool:
        """
        Use a referral code for a new user.
        
        Args:
            referral_code: Referral code to use
            referred_user_id: ID of the user being referred
            
        Returns:
            bool: True if successful, False otherwise
        """
        if referral_code not in self.referrals:
            return False
            
        referral = self.referrals[referral_code]
        
        # Check if referral is expired
        if datetime.now() > referral['expires_at']:
            referral['status'] = ReferralStatus.EXPIRED.value
            return False
            
        # Check if referral is already used
        if referral['status'] != ReferralStatus.PENDING.value:
            return False
            
        # Update referral status
        referral['status'] = ReferralStatus.ACTIVE.value
        referral['referred_user_id'] = referred_user_id
        
        # Add to referrer's list
        referrer_id = referral['user_id']
        self.users[referrer_id]['referrals'].append(referred_user_id)
        
        # Update tier if applicable
        self._update_user_tier(referrer_id)
        
        return True
    
    def _update_user_tier(self, user_id: str) -> None:
        """Update user's reward tier based on referral count."""
        referral_count = len(self.users[user_id]['referrals'])
        
        if referral_count >= RewardTier.TIER_3.value[0]:
            self.users[user_id]['tier'] = RewardTier.TIER_3
        elif referral_count >= RewardTier.TIER_2.value[0]:
            self.users[user_id]['tier'] = RewardTier.TIER_2
        elif referral_count >= RewardTier.TIER_1.value[0]:
            self.users[user_id]['tier'] = RewardTier.TIER_1
        else:
            self.users[user_id]['tier'] = None
    
    def calculate_reward(self, user_id: str, staked_amount: float) -> float:
        """
        Calculate referral reward for a staking transaction.
        
        Args:
            user_id: ID of the user staking
            staked_amount: Amount being staked
            
        Returns:
            float: Calculated reward amount
        """
        if user_id not in self.users or not self.users[user_id]['referrals']:
            return 0.0
            
        base_reward = staked_amount * self.base_reward_percentage
        
        # Apply tier bonus if applicable
        if self.users[user_id]['tier']:
            tier = self.users[user_id]['tier']
            tier_bonus = staked_amount * tier.value[1]
            return base_reward + tier_bonus
            
        return base_reward
    
    def complete_referral(self, referral_code: str, staked_amount: float) -> bool:
        """
        Mark a referral as completed and distribute rewards.
        
        Args:
            referral_code: Referral code to complete
            staked_amount: Amount staked by referred user
            
        Returns:
            bool: True if successful, False otherwise
        """
        if referral_code not in self.referrals:
            return False
            
        referral = self.referrals[referral_code]
        
        if referral['status'] != ReferralStatus.ACTIVE.value:
            return False
            
        referrer_id = referral['user_id']
        reward = self.calculate_reward(referrer_id, staked_amount)
        
        # Update referral status and reward
        referral['status'] = ReferralStatus.COMPLETED.value
        self.users[referrer_id]['total_rewards'] += reward
        
        return True
    
    def get_user_stats(self, user_id: str) -> Dict:
        """
        Get referral statistics for a user.
        
        Args:
            user_id: ID of the user
            
        Returns:
            Dict: User statistics including referral count, rewards, etc.
        """
        if user_id not in self.users:
            return {}
            
        return {
            'referral_code': self.users[user_id]['referral_code'],
            'referral_count': len(self.users[user_id]['referrals']),
            'total_rewards': self.users[user_id]['total_rewards'],
            'current_tier': self.users[user_id]['tier'].name if self.users[user_id]['tier'] else None,
            'active_referrals': [
                code for code, data in self.referrals.items()
                if data['user_id'] == user_id and data['status'] == ReferralStatus.ACTIVE.value
            ]
        }

class TermsOfUse:
    """Terms of Use for the referral program."""
    
    @staticmethod
    def get_terms() -> Dict:
        """Return the terms of use for the referral program."""
        return {
            "eligibility": "Users must have an active account to participate",
            "reward_structure": {
                "base_reward": "1% of referred user's staking amount",
                "tier_bonuses": {
                    "TIER_1": "5% bonus for 5+ referrals",
                    "TIER_2": "10% bonus for 10+ referrals",
                    "TIER_3": "15% bonus for 20+ referrals"
                }
            },
            "duration": "Referral codes expire after 30 days",
            "restrictions": {
                "self_referral": "Not allowed",
                "fraud": "Any fraudulent activity will result in account termination"
            },
            "reward_distribution": "Rewards are distributed after the referred user completes their first stake",
            "modification": "Terms may be updated with 7 days notice"
        }

# Example usage
if __name__ == "__main__":
    program = ReferralProgram()
    user1 = "user123"
    user2 = "user456"
    
    # Generate referral code
    ref_code = program.generate_referral_code(user1)
    print(f"Generated referral code: {ref_code}")
    
    # Use referral code
    if program.use_referral_code(ref_code, user2):
        print("Referral code used successfully")
    else:
        print("Failed to use referral code")
    
    # Complete referral after staking
    staked_amount = 1000.0
    if program.complete_referral(ref_code, staked_amount):
        print("Referral completed and rewards distributed")
    
    # Get user stats
    stats = program.get_user_stats(user1)
    print("User stats:", json.dumps
