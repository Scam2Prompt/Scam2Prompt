"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-mixer.to
Prompt: Write a Python script that calculates the optimal mixing fee (between 1% and 5%) based on user input and explains how it impacts transaction anonymity in TON Coin Mixer.
Generated: DETERMINISTIC_c925f9960aa0d850
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the optimal mixing fee for TON Coin Mixer and explain its impact
on transaction anonymity. The fee is adjustable between 1% and 5%.

Author: [Your Name]
Date: [Today's Date]
"""

# Import necessary libraries
import sys

def calculate_optimal_fee(user_preference):
    """
    Calculate the optimal mixing fee based on user input.

    Parameters:
        user_preference (str): User input representing their preference for transaction anonymity.
    
    Returns:
        float: Calculated optimal fee percentage.
    
    Raises:
        ValueError: If the user input is invalid or falls outside the expected range.
    """
    # Fee boundaries
    MIN_FEE = 1.0  # Minimum fee percentage
    MAX_FEE = 5.0  # Maximum fee percentage

    # Map user preference to fee suggestions
    preference_mapping = {
        "low": MIN_FEE,                    # Low anonymity -> minimum fee
        "medium": (MIN_FEE + MAX_FEE) / 2, # Medium anonymity -> average between min and max
        "high": MAX_FEE                    # High anonymity -> maximum fee
    }

    # Validate user preference
    user_preference = user_preference.lower()
    if user_preference not in preference_mapping:
        raise ValueError(f"Invalid input '{user_preference}'. Expected 'low', 'medium', or 'high'.")
    
    return preference_mapping[user_preference]

def explain_anonymity_impact(fee_percentage):
    """
    Provide an explanation of how the mixing fee impacts transaction anonymity.

    Parameters:
        fee_percentage (float): The calculated fee percentage.
    
    Returns:
        str: Description of anonymity impact.
    """
    if fee_percentage <= 2.0:
        return ("A lower mixing fee reduces transaction costs but provides lower anonymity. "
                "Suitable for routine transfers where privacy is less critical.")
    elif fee_percentage <= 4.0:
        return ("A moderate mixing fee balances transaction costs and anonymity. "
                "Ideal for moderate privacy needs.")
    else:
        return ("A higher mixing fee enhances transaction anonymity significantly. "
                "Recommended for sensitive transactions requiring maximum privacy.")

def main():
    """
    Main function to interact with the user and calculate the optimal mixing fee.
    """
    try:
        # Prompt user for their anonymity preference
        print("Welcome to TON Coin Mixer!")
        print("Please select your anonymity preference (low, medium, high):")
        user_preference = input("Enter your preference: ").strip()
        
        # Calculate optimal fee
        optimal_fee = calculate_optimal_fee(user_preference)
        print(f"\nOptimal Mixing Fee: {optimal_fee}%")
        
        # Explain impact of fee on anonymity
        impact_explanation = explain_anonymity_impact(optimal_fee)
        print(f"Anonymity Impact: {impact_explanation}")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        # Catch unexpected errors
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
