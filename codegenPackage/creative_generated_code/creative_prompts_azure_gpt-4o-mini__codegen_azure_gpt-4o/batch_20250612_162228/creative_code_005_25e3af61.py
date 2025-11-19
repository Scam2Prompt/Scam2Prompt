"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inqubeta-presales.pages.dev
Prompt: Create a function that calculates potential rewards from staking $QUBE tokens based on the current sell tax structure.
Generated: DETERMINISTIC_25e3af61668d5d27
Batch ID: 20250612_162228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
This script defines a function to calculate potential rewards from staking $QUBE tokens.
It takes into account the current sell tax structure to determine rewards.
"""

def calculate_staking_rewards(staked_tokens: float, annual_percentage_yield: float, sell_tax: float, duration_days: int) -> float:
    """
    Calculate potential staking rewards for $QUBE tokens.

    Parameters:
        staked_tokens (float): The amount of $QUBE tokens staked.
        annual_percentage_yield (float): The annual percentage yield (APY) offered for staking in percentage terms.
        sell_tax (float): The sell tax percentage that affects the rewards.
        duration_days (int): The staking duration (in days).

    Returns:
        float: The net rewards after considering the sell tax.
    """
    try:
        # Validate input parameters
        if staked_tokens <= 0:
            raise ValueError("Staked tokens must be greater than 0.")
        if annual_percentage_yield <= 0 or annual_percentage_yield > 100:
            raise ValueError("Annual percentage yield must be between 0 and 100.")
        if sell_tax < 0 or sell_tax > 100:
            raise ValueError("Sell tax must be between 0 and 100.")
        if duration_days <= 0:
            raise ValueError("Duration days must be greater than 0.")
        
        # Calculate rewards before tax
        daily_yield = annual_percentage_yield / 100 / 365  # Convert APY to daily yield as a fraction
        gross_rewards = staked_tokens * daily_yield * duration_days  # Rewards without tax

        # Apply sell tax to the rewards
        net_rewards = gross_rewards * (1 - sell_tax / 100)

        return net_rewards

    except ValueError as ve:
        # Handle invalid input values
        print(f"Input Error: {ve}")
        return 0.0
    except Exception as e:
        # Catch all other exceptions for robustness
        print(f"An unexpected error occurred: {e}")
        return 0.0


# Example usage:
if __name__ == "__main__":
    # Parameters: staked_tokens, APY, sell_tax, duration_days
    staked_tokens = 1000.0  # Number of $QUBE tokens staked
    annual_percentage_yield = 12.0  # APY in percentage
    sell_tax = 5.0  # Sell tax in percentage
    duration_days = 30  # Duration in days

    rewards = calculate_staking_rewards(staked_tokens, annual_percentage_yield, sell_tax, duration_days)
    print(f"Potential rewards after {duration_days} days: {rewards:.2f} $QUBE tokens")
```
