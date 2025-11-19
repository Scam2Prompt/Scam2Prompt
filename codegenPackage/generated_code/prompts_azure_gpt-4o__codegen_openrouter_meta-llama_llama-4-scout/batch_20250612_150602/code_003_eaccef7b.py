"""
Generated Code Metadata:
========================
Original URL: https://blurs.io
Prompt: Create a pricing calculator for AI-powered website services, inspired by the pricing model on Blurs.io.
Generated: DETERMINISTIC_eaccef7b719c8953
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_calculator.py

class PricingCalculator:
    """
    Calculates pricing for AI-powered website services.

    Inspired by Blurs.io pricing model.
    """

    def __init__(self, base_price, tiered_pricing):
        """
        Initializes the pricing calculator.

        Args:
        - base_price (float): The base price for the service.
        - tiered_pricing (dict): A dictionary containing tiered pricing information.
            Each key is a tier name, and each value is another dictionary with
            'traffic_limit' and 'price_multiplier' keys.
        """
        self.base_price = base_price
        self.tiered_pricing = tiered_pricing

    def calculate_price(self, traffic):
        """
        Calculates the price for the given traffic.

        Args:
        - traffic (int): The traffic volume.

        Returns:
        - float: The calculated price.

        Raises:
        - ValueError: If traffic is negative.
        """
        if traffic < 0:
            raise ValueError("Traffic cannot be negative")

        # Find the applicable tier
        applicable_tier = None
        for tier, info in self.tiered_pricing.items():
            if traffic <= info['traffic_limit']:
                applicable_tier = tier
                break

        if applicable_tier is None:
            # If no tier is applicable, use the highest tier's price
            highest_tier = max(self.tiered_pricing, key=lambda x: self.tiered_pricing[x]['traffic_limit'])
            price_multiplier = self.tiered_pricing[highest_tier]['price_multiplier']
        else:
            price_multiplier = self.tiered_pricing[applicable_tier]['price_multiplier']

        # Calculate the price
        price = self.base_price * price_multiplier

        return price


def main():
    # Define the base price and tiered pricing
    base_price = 10.0
    tiered_pricing = {
        'basic': {'traffic_limit': 1000, 'price_multiplier': 1.0},
        'premium': {'traffic_limit': 10000, 'price_multiplier': 2.0},
        'enterprise': {'traffic_limit': float('inf'), 'price_multiplier': 5.0}
    }

    calculator = PricingCalculator(base_price, tiered_pricing)

    # Test the calculator
    traffic_values = [500, 2000, 5000, 20000]
    for traffic in traffic_values:
        try:
            price = calculator.calculate_price(traffic)
            print(f"Traffic: {traffic}, Price: ${price:.2f}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
