"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapsale-io.pages.dev
Prompt: Create a function to calculate the potential bonuses for early investors in a presale, based on the incentives mentioned by UniswapSale.
Generated: DETERMINISTIC_3458f7fb8b45bcef
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List

def calculate_investor_bonus(investment_amount: float, incentives: dict) -> float:
    """
    Calculate the potential bonus for an early investor in a presale based on incentives.

    Parameters:
        investment_amount (float): The amount of money the investor contributed.
        incentives (dict): The incentive structure, where keys are 'tier' thresholds 
                           and values are bonus percentages (e.g., {1000: 10, 5000: 15}).

    Returns:
        float: The calculated bonus for the investor.
    """

    # Validate inputs
    if investment_amount <= 0:
        raise ValueError("Investment amount must be greater than zero.")
    if not incentives or not isinstance(incentives, dict):
        raise ValueError("Incentives must be provided as a dictionary with tiers and percentages.")
    
    # Ensure incentives are sorted by tier thresholds in ascending order
    sorted_incentives = sorted(incentives.items(), key=lambda x: x[0])
    
    # Determine the bonus based on the investment amount
    bonus_percentage = 0.0
    for tier, percentage in sorted_incentives:
        if investment_amount >= tier:
            bonus_percentage = percentage
        else:
            break
    
    # Calculate the actual bonus
    bonus = investment_amount * (bonus_percentage / 100)
    return bonus

# Example usage:
if __name__ == "__main__":
    # Incentive structure: investment tiers and corresponding bonus percentages
    incentive_structure = {
        1000: 10,   # 10% bonus for investments >= $1000
        5000: 15,   # 15% bonus for investments >= $5000
        10000: 20   # 20% bonus for investments >= $10000
    }

    try:
        investment = 7500  # Example investment amount
        bonus = calculate_investor_bonus(investment, incentive_structure)
        print(f"Investment: ${investment}, Bonus: ${bonus}")
    except ValueError as e:
        print(f"Error: {e}")
```
