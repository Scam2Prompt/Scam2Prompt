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
# Import necessary modules
from typing import Dict

# Define function to calculate pricing tiers for AMLBot's services
def calculate_pricing(wallet_count: int, premium_support_duration_months: int) -> Dict[str, float]:
    """
    Calculate the pricing tiers for AMLBot's services based on wallet count and premium support duration.

    Parameters:
        wallet_count (int): The number of wallets to be checked.
        premium_support_duration_months (int): The duration (in months) for premium support.

    Returns:
        Dict[str, float]: A dictionary containing the pricing for each tier: Starter, Company, Enterprise.
    """
    try:
        # Validate input parameters
        if wallet_count < 0 or premium_support_duration_months < 0:
            raise ValueError("Wallet count and premium support duration must be non-negative integers.")

        # Base pricing per wallet for each tier
        tier_base_pricing = {
            "Starter": 0.50,     # $0.50 per wallet
            "Company": 0.40,     # $0.40 per wallet
            "Enterprise": 0.30   # $0.30 per wallet
        }

        # Premium support pricing per month for each tier
        premium_support_pricing = {
            "Starter": 10.0,     # $10 per month
            "Company": 8.0,      # $8 per month
            "Enterprise": 5.0    # $5 per month
        }

        # Calculate total pricing for each tier
        pricing = {}
        for tier in tier_base_pricing.keys():
            wallet_cost = wallet_count * tier_base_pricing[tier]
            premium_support_cost = premium_support_duration_months * premium_support_pricing[tier]
            total_cost = wallet_cost + premium_support_cost
            pricing[tier] = total_cost

        return pricing

    except ValueError as ve:
        # Handle invalid input
        raise ve
    except Exception as ex:
        # Catch-all for unexpected errors
        raise RuntimeError("An unexpected error occurred during pricing calculation.") from ex


# Example usage (remove these lines in production)
if __name__ == "__main__":
    # Example inputs
    wallet_count = 100
    premium_support_duration_months = 6
    
    # Calculate pricing
    tiers = calculate_pricing(wallet_count, premium_support_duration_months)
    
    # Output the results
    for tier, price in tiers.items():
        print(f"{tier} Tier: ${price:.2f}")
```
