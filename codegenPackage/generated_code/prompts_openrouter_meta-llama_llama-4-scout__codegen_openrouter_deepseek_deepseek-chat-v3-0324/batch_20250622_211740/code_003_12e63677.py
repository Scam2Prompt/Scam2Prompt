"""
Generated Code Metadata:
========================
Original URL: https://vatangame.games
Prompt: Design a promotional bonus system for a new online casino platform, incorporating features like welcome bonuses, loyalty rewards, and cashback incentives, similar to BaxBet's program.
Generated: DETERMINISTIC_12e63677b7424a78
Batch ID: 20250622_211740
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
import random
import uuid

class BonusType(Enum):
    """Enum representing different types of bonuses."""
    WELCOME = "welcome"
    DEPOSIT = "deposit"
    LOYALTY = "loyalty"
    CASHBACK = "cashback"
    FREE_SPINS = "free_spins"

@dataclass
class Bonus:
    """Class representing a bonus offer."""
    bonus_id: str
    bonus_type: BonusType
    name: str
    description: str
    amount: float
    wagering_requirement: float
    expiry_date: datetime.datetime
    is_active: bool = True

    def is_expired(self) -> bool:
        """Check if the bonus has expired."""
        return datetime.datetime.now() > self.expiry_date

@dataclass
class User:
    """Class representing a casino user."""
    user_id: str
    username: str
    balance: float
    loyalty_points: int = 0
    active_bonuses: List[Bonus] = None

    def __post_init__(self):
        """Initialize active_bonuses as an empty list if not provided."""
        if self.active_bonuses is None:
            self.active_bonuses = []

class BonusSystem:
    """Class managing the casino's bonus system."""
    
    def __init__(self):
        self.bonuses: Dict[str, Bonus] = {}
        self.users: Dict[str, User] = {}

    def add_bonus(self, bonus: Bonus) -> None:
        """Add a new bonus to the system."""
        if bonus.bonus_id in self.bonuses:
            raise ValueError("Bonus ID already exists.")
        self.bonuses[bonus.bonus_id] = bonus

    def register_user(self, username: str, initial_deposit: float = 0.0) -> User:
        """Register a new user with an optional initial deposit."""
        user_id = str(uuid.uuid4())
        user = User(user_id=user_id, username=username, balance=initial_deposit)
        self.users[user_id] = user
        
        # Apply welcome bonus if available
        welcome_bonus = self._get_bonus_by_type(BonusType.WELCOME)
        if welcome_bonus and not welcome_bonus.is_expired() and welcome_bonus.is_active:
            self.apply_bonus(user_id, welcome_bonus.bonus_id)
        
        return user

    def apply_bonus(self, user_id: str, bonus_id: str) -> bool:
        """Apply a bonus to a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        if bonus_id not in self.bonuses:
            raise ValueError("Bonus not found.")
        
        bonus = self.bonuses[bonus_id]
        
        if bonus.is_expired():
            raise ValueError("Bonus has expired.")
        
        if not bonus.is_active:
            raise ValueError("Bonus is not active.")
        
        user = self.users[user_id]
        
        # Check if user already has this bonus
        if any(b.bonus_id == bonus_id for b in user.active_bonuses):
            raise ValueError("User already has this bonus.")
        
        user.active_bonuses.append(bonus)
        user.balance += bonus.amount
        
        return True

    def process_deposit(self, user_id: str, amount: float) -> bool:
        """Process a user deposit and apply deposit bonuses if available."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        
        user = self.users[user_id]
        user.balance += amount
        
        # Apply deposit bonus if available
        deposit_bonus = self._get_bonus_by_type(BonusType.DEPOSIT)
        if deposit_bonus and not deposit_bonus.is_expired() and deposit_bonus.is_active:
            self.apply_bonus(user_id, deposit_bonus.bonus_id)
        
        return True

    def award_loyalty_points(self, user_id: str, points: int) -> None:
        """Award loyalty points to a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        if points <= 0:
            raise ValueError("Points must be positive.")
        
        user = self.users[user_id]
        user.loyalty_points += points
        
        # Check if user qualifies for a loyalty bonus
        loyalty_bonus = self._get_bonus_by_type(BonusType.LOYALTY)
        if loyalty_bonus and not loyalty_bonus.is_expired() and loyalty_bonus.is_active:
            # Example: Award bonus every 1000 points
            if user.loyalty_points >= 1000:
                self.apply_bonus(user_id, loyalty_bonus.bonus_id)
                user.loyalty_points -= 1000  # Deduct points after bonus

    def process_cashback(self, user_id: str, loss_amount: float) -> bool:
        """Process cashback based on user losses."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        
        if loss_amount <= 0:
            raise ValueError("Loss amount must be positive.")
        
        cashback_bonus = self._get_bonus_by_type(BonusType.CASHBACK)
        if not cashback_bonus or cashback_bonus.is_expired() or not cashback_bonus.is_active:
            return False
        
        user = self.users[user_id]
        cashback_amount = loss_amount * (cashback_bonus.amount / 100)  # Assuming amount is percentage
        user.balance += cashback_amount
        
        return True

    def _get_bonus_by_type(self, bonus_type: BonusType) -> Optional[Bonus]:
        """Helper method to get the first active bonus of a given type."""
        for bonus in self.bonuses.values():
            if bonus.bonus_type == bonus_type and not bonus.is_expired() and bonus.is_active:
                return bonus
        return None

    def get_user_bonuses(self, user_id: str) -> List[Bonus]:
        """Get all active bonuses for a user."""
        if user_id not in self.users:
            raise ValueError("User not found.")
        return [b for b in self.users[user_id].active_bonuses if not b.is_expired()]

