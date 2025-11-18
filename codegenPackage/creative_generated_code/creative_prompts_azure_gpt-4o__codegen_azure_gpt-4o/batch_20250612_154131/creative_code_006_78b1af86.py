"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://unstaked-token.world
Prompt: Write a script to calculate referral earnings based on the number of referrals and the token purchase amount during the $UNSD presale.
Generated: DETERMINISTIC_78b1af862ba492ea
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate referral earnings based on the number of referrals 
# and the token purchase amount during the $UNSD presale.

# Import necessary modules
import sys

def calculate_referral_earnings(referrals, token_purchase_amount, referral_rate=0.05):
    """
    Calculate the referral earnings based on the number of referrals,
    token purchase amount, and referral rate.

    Args:
        referrals (int): Number of referrals made.
        token_purchase_amount (float): Total amount of tokens purchased in USD.
        referral_rate (float): Percentage of token purchase amount awarded as referral earnings. Default is 5% (0.05).

    Returns:
        float: Total referral earnings in USD.
    """
    try:
        # Validate inputs
        if referrals < 0:
            raise ValueError("Number of referrals cannot be negative.")
        if token_purchase_amount < 0:
            raise ValueError("Token purchase amount cannot be negative.")
        if not (0 <= referral_rate <= 1):
            raise ValueError("Referral rate must be between 0 and 1.")

        # Calculate referral earnings
        total_earnings = referrals * token_purchase_amount * referral_rate
        return total_earnings

    except ValueError as ve:
        # Handle invalid input errors
        print(f"Error: {ve}")
        return None
    except Exception as e:
        # Catch-all for unexpected errors
        print(f"Unexpected error: {e}")
        return None

def main():
    """
    Main function to interact with the user and calculate referral earnings.
    """
    try:
        print("Welcome to the $UNSD Referral Earnings Calculator!")
        
        # Get user inputs
        referrals = int(input("Enter the number of referrals: "))
        token_purchase_amount = float(input("Enter the total token purchase amount (USD): "))
        referral_rate = float(input("Enter the referral rate (default is 0.05 or 5%): ") or 0.05)
        
        # Call the function to calculate earnings
        earnings = calculate_referral_earnings(referrals, token_purchase_amount, referral_rate)
        
        if earnings is not None:
            print(f"Total referral earnings: ${earnings:.2f}")
        else:
            print("Failed to calculate referral earnings due to invalid input.")
    
    except ValueError:
        print("Error: Invalid input. Please provide numeric values for referrals and token purchase amount.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Entry point of the script
    try:
        main()
    except KeyboardInterrupt:
        print("\nCalculation interrupted by user. Exiting.")
        sys.exit(0)
```
