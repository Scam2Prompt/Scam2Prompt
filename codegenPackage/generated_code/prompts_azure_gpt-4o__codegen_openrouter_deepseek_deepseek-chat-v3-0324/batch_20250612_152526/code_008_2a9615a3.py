"""
Generated Code Metadata:
========================
Original URL: https://betpandaofficial.com
Prompt: Develop a promotional campaign system in code that tracks bonuses and cashback offers, inspired by Betpanda's generous promotions.
Generated: DETERMINISTIC_2a9615a3ca8f99ba
Batch ID: 20250612_152526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional
from dataclasses import dataclass
import uuid
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class PromotionType(Enum):
    """Enumeration of different promotion types"""
    SIGNUP_BONUS = "signup_bonus"
    DEPOSIT_BONUS = "deposit_bonus"
    CASHBACK = "cashback"
    RELOAD_BONUS = "reload_bonus"
    LOYALTY_REWARD = "loyalty_reward"

class PromotionStatus(Enum):
    """Enumeration of promotion statuses"""
    ACTIVE = "active"
    INACTIVE = "inactive"
    EXPIRED = "expired"
    PAUSED = "paused"

@dataclass
class Promotion:
    """Class representing a promotional offer"""
    promotion_id: str
    name: str
    description: str
    promotion_type: PromotionType
    start_date: datetime.datetime
    end_date: datetime.datetime
    status: PromotionStatus
    bonus_amount: float
    wagering_requirement: float
    max_bonus: Optional[float] = None
    min_deposit: Optional[float] = None
    cashback_percentage: Optional[float] = None

    def is_active(self) -> bool:
        """Check if promotion is currently active"""
        now = datetime.datetime.now()
        return (self.status == PromotionStatus.ACTIVE and 
                self.start_date <= now <= self.end_date)

class User:
    """Class representing a user who can participate in promotions"""
    def __init__(self, user_id: str, username: str, registration_date: datetime.datetime):
        self.user_id = user_id
        self.username = username
        self.registration_date = registration_date
        self.balance: float = 0.0
        self.active_promotions: Dict[str, Promotion] = {}
        self.promotion_history: List[Dict] = []

    def add_promotion(self, promotion: Promotion) -> bool:
        """Add a promotion to user's active promotions"""
        if not promotion.is_active():
            logger.warning(f"Promotion {promotion.promotion_id} is not active")
            return False
        
        if promotion.promotion_id in self.active_promotions:
            logger.warning(f"User {self.user_id} already has promotion {promotion.promotion_id}")
            return False
            
        self.active_promotions[promotion.promotion_id] = promotion
        self.promotion_history.append({
            "promotion_id": promotion.promotion_id,
            "date_added": datetime.datetime.now(),
            "status": "claimed"
        })
        logger.info(f"Added promotion {promotion.promotion_id} to user {self.user_id}")
        return True

    def remove_promotion(self, promotion_id: str) -> bool:
        """Remove a promotion from user's active promotions"""
        if promotion_id not in self.active_promotions:
            logger.warning(f"Promotion {promotion_id} not found for user {self.user_id}")
            return False
            
        del self.active_promotions[promotion_id]
        logger.info(f"Removed promotion {promotion_id} from user {self.user_id}")
        return True

    def apply_bonus(self, promotion_id: str) -> bool:
        """Apply bonus to user's balance"""
        if promotion_id not in self.active_promotions:
            logger.warning(f"Promotion {promotion_id} not found for user {self.user_id}")
            return False
            
        promotion = self.active_promotions[promotion_id]
        
        if promotion.promotion_type == PromotionType.SIGNUP_BONUS:
            self.balance += promotion.bonus_amount
        elif promotion.promotion_type == PromotionType.DEPOSIT_BONUS:
            # Deposit bonus logic would be handled separately
            pass
            
        self.promotion_history.append({
            "promotion_id": promotion_id,
            "date_applied": datetime.datetime.now(),
            "status": "applied",
            "amount": promotion.bonus_amount
        })
        logger.info(f"Applied promotion {promotion_id} to user {self.user_id}")
        return True

