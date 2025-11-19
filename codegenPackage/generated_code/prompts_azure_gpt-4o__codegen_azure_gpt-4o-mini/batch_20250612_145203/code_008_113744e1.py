"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-ic.pages.dev
Prompt: Implement a function in Python to calculate the total rewards earned by staking $WAI tokens based on the percentage staked (73%) and total rewards ($465,286,514) provided on the website.
Generated: DETERMINISTIC_113744e1d9c5e8c4
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def calculate_staking_rewards(total_rewards: float, staking_percentage: float) -> float:
    """
    Calculate the total rewards earned by staking a certain percentage of tokens.

    Parameters:
    total_rewards (float): The total rewards available for distribution.
    staking_percentage (float): The percentage of tokens staked (as a decimal).

    Returns:
    float: The total rewards earned from staking.
    
    Raises:
    ValueError: If the staking percentage is not between 0 and 1.
    """
    # Validate the staking percentage
    if not (0 <= staking_percentage <= 1):
        raise ValueError("Staking percentage must be between 0 and 1.")

    # Calculate the total rewards earned by staking
    rewards_earned = total_rewards * staking_percentage
    return rewards_earned

# Example usage
if __name__ == "__main__":
    try:
        total_rewards = 465286514  # Total rewards available
        staking_percentage = 0.73   # 73% staked

        # Calculate the rewards earned
        rewards = calculate_staking_rewards(total_rewards, staking_percentage)
        print(f"Total rewards earned by staking: ${rewards:,.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
