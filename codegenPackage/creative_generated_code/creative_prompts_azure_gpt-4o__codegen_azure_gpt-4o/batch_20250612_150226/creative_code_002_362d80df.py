"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-70e.pages.dev
Prompt: Generate Python code to dynamically price on-chain messages based on wallet demand, as described in Bluwhale's incentivized outreach system.
Generated: DETERMINISTIC_362d80dfa26e57de
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import time
from collections import defaultdict

class DynamicPricingManager:
    """
    A class to manage dynamic pricing for on-chain messages based on wallet demand.
    """

    def __init__(self, base_price: float, adjustment_factor: float):
        """
        Initializes the pricing manager.
        
        :param base_price: The initial base price for messages.
        :param adjustment_factor: The multiplier for demand-based price adjustments.
        """
        self.base_price = base_price
        self.adjustment_factor = adjustment_factor
        self.wallet_message_count = defaultdict(int)  # Tracks message counts for each wallet
        self.last_updated = time.time()  # Time of the last price adjustment

    def record_message(self, wallet_address: str):
        """
        Records a message sent by a wallet.
        
        :param wallet_address: The wallet address sending the message.
        """
        self.wallet_message_count[wallet_address] += 1

    def calculate_price(self, wallet_address: str) -> float:
        """
        Calculates the price for a message based on wallet demand.
        
        :param wallet_address: The wallet address sending the message.
        :return: The calculated price for the next message.
        """
        # Base price + demand adjustment
        demand_factor = self.wallet_message_count[wallet_address] * self.adjustment_factor
        calculated_price = self.base_price + demand_factor

        return round(calculated_price, 2)  # Round to two decimal places for clarity

    def reset_demand(self):
        """
        Resets demand data periodically to ensure fairness and prevent perpetual price increases.
        """
        current_time = time.time()
        # Reset every 24 hours (86400 seconds)
        if current_time - self.last_updated > 86400:
            self.wallet_message_count.clear()
            self.last_updated = current_time

    def get_price(self, wallet_address: str) -> float:
        """
        Returns the current price for a wallet's message and performs necessary updates.
        
        :param wallet_address: The wallet address sending the message.
        :return: The current price for a message.
        """
        self.reset_demand()  # Ensure demand is reset periodically
        return self.calculate_price(wallet_address)


# Example usage
if __name__ == "__main__":
    # Initialize the dynamic pricing manager
    pricing_manager = DynamicPricingManager(base_price=0.5, adjustment_factor=0.1)
    
    wallet = "0xABC123"
    
    # Simulate sending messages and printing the prices
    for _ in range(5):
        price = pricing_manager.get_price(wallet)
        print(f"Message price for wallet {wallet}: {price}")
        pricing_manager.record_message(wallet)

    # After 24 hours, demand will reset automatically, and prices will return to the base price.
```
