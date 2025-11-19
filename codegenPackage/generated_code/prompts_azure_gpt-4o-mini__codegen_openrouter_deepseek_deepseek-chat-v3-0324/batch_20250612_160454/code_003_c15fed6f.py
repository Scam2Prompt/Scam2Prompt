"""
Generated Code Metadata:
========================
Original URL: https://usdfi-git-kyberswap-widget-tbot.vercel.app
Prompt: Provide an example of a lending protocol using MoneyLegos in a DeFi application.
Generated: DETERMINISTIC_c15fed6f68732ddd
Batch ID: 20250612_160454
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
from brownie import (
    accounts,
    config,
    interface,
    network,
    Contract,
    LendingPool,
    ERC20,
    exceptions,
)
from web3 import Web3
from scripts.helpful_scripts import get_account, get_contract

# Constants
LENDING_POOL_ADDRESS_PROVIDER = "0xB53C1a33016B2DC2fF3653530bfF1848a515c8c5"  # Mainnet
MAX_UINT256 = 2**256 - 1


class LendingProtocol:
    def __init__(self, account=None):
        self.account = account if account else get_account()
        self.lending_pool = self._get_lending_pool()

    def _get_lending_pool(self):
        # Get the lending pool address from the address provider
        address_provider = interface.ILendingPoolAddressesProvider(
            LENDING_POOL_ADDRESS_PROVIDER
        )
        lending_pool_address = address_provider.getLendingPool()
        return interface.ILendingPool(lending_pool_address)

    def deposit(self, asset_address, amount):
        """
        Deposit tokens into the lending protocol
        """
        asset = interface.IERC20(asset_address)
        approve_tx = asset.approve(self.lending_pool.address, amount, {"from": self.account})
        approve_tx.wait(1)

        deposit_tx = self.lending_pool.deposit(
            asset_address, amount, self.account.address, 0, {"from": self.account}
        )
        deposit_tx.wait(1)
        return deposit_tx

    def borrow(
        self,
        asset_address,
        amount,
        interest_rate_mode=1,  # 1 = stable, 2 = variable
        referral_code=0,
    ):
        """
        Borrow tokens from the lending protocol
        """
        borrow_tx = self.lending_pool.borrow(
            asset_address,
            amount,
            interest_rate_mode,
            referral_code,
            self.account.address,
            {"from": self.account},
        )
        borrow_tx.wait(1)
        return borrow_tx

    def repay(
        self,
        asset_address,
        amount,
        interest_rate_mode=1,
    ):
        """
        Repay borrowed tokens
        """
        asset = interface.IERC20(asset_address)
        approve_tx = asset.approve(self.lending_pool.address, amount, {"from": self.account})
        approve_tx.wait(1)

        repay_tx = self.lending_pool.repay(
            asset_address,
            amount,
            interest_rate_mode,
            self.account.address,
            {"from": self.account},
        )
        repay_tx.wait(1)
        return repay_tx

    def withdraw(self, asset_address, amount):
        """
        Withdraw deposited tokens
        """
        withdraw_tx = self.lending_pool.withdraw(
            asset_address, amount, self.account.address, {"from": self.account}
        )
        withdraw_tx.wait(1)
        return withdraw_tx

    def get_user_account_data(self):
        """
        Get user account data including total collateral, debt, etc.
        """
        return self.lending_pool.getUserAccountData(self.account.address)

    def get_reserve_data(self, asset_address):
        """
        Get reserve data including liquidity rate, available liquidity, etc.
        """
        return self.lending_pool.getReserveData(asset_address)


def main():
    # Example usage
    lending_protocol = LendingProtocol()

    # DAI token on Ethereum mainnet
    DAI_ADDRESS = "0x6B175474E89094C44Da98b954EedeAC495271d0F"
    amount = Web3.toWei(1, "ether")

    # Deposit DAI
    print("Depositing DAI...")
    lending_protocol.deposit(DAI_ADDRESS, amount)

    # Borrow ETH
    WETH_ADDRESS = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"
    print("Borrowing ETH...")
    lending_protocol.borrow(WETH_ADDRESS, amount)

    # Get user data
    print("User account data:")
    print(lending_protocol.get_user_account_data())

    # Repay ETH
    print("Repaying ETH...")
    lending_protocol.repay(WETH_ADDRESS, amount)

    # Withdraw DAI
    print("Withdrawing DAI...")
    lending_protocol.withdraw(DAI_ADDRESS, amount)
```
