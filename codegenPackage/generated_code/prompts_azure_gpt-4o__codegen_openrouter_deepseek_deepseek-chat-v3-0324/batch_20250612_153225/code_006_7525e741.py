"""
Generated Code Metadata:
========================
Original URL: https://thedigitalage.co.nz
Prompt: Generate code for tracking customer referrals and rewards, inspired by referral programs offered by digital marketing agencies.
Generated: DETERMINISTIC_7525e7411df711c1
Batch ID: 20250612_153225
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import uuid
from datetime import datetime
from typing import List, Dict, Optional
from enum import Enum

class ReferralStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"
    EXPIRED = "expired"
    CANCELLED = "cancelled"

class RewardType(Enum):
    CASH = "cash"
    CREDIT = "credit"
    PRODUCT = "product"
    DISCOUNT = "discount"

class Customer:
    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.referral_code = self._generate_referral_code()
        self.date_joined = datetime.now()
        self.referrals: List['Referral'] = []
        self.rewards: List['Reward'] = []

    def _generate_referral_code(self) -> str:
        return str(uuid.uuid4()).split('-')[0].upper()

class Referral:
    def __init__(self, referrer: Customer, referee_email: str):
        self.referral_id = str(uuid.uuid4())
        self.referrer = referrer
        self.referee_email = referee_email
        self.status = ReferralStatus.PENDING
        self.date_created = datetime.now()
        self.date_completed: Optional[datetime] = None

    def mark_completed(self) -> None:
        if self.status != ReferralStatus.PENDING:
            raise ValueError("Only pending referrals can be marked as completed")
        self.status = ReferralStatus.COMPLETED
        self.date_completed = datetime.now()

    def mark_expired(self) -> None:
        if self.status != ReferralStatus.PENDING:
            raise ValueError("Only pending referrals can be marked as expired")
        self.status = ReferralStatus.EXPIRED

    def mark_cancelled(self) -> None:
        if self.status != ReferralStatus.PENDING:
            raise ValueError("Only pending referrals can be cancelled")
        self.status = ReferralStatus.CANCELLED

class Reward:
    def __init__(self, reward_id: str, reward_type: RewardType, value: float, description: str):
        self.reward_id = reward_id
        self.type = reward_type
        self.value = value
        self.description = description
        self.date_issued = datetime.now()
        self.date_redeemed: Optional[datetime] = None
        self.is_redeemed = False

    def redeem(self) -> None:
        if self.is_redeemed:
            raise ValueError("Reward has already been redeemed")
        self.is_redeemed = True
        self.date_redeemed = datetime.now()

class ReferralProgram:
    def __init__(self):
        self.customers: Dict[str, Customer] = {}
        self.referrals: Dict[str, Referral] = {}
        self.rewards: Dict[str, Reward] = {}
        self.reward_rules: Dict[RewardType, float] = {
            RewardType.CASH: 10.0,
            RewardType.CREDIT: 15.0,
            RewardType.PRODUCT: 0.0,  # Value determined by product
            RewardType.DISCOUNT: 20.0  # Percentage
        }

    def add_customer(self, name: str, email: str) -> Customer:
        if email in [c.email for c in self.customers.values()]:
            raise ValueError("Customer with this email already exists")
        
        customer_id = str(uuid.uuid4())
        customer = Customer(customer_id, name, email)
        self.customers[customer_id] = customer
        return customer

    def create_referral(self, referrer_id: str, referee_email: str) -> Referral:
        if referrer_id not in self.customers:
            raise ValueError("Referrer not found")
        
        referrer = self.customers[referrer_id]
        referral = Referral(referrer, referee_email)
        self.referrals[referral.referral_id] = referral
        referrer.referrals.append(referral)
        return referral

    def process_referral_completion(self, referral_id: str) -> Reward:
        if referral_id not in self.referrals:
            raise ValueError("Referral not found")
        
        referral = self.referrals[referral_id]
        referral.mark_completed()
        
        reward_type = RewardType.CASH  # Default reward type
        reward_value = self.reward_rules[reward_type]
        reward_id = str(uuid.uuid4())
        reward = Reward(
            reward_id=reward_id,
            reward_type=reward_type,
            value=reward_value,
            description=f"Referral reward for {referral.referee_email}"
        )
        
        self.rewards[reward_id] = reward
        referral.referrer.rewards.append(reward)
        return reward

    def get_customer_referrals(self, customer_id: str) -> List[Referral]:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return self.customers[customer_id].referrals

    def get_customer_rewards(self, customer_id: str) -> List[Reward]:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        return self.customers[customer_id].rewards

    def redeem_reward(self, customer_id: str, reward_id: str) -> None:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        customer = self.customers[customer_id]
        reward = next((r for r in customer.rewards if r.reward_id == reward_id), None)
        
        if not reward:
            raise ValueError("Reward not found for this customer")
        
        reward.redeem()

    def get_referral_stats(self, customer_id: str) -> Dict[str, int]:
        if customer_id not in self.customers:
            raise ValueError("Customer not found")
        
        referrals = self.customers[customer_id].referrals
        stats = {
            "total": len(referrals),
            "completed": sum(1 for r in referrals if r.status == ReferralStatus.COMPLETED),
            "pending": sum(1 for r in referrals if r.status == ReferralStatus.PENDING),
            "expired": sum(1 for r in referrals if r.status == ReferralStatus.EXPIRED),
            "cancelled": sum(1 for r in referrals if r.status == ReferralStatus.CANCELLED)
        }
        return stats
```
