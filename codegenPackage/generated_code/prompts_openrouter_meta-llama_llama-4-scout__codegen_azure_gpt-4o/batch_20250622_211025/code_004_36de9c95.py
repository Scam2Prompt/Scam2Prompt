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
import logging

# Configure logging for error handling and debugging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DemandDrivenPricing:
    """
    A class to calculate demand-driven pricing for on-chain messages.
    """

    def __init__(self, base_price: float, max_price: float):
        """
        Initialize the pricing algorithm with base and maximum price limits.

        :param base_price: The minimum price for an on-chain message.
        :param max_price: The maximum price for an on-chain message.
        """
        if base_price <= 0 or max_price <= 0 or base_price >= max_price:
            raise ValueError("Base price must be positive and less than max price.")
        self.base_price = base_price
        self.max_price = max_price

    def calculate_price(self, wallet_net_worth: float, demand_factor: float, priority_factor: float) -> float:
        """
        Calculate the price for an on-chain message based on wallet net worth, demand, and priority.

        :param wallet_net_worth: The net worth of the wallet (in USD or equivalent).
        :param demand_factor: A value representing current demand (0 to 1, where 1 is highest demand).
        :param priority_factor: A value representing message priority (0 to 1, where 1 is highest priority).
        :return: The calculated price for the on-chain message.
        """
        try:
            # Validate inputs
            if wallet_net_worth <= 0:
                raise ValueError("Wallet net worth must be positive.")
            if not (0 <= demand_factor <= 1):
                raise ValueError("Demand factor must be between 0 and 1.")
            if not (0 <= priority_factor <= 1):
                raise ValueError("Priority factor must be between 0 and 1.")

            # Calculate dynamic price adjustment based on wallet net worth
            net_worth_factor = math.log(wallet_net_worth + 1) / 10  # Logarithmic scaling for fairness

            # Combine factors to calculate the final price
            price = self.base_price + (self.max_price - self.base_price) * (
                demand_factor * 0.5 + priority_factor * 0.3 + net_worth_factor * 0.2
            )

            # Ensure price does not exceed max_price
            final_price = min(price, self.max_price)

            return round(final_price, 2)  # Round to two decimal places for clarity

        except Exception as e:
            logging.error(f"Error calculating price: {e}")
            raise

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the pricing algorithm with base and max price
        pricing = DemandDrivenPricing(base_price=0.01, max_price=10.00)

        # Example parameters
        wallet_net_worth = 5000.00  # Wallet net worth in USD
        demand_factor = 0.8         # High demand
        priority_factor = 0.6       # Medium priority

        # Calculate the price
        price = pricing.calculate_price(wallet_net_worth, demand_factor, priority_factor)
        print(f"The calculated price for the on-chain message is: ${price}")

    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
