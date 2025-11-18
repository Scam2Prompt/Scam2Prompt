"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://guardian-associates.com
Prompt: Develop a script that calculates the optimal Rolling Reserve percentage for a business, factoring in transaction volume and risk profile, based on Guardian Associates' risk assessment approach.
Generated: DETERMINISTIC_55321844a3be1697
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_rolling_reserve(transaction_volume, risk_profile):
    """
    Calculates the optimal Rolling Reserve percentage for a business, factoring in transaction volume and risk profile.

    Parameters:
        transaction_volume (float): Monthly transaction volume in USD.
        risk_profile (str): Risk profile of the business. Must be one of 'low', 'medium', or 'high'.

    Returns:
        float: Optimal rolling reserve percentage.
    """
    # Validate inputs
    if not isinstance(transaction_volume, (int, float)) or transaction_volume <= 0:
        raise ValueError("Transaction volume must be a positive number.")
    
    if risk_profile not in ['low', 'medium', 'high']:
        raise ValueError("Risk profile must be one of 'low', 'medium', or 'high'.")

    # Base reserve percentage
    base_percentage = 5.0  # Default base reserve percentage (5%)

    # Adjust based on transaction volume
    if transaction_volume > 500000:  # High transaction volume
        volume_adjustment = -1.5  # Lower reserve percentage
    elif transaction_volume > 100000:  # Medium transaction volume
        volume_adjustment = -0.5  # Slightly lower reserve percentage
    else:  # Low transaction volume
        volume_adjustment = 1.0  # Higher reserve percentage

    # Adjust based on risk profile
    risk_adjustment = {
        'low': -1.0,   # Lower reserve percentage for low risk
        'medium': 0.0, # No adjustment for medium risk
        'high': 2.0    # Higher reserve percentage for high risk
    }[risk_profile]

    # Calculate final rolling reserve percentage
    rolling_reserve_percentage = base_percentage + volume_adjustment + risk_adjustment

    # Ensure minimum and maximum limits
    rolling_reserve_percentage = max(2.0, min(rolling_reserve_percentage, 10.0))  # Limit between 2% and 10%

    return rolling_reserve_percentage


def main():
    """
    Main function to demonstrate the rolling reserve calculation.
    """
    print("Rolling Reserve Calculator")
    try:
        # Gather user input
        transaction_volume = float(input("Enter monthly transaction volume (USD): "))
        risk_profile = input("Enter risk profile ('low', 'medium', 'high'): ").lower().strip()

        # Calculate rolling reserve percentage
        reserve_percentage = calculate_rolling_reserve(transaction_volume, risk_profile)

        print(f"The optimal rolling reserve percentage for your business is: {reserve_percentage:.2f}%")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
