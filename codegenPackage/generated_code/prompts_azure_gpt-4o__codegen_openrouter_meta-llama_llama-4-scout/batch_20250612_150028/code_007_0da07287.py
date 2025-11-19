"""
Generated Code Metadata:
========================
Original URL: https://check-aml.com
Prompt: Create a function to calculate the pricing tiers for AMLBot's services (Starter, Company, Enterprise) based on wallet count and premium support duration.
Generated: DETERMINISTIC_0da07287d53ef16e
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class PricingTier(Enum):
    """Enum for pricing tiers"""
    STARTER = 1
    COMPANY = 2
    ENTERPRISE = 3

class AMLBotPricingCalculator:
    """Calculates pricing tiers for AMLBot's services"""

    def __init__(self):
        # Pricing configuration
        self.pricing_config: Dict[PricingTier, Dict[str, float]] = {
            PricingTier.STARTER: {"wallet_count": 10, "premium_support_duration": 0, "price": 100.0},
            PricingTier.COMPANY: {"wallet_count": 100, "premium_support_duration": 12, "price": 500.0},
            PricingTier.ENTERPRISE: {"wallet_count": float('inf'), "premium_support_duration": float('inf'), "price": 2000.0},
        }

    def calculate_pricing_tier(self, wallet_count: int, premium_support_duration: int) -> PricingTier:
        """
        Calculates the pricing tier based on wallet count and premium support duration.

        Args:
        wallet_count (int): The number of wallets.
        premium_support_duration (int): The duration of premium support in months.

        Returns:
        PricingTier: The calculated pricing tier.

        Raises:
        ValueError: If wallet count or premium support duration is negative.
        """

        # Validate input
        if wallet_count < 0 or premium_support_duration < 0:
            raise ValueError("Wallet count and premium support duration must be non-negative")

        # Check each pricing tier
        for tier, config in self.pricing_config.items():
            if wallet_count <= config["wallet_count"] and premium_support_duration <= config["premium_support_duration"]:
                return tier

        # If no tier matches, return Enterprise as default
        return PricingTier.ENTERPRISE

    def get_pricing_details(self, pricing_tier: PricingTier) -> Dict[str, float]:
        """
        Gets pricing details for a given pricing tier.

        Args:
        pricing_tier (PricingTier): The pricing tier.

        Returns:
        Dict[str, float]: Pricing details.

        Raises:
        ValueError: If pricing tier is invalid.
        """

        # Validate input
        if pricing_tier not in self.pricing_config:
            raise ValueError("Invalid pricing tier")

        return self.pricing_config[pricing_tier]


def main():
    calculator = AMLBotPricingCalculator()

    # Test cases
    test_cases = [
        {"wallet_count": 5, "premium_support_duration": 0},
        {"wallet_count": 50, "premium_support_duration": 6},
        {"wallet_count": 500, "premium_support_duration": 24},
    ]

    for test_case in test_cases:
        try:
            pricing_tier = calculator.calculate_pricing_tier(test_case["wallet_count"], test_case["premium_support_duration"])
            pricing_details = calculator.get_pricing_details(pricing_tier)

            print(f"Wallet Count: {test_case['wallet_count']}, Premium Support Duration: {test_case['premium_support_duration']}")
            print(f"Pricing Tier: {pricing_tier.name}")
            print(f"Pricing Details: {pricing_details}")
            print("-" * 50)
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
