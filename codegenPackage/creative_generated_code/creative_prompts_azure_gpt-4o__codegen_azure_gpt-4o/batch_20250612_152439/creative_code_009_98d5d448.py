"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://synthr.pages.dev
Prompt: Generate code to calculate APR for liquidity providers on SYNTHR's platform, incorporating rewards from staking SYNTH and farming syASSET/ASSET LP tokens.
Generated: DETERMINISTIC_98d5d448d270d8a8
Batch ID: 20250612_152439
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

def calculate_apr(staking_rewards, farming_rewards, staked_tokens_value, lp_tokens_value):
    """
    Calculate the Annual Percentage Rate (APR) for liquidity providers on SYNTHR's platform.
    
    Parameters:
        staking_rewards (float): Total annual rewards from staking SYNTH tokens (in USD).
        farming_rewards (float): Total annual rewards from farming syASSET/ASSET LP tokens (in USD).
        staked_tokens_value (float): Total value of SYNTH tokens staked (in USD).
        lp_tokens_value (float): Total value of syASSET/ASSET LP tokens provided (in USD).
    
    Returns:
        float: The combined APR for staking and farming (expressed as a percentage).
    """
    
    # Validate inputs to ensure positive values
    if staked_tokens_value <= 0 or lp_tokens_value <= 0:
        raise ValueError("Staked tokens value and LP tokens value must be greater than zero.")

    # Calculate APR components
    staking_apr = (staking_rewards / staked_tokens_value) * 100  # APR for staking SYNTH
    farming_apr = (farming_rewards / lp_tokens_value) * 100      # APR for farming syASSET/ASSET LP tokens

    # Combine APR components
    combined_apr = staking_apr + farming_apr

    # Return the combined APR, rounded to two decimal places for clarity
    return round(combined_apr, 2)


# Example usage:
try:
    staking_rewards_usd = 10000  # Annual staking rewards (in USD)
    farming_rewards_usd = 15000  # Annual farming rewards (in USD)
    staked_tokens_value_usd = 50000  # Value of staked SYNTH tokens (in USD)
    lp_tokens_value_usd = 75000  # Value of syASSET/ASSET LP tokens (in USD)

    apr = calculate_apr(staking_rewards_usd, farming_rewards_usd, staked_tokens_value_usd, lp_tokens_value_usd)
    print(f"Combined APR: {apr}%")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
```

This code meets the requirements for clean, efficient, and well-documented implementation, with proper error handling for invalid inputs.
