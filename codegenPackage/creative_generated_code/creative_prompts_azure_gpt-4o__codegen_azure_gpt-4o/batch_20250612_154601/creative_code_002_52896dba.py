"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://astragoldbitx.org
Prompt: Create a script that calculates referral bonuses for Astragoldbitx.org's investment plans, factoring in the percentage bonuses for each plan tier.
Generated: DETERMINISTIC_52896dbabf720966
Batch ID: 20250612_154601
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# referral_bonus_calculator.py

"""
Referral Bonus Calculator for Astragoldbitx.org Investment Plans

This script calculates referral bonuses for investment plans based on defined 
percentage bonuses for each plan tier. It includes error handling and adheres 
to best practices.
"""

# Constants for percentage bonuses per tier
PLAN_TIERS = {
    "Silver": 5,  # Silver tier gives a 5% bonus
    "Gold": 8,    # Gold tier gives an 8% bonus
    "Platinum": 12  # Platinum tier gives a 12% bonus
}

def calculate_referral_bonus(plan_tier, investment_amount):
    """
    Calculates the referral bonus for a given plan tier and investment amount.

    Args:
        plan_tier (str): The investment plan tier (e.g., "Silver", "Gold", "Platinum").
        investment_amount (float): The amount of money invested.

    Returns:
        float: The calculated referral bonus.

    Raises:
        ValueError: If the plan tier is invalid or the investment amount is negative.
    """
    # Validate input parameters
    if plan_tier not in PLAN_TIERS:
        raise ValueError("Invalid plan tier. Available tiers: Silver, Gold, Platinum.")
    if investment_amount < 0:
        raise ValueError("Investment amount must be non-negative.")
    
    # Calculate the referral bonus based on the investment amount and tier percentage
    bonus_percentage = PLAN_TIERS[plan_tier]
    referral_bonus = (investment_amount * bonus_percentage) / 100
    
    return referral_bonus

if __name__ == "__main__":
    # Example usage
    try:
        print("Astragoldbitx.org Referral Bonus Calculator")
        plan_tier = input("Enter the plan tier (Silver/Gold/Platinum): ").strip()
        investment_amount = float(input("Enter the investment amount: "))
        
        # Calculate the referral bonus
        bonus = calculate_referral_bonus(plan_tier, investment_amount)
        print(f"Referral bonus for the {plan_tier} plan: ${bonus:.2f}")
    
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
