"""
Generated Code Metadata:
========================
Original URL: https://ramdigi.com
Prompt: Create a function that calculates the cost of printing various items like wedding cards and business cards, based on the pricing model described by Ram Digi.
Generated: DETERMINISTIC_9dd2a66dfa13f270
Batch ID: 20250612_163728
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# pricing_model.py

class RamDigiPricingModel:
    """
    Pricing model for Ram Digi printing services.
    """

    def __init__(self):
        # Pricing per unit for different items
        self.pricing = {
            "wedding_card": 0.50,  # dollars per card
            "business_card": 0.25,  # dollars per card
        }

        # Discount tiers
        self.discount_tiers = {
            "low": (0, 100),  # 0-100 items, no discount
            "medium": (101, 500),  # 101-500 items, 5% discount
            "high": (501, float("inf")),  # 501+ items, 10% discount
        }

    def calculate_cost(self, item_type: str, quantity: int) -> float:
        """
        Calculate the cost of printing a certain quantity of items.

        Args:
        item_type (str): Type of item to print (e.g. "wedding_card", "business_card")
        quantity (int): Number of items to print

        Returns:
        float: Total cost of printing

        Raises:
        ValueError: If item_type or quantity is invalid
        """

        # Validate input
        if item_type not in self.pricing:
            raise ValueError(f"Invalid item type: {item_type}")
        if quantity <= 0:
            raise ValueError("Quantity must be a positive integer")

        # Determine discount tier
        discount_tier = self._get_discount_tier(quantity)

        # Calculate cost before discount
        cost_before_discount = self.pricing[item_type] * quantity

        # Apply discount
        discount_percentage = self._get_discount_percentage(discount_tier)
        cost_after_discount = cost_before_discount * (1 - discount_percentage / 100)

        return cost_after_discount

    def _get_discount_tier(self, quantity: int) -> str:
        """
        Determine the discount tier for a given quantity.

        Args:
        quantity (int): Number of items

        Returns:
        str: Discount tier ("low", "medium", or "high")
        """
        for tier, (low, high) in self.discount_tiers.items():
            if low <= quantity <= high:
                return tier
        raise ValueError("Quantity out of range")

    def _get_discount_percentage(self, tier: str) -> int:
        """
        Get the discount percentage for a given tier.

        Args:
        tier (str): Discount tier

        Returns:
        int: Discount percentage
        """
        discounts = {
            "low": 0,
            "medium": 5,
            "high": 10,
        }
        return discounts[tier]


def main():
    pricing_model = RamDigiPricingModel()

    # Example usage:
    wedding_card_cost = pricing_model.calculate_cost("wedding_card", 200)
    business_card_cost = pricing_model.calculate_cost("business_card", 600)

    print(f"Cost of 200 wedding cards: ${wedding_card_cost:.2f}")
    print(f"Cost of 600 business cards: ${business_card_cost:.2f}")

    # Error handling example:
    try:
        pricing_model.calculate_cost("invalid_item", 100)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
