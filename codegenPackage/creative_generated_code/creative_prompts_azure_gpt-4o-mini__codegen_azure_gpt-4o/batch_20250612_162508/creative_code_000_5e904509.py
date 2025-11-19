"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cedefi-mantanetwork.pages.dev
Prompt: Write a code snippet to calculate the Total Value Locked (TVL) for Manta CeDeFi using BTC, ETH, USDT, and USDC contributions.
Generated: DETERMINISTIC_5e904509520d6c98
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
# Decimal is used to handle high precision calculations for financial operations
from decimal import Decimal

def calculate_tvl(contributions):
    """
    Calculate the Total Value Locked (TVL) for Manta CeDeFi.

    Parameters:
        contributions (dict): A dictionary containing the token contributions.
                              Expected keys are 'BTC', 'ETH', 'USDT', and 'USDC',
                              and values are dictionaries with 'amount' and 'price'.

                              Example:
                              {
                                  "BTC": {"amount": Decimal('0.5'), "price": Decimal('30000')},
                                  "ETH": {"amount": Decimal('10'), "price": Decimal('2000')},
                                  "USDT": {"amount": Decimal('5000'), "price": Decimal('1')},
                                  "USDC": {"amount": Decimal('3000'), "price": Decimal('1')}
                              }

    Returns:
        Decimal: The Total Value Locked (TVL) calculated as the sum of all token
                 contributions (amount * price).
    """
    try:
        tvl = Decimal('0')  # Initialize TVL to zero

        # Iterate through the contributions dictionary to calculate TVL
        for token, details in contributions.items():
            # Validate that the required fields are present
            if 'amount' not in details or 'price' not in details:
                raise ValueError(f"Missing 'amount' or 'price' for token: {token}")

            # Calculate the value locked for this token and add it to the total TVL
            tvl += details['amount'] * details['price']

        return tvl

    except Exception as e:
        # Handle any unexpected errors
        print(f"Error calculating TVL: {e}")
        return Decimal('0')  # Return zero as fallback in case of error

# Example usage
if __name__ == "__main__":
    # Example data for BTC, ETH, USDT, and USDC contributions
    contributions_data = {
        "BTC": {"amount": Decimal('0.5'), "price": Decimal('30000')},
        "ETH": {"amount": Decimal('10'), "price": Decimal('2000')},
        "USDT": {"amount": Decimal('5000'), "price": Decimal('1')},
        "USDC": {"amount": Decimal('3000'), "price": Decimal('1')}
    }

    # Calculate TVL
    total_value_locked = calculate_tvl(contributions_data)

    # Print the result
    print(f"Total Value Locked (TVL): ${total_value_locked}")
```
