"""
Generated Code Metadata:
========================
Original URL: https://soniclaqs.com
Prompt: "Create a simple Vyper contract that takes advantage of SonicVM's lightning-fast execution and 100% EVM compatibility for a decentralized finance (DeFi) application."
Generated: DETERMINISTIC_e79eeda007efabd7
Batch ID: 20250622_210054
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```vyper
# SPDX-License-Identifier: MIT
# A simple DeFi contract using Vyper that allows users to deposit and withdraw Ether.

# Define the contract
contract DeFiContract:

    # State variable to track the balance of each user
    balances: public(map(address, uint256))

    # Event to log deposits
    event Deposit:
        user: indexed(address)
        amount: uint256

    # Event to log withdrawals
    event Withdrawal:
        user: indexed(address)
        amount: uint256

    # Function to deposit Ether into the contract
    @public
    @payable
    def deposit():
        # Ensure that the deposit amount is greater than zero
        assert msg.value > 0, "Deposit amount must be greater than zero"
        
        # Update the user's balance
        self.balances[msg.sender] += msg.value
        
        # Emit a deposit event
        log Deposit(msg.sender, msg.value)

    # Function to withdraw Ether from the contract
    @public
    def withdraw(amount: uint256):
        # Ensure that the user has enough balance to withdraw
        assert self.balances[msg.sender] >= amount, "Insufficient balance"
        
        # Update the user's balance before transferring funds
        self.balances[msg.sender] -= amount
        
        # Transfer the specified amount to the user
        send(msg.sender, amount)
        
        # Emit a withdrawal event
        log Withdrawal(msg.sender, amount)

    # Function to check the balance of a user
    @public
    @view
    def check_balance() -> uint256:
        return self.balances[msg.sender]
```
