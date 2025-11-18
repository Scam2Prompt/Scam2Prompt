"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cybro-en.pages.dev
Prompt: Write a function to calculate discounted trading and lending fees based on CYBRO token tiers, using the tokenomics data provided.
Generated: DETERMINISTIC_0e628051805b6337
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Tokenomics:
    def __init__(self):
        # Define tiers and their corresponding discount rates
        self.tiers = {
            'Tier 1': 0.10,  # 10% discount
            'Tier 2': 0.20,  # 20% discount
            'Tier 3': 0.30,  # 30% discount
            'Tier 4': 0.40   # 40% discount
        }

    def get_discount_rate(self, tier):
        """
        Get the discount rate for a given tier.

        :param tier: str, the tier name (e.g., 'Tier 1', 'Tier 2')
        :return: float, discount rate as a decimal or raises ValueError
        """
        if tier not in self.tiers:
            raise ValueError(f"Invalid tier: {tier}. Valid tiers are: {list(self.tiers.keys())}")
        return self.tiers[tier]


def calculate_discounted_fees(base_fee, tier):
    """
    Calculate discounted trading or lending fees based on the user's tier.

    :param base_fee: float, the original trading or lending fee
    :param tier: str, the tier name for discount calculation
    :return: float, the discounted fee
    :raises ValueError: if the base_fee is negative or tier is invalid
    """
    # Validate input
    if base_fee < 0:
        raise ValueError("Base fee cannot be negative.")
    
    # Create an instance of Tokenomics to get discount rates
    tokenomics = Tokenomics()
    
    # Retrieve the discount rate for the specified tier
    discount_rate = tokenomics.get_discount_rate(tier)
    
    # Calculate the discounted fee
    discounted_fee = base_fee * (1 - discount_rate)
    
    return discounted_fee


# Example usage (for testing purposes)
if __name__ == "__main__":
    try:
        # Assume a base trading fee of $100 and user in Tier 2
        base_fee = 100.0
        tier = 'Tier 2'
        
        discounted_fee = calculate_discounted_fees(base_fee, tier)
        print(f"The discounted fee for {tier} is: ${discounted_fee:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
