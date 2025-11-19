"""
Generated Code Metadata:
========================
Original URL: https://whale.market
Prompt: "Design a system to incentivize growth on Whales Market using the $WHALES token, including airdrops, incentives, and vesting schedules."
Generated: DETERMINISTIC_5adb21f156b118f5
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# whales_market_incentives.py
import json
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple
import hashlib
import secrets

# Constants
TOKEN_NAME = "WHALES"
TOTAL_SUPPLY = 1_000_000_000  # 1 billion tokens
AIRDROP_PERCENTAGE = 0.10  # 10% of total supply for airdrops
INCENTIVES_PERCENTAGE = 0.20  # 20% for growth incentives
TEAM_VESTING_PERCENTAGE = 0.15  # 15% for team with vesting
VESTING_PERIOD_DAYS = 365 * 2  # 2 years vesting period
CLIFF_PERIOD_DAYS = 180  # 6 month cliff

class TokenAllocation:
    def __init__(self):
        self.allocations = {
            "airdrop": TOTAL_SUPPLY * AIRDROP_PERCENTAGE,
            "incentives": TOTAL_SUPPLY * INCENTIVES_PERCENTAGE,
            "team_vesting": TOTAL_SUPPLY * TEAM_VESTING_PERCENTAGE,
            "reserve": TOTAL_SUPPLY * (1 - (AIRDROP_PERCENTAGE + INCENTIVES_PERCENTAGE + TEAM_VESTING_PERCENTAGE))
        }
    
    def get_allocation(self, allocation_type: str) -> float:
        """Get allocated amount for a specific type."""
        if allocation_type not in self.allocations:
            raise ValueError(f"Invalid allocation type: {allocation_type}")
        return self.allocations[allocation_type]

class User:
    def __init__(self, user_id: str, email: str, registration_date: datetime):
        self.user_id = user_id
        self.email = email
        self.registration_date = registration_date
        self.balance = 0.0
        self.vesting_schedules = []
    
    def add_tokens(self, amount: float, vesting: bool = False, schedule: Optional[Dict] = None):
        """Add tokens to user balance or vesting schedule."""
        if amount <= 0:
            raise ValueError("Amount must be positive")
        
        if vesting:
            if not schedule:
                raise ValueError("Vesting schedule required for vesting tokens")
            self.vesting_schedules.append({
                "amount": amount,
                "start_date": schedule["start_date"],
                "cliff_date": schedule["cliff_date"],
                "end_date": schedule["end_date"],
                "claimed": 0.0
            })
        else:
            self.balance += amount
    
    def get_vested_tokens(self, current_date: datetime) -> float:
        """Calculate vested tokens available for claim."""
        total_available = 0.0
        
        for schedule in self.vesting_schedules:
            if current_date < schedule["cliff_date"]:
                continue
            
            if current_date >= schedule["end_date"]:
                total_available += schedule["amount"] - schedule["claimed"]
            else:
                elapsed = (current_date - schedule["start_date"]).days
                total_days = (schedule["end_date"] - schedule["start_date"]).days
                vested_amount = schedule["amount"] * (elapsed / total_days)
                total_available += max(0, vested_amount - schedule["claimed"])
        
        return total_available
    
    def claim_vested_tokens(self, current_date: datetime) -> float:
        """Claim vested tokens and add to balance."""
        claimable = self.get_vested_tokens(current_date)
        
        if claimable <= 0:
            return 0.0
        
        for schedule in self.vesting_schedules:
            if current_date < schedule["cliff_date"]:
                continue
            
            if current_date >= schedule["end_date"]:
                claimable_from_schedule = schedule["amount"] - schedule["claimed"]
                schedule["claimed"] = schedule["amount"]
            else:
                elapsed = (current_date - schedule["start_date"]).days
                total_days = (schedule["end_date"] - schedule["start_date"]).days
                vested_amount = schedule["amount"] * (elapsed / total_days)
                claimable_from_schedule = max(0, vested_amount - schedule["claimed"])
                schedule["claimed"] += claimable_from_schedule
            
            self.balance += claimable_from_schedule
        
        return claimable

class Airdrop:
    def __init__(self, allocation: float):
        self.total_amount = allocation
        self.remaining_amount = allocation
        self.recipients = {}
    
    def generate_merkle_root(self, recipients: List[Tuple[str, float]]) -> str:
        """Generate Merkle root for airdrop verification."""
        if not recipients:
            raise ValueError("Recipients list cannot be empty")
        
        hashes = []
        for user_id, amount in recipients:
            data = f"{user_id}{amount}".encode()
            hashes.append(hashlib.sha256(data).hexdigest())
        
        while len(hashes) > 1:
            new_hashes = []
            for i in range(0, len(hashes), 2):
                if i + 1 < len(hashes):
                    combined = hashes[i] + hashes[i+1]
                else:
                    combined = hashes[i] + hashes[i]
                new_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
            hashes = new_hashes
        
        self.merkle_root = hashes[0]
        return self.merkle_root
    
    def register_recipients(self, recipients: List[Tuple[str, float]]):
        """Register airdrop recipients with their allocated amounts."""
        total = sum(amount for _, amount in recipients)
        if total > self.remaining_amount:
            raise ValueError("Total airdrop amount exceeds remaining allocation")
        
        for user_id, amount in recipients:
            if user_id in self.recipients:
                raise ValueError(f"Duplicate user ID: {user_id}")
            self.recipients[user_id] = amount
        
        self.remaining_amount -= total
        self.generate_merkle_root(recipients)
    
    def claim_airdrop(self, user_id: str, user: User) -> float:
        """Claim airdrop tokens for a user."""
        if user_id not in self.recipients:
            raise ValueError("User not eligible for airdrop")
        
        amount = self.recipients[user_id]
        user.add_tokens(amount)
        del self.recipients[user_id]
        return amount

class GrowthIncentives:
    def __init__(self, allocation: float):
        self.total_amount = allocation
        self.remaining_amount = allocation
        self.active_campaigns = {}
    
    def create_campaign(self, campaign_id: str, total_rewards: float, rules: Dict):
        """Create a new growth incentive campaign."""
        if campaign_id in self.active_campaigns:
            raise ValueError("Campaign ID already exists")
        
        if total_rewards > self.remaining_amount:
            raise ValueError("Not enough tokens remaining for this campaign")
        
        self.active_campaigns[campaign_id] = {
            "total_rewards": total_rewards,
            "remaining_rewards": total_rewards,
            "rules": rules,
            "participants": {}
        }
        self.remaining_amount -= total_rewards
    
    def participate(self, campaign_id: str, user_id: str, contribution: float) -> float:
        """Participate in a growth campaign and earn rewards."""
        if campaign_id not in self.active_campaigns:
            raise ValueError("Invalid campaign ID")
        
        campaign = self.active_campaigns[campaign_id]
        
        # Calculate reward based on campaign rules
        if campaign["rules"]["type"] == "fixed":
            reward = campaign["rules"]["amount"]
        elif campaign["rules"]["type"] == "percentage":
            reward = contribution * campaign["rules"]["rate"]
        else:
            raise ValueError("Invalid reward type in campaign rules")
        
        if reward > campaign["remaining_rewards"]:
            reward = campaign["remaining_rewards"]
        
        if reward <= 0:
            return 0.0
        
        if user_id in campaign["participants"]:
            campaign["participants"][user_id] += reward
        else:
            campaign["participants"][user_id] = reward
        
        campaign["remaining_rewards"] -= reward
        return reward
    
    def distribute_rewards(self, campaign_id: str, users: Dict[str, User]):
        """Distribute rewards to participants of a campaign."""
        if campaign_id not in self.active_campaigns:
            raise ValueError("Invalid campaign ID")
        
        campaign = self.active_campaigns[campaign_id]
        
        for user_id, amount in campaign["participants"].items():
            if user_id in users:
                users[user_id].add_tokens(amount)
        
        self.remaining_amount += campaign["remaining_rewards"]
        del self.active_campaigns[campaign_id]

class VestingSchedule:
    def __init__(self, allocation: float):
        self.total_amount = allocation
        self.remaining_amount = allocation
