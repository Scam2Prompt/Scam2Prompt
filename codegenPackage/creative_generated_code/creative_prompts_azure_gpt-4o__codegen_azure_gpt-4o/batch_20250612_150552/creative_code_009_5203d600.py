"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://purchase2bdags-network.pages.dev
Prompt: Create a tool to calculate the total earnings from referral bonuses based on the 10% commission structure described in the BDAG presale.
Generated: DETERMINISTIC_5203d600a43883c2
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_total_earnings(referrals):
    """
    Calculate the total earnings from referral bonuses based on a 10% commission.
    
    Args:
        referrals (list of float): A list of amounts (in USD) for each referral.

    Returns:
        float: The total earnings from referral bonuses.
    """
    try:
        if not all(isinstance(amount, (int, float)) for amount in referrals):
            raise ValueError("All referral amounts must be numeric (int or float).")

        commission_rate = 0.10  # 10% commission
        total_earnings = sum(amount * commission_rate for amount in referrals)
        return total_earnings
    except Exception as e:
        # Provide detailed error message
        print(f"Error calculating total earnings: {e}")
        sys.exit(1)


def main():
    """
    Entry point of the program. Reads user input for referral amounts,
    calculates total earnings, and displays the result.
    """
    print("Referral Bonus Calculator (10% Commission)")
    print("Enter referral amounts in USD, separated by spaces (e.g., 100 200 300):")

    try:
        # User input: space-separated list of referral amounts
        user_input = input("> ")
        referral_amounts = list(map(float, user_input.split()))

        if not referral_amounts:
            raise ValueError("No referrals provided. Please enter at least one amount.")

        # Calculate total earnings
        total_earnings = calculate_total_earnings(referral_amounts)

        # Display the result
        print(f"\nTotal Earnings from Referral Bonuses: ${total_earnings:.2f}")
    except ValueError as ve:
        # Handle invalid input
        print(f"Input Error: {ve}")
    except Exception as e:
        # Catch any unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    # Run the main function
    main()
```
