"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethenaapp.pages.dev
Prompt: Write code to enable minting of synthetic dollars against liquid staking tokens while maintaining long exposure to Ethereum, as described in Ethena's composable leverage mechanism.
Generated: DETERMINISTIC_7323c39a87272850
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from decimal import Decimal
from typing import Dict, Any

class SyntheticDollarMintingSystem:
    """
    A system for minting synthetic dollars against liquid staking tokens while maintaining long exposure to Ethereum.
    """

    def __init__(self, eth_price_usd: Decimal, collateral_ratio: Decimal):
        """
        Initialize the system with the price of Ethereum and collateral ratio.
        
        :param eth_price_usd: The current price of 1 ETH in USD.
        :param collateral_ratio: Required collateral ratio (e.g., 1.5 means 150% collateral is required).
        """
        self.eth_price_usd = eth_price_usd
        self.collateral_ratio = collateral_ratio
        self.accounts: Dict[str, Dict[str, Any]] = {}

    def deposit_collateral(self, user_id: str, amount_eth: Decimal):
        """
        Deposit ETH as collateral.

        :param user_id: The ID of the user depositing collateral.
        :param amount_eth: The amount of ETH to deposit.
        """
        if amount_eth <= 0:
            raise ValueError("Amount of ETH must be greater than zero.")
        
        if user_id not in self.accounts:
            self.accounts[user_id] = {"collateral_eth": Decimal(0), "synthetic_usd": Decimal(0)}
        
        self.accounts[user_id]["collateral_eth"] += amount_eth

    def mint_synthetic_dollars(self, user_id: str, amount_usd: Decimal):
        """
        Mint synthetic dollars against deposited collateral.

        :param user_id: The ID of the user minting synthetic dollars.
        :param amount_usd: The amount of synthetic USD to mint.
        """
        if user_id not in self.accounts:
            raise ValueError("User has not deposited any collateral.")
        
        collateral_eth = self.accounts[user_id]["collateral_eth"]
        max_mintable_usd = collateral_eth * self.eth_price_usd / self.collateral_ratio

        if amount_usd > max_mintable_usd:
            raise ValueError(f"Minting amount exceeds collateral limit. Max mintable: {max_mintable_usd:.2f} USD.")

        self.accounts[user_id]["synthetic_usd"] += amount_usd

    def withdraw_collateral(self, user_id: str, amount_eth: Decimal):
        """
        Withdraw collateral ETH if the collateral requirements are met.

        :param user_id: The ID of the user withdrawing collateral.
        :param amount_eth: The amount of ETH to withdraw.
        """
        if user_id not in self.accounts:
            raise ValueError("User does not exist.")
        
        if amount_eth <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        collateral_eth = self.accounts[user_id]["collateral_eth"]
        synthetic_usd = self.accounts[user_id]["synthetic_usd"]

        # Ensure the withdrawal does not violate the collateral ratio
        remaining_collateral_eth = collateral_eth - amount_eth
        if remaining_collateral_eth * self.eth_price_usd < synthetic_usd * self.collateral_ratio:
            raise ValueError("Insufficient collateral after withdrawal.")

        self.accounts[user_id]["collateral_eth"] -= amount_eth

    def get_user_account(self, user_id: str) -> Dict[str, Any]:
        """
        Get the account details of a user.

        :param user_id: The ID of the user.
        :return: A dictionary containing account details.
        """
        if user_id not in self.accounts:
            raise ValueError("User does not exist.")
        
        return self.accounts[user_id]

    def update_eth_price(self, new_eth_price_usd: Decimal):
        """
        Update the price of Ethereum in USD.

        :param new_eth_price_usd: The updated ETH price in USD.
        """
        if new_eth_price_usd <= 0:
            raise ValueError("ETH price must be greater than zero.")
        
        self.eth_price_usd = new_eth_price_usd

# Example usage
if __name__ == "__main__":
    try:
        system = SyntheticDollarMintingSystem(eth_price_usd=Decimal("1500"), collateral_ratio=Decimal("1.5"))

        user_id = "user123"
        system.deposit_collateral(user_id, amount_eth=Decimal("10"))
        system.mint_synthetic_dollars(user_id, amount_usd=Decimal("5000"))
        
        print(system.get_user_account(user_id))

        system.withdraw_collateral(user_id, amount_eth=Decimal("2"))
        print(system.get_user_account(user_id))

    except ValueError as e:
        print(f"Error: {e}")
```
