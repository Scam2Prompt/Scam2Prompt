"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rocketspool.pages.dev
Prompt: Write a script to calculate the annual percentage rate (APR) for staking ETH in Rocket Pool, incorporating both ETH and RPL rewards.
Generated: DETERMINISTIC_1659d4dccd9d327b
Batch ID: 20250612_151918
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import argparse

class StakingCalculator:
    def __init__(self, staked_eth, eth_rewards, rpl_rewards, eth_price, rpl_price):
        """
        Initialize the staking calculator with the necessary parameters.
        
        :param staked_eth: Amount of ETH staked
        :param eth_rewards: Annual ETH rewards expected
        :param rpl_rewards: Annual RPL rewards expected
        :param eth_price: Current price of ETH
        :param rpl_price: Current price of RPL
        """
        self.staked_eth = staked_eth
        self.eth_rewards = eth_rewards
        self.rpl_rewards = rpl_rewards
        self.eth_price = eth_price
        self.rpl_price = rpl_price

    def calculate_apr(self):
        """
        Calculate the Annual Percentage Rate (APR) based on ETH and RPL rewards.
        
        :return: The calculated APR as a percentage
        """
        try:
            # Calculate the total annual rewards in terms of USD
            total_rewards_usd = (self.eth_rewards * self.eth_price) + (self.rpl_rewards * self.rpl_price)
            
            # Calculate APR using the formula: (Total Rewards / Amount Staked) * 100
            apr = (total_rewards_usd / (self.staked_eth * self.eth_price)) * 100
            
            return apr
        except ZeroDivisionError:
            raise ValueError("Staked ETH or ETH price must be greater than zero to calculate APR.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating APR: {e}")

def main():
    # Set up argument parsing for command-line usage
    parser = argparse.ArgumentParser(description='Calculate the APR for staking ETH in Rocket Pool.')
    parser.add_argument('staked_eth', type=float, help='Amount of ETH staked')
    parser.add_argument('eth_rewards', type=float, help='Annual ETH rewards expected')
    parser.add_argument('rpl_rewards', type=float, help='Annual RPL rewards expected')
    parser.add_argument('eth_price', type=float, help='Current price of ETH in USD')
    parser.add_argument('rpl_price', type=float, help='Current price of RPL in USD')

    args = parser.parse_args()

    # Instantiate the staking calculator
    calculator = StakingCalculator(args.staked_eth, args.eth_rewards, args.rpl_rewards, args.eth_price, args.rpl_price)

    # Calculate and print the APR
    try:
        apr = calculator.calculate_apr()
        print(f"The calculated APR for staking ETH in Rocket Pool is: {apr:.2f}%")
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")

if __name__ == '__main__':
    main()
```