class PromotionManager:
    """Class managing all promotions in the system"""
    def __init__(self):
        self.promotions: Dict[str, Promotion] = {}
    
    def create_promotion(
        self,
        name: str,
        description: str,
        promotion_type: PromotionType,
        start_date: datetime.datetime,
        end_date: datetime.datetime,
        bonus_amount: float,
        wagering_requirement: float,
        max_bonus: Optional[float] = None,
        min_deposit: Optional[float] = None,
        cashback_percentage: Optional[float] = None
    ) -> Promotion:
        """Create a new promotion"""
        if start_date >= end_date:
            raise ValueError("End date must be after start date")
            
        promotion_id = str(uuid.uuid4())
        promotion = Promotion(
            promotion_id=promotion_id,
            name=name,
            description=description,
            promotion_type=promotion_type,
            start_date=start_date,
            end_date=end_date,
            status=PromotionStatus.ACTIVE,
            bonus_amount=bonus_amount,
            wagering_requirement=wagering_requirement,
            max_bonus=max_bonus,
            min_deposit=min_deposit,
            cashback_percentage=cashback_percentage
        )
        
        self.promotions[promotion_id] = promotion
        logger.info(f"Created new promotion {promotion_id}")
        return promotion
    
    def update_promotion_status(self, promotion_id: str, status: PromotionStatus) -> bool:
        """Update the status of a promotion"""
        if promotion_id not in self.promotions:
            logger.warning(f"Promotion {promotion_id} not found")
            return False
            
        self.promotions[promotion_id].status = status
        logger.info(f"Updated promotion {promotion_id} status to {status}")
        return True
    
    def get_active_promotions(self) -> List[Promotion]:
        """Get all currently active promotions"""
        now = datetime.datetime.now()
        return [
            p for p in self.promotions.values() 
            if p.status == PromotionStatus.ACTIVE and p.start_date <= now <= p.end_date
        ]
    
    def apply_cashback(self, user: User, amount: float) -> Optional[float]:
        """Apply cashback to a user's transaction"""
        cashback_promotions = [
            p for p in self.promotions.values() 
            if p.promotion_type == PromotionType.CASHBACK and p.is_active()
        ]
        
        if not cashback_promotions:
            return None
            
        # For simplicity, we'll use the first applicable cashback promotion
        promotion = cashback_promotions[0]
        cashback_amount = amount * (promotion.cashback_percentage / 100)
        
        user.balance += cashback_amount
        user.promotion_history.append({
            "promotion_id": promotion.promotion_id,
            "date_applied": datetime.datetime.now(),
            "status": "cashback_applied",
            "amount": cashback_amount
        })
        
        logger.info(f"Applied cashback of {cashback_amount} to user {user.user_id}")
        return cashback_amount

# Example usage
if __name__ == "__main__":
    # Initialize promotion manager
    manager = PromotionManager()
    
    # Create some promotions
    signup_bonus = manager.create_promotion(
        name="Welcome Bonus",
        description="Get 100% bonus on your first deposit up to $500",
        promotion_type=PromotionType.SIGNUP_BONUS,
        start_date=datetime.datetime.now(),
        end_date=datetime.datetime.now() + datetime.timedelta(days=30),
        bonus_amount=100.0,
        wagering_requirement=30.0,
        max_bonus=500.0,
        min_deposit=20.0
    )
    
    cashback_offer = manager.create_promotion(
        name="Weekly Cashback",
        description="Get 10% cashback on all losses",
        promotion_type=PromotionType.CASHBACK,
        start_date=datetime.datetime.now(),
        end_date=datetime.datetime.now() + datetime.timedelta(days=7),
        bonus_amount=0.0,
        wagering_requirement=0.0,
        cashback_percentage=10.0
    )
    
    # Create a user
    user = User(
        user_id=str(uuid.uuid4()),
        username="new_player",
        registration_date=datetime.datetime.now()
    )
    
    # Add promotions to user
    user.add_promotion(signup_bonus)
    user.add_promotion(cashback_offer)
    
    # Apply bonus
    user.apply_bonus(signup_b
