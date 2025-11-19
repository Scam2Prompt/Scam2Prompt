"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-is.pages.dev
Prompt: Generate a code snippet for a rewards calculator that estimates potential earnings from staking DOGE20 tokens at varying prices.
Generated: DETERMINISTIC_335b719e5f3b73f9
Batch ID: 20250612_162404
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_calculator.py

# Import necessary modules
import sys

def calculate_rewards(staked_tokens, annual_percentage_rate, token_price, days_staked):
    """
    Calculate potential earnings from staking tokens.

    Parameters:
        staked_tokens (float): Number of tokens staked.
        annual_percentage_rate (float): Annual percentage rate (APR) for staking.
        token_price (float): Current price of the token in USD.
        days_staked (int): Number of days the tokens are staked.

    Returns:
        dict: A dictionary containing estimated rewards in tokens and USD.
    """
    try:
        # Validate inputs
        if staked_tokens <= 0 or annual_percentage_rate <= 0 or token_price <= 0 or days_staked <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate daily rewards rate
        daily_rate = annual_percentage_rate / 365 / 100

        # Calculate rewards in tokens
        rewards_in_tokens = staked_tokens * daily_rate * days_staked

        # Calculate rewards in USD
        rewards_in_usd = rewards_in_tokens * token_price

        return {
            "rewards_in_tokens": round(rewards_in_tokens, 4),
            "rewards_in_usd": round(rewards_in_usd, 2)
        }
    except ValueError as ve:
        print(f"Input Error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Example usage
    try:
        # User inputs
        staked_tokens = float(input("Enter the number of DOGE20 tokens staked: "))
        annual_percentage_rate = float(input("Enter the annual percentage rate (APR) for staking: "))
        token_price = float(input("Enter the current price of DOGE20 token in USD: "))
        days_staked = int(input("Enter the number of days you plan to stake: "))

        # Calculate rewards
        rewards = calculate_rewards(staked_tokens, annual_percentage_rate, token_price, days_staked)

        # Display results
        print("\nEstimated Rewards:")
        print(f"Rewards in Tokens: {rewards['rewards_in_tokens']} DOGE20")
        print(f"Rewards in USD: ${rewards['rewards_in_usd']}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
