"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: Write a program to simulate the revenue allocation process described in the World Mobile Token ecosystem, including purchasing WMTx from open markets and distributing rewards to stakers.
Generated: DETERMINISTIC_1890baf38710e0aa
Batch ID: 20250612_153954
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
from typing import List, Dict, Optional
from decimal import Decimal, getcontext
import random
import time
from datetime import datetime, timedelta

# Set precision for Decimal operations
getcontext().prec = 18

@dataclass
class Staker:
    """Represents a staker in the WMT ecosystem."""
    address: str
    staked_amount: Decimal
    staking_duration: int  # in days
    last_reward_date: Optional[datetime] = None

@dataclass
class MarketTransaction:
    """Represents a WMTx purchase transaction from the open market."""
    tx_id: str
    amount: Decimal
    price: Decimal  # in USD
    timestamp: datetime

class RevenueAllocator:
    """Simulates the revenue allocation process in the WMT ecosystem."""
    
    def __init__(self):
        self.stakers: List[Staker] = []
        self.transactions: List[MarketTransaction] = []
        self.revenue_pool: Decimal = Decimal('0')
        self.wmtx_supply: Decimal = Decimal('100000000')  # 100M WMTx
        self.current_price: Decimal = Decimal('0.10')  # Initial price in USD
        
    def add_staker(self, address: str, amount: Decimal, duration: int) -> None:
        """Add a new staker to the ecosystem."""
        if amount <= Decimal('0'):
            raise ValueError("Staked amount must be positive")
        if duration <= 0:
            raise ValueError("Staking duration must be positive")
            
        self.stakers.append(
            Staker(
                address=address,
                staked_amount=amount,
                staking_duration=duration,
                last_reward_date=datetime.now()
            )
        )
    
    def record_market_purchase(self, amount: Decimal) -> None:
        """Record a WMTx purchase from the open market."""
        if amount <= Decimal('0'):
            raise ValueError("Purchase amount must be positive")
            
        tx = MarketTransaction(
            tx_id=f"tx_{int(time.time())}_{random.randint(1000, 9999)}",
            amount=amount,
            price=self.current_price,
            timestamp=datetime.now()
        )
        self.transactions.append(tx)
        
        # Add to revenue pool (5% of purchase value)
        purchase_value = amount * self.current_price
        revenue_contribution = purchase_value * Decimal('0.05')
        self.revenue_pool += revenue_contribution
        
        # Simulate price impact (1% increase per 1M WMTx purchased)
        self.current_price *= Decimal('1') + (amount / Decimal('1000000') * Decimal('0.01'))
    
    def calculate_staking_multiplier(self, duration: int) -> Decimal:
        """Calculate the staking multiplier based on duration."""
        if duration >= 365:
            return Decimal('2.0')
        elif duration >= 180:
            return Decimal('1.5')
        elif duration >= 90:
            return Decimal('1.2')
        else:
            return Decimal('1.0')
    
    def distribute_rewards(self) -> Dict[str, Decimal]:
        """Distribute rewards from the revenue pool to stakers."""
        if not self.stakers:
            return {}
            
        total_weighted_stake = Decimal('0')
        reward_distribution = {}
        
        # Calculate total weighted stake
        for staker in self.stakers:
            multiplier = self.calculate_staking_multiplier(staker.staking_duration)
            weighted_stake = staker.staked_amount * multiplier
            total_weighted_stake += weighted_stake
        
        if total_weighted_stake == Decimal('0'):
            return {}
        
        # Distribute rewards proportionally
        for staker in self.stakers:
            multiplier = self.calculate_staking_multiplier(staker.staking_duration)
            weighted_stake = staker.staked_amount * multiplier
            reward_share = weighted_stake / total_weighted_stake
            reward_amount = self.revenue_pool * reward_share
            
            reward_distribution[staker.address] = reward_amount
            staker.last_reward_date = datetime.now()
        
        # Reset revenue pool after distribution
        self.revenue_pool = Decimal('0')
        
        return reward_distribution
    
    def simulate_market_activity(self, days: int) -> None:
        """Simulate market activity over a number of days."""
        if days <= 0:
            raise ValueError("Days must be positive")
            
        end_date = datetime.now() + timedelta(days=days)
        current_date = datetime.now()
        
        while current_date < end_date:
            # Simulate random purchases
            purchase_amount = Decimal(random.randint(1000, 100000))
            self.record_market_purchase(purchase_amount)
            
            # Daily reward distribution
            if current_date.hour == 0:  # Midnight
                rewards = self.distribute_rewards()
                if rewards:
                    print(f"Rewards distributed on {current_date.date()}:")
                    for addr, amount in rewards.items():
                        print(f"  {addr}: ${amount:.2f}")
            
            # Advance time by 1 hour
            current_date += timedelta(hours=1)
            
            # Random price fluctuations
            if random.random() < 0.1:  # 10% chance of price change
                change = Decimal(random.uniform(-0.05, 0.05))
                self.current_price *= (Decimal('1') + change)
                self.current_price = max(self.current_price, Decimal('0.01'))  # Floor price
    
    def get_system_state(self) -> Dict:
        """Return the current state of the system."""
        return {
            "stakers": len(self.stakers),
            "total_staked": sum(s.staked_amount for s in self.stakers),
            "revenue_pool": float(self.revenue_pool),
            "wmtx_price": float(self.current_price),
            "market_transactions": len(self.transactions),
            "total_revenue_generated": float(sum(tx.amount * tx.price * Decimal('0.05') for tx in self.transactions))
        }

# Example usage
if __name__ == "__main__":
    allocator = RevenueAllocator()
    
    # Add some stakers
    allocator.add_staker("addr1", Decimal('50000'), 90)
    allocator.add_staker("addr2", Decimal('100000'), 180)
    allocator.add_staker("addr3", Decimal('200000'), 365)
    
    # Simulate 7 days of market activity
    print("Starting simulation...")
    allocator.simulate_market_activity(7)
    
    # Print final state
    print("\nFinal system state:")
    state = allocator.get_system_state()
    for key, value in state.items():
        print(f"{key}: {value}")
```
