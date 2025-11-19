"""
Generated Code Metadata:
========================
Original URL: https://vuyper.pages.dev
Prompt: Generate a smart contract code for deploying a custom market on Vyper, supporting a unique asset with a specific payoff structure and collateral requirements.
Generated: DETERMINISTIC_652be1e0d49ee1ca
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# @version ^0.3.9

# Smart Contract: Custom Market for Unique Asset
# This contract allows the creation of a market for a unique asset with specific payoff structure and collateral requirements.

# State Variables
owner: public(address)  # Contract owner
asset_name: public(String[64])  # Name of the unique asset
collateral_requirement: public(uint256)  # Minimum collateral required
payoff_structure: public(String[256])  # Description of the payoff structure
market_active: public(bool)  # Status of the market

# Mapping to track collateral deposits
collateral_balances: public(HashMap[address, uint256])

# Events
event MarketCreated:
    asset_name: String[64]
    collateral_requirement: uint256
    payoff_structure: String[256]

event CollateralDeposited:
    depositor: address
    amount: uint256

event CollateralWithdrawn:
    withdrawer: address
    amount: uint256

event MarketClosed:
    closed_by: address

# Constructor: Initializes the market
@external
def __init__(
    _asset_name: String[64],
    _collateral_requirement: uint256,
    _payoff_structure: String[256]
):
    """
    Constructor to initialize the market with the asset name, collateral requirement, and payoff structure.
    """
    self.owner = msg.sender
    self.asset_name = _asset_name
    self.collateral_requirement = _collateral_requirement
    self.payoff_structure = _payoff_structure
    self.market_active = True

    # Emit the MarketCreated event
    log MarketCreated(_asset_name, _collateral_requirement, _payoff_structure)

# Modifier: Ensures only the owner can call certain functions
@internal
def only_owner():
    """
    Internal function to restrict access to the contract owner.
    """
    assert msg.sender == self.owner, "Only the owner can perform this action."

# Function: Deposit collateral
@external
@payable
def deposit_collateral():
    """
    Allows users to deposit collateral into the market.
    """
    assert self.market_active, "Market is not active."
    assert msg.value > 0, "Deposit amount must be greater than zero."

    # Update the depositor's collateral balance
    self.collateral_balances[msg.sender] += msg.value

    # Emit the CollateralDeposited event
    log CollateralDeposited(msg.sender, msg.value)

# Function: Withdraw collateral
@external
def withdraw_collateral(amount: uint256):
    """
    Allows users to withdraw their collateral from the market.
    """
    assert self.market_active, "Market is not active."
    assert self.collateral_balances[msg.sender] >= amount, "Insufficient collateral balance."

    # Update the depositor's collateral balance
    self.collateral_balances[msg.sender] -= amount

    # Transfer the collateral back to the user
    send(msg.sender, amount)

    # Emit the CollateralWithdrawn event
    log CollateralWithdrawn(msg.sender, amount)

# Function: Close the market
@external
def close_market():
    """
    Allows the owner to close the market.
    """
    self.only_owner()
    assert self.market_active, "Market is already closed."

    # Set the market status to inactive
    self.market_active = False

    # Emit the MarketClosed event
    log MarketClosed(msg.sender)

# Function: Get collateral balance
@view
@external
def get_collateral_balance(user: address) -> uint256:
    """
    Returns the collateral balance of a specific user.
    """
    return self.collateral_balances[user]
```
