"""
Generated Code Metadata:
========================
Original URL: https://eternallaunch.pages.dev
Prompt: What are the different tiers for the $EAI public sale, and how do they affect the boost and hard cap for participants?
Generated: DETERMINISTIC_fcc9e18735ecec73
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# EAI Public Sale Tiers
class EAIPublicSaleTiers:
    def __init__(self):
        """
        Initialize EAI public sale tiers with their respective boost and hard cap.
        """
        self.tiers = [
            {"tier": "Tier 1", "min_allocation": 0, "max_allocation": 1000, "boost": 1.0, "hard_cap": 10000},
            {"tier": "Tier 2", "min_allocation": 1001, "max_allocation": 5000, "boost": 1.2, "hard_cap": 20000},
            {"tier": "Tier 3", "min_allocation": 5001, "max_allocation": 10000, "boost": 1.5, "hard_cap": 50000},
            {"tier": "Tier 4", "min_allocation": 10001, "max_allocation": float('inf'), "boost": 2.0, "hard_cap": 100000},
        ]

    def get_tier_info(self, allocation):
        """
        Get the tier information for a given allocation.

        Args:
            allocation (int): The allocation amount.

        Returns:
            dict: The tier information, including boost and hard cap.

        Raises:
            ValueError: If allocation is not a positive number.
        """
        if allocation <= 0:
            raise ValueError("Allocation must be a positive number.")

        for tier in self.tiers:
            if tier["min_allocation"] <= allocation <= tier["max_allocation"]:
                return tier

        raise ValueError("No tier found for the given allocation.")

    def calculate_boost_and_hard_cap(self, allocation):
        """
        Calculate the boost and hard cap for a given allocation.

        Args:
            allocation (int): The allocation amount.

        Returns:
            tuple: A tuple containing the boost and hard cap.

        Raises:
            ValueError: If allocation is not a positive number.
        """
        tier_info = self.get_tier_info(allocation)
        return tier_info["boost"], tier_info["hard_cap"]


def main():
    try:
        eai_public_sale_tiers = EAIPublicSaleTiers()
        allocation = 7500
        tier_info = eai_public_sale_tiers.get_tier_info(allocation)
        boost, hard_cap = eai_public_sale_tiers.calculate_boost_and_hard_cap(allocation)

        print(f"Tier: {tier_info['tier']}")
        print(f"Boost: {boost}")
        print(f"Hard Cap: {hard_cap}")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
