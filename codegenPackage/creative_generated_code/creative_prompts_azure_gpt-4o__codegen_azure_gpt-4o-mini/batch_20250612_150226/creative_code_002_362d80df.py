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
from typing import Dict, List

class OnChainMessagePricing:
    """
    A class to dynamically price on-chain messages based on wallet demand.
    """

    def __init__(self):
        """
        Initializes the pricing system with default parameters.
        """
        self.wallet_demand: Dict[str, int] = {}  # Dictionary to track wallet demand
        self.base_price: float = 0.01  # Base price for on-chain message
        self.price_multiplier: float = 1.5  # Multiplier to adjust price based on demand
        self.price_history: List[float] = []  # History of prices set

    def update_demand(self, wallet_id: str, demand_weight: int) -> None:
        """
        Update the demand for a specific wallet.

        Args:
            wallet_id (str): Unique identifier for the wallet.
            demand_weight (int): The new demand weight for the wallet.

        Raises:
            ValueError: If demand_weight is negative.
        """
        if demand_weight < 0:
            raise ValueError("Demand weight cannot be negative.")
        
        self.wallet_demand[wallet_id] = demand_weight

    def calculate_price(self) -> float:
        """
        Calculate the price of on-chain messages based on demand.

        Returns:
            float: The dynamically calculated price.
        """
        total_demand = sum(self.wallet_demand.values())
        if total_demand == 0:
            return self.base_price  # If no demand, return base price
        
        # Calculate new price based on demand
        dynamic_price = self.base_price * (1 + (total_demand * self.price_multiplier))
        self.price_history.append(dynamic_price)
        return dynamic_price

    def simulate_demand_change(self, changes: Dict[str, int]) -> None:
        """
        Simulate changes in wallet demand.

        Args:
            changes (Dict[str, int]): A dictionary of wallet_id to new demand weights.
        """
        for wallet_id, demand_weight in changes.items():
            try:
                self.update_demand(wallet_id, demand_weight)
            except ValueError as e:
                print(f"Error updating demand for wallet {wallet_id}: {e}")

    def display_price_history(self) -> None:
        """
        Display the history of prices set for on-chain messages.
        """
        print("Price History:")
        for price in self.price_history:
            print(f"${price:.4f}")

# Example usage
if __name__ == "__main__":
    pricing_system = OnChainMessagePricing()
    
    # Simulating some demand changes
    demand_changes = {
        "wallet_1": 5,
        "wallet_2": 3,
        "wallet_3": 0,  # No demand from this wallet
    }
    
    pricing_system.simulate_demand_change(demand_changes)
    
    # Calculate and display the current price
    current_price = pricing_system.calculate_price()
    print(f"Current Price for on-chain messages: ${current_price:.4f}")
    
    # Display price history
    pricing_system.display_price_history()
```
