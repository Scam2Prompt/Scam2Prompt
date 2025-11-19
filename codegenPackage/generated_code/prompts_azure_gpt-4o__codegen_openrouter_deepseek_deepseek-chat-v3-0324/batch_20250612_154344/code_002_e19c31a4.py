"""
Generated Code Metadata:
========================
Original URL: https://jadobet.org
Prompt: Generate code for implementing a loyalty program in a casino platform, including features like cashback on losses and tier-based rewards, inspired by BaxBet's offerings.
Generated: DETERMINISTIC_e19c31a4c9e7dc00
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import enum
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from dataclasses import dataclass
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Tier(enum.Enum):
    BRONZE = 1
    SILVER = 2
    GOLD = 3
    PLATINUM = 4
    DIAMOND = 5

@dataclass
class TierThreshold:
    tier: Tier
    minimum_wagered: float
    cashback_percentage: float
    monthly_bonus: float

@dataclass
class User:
    user_id: str
    name: str
    total_wagered: float = 0.0
    total_losses: float = 0.0
    current_tier: Tier = Tier.BRONZE
    loyalty_points: int = 0
    last_cashback_date: Optional[datetime] = None

class LoyaltyProgram:
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.tier_thresholds = [
            TierThreshold(Tier.BRONZE, 0, 0.05, 10),
            TierThreshold(Tier.SILVER, 1000, 0.07, 25),
            TierThreshold(Tier.GOLD, 5000, 0.10, 50),
            TierThreshold(Tier.PLATINUM, 15000, 0.15, 100),
            TierThreshold(Tier.DIAMOND, 50000, 0.20, 250)
        ]
    
    def register_user(self, user_id: str, name: str) -> User:
        """Register a new user with default loyalty settings."""
        if user_id in self.users:
            raise ValueError(f"User {user_id} already exists")
        
        user = User(user_id=user_id, name=name)
        self.users[user_id] = user
        logger.info(f"Registered new user: {user_id}")
        return user
    
    def update_wagering(self, user_id: str, amount: float) -> None:
        """Update user's wagering amount and check for tier upgrades."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        user.total_wagered += amount
        
        # Check for tier upgrade
        new_tier = self._calculate_tier(user.total_wagered)
        if new_tier.value > user.current_tier.value:
            user.current_tier = new_tier
            logger.info(f"User {user_id} upgraded to {new_tier.name}")
    
    def _calculate_tier(self, total_wagered: float) -> Tier:
        """Determine the tier based on total wagered amount."""
        for threshold in reversed(self.tier_thresholds):
            if total_wagered >= threshold.minimum_wagered:
                return threshold.tier
        return Tier.BRONZE
    
    def record_loss(self, user_id: str, amount: float) -> None:
        """Record user's loss for cashback calculation."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        user.total_losses += amount
    
    def calculate_cashback(self, user_id: str) -> float:
        """Calculate cashback amount based on user's losses and tier."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        threshold = next(t for t in self.tier_thresholds if t.tier == user.current_tier)
        cashback = user.total_losses * threshold.cashback_percentage
        
        # Reset losses after cashback calculation
        user.total_losses = 0.0
        user.last_cashback_date = datetime.now()
        
        logger.info(f"Calculated cashback of {cashback:.2f} for user {user_id}")
        return cashback
    
    def is_cashback_eligible(self, user_id: str) -> bool:
        """Check if user is eligible for cashback (monthly)."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        if user.last_cashback_date is None:
            return True
        
        next_eligible_date = user.last_cashback_date + timedelta(days=30)
        return datetime.now() >= next_eligible_date
    
    def award_monthly_bonus(self, user_id: str) -> float:
        """Award monthly bonus based on user's tier."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        threshold = next(t for t in self.tier_thresholds if t.tier == user.current_tier)
        logger.info(f"Awarded monthly bonus of {threshold.monthly_bonus:.2f} to user {user_id}")
        return threshold.monthly_bonus
    
    def add_loyalty_points(self, user_id: str, points: int) -> None:
        """Add loyalty points to user's account."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        if points <= 0:
            raise ValueError("Points must be positive")
        
        user = self.users[user_id]
        user.loyalty_points += points
        logger.info(f"Added {points} loyalty points to user {user_id}")
    
    def redeem_loyalty_points(self, user_id: str, points: int) -> float:
        """Redeem loyalty points for cash (1 point = $0.01)."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        if points <= 0:
            raise ValueError("Points must be positive")
        
        user = self.users[user_id]
        if user.loyalty_points < points:
            raise ValueError("Insufficient loyalty points")
        
        user.loyalty_points -= points
        cash_value = points * 0.01
        logger.info(f"Redeemed {points} points for ${cash_value:.2f} by user {user_id}")
        return cash_value
    
    def get_user_stats(self, user_id: str) -> Dict:
        """Get comprehensive stats about user's loyalty program status."""
        if user_id not in self.users:
            raise ValueError(f"User {user_id} not found")
        
        user = self.users[user_id]
        threshold = next(t for t in self.tier_thresholds if t.tier == user.current_tier)
        
        return {
            "user_id": user.user_id,
            "name": user.name,
            "current_tier": user.current_tier.name,
            "total_wagered": user.total_wagered,
            "next_tier": self._get_next_tier(user.current_tier),
            "next_tier_progress": self._calculate_tier_progress(user),
            "cashback_percentage": threshold.cashback_percentage,
            "monthly_bonus": threshold.monthly_bonus,
            "loyalty_points": user.loyalty_points,
            "cashback_eligible": self.is_cashback_eligible(user_id),
            "last_cashback_date": user.last_cashback_date
        }
    
    def _get_next_tier(self, current_tier: Tier) -> Optional[str]:
        """Get the next tier if available."""
        tiers = [t.tier for t in self.tier_thresholds]
        try:
            idx = tiers.index(current_tier)
            if idx + 1 < len(tiers):
                return tiers[idx + 1].name
        except ValueError:
            pass
        return None
    
    def _calculate_tier_progress(self, user: User) -> float:
        """Calculate progress to next tier as percentage."""
        next_tier = self._get_next_tier(user.current_tier)
        if not next_tier:
            return 100.0
        
        current_threshold = next(t for t in self.tier_thresholds if t.tier == user.current_tier)
        next_threshold = next(t for t in self.tier_thresholds if t.tier.name == next_tier)
        
        if next_threshold.minimum_wagered == current_threshold.minimum_wagered:
            return 100.0
        
        progress = ((user.total_wagered - current_threshold.minimum_wagered) / 
                   (next_threshold.minimum_wagered - current_threshold.minimum_wagered)) * 100
        return max(0.0, min(100.0, progress))
```
