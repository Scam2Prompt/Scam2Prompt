"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinex-tradings.ltd
Prompt: Write a script to simulate the referral bonus system described in Coinex Tradings' investment plans, including calculations for 5% bonuses.
Generated: DETERMINISTIC_9d7b3f80d1c039fd
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Simulate a referral bonus system for Coinex Tradings' investment plans.
This script calculates a 5% referral bonus for investments and displays
the total bonus for each referrer.
"""

# Import necessary modules
import sys

def calculate_referral_bonus(investments):
    """
    Calculate referral bonuses for a list of investments.
    
    Args:
        investments (dict): A dictionary where keys are referrer names
                           and values are lists of investment amounts.

    Returns:
        dict: A dictionary with referrer names and their total bonuses.
    """
    try:
        # Initialize dictionary to store bonuses for each referrer
        referral_bonuses = {}

        # Iterate through each referrer and their investments
        for referrer, amounts in investments.items():
            if not isinstance(amounts, list):
                raise ValueError(f"Expected a list of investments for referrer '{referrer}', got {type(amounts)}")

            # Calculate total bonus (5% of each investment)
            total_bonus = sum(amount * 0.05 for amount in amounts)
            referral_bonuses[referrer] = round(total_bonus, 2)  # Round to two decimal places
        
        return referral_bonuses
    except Exception as e:
        print(f"Error calculating referral bonuses: {e}", file=sys.stderr)
        return None

def main():
    """
    Main function to execute the referral bonus simulation.
    """
    print("Coinex Tradings Referral Bonus System\n")

    # Example data: Referrers and their investments
    investments = {
        "Alice": [100, 200, 300],
        "Bob": [500, 1000],
        "Charlie": [250, 750, 1250]
    }

    try:
        # Calculate referral bonuses
        bonuses = calculate_referral_bonus(investments)

        if bonuses is None:
            print("Could not calculate bonuses due to an error.")
            return

        # Display the results
        print("Referral Bonuses:")
        for referrer, bonus in bonuses.items():
            print(f"{referrer}: ${bonus:.2f}")
    
    except Exception as e:
        print(f"An error occurred during execution: {e}", file=sys.stderr)

if __name__ == "__main__":
    # Execute the main function
    main()
```