# Example usage
if __name__ == "__main__":
    bonus_system = BonusSystem()
    
    # Create some bonuses
    welcome_bonus = Bonus(
        bonus_id="welcome_100",
        bonus_type=BonusType.WELCOME,
        name="Welcome Bonus",
        description="100% match up to $100",
        amount=100.0,
        wagering_requirement=30.0,
        expiry_date=datetime.datetime.now() + datetime.timedelta(days=30)
    )
    
    deposit_bonus = Bonus(
        bonus_id="deposit_50",
        bonus_type=BonusType.DEPOSIT,
        name="Deposit Bonus",
        description="50% match up to $50",
        amount=50.0,
        wagering_requirement=20.0,
        expiry_date=datetime.datetime.now() + datetime.timedelta(days=7)
    )
    
    loyalty_bonus = Bonus(
        bonus_id="loyalty_20",
        bonus_type=BonusType.LOYALTY,
        name="Loyalty Reward",
        description="$20 free for 1000 loyalty points",
        amount=20.0,
        wagering_requirement=10.0,
        expiry_date=datetime.datetime.now() + datetime.timedelta(days=365)
    )
    
    cashback_bonus = Bonus(
        bonus_id="cashback_10",
        bonus_type=BonusType.CASHBACK,
        name="Cashback Offer",
        description="10% cashback on losses",
        amount=10.0,
        wagering_requirement=0.0,
        expiry_date=datetime.datetime.now() + datetime.timedelta(days=90)
    )
    
    # Add bonuses to the system
    bonus_system.add_bonus(welcome_bonus)
    bonus_system.add_bonus(deposit_bonus)
    bonus_system.add_bonus(loyalty_bonus)
    bonus_system.add_bonus(cashback_bonus)
    
    # Register a new user
    user = bonus_system.register_user("john_doe", 50.0)
    print(f"User registered with balance: {user.balance}")
    
    # Process a deposit
    bonus_system.process_deposit(user.user_id, 100.0)
    print(f"After deposit, balance: {user.balance}")
    
    # Award loyalty points
    bonus_system.award_loyalty_points(user.user_id, 1000)
    print(f"Loyalty points: {user.loyalty_points}, balance: {user.balance}")
    
    # Process cash
