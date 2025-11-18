"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scapemania-0x2eca5.pages.dev
Prompt: Develop a function that calculates the bonus percentage for referrals based on the purchase amount of $MANIA tokens, using the tiered bonus system (5% to 15%).
Generated: DETERMINISTIC_d871ecb64d080501
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_referral_bonus(purchase_amount):
    """
    Calculates the referral bonus percentage based on a tiered system.

    :param purchase_amount: float, the amount of $MANIA tokens purchased.
    :return: float, the bonus percentage.
    """
    try:
        # Ensure the input is valid
        if not isinstance(purchase_amount, (int, float)) or purchase_amount < 0:
            raise ValueError("Invalid purchase amount. It must be a positive number.")

        # Tiered bonus system based on purchase amount
        if purchase_amount < 100:
            bonus_percentage = 5.0  # Tier 1: 5% for purchases below 100 $MANIA tokens
        elif 100 <= purchase_amount < 500:
            bonus_percentage = 10.0  # Tier 2: 10% for purchases between 100 and 499 $MANIA tokens
        else:
            bonus_percentage = 15.0  # Tier 3: 15% for purchases of 500 or more $MANIA tokens

        return bonus_percentage

    except ValueError as ve:
        # Handle invalid input
        print(f"Error: {ve}")
        return 0.0  # Return a default bonus percentage in case of error
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return 0.0  # Return a default bonus percentage in case of error


# Example usage:
# Uncomment the following lines to test the function.
# purchase_amount = 250
# bonus = calculate_referral_bonus(purchase_amount)
# print(f"For a purchase of {purchase_amount} $MANIA tokens, the bonus is {bonus}%")
```
