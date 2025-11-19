"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mike-token-web-olj7orfr7-percenal-miketoken.vercel.app
Prompt: Write a function that calculates potential rewards from staking in Mike Token's farming pools based on the tokenomics provided.
Generated: DETERMINISTIC_dff19569bf95a58c
Batch ID: 20250612_163526
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# File: staking_rewards_calculator.py

def calculate_staking_rewards(amount_staked, annual_percentage_yield, days_staked):
    """
    Calculate potential rewards from staking in Mike Token's farming pools.

    Parameters:
        amount_staked (float): The amount of Mike Token staked (in tokens).
        annual_percentage_yield (float): The annual percentage yield (APY) in percentage (e.g., 12.5 for 12.5% APY).
        days_staked (int): The number of days the tokens have been staked.

    Returns:
        float: The potential reward earned in Mike Tokens.
    """
    try:
        # Validate input types
        if not isinstance(amount_staked, (int, float)) or amount_staked < 0:
            raise ValueError("amount_staked must be a positive number.")
        if not isinstance(annual_percentage_yield, (int, float)) or annual_percentage_yield < 0:
            raise ValueError("annual_percentage_yield must be a positive number.")
        if not isinstance(days_staked, int) or days_staked < 0:
            raise ValueError("days_staked must be a positive integer.")

        # Convert APY from percentage to decimal for calculation
        apy_decimal = annual_percentage_yield / 100

        # Calculate rewards based on APY and staking duration
        rewards = amount_staked * apy_decimal * (days_staked / 365)

        return round(rewards, 6)  # Round to 6 decimal places for precision
    except Exception as e:
        # Handle errors and provide meaningful messages
        print(f"Error calculating staking rewards: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # User inputs
    try:
        amount_staked = float(input("Enter the amount of Mike Tokens staked: "))
        annual_percentage_yield = float(input("Enter the annual percentage yield (APY) as a percentage: "))
        days_staked = int(input("Enter the number of days staked: "))

        # Calculate rewards
        rewards = calculate_staking_rewards(amount_staked, annual_percentage_yield, days_staked)
        print(f"Potential Rewards: {rewards} Mike Tokens")
    except Exception as e:
        print(f"Error: {e}")
```
