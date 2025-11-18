"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://worldmobile-token.pages.dev
Prompt: Write a program to simulate the revenue allocation process described in the World Mobile Token ecosystem, including purchasing WMTx from open markets and distributing rewards to stakers.
Generated: DETERMINISTIC_1890baf38710e0aa
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class WMTXToken:
    """
    A class to represent the WMTx token in the World Mobile Token ecosystem.
    """

    def __init__(self, total_supply: float):
        """
        Initialize the WMTx token with a total supply.

        :param total_supply: Total amount of WMTx available.
        """
        self.total_supply = total_supply
        self.stakers: Dict[str, float] = {}  # Maps staker's address to their staked amount
        self.reward_pool = 0.0  # Total amount of rewards available for distribution

    def purchase_tokens(self, amount: float) -> bool:
        """
        Simulate purchasing WMTx tokens from the open market.

        :param amount: Amount of WMTx to purchase.
        :return: True if the purchase was successful, False otherwise.
        """
        if amount <= 0 or amount > self.total_supply:
            print("Purchase amount must be greater than 0 and less than the total supply.")
            return False

        self.total_supply -= amount
        print(f"Purchased {amount} WMTx. Remaining supply: {self.total_supply}.")
        return True

    def stake_tokens(self, address: str, amount: float) -> bool:
        """
        Stake tokens in the ecosystem.

        :param address: The address of the staker.
        :param amount: Amount of WMTx to stake.
        :return: True if staking was successful, False otherwise.
        """
        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount
        
        print(f"{address} has staked {amount} WMTx. Total staked: {self.stakers[address]}.")
        return True

    def distribute_rewards(self, rewards: float):
        """
        Distribute rewards to stakers based on their stake proportion.

        :param rewards: Total rewards to distribute.
        """
        if rewards <= 0:
            print("No rewards to distribute.")
            return

        self.reward_pool += rewards
        print(f"Added {rewards} to reward pool. Total rewards available: {self.reward_pool}.")

        total_staked = sum(self.stakers.values())
        if total_staked == 0:
            print("No stakers to distribute rewards to.")
            return

        for address, amount in self.stakers.items():
            # Calculate reward based on proportion of stake
            reward = (amount / total_staked) * self.reward_pool
            print(f"Distributing {reward} to {address}.")
            self.reward_pool -= reward

        print(f"All rewards distributed. Remaining reward pool: {self.reward_pool}.")

def main():
    wmtx = WMTXToken(total_supply=1000000.0)  # Initialize the token with a total supply of 1,000,000 WMTx

    # Simulate purchasing tokens
    if not wmtx.purchase_tokens(10000.0):
        return

    # Simulate staking
    wmtx.stake_tokens("address_1", 5000.0)
    wmtx.stake_tokens("address_2", 3000.0)

    # Simulate distributing rewards
    wmtx.distribute_rewards(2000.0)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
