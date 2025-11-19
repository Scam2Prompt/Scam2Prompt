"""
Generated Code Metadata:
========================
Original URL: https://vuyper.pages.dev
Prompt: Describe how to set up a smart contract on Vyper for trading synthetic assets and managing collateral requirements.
Generated: DETERMINISTIC_cf4ee3ccbbdd474d
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# @version ^0.3.7

# A Vyper smart contract for trading synthetic assets with collateral management

from vyper.interfaces import ERC20

# Events
Deposit: event({account: indexed(address), amount: uint256})
Withdraw: event({account: indexed(address), amount: uint256})
Trade: event({account: indexed(address), asset: indexed(bytes32), amount: int256, price: uint256})
Liquidate: event({account: indexed(address), liquidator: indexed(address), amount: uint256})

# Constants
MIN_COLLATERAL_RATIO: constant(uint256) = 1500000000000000000  # 150% in 18 decimals
LIQUIDATION_PENALTY: constant(uint256) = 1100000000000000000   # 10% penalty
PRICE_DECIMALS: constant(uint256) = 10 ** 18

# Storage variables
collateral_token: public(ERC20)
synthetic_assets: public(HashMap[bytes32, bool])
positions: public(HashMap[address, HashMap[bytes32, int256]])  # +long, -short
collateral: public(HashMap[address, uint256])
total_collateral: public(uint256)
admin: public(address)
paused: public(bool)

@external
def __init__(_collateral_token: address):
    self.collateral_token = ERC20(_collateral_token)
    self.admin = msg.sender

@external
def add_synthetic_asset(_asset: bytes32):
    assert msg.sender == self.admin, "Only admin"
    self.synthetic_assets[_asset] = True

@external
def remove_synthetic_asset(_asset: bytes32):
    assert msg.sender == self.admin, "Only admin"
    self.synthetic_assets[_asset] = False

@external
def set_paused(_paused: bool):
    assert msg.sender == self.admin, "Only admin"
    self.paused = _paused

@external
@payable
def deposit(_amount: uint256):
    assert not self.paused, "Contract paused"
    assert _amount > 0, "Amount must be > 0"
    
    # Transfer collateral from user
    assert self.collateral_token.transferFrom(msg.sender, self, _amount), "Transfer failed"
    
    # Update balances
    self.collateral[msg.sender] += _amount
    self.total_collateral += _amount
    
    log Deposit(msg.sender, _amount)

@external
def withdraw(_amount: uint256):
    assert not self.paused, "Contract paused"
    assert _amount > 0, "Amount must be > 0"
    assert self.collateral[msg.sender] >= _amount, "Insufficient collateral"
    
    # Check collateral ratio after withdrawal
    assert self._check_collateral_ratio(msg.sender, _amount), "Collateral ratio too low"
    
    # Update balances
    self.collateral[msg.sender] -= _amount
    self.total_collateral -= _amount
    
    # Transfer collateral to user
    assert self.collateral_token.transfer(msg.sender, _amount), "Transfer failed"
    
    log Withdraw(msg.sender, _amount)

@external
def trade(_asset: bytes32, _amount: int256, _price: uint256):
    assert not self.paused, "Contract paused"
    assert self.synthetic_assets[_asset], "Invalid asset"
    assert _amount != 0, "Amount cannot be zero"
    
    # Update position
    self.positions[msg.sender][_asset] += _amount
    
    # Check collateral ratio
    assert self._check_collateral_ratio(msg.sender, 0), "Insufficient collateral"
    
    log Trade(msg.sender, _asset, _amount, _price)

@external
def liquidate(_account: address, _asset: bytes32):
    assert not self.paused, "Contract paused"
    assert not self._check_collateral_ratio(_account, 0), "Account not undercollateralized"
    
    position: int256 = self.positions[_account][_asset]
    assert position != 0, "No position to liquidate"
    
    # Calculate liquidation amount (entire position)
    liquidation_amount: uint256 = convert(abs(position), uint256)
    
    # Apply penalty
    penalty_amount: uint256 = liquidation_amount * LIQUIDATION_PENALTY / PRICE_DECIMALS
    
    # Check if account has enough collateral
    assert self.collateral[_account] >= penalty_amount, "Not enough collateral for penalty"
    
    # Update balances
    self.collateral[_account] -= penalty_amount
    self.total_collateral -= penalty_amount
    
    # Close position
    self.positions[_account][_asset] = 0
    
    # Transfer penalty to liquidator (50%) and protocol (50%)
    half_penalty: uint256 = penalty_amount / 2
    assert self.collateral_token.transfer(msg.sender, half_penalty), "Transfer failed"
    assert self.collateral_token.transfer(self.admin, half_penalty), "Transfer failed"
    
    log Liquidate(_account, msg.sender, penalty_amount)

@internal
def _check_collateral_ratio(_account: address, _withdraw_amount: uint256) -> bool:
    # Get total collateral value after potential withdrawal
    collateral_value: uint256 = self.collateral[_account] - _withdraw_amount
    
    # Calculate total position value (simplified - would use oracle in production)
    total_position_value: uint256 = 0
    for asset in self.synthetic_assets:
        position: int256 = self.positions[_account][asset]
        if position != 0:
            # In production, would multiply by asset price from oracle
            total_position_value += convert(abs(position), uint256)
    
    # Avoid division by zero
    if total_position_value == 0:
        return True
    
    # Check if collateral ratio is sufficient
    ratio: uint256 = (collateral_value * PRICE_DECIMALS) / total_position_value
    return ratio >= MIN_COLLATERAL_RATIO

@view
@external
def get_collateral_ratio(_account: address) -> uint256:
    collateral_value: uint256 = self.collateral[_account]
    total_position_value: uint256 = 0
    
    for asset in self.synthetic_assets:
        position: int256 = self.positions[_account][asset]
        if position != 0:
            total_position_value += convert(abs(position), uint256)
    
    if total_position_value == 0:
        return 0
    
    return (collateral_value * PRICE_DECIMALS) / total_position_value
```
