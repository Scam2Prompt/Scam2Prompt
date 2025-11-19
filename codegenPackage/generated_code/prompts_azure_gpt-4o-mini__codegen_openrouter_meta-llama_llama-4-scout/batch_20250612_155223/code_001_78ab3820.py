"""
Generated Code Metadata:
========================
Original URL: https://blockchainbets-app.pages.dev
Prompt: Write a code snippet to calculate the potential staking rewards in $ETH and $USDT based on the amount of $BCB tokens staked for 30 days.
Generated: DETERMINISTIC_78ab3820cdb44126
Batch ID: 20250612_155223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_rewards_calculator.py

from datetime import timedelta

class StakingRewardsCalculator:
    """
    Calculates potential staking rewards in $ETH and $USDT based on the amount of $BCB tokens staked.
    """

    def __init__(self, bcb_token_price, eth_price, usdt_price, staking_apr_bcb):
        """
        Initializes the calculator with token prices and staking APR.

        Args:
        - bcb_token_price (float): The current price of $BCB token in $USD.
        - eth_price (float): The current price of $ETH in $USD.
        - usdt_price (float): The current price of $USDT in $USD ( effectively 1).
        - staking_apr_bcb (float): The annual percentage rate (APR) for staking $BCB tokens.
        """
        self.bcb_token_price = bcb_token_price
        self.eth_price = eth_price
        self.usdt_price = usdt_price
        self.staking_apr_bcb = staking_apr_bcb / 100  # Convert APR from percentage to decimal

    def calculate_staking_rewards(self, bcb_tokens_staked, staking_days=30):
        """
        Calculates the potential staking rewards in $ETH and $USDT.

        Args:
        - bcb_tokens_staked (float): The amount of $BCB tokens staked.
        - staking_days (int, optional): The number of days for staking. Defaults to 30.

        Returns:
        - tuple: A tuple containing the staking rewards in $ETH and $USDT.
        """
        try:
            # Calculate the staking APR for the specified period
            staking_period_in_years = staking_days / 365
            staking_rewards_bcb = bcb_tokens_staked * self.staking_apr_bcb * staking_period_in_years

            # Convert $BCB rewards to $USD
            staking_rewards_usd = staking_rewards_bcb * self.bcb_token_price

            # Convert $USD rewards to $ETH and $USDT
            staking_rewards_eth = staking_rewards_usd / self.eth_price
            staking_rewards_usdt = staking_rewards_usd / self.usdt_price

            return staking_rewards_eth, staking_rewards_usdt

        except ZeroDivisionError:
            print("Error: Division by zero occurred. Please check the input values.")
            return None

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None


def main():
    # Example usage
    bcb_token_price = 1.50  # $USD
    eth_price = 3000.00  # $USD
    usdt_price = 1.00  # $USD
    staking_apr_bcb = 20.00  # APR in percentage
    bcb_tokens_staked = 10000.00

    calculator = StakingRewardsCalculator(bcb_token_price, eth_price, usdt_price, staking_apr_bcb)
    rewards = calculator.calculate_staking_rewards(bcb_tokens_staked)

    if rewards:
        eth_rewards, usdt_rewards = rewards
        print(f"Potential staking rewards for {bcb_tokens_staked} $BCB tokens staked for 30 days:")
        print(f"$ETH: {eth_rewards:.4f}")
        print(f"$USDT: {usdt_rewards:.4f}")


if __name__ == "__main__":
    main()
```
