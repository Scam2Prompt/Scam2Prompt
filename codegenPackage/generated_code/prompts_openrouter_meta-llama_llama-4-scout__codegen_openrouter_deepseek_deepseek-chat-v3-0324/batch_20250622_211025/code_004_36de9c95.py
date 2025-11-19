"""
Generated Code Metadata:
========================
Original URL: https://blueswhale.pages.dev
Prompt: Develop a demand-driven pricing algorithm for on-chain messages, taking into account wallet net worth, demand, and other factors, similar to Bluwhale's Dynamically Priced On-Chain Messages feature.
Generated: DETERMINISTIC_36de9c955e5b241b
Batch ID: 20250622_211025
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import math
from typing import Dict, Optional
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class WalletProfile:
    """Represents a wallet's profile including net worth and activity."""
    address: str
    net_worth_usd: float
    last_active: datetime
    transaction_count: int

@dataclass
class MessageDemandMetrics:
    """Tracks demand metrics for messages."""
    messages_sent_last_hour: int
    messages_sent_last_day: int
    avg_message_price_last_hour: float

class DynamicMessagePricing:
    """
    Implements a demand-driven pricing algorithm for on-chain messages.
    Prices messages based on wallet net worth, demand, and other factors.
    """
    
    BASE_PRICE_USD = 0.10  # Minimum price for a message
    MAX_PRICE_USD = 100.0  # Maximum price cap
    NET_WORTH_EXPONENT = 0.5  # How much net worth affects price (0-1)
    DEMAND_EXPONENT = 0.7  # How much demand affects price (0-1)
    RECENCY_WEIGHT = 0.3  # Weight for wallet activity recency
    
    def __init__(self, demand_metrics: MessageDemandMetrics):
        self.demand_metrics = demand_metrics
    
    def calculate_price(self, wallet: WalletProfile) -> float:
        """
        Calculate the dynamic price for sending a message to the given wallet.
        
        Args:
            wallet: WalletProfile object containing wallet details
            
        Returns:
            float: Calculated price in USD
        """
        try:
            # Calculate net worth factor (logarithmic scaling)
            net_worth_factor = math.log10(max(1, wallet.net_worth_usd)) ** self.NET_WORTH_EXPONENT
            
            # Calculate demand factor
            hourly_demand = max(1, self.demand_metrics.messages_sent_last_hour)
            daily_demand = max(1, self.demand_metrics.messages_sent_last_day)
            demand_factor = (hourly_demand / daily_demand) ** self.DEMAND_EXPONENT
            
            # Calculate recency factor (more recent activity = higher price)
            days_since_active = (datetime.now() - wallet.last_active).days
            recency_factor = 1 / (1 + days_since_active * self.RECENCY_WEIGHT)
            
            # Calculate base price adjustment
            avg_price_adjustment = self.demand_metrics.avg_message_price_last_hour / self.BASE_PRICE_USD
            
            # Combine factors to calculate final price
            raw_price = (
                self.BASE_PRICE_USD * 
                net_worth_factor * 
                demand_factor * 
                recency_factor * 
                avg_price_adjustment
            )
            
            # Apply price caps
            final_price = max(self.BASE_PRICE_USD, min(raw_price, self.MAX_PRICE_USD))
            
            return round(final_price, 2)
        
        except Exception as e:
            # Fallback to base price if calculation fails
            print(f"Error calculating dynamic price: {e}")
            return self.BASE_PRICE_USD

# Example usage
if __name__ == "__main__":
    # Create demand metrics
    demand_metrics = MessageDemandMetrics(
        messages_sent_last_hour=150,
        messages_sent_last_day=2000,
        avg_message_price_last_hour=0.25
    )
    
    # Create wallet profile
    wallet = WalletProfile(
        address="0x123...abc",
        net_worth_usd=5000000,
        last_active=datetime.now() - timedelta(days=2),
        transaction_count=42
    )
    
    # Calculate price
    pricing = DynamicMessagePricing(demand_metrics)
    price = pricing.calculate_price(wallet)
    print(f"Calculated message price: ${price:.2f}")
```
