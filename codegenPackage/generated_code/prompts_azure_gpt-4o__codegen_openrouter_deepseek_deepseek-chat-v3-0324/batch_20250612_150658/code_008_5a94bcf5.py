"""
Generated Code Metadata:
========================
Original URL: https://tonroll.cc
Prompt: Write code to implement a subscription system where traders earn bonuses based on the number of users copying their trades, as outlined in Earnie's app features.
Generated: DETERMINISTIC_5a94bcf532757935
Batch ID: 20250612_150658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import logging
from enum import Enum

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SubscriptionTier(Enum):
    """Enum representing different subscription tiers."""
    BASIC = 1
    PRO = 2
    ELITE = 3

class Trader:
    """Class representing a trader in the system."""
    def __init__(self, trader_id: str, name: str, subscription_tier: SubscriptionTier):
        self.trader_id = trader_id
        self.name = name
        self.subscription_tier = subscription_tier
        self.copiers: List[str] = []  # List of user IDs copying this trader
        self.bonus_balance: float = 0.0
        self.last_bonus_calculation: Optional[datetime] = None

class SubscriptionSystem:
    """Main class implementing the subscription and bonus system."""
    
    def __init__(self):
        self.traders: Dict[str, Trader] = {}  # trader_id -> Trader object
        self.bonus_rates = {
            SubscriptionTier.BASIC: 0.05,
            SubscriptionTier.PRO: 0.10,
            SubscriptionTier.ELITE: 0.15
        }
        self.min_copiers_for_bonus = {
            SubscriptionTier.BASIC: 10,
            SubscriptionTier.PRO: 5,
            SubscriptionTier.ELITE: 3
        }
    
    def add_trader(self, trader_id: str, name: str, subscription_tier: SubscriptionTier) -> None:
        """Add a new trader to the system."""
        if trader_id in self.traders:
            raise ValueError(f"Trader with ID {trader_id} already exists")
        self.traders[trader_id] = Trader(trader_id, name, subscription_tier)
        logger.info(f"Added trader {name} with ID {trader_id}")
    
    def add_copier(self, trader_id: str, user_id: str) -> None:
        """Add a user as a copier to a trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader with ID {trader_id} not found")
        
        trader = self.traders[trader_id]
        if user_id not in trader.copiers:
            trader.copiers.append(user_id)
            logger.info(f"User {user_id} started copying trader {trader_id}")
    
    def remove_copier(self, trader_id: str, user_id: str) -> None:
        """Remove a user from a trader's copiers."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader with ID {trader_id} not found")
        
        trader = self.traders[trader_id]
        if user_id in trader.copiers:
            trader.copiers.remove(user_id)
            logger.info(f"User {user_id} stopped copying trader {trader_id}")
    
    def calculate_bonuses(self) -> None:
        """Calculate bonuses for all eligible traders."""
        current_time = datetime.now()
        
        for trader in self.traders.values():
            # Check if bonus was calculated in the last 24 hours
            if trader.last_bonus_calculation and (current_time - trader.last_bonus_calculation) < timedelta(days=1):
                continue
            
            min_copiers = self.min_copiers_for_bonus[trader.subscription_tier]
            if len(trader.copiers) >= min_copiers:
                bonus_rate = self.bonus_rates[trader.subscription_tier]
                bonus_amount = len(trader.copiers) * bonus_rate
                trader.bonus_balance += bonus_amount
                trader.last_bonus_calculation = current_time
                logger.info(f"Calculated bonus of {bonus_amount} for trader {trader.trader_id}")
    
    def get_trader_bonus_balance(self, trader_id: str) -> float:
        """Get the current bonus balance for a trader."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader with ID {trader_id} not found")
        return self.traders[trader_id].bonus_balance
    
    def withdraw_bonus(self, trader_id: str, amount: float) -> float:
        """Withdraw a specified amount from a trader's bonus balance."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader with ID {trader_id} not found")
        
        trader = self.traders[trader_id]
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > trader.bonus_balance:
            raise ValueError("Insufficient bonus balance")
        
        trader.bonus_balance -= amount
        logger.info(f"Withdrew {amount} from trader {trader_id}'s bonus balance")
        return trader.bonus_balance
    
    def upgrade_subscription(self, trader_id: str, new_tier: SubscriptionTier) -> None:
        """Upgrade a trader's subscription tier."""
        if trader_id not in self.traders:
            raise ValueError(f"Trader with ID {trader_id} not found")
        
        trader = self.traders[trader_id]
        if new_tier.value <= trader.subscription_tier.value:
            raise ValueError("New tier must be higher than current tier")
        
        trader.subscription_tier = new_tier
        logger.info(f"Upgraded trader {trader_id} to {new_tier.name} tier")

# Example usage
if __name__ == "__main__":
    system = SubscriptionSystem()
    
    # Add traders
    system.add_trader("t1", "Trader Alice", SubscriptionTier.BASIC)
    system.add_trader("t2", "Trader Bob", SubscriptionTier.PRO)
    system.add_trader("t3", "Trader Charlie", SubscriptionTier.ELITE)
    
    # Add copiers
    for i in range(15):
        system.add_copier("t1", f"user{i}")
    
    for i in range(10):
        system.add_copier("t2", f"user{i}")
    
    for i in range(5):
        system.add_copier("t3", f"user{i}")
    
    # Calculate bonuses
    system.calculate_bonuses()
    
    # Check balances
    print(f"Trader t1 bonus balance: {system.get_trader_bonus_balance('t1')}")
    print(f"Trader t2 bonus balance: {system.get_trader_bonus_balance('t2')}")
    print(f"Trader t3 bonus balance: {system.get_trader_bonus_balance('t3')}")
```
