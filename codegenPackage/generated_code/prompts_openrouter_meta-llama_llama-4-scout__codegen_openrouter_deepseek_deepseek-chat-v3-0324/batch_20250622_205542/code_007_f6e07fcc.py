"""
Generated Code Metadata:
========================
Original URL: https://banksocialio.pages.dev
Prompt: "Propose a use case for BankSocial's $rUSD Token in a decentralized finance (DeFi) application, focusing on its utility and benefits in a borderless financial system."
Generated: DETERMINISTIC_f6e07fccfba8021f
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
DeFi Application for BankSocial's rUSD Token
This smart contract demonstrates a lending protocol using rUSD as collateral
and stablecoin for borderless financial operations.
"""

from brownie import (
    accounts,
    config,
    network,
    interface,
    Contract,
    LendingProtocol,
    rUSDToken,
    MockV3Aggregator,
)
from web3 import Web3
from decimal import Decimal

# Constants
INITIAL_PRICE_FEED_VALUE = Web3.toWei(1, "ether")  # 1:1 peg with USD
LOAN_TO_VALUE_RATIO = 75  # 75% LTV ratio
INTEREST_RATE = 5  # 5% annual interest
MINIMUM_COLLATERAL = Web3.toWei(100, "ether")  # Minimum 100 rUSD collateral

def main():
    """
    Deploy and demonstrate a DeFi lending protocol using BankSocial's rUSD token
    """
    # Setup
    account = accounts.add(config["wallets"]["from_key"])
    print(f"Using account: {account.address}")

    # Deploy or get token contracts
    print("Deploying rUSD token...")
    rusd_token = rUSDToken.deploy({"from": account})
    
    print("Deploying price feed...")
    price_feed = MockV3Aggregator.deploy(
        18, INITIAL_PRICE_FEED_VALUE, {"from": account}
    )
    
    print("Deploying lending protocol...")
    lending_protocol = LendingProtocol.deploy(
        rusd_token.address,
        price_feed.address,
        LOAN_TO_VALUE_RATIO,
        INTEREST_RATE,
        {"from": account},
    )
    
    # Fund the protocol with initial liquidity
    print("Funding protocol with initial liquidity...")
    rusd_token.mint(lending_protocol.address, Web3.toWei(100000, "ether"), {"from": account})
    
    # Demo user operations
    user = accounts.add()
    print(f"\nDemo user: {user.address}")
    
    # User gets rUSD tokens
    print("Minting rUSD to user...")
    rusd_token.mint(user.address, Web3.toWei(500, "ether"), {"from": account})
    
    # User deposits collateral
    print("User depositing collateral...")
    rusd_token.approve(
        lending_protocol.address, Web3.toWei(500, "ether"), {"from": user}
    )
    lending_protocol.depositCollateral(
        Web3.toWei(500, "ether"), {"from": user}
    )
    
    # User borrows against collateral
    print("User borrowing against collateral...")
    lending_protocol.borrow(Web3.toWei(375, "ether"), {"from": user})  # 75% of 500
    
    # Display balances
    user_rusd_balance = rusd_token.balanceOf(user.address)
    user_loan_amount = lending_protocol.getUserLoanAmount(user.address)
    print(f"\nUser rUSD balance: {Web3.fromWei(user_rusd_balance, 'ether')}")
    print(f"User loan amount: {Web3.fromWei(user_loan_amount, 'ether')}")
    
    # Repay loan
    print("\nUser repaying loan...")
    rusd_token.approve(
        lending_protocol.address, Web3.toWei(375, "ether"), {"from": user}
    )
    lending_protocol.repayLoan(Web3.toWei(375, "ether"), {"from": user})
    
    # Withdraw collateral
    print("User withdrawing collateral...")
    lending_protocol.withdrawCollateral(Web3.toWei(500, "ether"), {"from": user})
    
    # Final balances
    final_rusd_balance = rusd_token.balanceOf(user.address)
    final_loan_amount = lending_protocol.getUserLoanAmount(user.address)
    print(f"\nFinal rUSD balance: {Web3.fromWei(final_rusd_balance, 'ether')}")
    print(f"Final loan amount: {Web3.fromWei(final_loan_amount, 'ether')}")
    
    print("\nDemo completed successfully!")
```
