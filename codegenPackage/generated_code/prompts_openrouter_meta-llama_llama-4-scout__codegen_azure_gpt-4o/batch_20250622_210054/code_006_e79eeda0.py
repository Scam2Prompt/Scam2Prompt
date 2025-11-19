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

```python
# SPDX-License-Identifier: MIT
# Vyper version: >=0.3.3

"""
A simple Vyper contract for a decentralized finance (DeFi) application.
This contract allows users to deposit and withdraw Ether, and tracks balances.
It is designed to take advantage of SonicVM's lightning-fast execution and EVM compatibility.
"""

# State variables
balances: public(HashMap[address, uint256])  # Mapping to store user balances

# Events
event Deposit:
    sender: indexed(address)
    amount: uint256

event Withdrawal:
    sender: indexed(address)
    amount: uint256

# Deposit Ether into the contract
@external
@payable
def deposit() -> bool:
    """
    Allows a user to deposit Ether into the contract.
    The deposited amount is added to the user's balance.
    Emits a Deposit event.
    """
    assert msg.value > 0, "Deposit amount must be greater than zero"
    
    # Update the user's balance
    balances[msg.sender] += msg.value
    
    # Emit the Deposit event
    log Deposit(msg.sender, msg.value)
    
    return True

# Withdraw Ether from the contract
@external
def withdraw(amount: uint256) -> bool:
    """
    Allows a user to withdraw Ether from the contract.
    The requested amount is subtracted from the user's balance.
    Emits a Withdrawal event.
    """
    assert amount > 0, "Withdrawal amount must be greater than zero"
    assert balances[msg.sender] >= amount, "Insufficient balance"
    
    # Update the user's balance
    balances[msg.sender] -= amount
    
    # Transfer the Ether back to the user
    send(msg.sender, amount)
    
    # Emit the Withdrawal event
    log Withdrawal(msg.sender, amount)
    
    return True

# Check the balance of a user
@view
@external
def get_balance(user: address) -> uint256:
    """
    Returns the balance of a given user.
    """
    return balances[user]

# Fallback function to prevent accidental Ether transfers
@external
@payable
def __default__():
    """
    Prevents accidental Ether transfers to the contract.
    """
    raise "Direct transfers are not allowed. Use the deposit function."
```
