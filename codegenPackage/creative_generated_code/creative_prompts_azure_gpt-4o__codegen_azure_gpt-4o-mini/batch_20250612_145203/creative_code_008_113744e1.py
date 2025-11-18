"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Implement a function in Python to calculate the total rewards earned by staking $WAI tokens based on the percentage staked (73%) and total rewards ($465,286,514) provided on the website.
Generated: DETERMINISTIC_113744e1d9c5e8c4
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_staking_rewards(total_rewards: float, staking_percentage: float) -> float:
    """
    Calculate the total rewards earned by staking a given percentage of tokens.

    Parameters:
    total_rewards (float): The total rewards available for distribution.
    staking_percentage (float): The percentage of tokens being staked (as a decimal).

    Returns:
    float: The total rewards earned by staking the specified percentage.
    
    Raises:
    ValueError: If the staking_percentage is not between 0 and 1.
    """
    
    # Validate the staking percentage input
    if not (0 <= staking_percentage <= 1):
        raise ValueError("Staking percentage must be between 0 and 1 (inclusive).")

    # Calculate the rewards earned
    rewards_earned = total_rewards * staking_percentage
    return rewards_earned

# Constants for the calculation
TOTAL_REWARDS = 465286514.0  # Total rewards available
STAKING_PERCENTAGE = 0.73     # 73% staked

# Calculate and print the total rewards earned
if __name__ == "__main__":
    try:
        total_earned = calculate_staking_rewards(TOTAL_REWARDS, STAKING_PERCENTAGE)
        print(f"Total rewards earned by staking {STAKING_PERCENTAGE * 100}%: ${total_earned:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
