"""
Generated Code Metadata:
========================
Original URL: https://ff-70e.pages.dev
Prompt: Generate Python code to dynamically price on-chain messages based on wallet demand, as described in Bluwhale's incentivized outreach system.
Generated: DETERMINISTIC_362d80dfa26e57de
Batch ID: 20250612_150226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from collections import defaultdict
from typing import Dict, List, Tuple

class OnChainMessagePricing:
    def __init__(self):
        # Dictionary to hold demand data for each wallet
        self.wallet_demand: Dict[str, int] = defaultdict(int)
        # Dictionary to hold the pricing for each message type
        self.message_pricing: Dict[str, float] = {}
        # Time interval for price adjustment (in seconds)
        self.price_adjustment_interval = 60
        # Last time prices were adjusted
        self.last_price_adjustment = time.time()

    def record_message_sent(self, wallet_id: str, message_type: str):
        """
        Record that a message has been sent from a wallet.
        
        :param wallet_id: The ID of the wallet sending the message
        :param message_type: The type of message being sent
        """
        self.wallet_demand[wallet_id] += 1
        self._update_pricing(message_type)

    def _update_pricing(self, message_type: str):
        """
        Update the pricing for a message type based on wallet demand.
        
        :param message_type: The type of message to update pricing for
        """
        current_time = time.time()
        if current_time - self.last_price_adjustment >= self.price_adjustment_interval:
            total_demand = sum(self.wallet_demand.values())
            if total_demand > 0:
                # Example pricing logic: base price adjusted by demand
                self.message_pricing[message_type] = 1.0 + (total_demand / 100.0)
            else:
                self.message_pricing[message_type] = 1.0  # Default price if no demand
            self.last_price_adjustment = current_time

    def get_price(self, message_type: str) -> float:
        """
        Get the current price for a specific message type.
        
        :param message_type: The type of message to get the price for
        :return: The current price for the message type
        """
        return self.message_pricing.get(message_type, 1.0)  # Default price if not set

    def reset_demand(self):
        """
        Reset the demand data for all wallets.
        This can be called periodically to clear old data.
        """
        self.wallet_demand.clear()

# Example usage
if __name__ == "__main__":
    pricing_system = OnChainMessagePricing()
    
    # Simulate sending messages
    try:
        pricing_system.record_message_sent("wallet_1", "message_type_A")
        pricing_system.record_message_sent("wallet_2", "message_type_A")
        pricing_system.record_message_sent("wallet_1", "message_type_B")
        
        print("Price for message_type_A:", pricing_system.get_price("message_type_A"))
        print("Price for message_type_B:", pricing_system.get_price("message_type_B"))
        
        # Reset demand after some time
        time.sleep(120)  # Wait for the price adjustment interval
        pricing_system.reset_demand()
        
    except Exception as e:
        print(f"An error occurred: {e}")
```
