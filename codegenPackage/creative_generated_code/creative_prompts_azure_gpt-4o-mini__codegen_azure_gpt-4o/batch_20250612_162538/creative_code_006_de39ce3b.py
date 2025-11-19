"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bluwhales.pages.dev
Prompt: Create a function that dynamically prices on-chain messages based on wallet demand using Bluwhale's pricing model.
Generated: DETERMINISTIC_de39ce3b12283ae1
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class DynamicPricing:
    def __init__(self, base_price: float, demand_factor: float):
        """
        Initialize the DynamicPricing model.
        
        :param base_price: The base price for the service.
        :param demand_factor: The multiplier to adjust pricing based on wallet demand.
        """
        if base_price <= 0 or demand_factor <= 0:
            raise ValueError("Base price and demand factor must be positive numbers.")
        
        self.base_price = base_price
        self.demand_factor = demand_factor

    def calculate_price(self, active_wallets: int) -> float:
        """
        Calculate the dynamic price based on active wallet demand.
        
        :param active_wallets: Number of active wallets sending messages.
        :return: Dynamically calculated price.
        """
        if active_wallets < 0:
            raise ValueError("Active wallets cannot be negative.")

        # Bluwhale's pricing formula: price = base_price * log(active_wallets + 1) * demand_factor
        price = self.base_price * math.log(active_wallets + 1) * self.demand_factor
        return round(price, 2)  # Return price rounded to 2 decimal places


# Error Handling Example - Usage
def main():
    try:
        # Initialize the pricing model (base price = 0.05, demand factor = 1.5)
        pricing_model = DynamicPricing(base_price=0.05, demand_factor=1.5)

        # Example usage: Calculate price for 500 active wallets
        active_wallet_count = 500
        dynamic_price = pricing_model.calculate_price(active_wallets=active_wallet_count)

        print(f"Dynamic price for {active_wallet_count} active wallets: ${dynamic_price}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error occurred: {e}")


# Entry point
if __name__ == "__main__":
    main()
```
