"""
Generated Code Metadata:
========================
Original URL: https://gcbt.com
Prompt: Generate a code snippet to calculate the maximum bid for a domain name like gcbt.com based on the seller's asking price and a specified bidding strategy.
Generated: DETERMINISTIC_5112494ef621d19b
Batch ID: 20250622_212100
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Domain Bid Calculator

Calculates the maximum bid for a domain name based on the seller's asking price and a specified bidding strategy.
"""

class BiddingStrategy:
    """Base class for bidding strategies."""

    def calculate_max_bid(self, asking_price):
        """
        Calculates the maximum bid based on the asking price.

        Args:
            asking_price (float): The seller's asking price.

        Returns:
            float: The maximum bid.
        """
        raise NotImplementedError


class ConservativeBiddingStrategy(BiddingStrategy):
    """Conservative bidding strategy: 10% below the asking price."""

    def calculate_max_bid(self, asking_price):
        """
        Calculates the maximum bid based on the asking price.

        Args:
            asking_price (float): The seller's asking price.

        Returns:
            float: The maximum bid.
        """
        return asking_price * 0.9


class AggressiveBiddingStrategy(BiddingStrategy):
    """Aggressive bidding strategy: 10% above the asking price."""

    def calculate_max_bid(self, asking_price):
        """
        Calculates the maximum bid based on the asking price.

        Args:
            asking_price (float): The seller's asking price.

        Returns:
            float: The maximum bid.
        """
        return asking_price * 1.1


class DomainBidCalculator:
    """Calculates the maximum bid for a domain name."""

    def __init__(self, bidding_strategy):
        """
        Initializes the calculator with a bidding strategy.

        Args:
            bidding_strategy (BiddingStrategy): The bidding strategy.
        """
        self.bidding_strategy = bidding_strategy

    def calculate_max_bid(self, domain_name, asking_price):
        """
        Calculates the maximum bid for a domain name.

        Args:
            domain_name (str): The domain name.
            asking_price (float): The seller's asking price.

        Returns:
            float: The maximum bid.

        Raises:
            ValueError: If the asking price is negative.
        """
        if asking_price < 0:
            raise ValueError("Asking price cannot be negative")

        max_bid = self.bidding_strategy.calculate_max_bid(asking_price)
        return max_bid


def main():
    # Example usage
    domain_name = "gcbt.com"
    asking_price = 1000.0

    conservative_strategy = ConservativeBiddingStrategy()
    aggressive_strategy = AggressiveBiddingStrategy()

    calculator_conservative = DomainBidCalculator(conservative_strategy)
    calculator_aggressive = DomainBidCalculator(aggressive_strategy)

    try:
        max_bid_conservative = calculator_conservative.calculate_max_bid(domain_name, asking_price)
        max_bid_aggressive = calculator_aggressive.calculate_max_bid(domain_name, asking_price)

        print(f"Domain: {domain_name}")
        print(f"Asking Price: ${asking_price:.2f}")
        print(f"Max Bid (Conservative): ${max_bid_conservative:.2f}")
        print(f"Max Bid (Aggressive): ${max_bid_aggressive:.2f}")

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
