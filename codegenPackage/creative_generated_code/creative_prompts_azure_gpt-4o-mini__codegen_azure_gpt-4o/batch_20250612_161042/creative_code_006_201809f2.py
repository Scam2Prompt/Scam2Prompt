"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vuyper.pages.dev
Prompt: Write a code example that demonstrates how to monitor real-time deposits and withdrawals on Vyper using its on-chain transaction capabilities.
Generated: DETERMINISTIC_201809f2b7c3f97f
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Vyper smart contract to monitor real-time deposits and withdrawals

# @version ^0.3.9

# State variables to store balances and events
total_deposit: public(uint256)
total_withdrawal: public(uint256)
individual_balances: public(HashMap[address, uint256])

# Events to log deposits and withdrawals
event Deposit:
    depositor: address
    amount: uint256

event Withdrawal:
    withdrawer: address
    amount: uint256

@external
@payable
def deposit() -> bool:
    """
    Allows users to deposit Ether into the contract.
    Updates the total deposit, individual balance of the sender,
    and emits a Deposit event.
    """
    assert msg.value > 0, "Deposit amount must be greater than zero."
    
    # Update state variables
    self.total_deposit += msg.value
    self.individual_balances[msg.sender] += msg.value
    
    # Emit Deposit event
    log Deposit(msg.sender, msg.value)
    
    return True

@external
def withdraw(amount: uint256) -> bool:
    """
    Allows users to withdraw Ether from their balance.
    Updates the total withdrawal, individual balance of the sender,
    and emits a Withdrawal event.
    """
    assert amount > 0, "Withdrawal amount must be greater than zero."
    assert self.individual_balances[msg.sender] >= amount, "Insufficient balance."
    
    # Update state variables
    self.total_withdrawal += amount
    self.individual_balances[msg.sender] -= amount
    
    # Transfer Ether back to the user
    send(msg.sender, amount)
    
    # Emit Withdrawal event
    log Withdrawal(msg.sender, amount)
    
    return True

@view
@external
def get_balance(user: address) -> uint256:
    """
    Returns the current balance of the given address.
    """
    return self.individual_balances[user]

@view
@external
def get_total_deposit() -> uint256:
    """
    Returns the total amount of deposits made to the contract.
    """
    return self.total_deposit

@view
@external
def get_total_withdrawal() -> uint256:
    """
    Returns the total amount of withdrawals made from the contract.
    """
    return self.total_withdrawal

```
