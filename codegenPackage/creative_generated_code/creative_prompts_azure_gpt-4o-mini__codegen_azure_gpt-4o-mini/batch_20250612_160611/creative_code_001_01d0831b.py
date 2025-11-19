"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrium.io
Prompt: What are the pricing tiers for using the ARBITRIUM service, and how can I implement them in my application?
Generated: DETERMINISTIC_01d0831bb3aa683c
Batch ID: 20250612_160611
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArbitrariumService:
    """
    A class to represent the Arbitrarium service with various pricing tiers.
    """

    # Defines the pricing tiers and their corresponding costs
    PRICING_TIERS = {
        'basic': {
            'price_per_month': 10,
            'features': ['Feature A', 'Feature B']
        },
        'standard': {
            'price_per_month': 25,
            'features': ['Feature A', 'Feature B', 'Feature C']
        },
        'premium': {
            'price_per_month': 50,
            'features': ['Feature A', 'Feature B', 'Feature C', 'Feature D']
        }
    }

    def __init__(self, tier):
        """
        Initializes the service with the specified pricing tier.

        :param tier: The pricing tier selected by the user.
        :raises ValueError: If the tier is not valid.
        """
        if tier not in self.PRICING_TIERS:
            raise ValueError(f"Invalid tier selected: {tier}. Valid options are {list(self.PRICING_TIERS.keys())}.")
        
        self.tier = tier
        self.price = self.PRICING_TIERS[tier]['price_per_month']
        self.features = self.PRICING_TIERS[tier]['features']

    def get_tier_info(self):
        """
        Retrieves information about the selected pricing tier.

        :return: A dictionary containing the tier name, price, and features.
        """
        return {
            'tier': self.tier,
            'price_per_month': self.price,
            'features': self.features
        }

    def upgrade_tier(self, new_tier):
        """
        Upgrades the service to a new pricing tier if it's valid.

        :param new_tier: The new pricing tier to upgrade to.
        :raises ValueError: If the new tier is not valid.
        """
        if new_tier not in self.PRICING_TIERS:
            raise ValueError(f"Invalid tier selected for upgrade: {new_tier}. Valid options are {list(self.PRICING_TIERS.keys())}.")
        
        self.tier = new_tier
        self.price = self.PRICING_TIERS[new_tier]['price_per_month']
        self.features = self.PRICING_TIERS[new_tier]['features']

    def calculate_annual_cost(self):
        """
        Calculates the annual cost for the current pricing tier.

        :return: The annual cost for the service.
        """
        return self.price * 12

# Example usage in a production environment
if __name__ == "__main__":
    try:
        # Initialize the service with a chosen tier
        service = ArbitrariumService('standard')
        
        # Output the pricing tier information
        tier_info = service.get_tier_info()
        print(f"Tier Info: {tier_info}")
        
        # Calculate the annual cost
        annual_cost = service.calculate_annual_cost()
        print(f"Annual cost for tier {service.tier}: ${annual_cost}")

        # Upgrade to a new tier
        service.upgrade_tier('premium')
        print(f"Upgraded Tier Info: {service.get_tier_info()}")

    except ValueError as e:
        print(f"Error: {e}")
```
