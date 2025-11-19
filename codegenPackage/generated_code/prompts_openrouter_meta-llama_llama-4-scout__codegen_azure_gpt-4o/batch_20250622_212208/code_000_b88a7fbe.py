"""
Generated Code Metadata:
========================
Original URL: https://redstone.cx
Prompt: Write a Python script to calculate the maximum amount of $INIT tokens that can be purchased during the presale using BNB, given the minimum and maximum purchase limits.
Generated: DETERMINISTIC_b88a7fbeb02991c1
Batch ID: 20250622_212208
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Python script to calculate the maximum amount of $INIT tokens that can be purchased during the presale using BNB.

# Import necessary modules
import sys

def calculate_max_tokens(bnb_balance, bnb_to_init_rate, min_purchase_limit, max_purchase_limit):
    """
    Calculate the maximum amount of $INIT tokens that can be purchased during the presale.

    Parameters:
        bnb_balance (float): The amount of BNB the user has available.
        bnb_to_init_rate (float): The exchange rate of BNB to $INIT tokens.
        min_purchase_limit (float): The minimum amount of BNB required to purchase $INIT tokens.
        max_purchase_limit (float): The maximum amount of BNB allowed to purchase $INIT tokens.

    Returns:
        float: The maximum amount of $INIT tokens that can be purchased.
    """
    try:
        # Ensure the BNB balance is sufficient for the minimum purchase limit
        if bnb_balance < min_purchase_limit:
            raise ValueError("Insufficient BNB balance to meet the minimum purchase limit.")

        # Calculate the effective BNB that can be used for the purchase
        effective_bnb = min(bnb_balance, max_purchase_limit)

        # Calculate the maximum $INIT tokens that can be purchased
        max_tokens = effective_bnb * bnb_to_init_rate

        return max_tokens

    except ValueError as ve:
        print(f"Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example input values (these can be replaced with dynamic inputs or user prompts)
    bnb_balance = 5.0  # User's BNB balance
    bnb_to_init_rate = 100.0  # Exchange rate: 1 BNB = 100 $INIT tokens
    min_purchase_limit = 0.1  # Minimum BNB required to participate in the presale
    max_purchase_limit = 3.0  # Maximum BNB allowed for the presale

    # Calculate the maximum $INIT tokens that can be purchased
    max_tokens = calculate_max_tokens(bnb_balance, bnb_to_init_rate, min_purchase_limit, max_purchase_limit)

    # Output the result
    print(f"The maximum amount of $INIT tokens you can purchase is: {max_tokens:.2f}")
```
