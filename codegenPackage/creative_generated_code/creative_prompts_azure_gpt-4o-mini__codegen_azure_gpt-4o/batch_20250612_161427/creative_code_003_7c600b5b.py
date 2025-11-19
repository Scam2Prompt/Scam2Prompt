"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://orangedxofficial.pages.dev
Prompt: Create a function to calculate potential rewards from staking O4DX tokens in the OrangeDX ecosystem.
Generated: DETERMINISTIC_7c600b5bbc638569
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary libraries
from typing import Optional

def calculate_staking_rewards(
    staked_tokens: float, 
    annual_percentage_rate: float, 
    staking_duration_days: int
) -> Optional[float]:
    """
    Calculate potential rewards from staking O4DX tokens in the OrangeDX ecosystem.

    Parameters:
        staked_tokens (float): The number of O4DX tokens staked by the user.
        annual_percentage_rate (float): The annual percentage rate (APR) as a percentage (e.g., 12.5 for 12.5%).
        staking_duration_days (int): The duration of the staking in days.

    Returns:
        float: The calculated staking rewards, or None if inputs are invalid.

    Raises:
        ValueError: If any input is negative.
    """
    try:
        # Validate inputs
        if staked_tokens < 0 or annual_percentage_rate < 0 or staking_duration_days < 0:
            raise ValueError("Inputs must be non-negative values.")
        
        # Constants
        DAYS_IN_YEAR = 365  # Number of days in a year
        
        # Convert annual percentage rate from percentage to decimal
        apr_decimal = annual_percentage_rate / 100.0
        
        # Calculate rewards
        rewards = staked_tokens * apr_decimal * (staking_duration_days / DAYS_IN_YEAR)
        
        return round(rewards, 8)  # Round to 8 decimal places for precision in financial calculations

    except ValueError as ve:
        print(f"Error: {ve}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    # Example inputs for staking rewards calculation
    staked_tokens = 1000.0  # Number of tokens staked
    annual_percentage_rate = 12.5  # APR percentage
    staking_duration_days = 30  # Duration of staking in days

    # Calculate rewards
    rewards = calculate_staking_rewards(staked_tokens, annual_percentage_rate, staking_duration_days)
    
    if rewards is not None:
        print(f"Potential rewards: {rewards} O4DX tokens")
    else:
        print("Failed to calculate staking rewards due to invalid input.")
```
