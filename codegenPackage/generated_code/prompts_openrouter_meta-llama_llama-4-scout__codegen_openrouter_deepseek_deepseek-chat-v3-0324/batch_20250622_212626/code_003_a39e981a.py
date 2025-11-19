"""
Generated Code Metadata:
========================
Original URL: https://hypurrnft.org
Prompt: What are the requirements for users to be allocated for the Genesis Collection on the Hypurr NFT Mint Portal?
Generated: DETERMINISTIC_a39e981a2886ba8e
Batch ID: 20250622_212626
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Optional
from enum import Enum
from pydantic import BaseModel, validator
from datetime import datetime

class AllocationTier(Enum):
    """Enum representing different allocation tiers for users."""
    TIER_1 = "Tier 1"
    TIER_2 = "Tier 2"
    TIER_3 = "Tier 3"

class User(BaseModel):
    """Represents a user eligible for NFT allocation."""
    wallet_address: str
    whitelisted: bool
    tier: Optional[AllocationTier] = None
    has_held_hypurr_nft: bool
    holding_period_days: int
    last_interaction_date: datetime

    @validator('wallet_address')
    def validate_wallet_address(cls, v):
        """Validate the wallet address format."""
        if not v.startswith("0x") or len(v) != 42:
            raise ValueError("Invalid Ethereum wallet address format")
        return v

class GenesisCollectionAllocator:
    """Handles allocation logic for the Genesis Collection."""
    
    def __init__(self, min_holding_days: int = 30):
        self.min_holding_days = min_holding_days
    
    def check_eligibility(self, user: User) -> bool:
        """Check if a user meets the basic eligibility requirements."""
        return (
            user.whitelisted 
            and user.has_held_hypurr_nft 
            and user.holding_period_days >= self.min_holding_days
        )
    
    def determine_tier(self, user: User) -> Optional[AllocationTier]:
        """Determine the allocation tier based on user's activity."""
        if not self.check_eligibility(user):
            return None
            
        days_since_interaction = (datetime.now() - user.last_interaction_date).days
        
        if days_since_interaction <= 7:
            return AllocationTier.TIER_1
        elif days_since_interaction <= 30:
            return AllocationTier.TIER_2
        elif days_since_interaction <= 90:
            return AllocationTier.TIER_3
        return None
    
    def allocate_nft(self, user: User) -> bool:
        """Allocate NFT to user if they meet requirements."""
        user.tier = self.determine_tier(user)
        return user.tier is not None
    
    def batch_allocate(self, users: List[User]) -> List[User]:
        """Process allocation for multiple users."""
        for user in users:
            self.allocate_nft(user)
        return users
```
