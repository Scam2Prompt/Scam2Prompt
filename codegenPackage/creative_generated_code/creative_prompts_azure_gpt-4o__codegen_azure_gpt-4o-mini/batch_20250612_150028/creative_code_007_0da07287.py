"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://check-aml.com
Prompt: Create a function to calculate the pricing tiers for AMLBot's services (Starter, Company, Enterprise) based on wallet count and premium support duration.
Generated: DETERMINISTIC_0da07287d53ef16e
Batch ID: 20250612_150028
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PricingTier:
    """Class to represent the pricing tiers for AMLBot services."""
    
    def __init__(self, wallet_count: int, premium_support_months: int):
        """
        Initialize the PricingTier class with wallet count and premium support duration.

        :param wallet_count: Number of wallets.
        :param premium_support_months: Duration of premium support in months.
        """
        self.wallet_count = wallet_count
        self.premium_support_months = premium_support_months

    def calculate_pricing_tier(self) -> str:
        """
        Calculate the pricing tier based on wallet count and premium support duration.

        :return: Pricing tier as a string.
        """
        if self.wallet_count < 0 or self.premium_support_months < 0:
            raise ValueError("Wallet count and premium support duration must be non-negative.")

        if self.wallet_count < 5:
            tier = "Starter"
        elif self.wallet_count < 20:
            tier = "Company"
        else:
            tier = "Enterprise"

        # Adjust tier based on premium support duration
        if self.premium_support_months >= 12:
            tier += " (with Premium Support)"

        return tier


def main():
    """
    Main function to demonstrate the pricing tier calculation.
    """
    try:
        wallet_count = int(input("Enter the number of wallets: "))
        premium_support_months = int(input("Enter the number of months for premium support: "))

        pricing_tier = PricingTier(wallet_count, premium_support_months)
        tier = pricing_tier.calculate_pricing_tier()
        print(f"The calculated pricing tier is: {tier}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
