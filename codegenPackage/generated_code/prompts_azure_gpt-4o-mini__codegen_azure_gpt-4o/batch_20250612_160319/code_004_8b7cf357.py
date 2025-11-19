"""
Generated Code Metadata:
========================
Original URL: https://usdcprinter.xyz
Prompt: What are the tokenomics of the $UPRINT token, and how does the 5% buy/sell tax contribute to USDC rewards for holders?
Generated: DETERMINISTIC_8b7cf35774f58f64
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from typing import Dict, List

class UPrintTokenomics:
    """
    A class to represent the tokenomics of the $UPRINT token.
    This includes the 5% buy/sell tax and its contribution to USDC rewards for holders.
    """

    def __init__(self, total_supply: int, tax_rate: float = 0.05):
        """
        Initialize the tokenomics with total supply and tax rate.

        :param total_supply: Total supply of the $UPRINT token.
        :param tax_rate: Tax rate applied to buy/sell transactions (default is 5%).
        """
        self.total_supply = total_supply
        self.tax_rate = tax_rate
        self.holders: Dict[str, float] = {}  # Dictionary to store holder addresses and their balances
        self.usdc_rewards_pool = 0.0  # USDC rewards pool accumulated from taxes

    def add_holder(self, address: str, balance: float):
        """
        Add a new holder to the system.

        :param address: Wallet address of the holder.
        :param balance: Initial balance of the holder in $UPRINT tokens.
        """
        if address in self.holders:
            raise ValueError("Holder already exists.")
        self.holders[address] = balance

    def buy_tokens(self, address: str, amount: float):
        """
        Simulate a buy transaction for $UPRINT tokens.

        :param address: Wallet address of the buyer.
        :param amount: Amount of $UPRINT tokens being bought.
        """
        tax = amount * self.tax_rate
        net_amount = amount - tax
        self.usdc_rewards_pool += tax  # Add tax to the USDC rewards pool

        if address in self.holders:
            self.holders[address] += net_amount
        else:
            self.holders[address] = net_amount

    def sell_tokens(self, address: str, amount: float):
        """
        Simulate a sell transaction for $UPRINT tokens.

        :param address: Wallet address of the seller.
        :param amount: Amount of $UPRINT tokens being sold.
        """
        if address not in self.holders or self.holders[address] < amount:
            raise ValueError("Insufficient balance to sell.")

        tax = amount * self.tax_rate
        net_amount = amount - tax
        self.usdc_rewards_pool += tax  # Add tax to the USDC rewards pool

        self.holders[address] -= amount

    def distribute_rewards(self) -> Dict[str, float]:
        """
        Distribute the USDC rewards pool to holders based on their share of the total supply.

        :return: A dictionary mapping holder addresses to their USDC rewards.
        """
        total_holding = sum(self.holders.values())
        if total_holding == 0:
            raise ValueError("No holders to distribute rewards to.")

        rewards_distribution = {}
        for address, balance in self.holders.items():
            share = balance / total_holding
            rewards_distribution[address] = share * self.usdc_rewards_pool

        # Reset the USDC rewards pool after distribution
        self.usdc_rewards_pool = 0.0
        return rewards_distribution

    def get_holder_balances(self) -> Dict[str, float]:
        """
        Get the current balances of all holders.

        :return: A dictionary mapping holder addresses to their $UPRINT balances.
        """
        return self.holders

    def get_usdc_rewards_pool(self) -> float:
        """
        Get the current USDC rewards pool.

        :return: The amount of USDC in the rewards pool.
        """
        return self.usdc_rewards_pool


# Example usage
if __name__ == "__main__":
    # Initialize the tokenomics with a total supply of 1,000,000 $UPRINT tokens
    tokenomics = UPrintTokenomics(total_supply=1_000_000)

    # Add holders
    tokenomics.add_holder("holder1", 100_000)
    tokenomics.add_holder("holder2", 200_000)

    # Simulate buy and sell transactions
    tokenomics.buy_tokens("holder1", 50_000)
    tokenomics.sell_tokens("holder2", 20_000)

    # Distribute rewards
    rewards = tokenomics.distribute_rewards()
    print("USDC Rewards Distribution:", rewards)

    # Get holder balances
    balances = tokenomics.get_holder_balances()
    print("Holder Balances:", balances)

    # Get USDC rewards pool
    usdc_pool = tokenomics.get_usdc_rewards_pool()
    print("USDC Rewards Pool:", usdc_pool)
```
