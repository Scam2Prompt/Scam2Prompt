"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-ae.pages.dev
Prompt: Generate a code snippet that calculates potential rewards for staking $GBTC tokens based on the current staking percentage and annual rewards.
Generated: DETERMINISTIC_e5e94164eabda954
Batch ID: 20250612_135343
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_staking_rewards(staked_tokens, staking_percentage, annual_rewards_percentage):
    """
    Calculate potential rewards for staking tokens.

    :param staked_tokens: float - Amount of $GBTC tokens staked by the user.
    :param staking_percentage: float - User staking percentage (as a fraction, e.g., 0.05 for 5%).
    :param annual_rewards_percentage: float - Annual rewards percentage (as a fraction, e.g., 0.1 for 10%).
    :return: float - Potential annual rewards based on staking.
    """
    try:
        # Input validation
        if staked_tokens < 0:
            raise ValueError("Staked tokens must be a non-negative value.")
        if not (0 <= staking_percentage <= 1):
            raise ValueError("Staking percentage must be between 0 and 1.")
        if not (0 <= annual_rewards_percentage <= 1):
            raise ValueError("Annual rewards percentage must be between 0 and 1.")

        # Calculate the rewards
        total_rewards = staked_tokens * staking_percentage * annual_rewards_percentage
        return total_rewards
    except Exception as e:
        print(f"An error occurred: {e}", file=sys.stderr)
        return None

# Example usage
if __name__ == "__main__":
    try:
        # Input parameters (these values can be replaced with user input or dynamic data)
        staked_tokens = 1000.0  # User's staked $GBTC tokens
        staking_percentage = 0.05  # 5% staking percentage
        annual_rewards_percentage = 0.1  # 10% annual rewards

        # Calculate rewards
        rewards = calculate_staking_rewards(staked_tokens, staking_percentage, annual_rewards_percentage)

        if rewards is not None:
            print(f"Potential annual staking rewards: {rewards:.2f} $GBTC tokens")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
```
