"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kaketosdelano.ru
Prompt: Create a function that calculates potential earnings from staking tokens on the Beethoven X platform.
Generated: DETERMINISTIC_18c9d563637a1494
Batch ID: 20250612_161317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import requests

def calculate_staking_earnings(token_amount, token_price, annual_percentage_yield, staking_duration_days):
    """
    Calculate potential earnings from staking tokens.

    :param token_amount: Amount of tokens staked (float).
    :param token_price: Price of the token in USD (float).
    :param annual_percentage_yield: Annual percentage yield (APY) in decimal form (e.g., 0.10 for 10%) (float).
    :param staking_duration_days: Duration of staking in days (int).
    :return: Dictionary containing earnings breakdown and total value accrued during staking (dict).
    """
    try:
        # Validate inputs
        if token_amount <= 0 or token_price <= 0 or annual_percentage_yield < 0 or staking_duration_days <= 0:
            raise ValueError("All inputs must be positive numbers, and APY should not be negative.")

        # Convert staking duration from days to years for APY calculation
        staking_duration_years = staking_duration_days / 365.0

        # Calculate earnings from staking
        staking_earnings_usd = token_amount * token_price * annual_percentage_yield * staking_duration_years

        # Total value after staking (original token value + earnings)
        total_value_usd = (token_amount * token_price) + staking_earnings_usd

        return {
            "staking_earnings_usd": round(staking_earnings_usd, 2),
            "total_value_usd": round(total_value_usd, 2)
        }
    except ValueError as e:
        print(f"Input Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


# Example usage
if __name__ == "__main__":
    # Replace with actual input values
    token_amount = 1000  # Amount of tokens
    token_price = 2.5  # Price of each token in USD
    annual_percentage_yield = 0.15  # APY (15%)
    staking_duration_days = 90  # Duration in days

    earnings = calculate_staking_earnings(
        token_amount=token_amount,
        token_price=token_price,
        annual_percentage_yield=annual_percentage_yield,
        staking_duration_days=staking_duration_days
    )

    if earnings:
        print("Staking Earnings:")
        print(f"Earnings (USD): ${earnings['staking_earnings_usd']}")
        print(f"Total Value after Staking (USD): ${earnings['total_value_usd']}")
```
