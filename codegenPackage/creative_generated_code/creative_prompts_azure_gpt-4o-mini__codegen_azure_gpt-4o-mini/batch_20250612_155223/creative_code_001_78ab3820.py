"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blockchainbets-app.pages.dev
Prompt: Write a code snippet to calculate the potential staking rewards in $ETH and $USDT based on the amount of $BCB tokens staked for 30 days.
Generated: DETERMINISTIC_78ab3820cdb44126
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal

class StakingCalculator:
    """
    A class to calculate potential staking rewards for $ETH and $USDT based on 
    the amount of $BCB tokens staked over a period of 30 days.
    """
    
    def __init__(self, bcb_staked, eth_reward_rate, usdt_reward_rate):
        """
        Initializes the StakingCalculator with the amount of $BCB tokens staked 
        and the respective reward rates for $ETH and $USDT.
        
        Parameters:
            bcb_staked (float): Amount of $BCB tokens staked.
            eth_reward_rate (float): Daily reward rate for $ETH as a percentage.
            usdt_reward_rate (float): Daily reward rate for $USDT as a percentage.
        """
        self.bcb_staked = decimal.Decimal(bcb_staked)
        self.eth_reward_rate = decimal.Decimal(eth_reward_rate) / 100  # Convert to decimal
        self.usdt_reward_rate = decimal.Decimal(usdt_reward_rate) / 100  # Convert to decimal
    
    def calculate_rewards(self):
        """
        Calculates the potential staking rewards in $ETH and $USDT for 30 days.

        Returns:
            tuple: A tuple containing the potential rewards in $ETH and $USDT.
        """
        try:
            # Calculate rewards for 30 days
            eth_rewards = self.bcb_staked * self.eth_reward_rate * 30
            usdt_rewards = self.bcb_staked * self.usdt_reward_rate * 30
            
            return eth_rewards, usdt_rewards
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")
            return None, None

if __name__ == "__main__":
    # Example parameters
    bcb_staked_amount = 1000  # Amount of $BCB staked
    eth_daily_reward_rate = 0.05  # Daily reward rate for $ETH in percentage
    usdt_daily_reward_rate = 0.03  # Daily reward rate for $USDT in percentage

    # Initialize the staking calculator
    staking_calculator = StakingCalculator(bcb_staked_amount, eth_daily_reward_rate, usdt_daily_reward_rate)

    # Calculate the potential rewards
    eth_rewards, usdt_rewards = staking_calculator.calculate_rewards()

    # Print the results
    if eth_rewards is not None and usdt_rewards is not None:
        print(f"Potential Rewards for staking {bcb_staked_amount} $BCB tokens for 30 days:")
        print(f"- $ETH Rewards: {eth_rewards:.4f} ETH")
        print(f"- $USDT Rewards: {usdt_rewards:.4f} USDT")
```
