"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimusdtbox.in
Prompt: Generate a script to calculate total earnings from bonuses and referrals on the "Claim USDT Box" cryptocurrency rewards program.
Generated: DETERMINISTIC_5adcc3093024468d
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_earnings(bonuses, referrals):
    """
    Calculate total earnings from bonuses and referrals.

    Args:
        bonuses (list of float): A list containing bonus amounts.
        referrals (list of float): A list containing referral amounts.

    Returns:
        float: Total earnings calculated by summing bonuses and referrals.
    """
    try:
        # Validate input data types
        if not all(isinstance(bonus, (int, float)) for bonus in bonuses):
            raise ValueError("All bonus amounts must be numeric.")
        if not all(isinstance(referral, (int, float)) for referral in referrals):
            raise ValueError("All referral amounts must be numeric.")

        # Calculate total earnings
        total_bonuses = sum(bonuses)
        total_referrals = sum(referrals)
        total_earnings = total_bonuses + total_referrals

        return total_earnings
    except ValueError as ve:
        # Handle value errors and provide meaningful feedback
        print(f"Error: {ve}")
    except Exception as e:
        # Catch unexpected errors
        print(f"Unexpected error: {e}")
        sys.exit(1)

# Example usage
if __name__ == "__main__":
    # Test data - Replace these with actual program inputs
    bonuses = [10.5, 20.0, 15.75]  # Sample bonus amounts
    referrals = [5.0, 10.0, 7.25]  # Sample referral amounts

    # Calculate and display total earnings
    total_earnings = calculate_total_earnings(bonuses, referrals)
    if total_earnings is not None:  # Ensure earnings calculation succeeded
        print(f"Total earnings from bonuses and referrals: {total_earnings} USDT")
```
