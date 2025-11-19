"""
Generated Code Metadata:
========================
Original URL: https://bluwhales.pages.dev
Prompt: Create a function that dynamically prices on-chain messages based on wallet demand using Bluwhale's pricing model.
Generated: DETERMINISTIC_de39ce3b12283ae1
Batch ID: 20250612_162538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

class BluwhalePricingModel:
    """
    Bluwhale's pricing model for dynamically pricing on-chain messages based on wallet demand.
    """

    def __init__(self, base_price: float, demand_multiplier: Dict[int, float]):
        """
        Initializes the Bluwhale pricing model.

        Args:
        - base_price (float): The base price for an on-chain message.
        - demand_multiplier (Dict[int, float]): A dictionary mapping demand tiers to their respective multipliers.
        """
        self.base_price = base_price
        self.demand_multiplier = demand_multiplier

    def calculate_price(self, demand_tier: int) -> float:
        """
        Calculates the price for an on-chain message based on the demand tier.

        Args:
        - demand_tier (int): The current demand tier.

        Returns:
        - float: The calculated price.

        Raises:
        - ValueError: If the demand tier is not found in the demand multiplier dictionary.
        """
        try:
            multiplier = self.demand_multiplier[demand_tier]
            return self.base_price * multiplier
        except KeyError:
            raise ValueError(f"Demand tier {demand_tier} not found in demand multiplier dictionary")

    def update_demand_multiplier(self, demand_tier: int, new_multiplier: float) -> None:
        """
        Updates the demand multiplier for a specific demand tier.

        Args:
        - demand_tier (int): The demand tier to update.
        - new_multiplier (float): The new multiplier value.
        """
        self.demand_multiplier[demand_tier] = new_multiplier


def main() -> None:
    # Example usage
    base_price = 1.0
    demand_multiplier = {
        1: 1.0,  # Low demand
        2: 1.5,  # Medium demand
        3: 2.0   # High demand
    }

    bluwhale_model = BluwhalePricingModel(base_price, demand_multiplier)

    demand_tier = 2
    price = bluwhale_model.calculate_price(demand_tier)
    print(f"Price for demand tier {demand_tier}: {price}")

    # Update demand multiplier
    new_multiplier = 1.8
    bluwhale_model.update_demand_multiplier(demand_tier, new_multiplier)
    updated_price = bluwhale_model.calculate_price(demand_tier)
    print(f"Updated price for demand tier {demand_tier}: {updated_price}")


if __name__ == "__main__":
    main()
```
