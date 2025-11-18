"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bananagunn.io
Prompt: Develop a script to extrapolate APR over different time ranges for reward calculation, incorporating both EVM and Solana reward mechanisms.
Generated: DETERMINISTIC_3e2e12f3324fc6e2
Batch ID: 20250612_151931
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

# Constants for reward calculation (adjust as needed for your implementation)
SOLANA_REWARD_RATE = 0.05  # Example annual percentage rate for Solana
EVM_REWARD_RATE = 0.03    # Example annual percentage rate for EVM

def extrapolate_apr(reward_rate, periods, period_length_in_days):
    """
    Extrapolate APR over different time ranges.
    
    Args:
        reward_rate (float): Annual percentage rate (APR) as a decimal (e.g., 0.05 for 5%).
        periods (int): Number of periods to calculate rewards for.
        period_length_in_days (int): Length of each period in days.
    
    Returns:
        list: List of projected rewards for each period.
    """
    try:
        # Validate inputs
        if reward_rate <= 0 or periods <= 0 or period_length_in_days <= 0:
            raise ValueError("All input values must be positive.")
        
        # Calculate daily reward rate
        daily_rate = reward_rate / 365
        
        # Calculate rewards for each period
        rewards = []
        for period in range(1, periods + 1):
            reward = (1 + daily_rate) ** (period * period_length_in_days) - 1
            rewards.append(reward)
        
        return rewards
    except Exception as e:
        print(f"Error in extrapolate_apr: {e}")
        return []

def calculate_rewards(chain, periods, period_length_in_days):
    """
    Calculate rewards based on the blockchain mechanism.
    
    Args:
        chain (str): Blockchain type, either "solana" or "evm".
        periods (int): Number of periods to calculate rewards for.
        period_length_in_days (int): Length of each period in days.
    
    Returns:
        list: List of rewards for each period.
    """
    try:
        if chain.lower() == "solana":
            reward_rate = SOLANA_REWARD_RATE
        elif chain.lower() == "evm":
            reward_rate = EVM_REWARD_RATE
        else:
            raise ValueError("Unsupported blockchain type.")
        
        return extrapolate_apr(reward_rate, periods, period_length_in_days)
    except Exception as e:
        print(f"Error in calculate_rewards: {e}")
        return []

# Example usage
if __name__ == "__main__":
    try:
        chain_type = "solana"  # Change to "evm" for EVM rewards
        periods = 12          # Number of months
        period_length = 30    # Length of each period in days (approximate for monthly)
        
        rewards = calculate_rewards(chain_type, periods, period_length)
        if rewards:
            print(f"Projected rewards for {chain_type.capitalize()} over {periods} periods:")
            for i, reward in enumerate(rewards, start=1):
                print(f"Period {i}: {reward:.6f}")
    except Exception as e:
        print(f"Error in script execution: {e}")
```
