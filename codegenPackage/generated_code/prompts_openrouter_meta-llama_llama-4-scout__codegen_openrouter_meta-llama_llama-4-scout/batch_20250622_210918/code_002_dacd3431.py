"""
Generated Code Metadata:
========================
Original URL: https://app-bitcoinminetrix.pages.dev
Prompt: Design a function to calculate the mining credits earned by staking a certain amount of BTCMTX tokens, considering the tokenomics and staking rewards.
Generated: DETERMINISTIC_dacd343133143bef
Batch ID: 20250622_210918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import Dict

def calculate_mining_credits(stake_amount: float, tokenomics: Dict[str, float], staking_rewards: Dict[str, float]) -> float:
    """
    Calculate the mining credits earned by staking a certain amount of BTCMTX tokens.

    Args:
    - stake_amount (float): The amount of BTCMTX tokens staked.
    - tokenomics (Dict[str, float]): A dictionary containing tokenomics information.
        - 'total_supply' (float): The total supply of BTCMTX tokens.
        - 'circulating_supply' (float): The circulating supply of BTCMTX tokens.
    - staking_rewards (Dict[str, float]): A dictionary containing staking rewards information.
        - 'reward_rate' (float): The reward rate for staking BTCMTX tokens.
        - 'min_stake_amount' (float): The minimum stake amount required.

    Returns:
    - float: The mining credits earned.

    Raises:
    - ValueError: If the stake amount is less than the minimum stake amount.
    - KeyError: If required keys are missing from tokenomics or staking_rewards.
    """

    # Check if required keys exist in tokenomics and staking_rewards
    required_tokenomics_keys = ['total_supply', 'circulating_supply']
    required_staking_rewards_keys = ['reward_rate', 'min_stake_amount']

    if not all(key in tokenomics for key in required_tokenomics_keys):
        raise KeyError("Tokenomics dictionary is missing required keys.")
    if not all(key in staking_rewards for key in required_staking_rewards_keys):
        raise KeyError("Staking rewards dictionary is missing required keys.")

    # Check if stake amount is valid
    if stake_amount < staking_rewards['min_stake_amount']:
        raise ValueError("Stake amount must be greater than or equal to the minimum stake amount.")

    # Calculate the mining credits earned
    try:
        reward_rate = staking_rewards['reward_rate']
        mining_credits = stake_amount * reward_rate / tokenomics['total_supply'] * tokenomics['circulating_supply']
        return mining_credits
    except ZeroDivisionError:
        raise ValueError("Total supply cannot be zero.")

def main():
    tokenomics = {
        'total_supply': 1000000.0,
        'circulating_supply': 500000.0
    }

    staking_rewards = {
        'reward_rate': 0.1,
        'min_stake_amount': 100.0
    }

    stake_amount = 1000.0

    try:
        mining_credits = calculate_mining_credits(stake_amount, tokenomics, staking_rewards)
        print(f"The mining credits earned are: {mining_credits}")
    except (ValueError, KeyError) as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
