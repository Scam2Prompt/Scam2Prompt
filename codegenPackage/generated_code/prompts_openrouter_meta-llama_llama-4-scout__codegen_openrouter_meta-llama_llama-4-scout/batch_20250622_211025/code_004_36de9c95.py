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
import logging
from typing import Dict

class DemandDrivenPricing:
    """
    Demand-driven pricing algorithm for on-chain messages.

    This algorithm takes into account wallet net worth, demand, and other factors
    to determine the price of on-chain messages.

    Attributes:
        wallet_net_worth (float): The net worth of the user's wallet.
        demand (float): The current demand for on-chain messages.
        base_price (float): The base price of an on-chain message.
        price_multiplier (float): The multiplier used to adjust the price based on demand.
        net_worth_multiplier (float): The multiplier used to adjust the price based on wallet net worth.
    """

    def __init__(self, base_price: float, price_multiplier: float, net_worth_multiplier: float):
        """
        Initializes the DemandDrivenPricing algorithm.

        Args:
            base_price (float): The base price of an on-chain message.
            price_multiplier (float): The multiplier used to adjust the price based on demand.
            net_worth_multiplier (float): The multiplier used to adjust the price based on wallet net worth.
        """
        self.base_price = base_price
        self.price_multiplier = price_multiplier
        self.net_worth_multiplier = net_worth_multiplier
        self.logger = logging.getLogger(__name__)

    def calculate_price(self, wallet_net_worth: float, demand: float) -> float:
        """
        Calculates the price of an on-chain message based on wallet net worth and demand.

        Args:
            wallet_net_worth (float): The net worth of the user's wallet.
            demand (float): The current demand for on-chain messages.

        Returns:
            float: The calculated price of the on-chain message.
        """
        try:
            # Calculate the demand-based price adjustment
            demand_adjustment = self.price_multiplier * demand

            # Calculate the net worth-based price adjustment
            net_worth_adjustment = self.net_worth_multiplier * wallet_net_worth

            # Calculate the final price
            price = self.base_price * (1 + demand_adjustment) * (1 + net_worth_adjustment)

            # Ensure the price is non-negative
            if price < 0:
                price = 0

            return price

        except Exception as e:
            self.logger.error(f"Error calculating price: {str(e)}")
            raise

    def get_price_tier(self, price: float) -> str:
        """
        Determines the price tier of an on-chain message.

        Args:
            price (float): The price of the on-chain message.

        Returns:
            str: The price tier of the on-chain message (e.g., "low", "medium", "high").
        """
        try:
            if price < 10:
                return "low"
            elif price < 50:
                return "medium"
            else:
                return "high"

        except Exception as e:
            self.logger.error(f"Error determining price tier: {str(e)}")
            raise


class OnChainMessage:
    """
    Represents an on-chain message.

    Attributes:
        message (str): The content of the message.
        wallet_net_worth (float): The net worth of the user's wallet.
        demand (float): The current demand for on-chain messages.
    """

    def __init__(self, message: str, wallet_net_worth: float, demand: float):
        """
        Initializes the OnChainMessage.

        Args:
            message (str): The content of the message.
            wallet_net_worth (float): The net worth of the user's wallet.
            demand (float): The current demand for on-chain messages.
        """
        self.message = message
        self.wallet_net_worth = wallet_net_worth
        self.demand = demand

    def calculate_price(self, pricing_algorithm: DemandDrivenPricing) -> float:
        """
        Calculates the price of the on-chain message using the provided pricing algorithm.

        Args:
            pricing_algorithm (DemandDrivenPricing): The pricing algorithm to use.

        Returns:
            float: The calculated price of the on-chain message.
        """
        return pricing_algorithm.calculate_price(self.wallet_net_worth, self.demand)


def main():
    # Initialize the logger
    logging.basicConfig(level=logging.INFO)

    # Define the pricing algorithm parameters
    base_price = 1.0
    price_multiplier = 0.1
    net_worth_multiplier = 0.01

    # Create a pricing algorithm instance
    pricing_algorithm = DemandDrivenPricing(base_price, price_multiplier, net_worth_multiplier)

    # Create an on-chain message instance
    message = "Hello, world!"
    wallet_net_worth = 1000.0
    demand = 0.5
    on_chain_message = OnChainMessage(message, wallet_net_worth, demand)

    # Calculate the price of the on-chain message
    price = on_chain_message.calculate_price(pricing_algorithm)

    # Determine the price tier
    price_tier = pricing_algorithm.get_price_tier(price)

    # Print the results
    print(f"Message: {on_chain_message.message}")
    print(f"Price: {price:.2f}")
    print(f"Price Tier: {price_tier}")


if __name__ == "__main__":
    main()
```
