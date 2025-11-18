"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cashb90.net
Prompt: Write a Python script to simulate a cashback calculation for a casino platform, including user loyalty tiers and bonus percentages as described in BaxBet's loyalty program.
Generated: DETERMINISTIC_6e63ec61c0a39ddc
Batch ID: 20250612_154239
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This Python script simulates a cashback calculation for a casino platform, 
including user loyalty tiers and bonus percentages based on BaxBet's loyalty program.
The script calculates cashback based on user spending and their loyalty tier.
"""

# Import necessary libraries
from typing import Dict, Tuple

# Define a dictionary to represent loyalty tiers and their cashback percentages
LOYALTY_TIERS = {
    "Bronze": 0.01,  # 1% cashback
    "Silver": 0.02,  # 2% cashback
    "Gold": 0.05,    # 5% cashback
    "Platinum": 0.10 # 10% cashback
}

class InvalidTierError(Exception):
    """Exception raised for invalid loyalty tiers."""
    pass

def calculate_cashback(tier: str, amount_spent: float) -> Tuple[float, str]:
    """
    Calculates the cashback based on the user's loyalty tier and the total amount spent.

    Args:
        tier (str): The user's loyalty tier (Bronze, Silver, Gold, Platinum).
        amount_spent (float): The total amount spent by the user.

    Returns:
        Tuple[float, str]: The calculated cashback amount and the tier applied.

    Raises:
        InvalidTierError: If the provided tier is not valid.
        ValueError: If the amount spent is negative.
    """
    # Validate the tier
    if tier not in LOYALTY_TIERS:
        raise InvalidTierError(f"'{tier}' is not a valid loyalty tier. Valid tiers are: {', '.join(LOYALTY_TIERS.keys())}")
    
    # Validate the spending amount
    if amount_spent < 0:
        raise ValueError("Amount spent cannot be negative.")
    
    # Calculate cashback
    cashback_percentage = LOYALTY_TIERS[tier]
    cashback_amount = amount_spent * cashback_percentage
    return cashback_amount, tier

def simulate_cashback_calculation(user_data: Dict[str, float]):
    """
    Simulates cashback calculations for multiple users based on their loyalty tiers and spending.

    Args:
        user_data (Dict[str, float]): Dictionary containing user loyalty tiers
                                      and their respective spending amounts.

    Returns:
        None. Displays the cashback calculation for each user.
    """
    for user, (tier, spending) in user_data.items():
        try:
            cashback, applied_tier = calculate_cashback(tier, spending)
            print(f"User: {user}, Tier: {applied_tier}, Spending: ${spending:.2f}, Cashback: ${cashback:.2f}")
        except (InvalidTierError, ValueError) as e:
            print(f"Error for user '{user}': {e}")

# Example usage
if __name__ == "__main__":
    # Sample user data
    user_data = {
        "Alice": ("Gold", 500.0),
        "Bob": ("Silver", 300.0),
        "Charlie": ("Bronze", 100.0),
        "Dana": ("Platinum", 1000.0),
        "Eve": ("Diamond", 200.0),  # Invalid tier
        "Frank": ("Gold", -50.0)    # Invalid spending
    }

    print("---------- Cashback Simulation ----------")
    simulate_cashback_calculation(user_data)
    print("-----------------------------------------")
```
