"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fintradeoptions.com
Prompt: Develop a referral bonus system in Python that calculates bonuses based on Fintradeoptions' referral level system.
Generated: DETERMINISTIC_ef19f488155dcebc
Batch ID: 20250612_150816
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
from typing import Dict, List

# Constants for referral levels and their respective bonus percentages
REFERRAL_LEVEL_BONUSES = {
    1: 0.10,  # Level 1: 10%
    2: 0.05,  # Level 2: 5%
    3: 0.02,  # Level 3: 2%
}

# Function to calculate referral bonuses
def calculate_referral_bonus(referral_hierarchy: Dict[str, List[str]], transaction_amount: float) -> Dict[str, float]:
    """
    Calculate referral bonuses based on Fintradeoptions' referral level system.

    Args:
        referral_hierarchy (Dict[str, List[str]]): A dictionary where keys are user IDs and values are lists of referred user IDs.
        transaction_amount (float): The transaction amount from which bonuses will be calculated.

    Returns:
        Dict[str, float]: A dictionary where keys are user IDs and values are the calculated bonus amounts.
    """
    # Dictionary to store the bonus amounts for each user
    bonuses = {user: 0.0 for user in referral_hierarchy}

    # Iterate over each user in the referral hierarchy
    for referrer, referrals in referral_hierarchy.items():
        # Process each referral for the referrer
        for level, referral in enumerate(referrals, start=1):
            # Ensure the referral level exists in the bonus system
            if level in REFERRAL_LEVEL_BONUSES:
                # Calculate the bonus for the current level
                bonus_percentage = REFERRAL_LEVEL_BONUSES[level]
                bonus = transaction_amount * bonus_percentage
                
                # Accumulate the bonus for the referrer
                bonuses[referrer] += bonus

    return bonuses

# Example usage
if __name__ == "__main__":
    try:
        # Sample referral hierarchy
        referral_hierarchy = {
            "User1": ["User2", "User3"],  # User1 referred User2 and User3
            "User2": ["User4"],          # User2 referred User4
            "User3": [],                 # User3 has no referrals
            "User4": []                  # User4 has no referrals
        }

        # Example transaction amount
        transaction_amount = 100.0  # $100 transaction

        # Calculate bonuses
        bonuses = calculate_referral_bonus(referral_hierarchy, transaction_amount)

        # Output the results
        print("Referral Bonuses:")
        for user, bonus in bonuses.items():
            print(f"{user}: ${bonus:.2f}")

    except Exception as e:
        # Handle unexpected errors
        print(f"An error occurred: {e}")
```
