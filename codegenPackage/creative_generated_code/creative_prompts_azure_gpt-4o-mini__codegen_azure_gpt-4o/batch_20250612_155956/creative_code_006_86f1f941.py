"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nexus-mutual.xyz
Prompt: Create a function that calculates the rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.
Generated: DETERMINISTIC_86f1f94191ae62ee
Batch ID: 20250612_155956
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

def calculate_staking_rewards(nxm_tokens, risk_level):
    """
    Calculate the rewards for members staking NXM tokens based on the risk level of smart contracts in Nexus Mutual.

    :param nxm_tokens: Decimal or float value indicating the number of NXM tokens staked.
    :param risk_level: String value indicating the risk level ("low", "medium", "high").
    :return: Decimal value indicating the calculated rewards (in NXM tokens).
    :raises ValueError: If the risk_level is invalid or nxm_tokens is negative.
    """

    # Ensure nxm_tokens is a valid number and non-negative
    if nxm_tokens < 0:
        raise ValueError("NXM tokens cannot be negative.")
    
    # Define reward multipliers based on risk level
    reward_multipliers = {
        "low": decimal.Decimal("0.05"),    # 5% rewards for low risk
        "medium": decimal.Decimal("0.10"), # 10% rewards for medium risk
        "high": decimal.Decimal("0.20")    # 20% rewards for high risk
    }

    # Validate risk level
    if risk_level not in reward_multipliers:
        raise ValueError(f"Invalid risk level: {risk_level}. Valid options are 'low', 'medium', or 'high'.")

    # Convert input to Decimal for accurate calculations
    nxm_tokens_decimal = decimal.Decimal(str(nxm_tokens))
    
    # Calculate rewards
    reward_multiplier = reward_multipliers[risk_level]
    staking_rewards = nxm_tokens_decimal * reward_multiplier

    return staking_rewards

# Example usage
if __name__ == "__main__":
    try:
        # Inputs
        staked_tokens = 1000.0
        risk = "medium"
        
        # Calculate rewards
        rewards = calculate_staking_rewards(staked_tokens, risk)
        print(f"Rewards for staking {staked_tokens} NXM tokens at {risk} risk level: {rewards} NXM tokens")
    
    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
```
