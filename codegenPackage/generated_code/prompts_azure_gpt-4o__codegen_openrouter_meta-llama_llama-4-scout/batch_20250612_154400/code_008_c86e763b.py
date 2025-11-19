"""
Generated Code Metadata:
========================
Original URL: https://quantprotocol.xyz
Prompt: Develop a script to calculate and display the rewards earned by Quant Protocol token holders based on gaming platform revenue, exchange trading fees, and wallet service fees.
Generated: DETERMINISTIC_c86e763bd51f9906
Batch ID: 20250612_154400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# rewards_calculator.py

import logging

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class QuantProtocolRewardsCalculator:
    """
    Calculates and displays rewards earned by Quant Protocol token holders.

    Attributes:
        gaming_revenue (float): Gaming platform revenue.
        exchange_trading_fees (float): Exchange trading fees.
        wallet_service_fees (float): Wallet service fees.
        total_revenue (float): Total revenue from all sources.
        token_holders (dict): Dictionary of token holders and their respective holdings.
    """

    def __init__(self, gaming_revenue, exchange_trading_fees, wallet_service_fees, token_holders):
        """
        Initializes the QuantProtocolRewardsCalculator.

        Args:
            gaming_revenue (float): Gaming platform revenue.
            exchange_trading_fees (float): Exchange trading fees.
            wallet_service_fees (float): Wallet service fees.
            token_holders (dict): Dictionary of token holders and their respective holdings.
        """
        self.gaming_revenue = gaming_revenue
        self.exchange_trading_fees = exchange_trading_fees
        self.wallet_service_fees = wallet_service_fees
        self.total_revenue = gaming_revenue + exchange_trading_fees + wallet_service_fees
        self.token_holders = token_holders

    def calculate_rewards(self):
        """
        Calculates rewards for each token holder based on their holdings.

        Returns:
            dict: Dictionary of token holders and their respective rewards.
        """
        if self.total_revenue <= 0:
            logging.error("Total revenue must be greater than zero.")
            raise ValueError("Total revenue must be greater than zero.")

        total_holdings = sum(self.token_holders.values())
        if total_holdings <= 0:
            logging.error("Total holdings must be greater than zero.")
            raise ValueError("Total holdings must be greater than zero.")

        rewards = {}
        for holder, holdings in self.token_holders.items():
            reward_percentage = holdings / total_holdings
            rewards[holder] = self.total_revenue * reward_percentage

        return rewards

    def display_rewards(self, rewards):
        """
        Displays rewards earned by each token holder.

        Args:
            rewards (dict): Dictionary of token holders and their respective rewards.
        """
        logging.info("Rewards earned by Quant Protocol token holders:")
        for holder, reward in rewards.items():
            logging.info(f"{holder}: {reward:.2f}")


def main():
    try:
        gaming_revenue = 10000.0
        exchange_trading_fees = 5000.0
        wallet_service_fees = 2000.0
        token_holders = {
            "Holder1": 1000,
            "Holder2": 2000,
            "Holder3": 3000
        }

        calculator = QuantProtocolRewardsCalculator(gaming_revenue, exchange_trading_fees, wallet_service_fees, token_holders)
        rewards = calculator.calculate_rewards()
        calculator.display_rewards(rewards)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    main()
```
