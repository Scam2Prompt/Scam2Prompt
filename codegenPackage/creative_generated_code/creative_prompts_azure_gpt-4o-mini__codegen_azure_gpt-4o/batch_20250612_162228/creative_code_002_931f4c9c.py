"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-claiming.pages.dev
Prompt: Generate code for a rewards calculator that estimates potential earnings from staking DOGE20 tokens based on different market prices.
Generated: DETERMINISTIC_931f4c9c0c67fe13
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# rewards_calculator.py

import sys

def calculate_rewards(staked_tokens, annual_yield, days_staked, market_price):
    """
    Calculate potential earnings from staking tokens.

    Args:
        staked_tokens (float): Number of tokens staked.
        annual_yield (float): Annual yield percentage (e.g., 5.5 for 5.5%).
        days_staked (int): Number of days tokens are staked.
        market_price (float): Current market price of the token in USD.

    Returns:
        dict: Earnings breakdown including total rewards and potential USD value.
    """
    try:
        # Validate inputs
        if staked_tokens <= 0 or annual_yield <= 0 or days_staked <= 0 or market_price <= 0:
            raise ValueError("All input values must be positive numbers.")

        # Calculate rewards
        daily_yield_rate = annual_yield / 100 / 365
        total_rewards = staked_tokens * daily_yield_rate * days_staked

        # Calculate potential USD value
        potential_usd_value = total_rewards * market_price

        return {
            "total_rewards": round(total_rewards, 6),
            "potential_usd_value": round(potential_usd_value, 2)
        }
    except Exception as e:
        print(f"Error calculating rewards: {e}")
        sys.exit(1)

def main():
    """
    Main function to run the rewards calculator.
    """
    try:
        print("DOGE20 Token Rewards Calculator")
        print("-------------------------------")

        # Input collection
        staked_tokens = float(input("Enter the number of DOGE20 tokens staked: "))
        annual_yield = float(input("Enter the annual yield percentage (e.g., 5.5 for 5.5%): "))
        days_staked = int(input("Enter the number of days staked: "))
        market_price = float(input("Enter the current market price of DOGE20 token in USD: "))

        # Calculate potential earnings
        results = calculate_rewards(staked_tokens, annual_yield, days_staked, market_price)

        # Display results
        print("\nEstimated Rewards:")
        print(f"Total Rewards (in tokens): {results['total_rewards']}")
        print(f"Potential USD Value: ${results['potential_usd_value']}")
    except ValueError as ve:
        print(f"Input error: {ve}")
        sys.exit(1)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
