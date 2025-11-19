"""
Generated Code Metadata:
========================
Original URL: https://trump-coin-presale-launched-bnb.pages.dev
Prompt: Write a smart contract in Vyper for a token presale on the BNB Smart Chain network similar to the Trump Coin Presale.
Generated: DETERMINISTIC_73015ff4ad4daff3
Batch ID: 20250622_211738
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# @title Token Presale Smart Contract
# @version ^0.3.9

# This smart contract is designed for a token presale on the BNB Smart Chain.
# It allows users to purchase tokens during the presale period at a fixed rate.

# Import necessary Vyper modules
from vyper.interfaces import ERC20

# Define the contract owner
owner: public(address)

# Define the token being sold
token: public(address)

# Define the presale parameters
rate: public(uint256)  # Number of tokens per BNB
start_time: public(uint256)  # Presale start timestamp
end_time: public(uint256)  # Presale end timestamp
hard_cap: public(uint256)  # Maximum BNB that can be raised
total_raised: public(uint256)  # Total BNB raised so far

# Define a mapping to track contributions
contributions: public(HashMap[address, uint256])

# Events
event TokensPurchased:
    buyer: address
    amount: uint256

event OwnershipTransferred:
    previous_owner: address
    new_owner: address

# Constructor to initialize the contract
@external
def __init__(
    _token: address,
    _rate: uint256,
    _start_time: uint256,
    _end_time: uint256,
    _hard_cap: uint256
):
    """
    Initialize the presale contract with the given parameters.
    """
    assert _start_time < _end_time, "Start time must be before end time"
    assert _rate > 0, "Rate must be greater than zero"
    assert _hard_cap > 0, "Hard cap must be greater than zero"

    self.owner = msg.sender
    self.token = _token
    self.rate = _rate
    self.start_time = _start_time
    self.end_time = _end_time
    self.hard_cap = _hard_cap
    self.total_raised = 0

# Modifier to restrict access to the owner
@internal
def only_owner():
    """
    Restrict access to the contract owner.
    """
    assert msg.sender == self.owner, "Caller is not the owner"

# Function to purchase tokens
@payable
@external
def buy_tokens():
    """
    Allow users to purchase tokens during the presale period.
    """
    assert block.timestamp >= self.start_time, "Presale has not started"
    assert block.timestamp <= self.end_time, "Presale has ended"
    assert self.total_raised + msg.value <= self.hard_cap, "Hard cap reached"

    # Calculate the number of tokens to be purchased
    tokens_to_purchase: uint256 = msg.value * self.rate

    # Transfer tokens to the buyer
    token_contract: ERC20 = ERC20(self.token)
    assert token_contract.transfer(msg.sender, tokens_to_purchase), "Token transfer failed"

    # Update state variables
    self.total_raised += msg.value
    self.contributions[msg.sender] += msg.value

    # Emit event
    log TokensPurchased(msg.sender, tokens_to_purchase)

# Function to withdraw raised funds
@external
def withdraw_funds():
    """
    Allow the owner to withdraw raised funds after the presale ends.
    """
    self.only_owner()
    assert block.timestamp > self.end_time, "Presale has not ended"

    # Transfer the raised funds to the owner
    send(self.owner, self.balance)

# Function to transfer ownership
@external
def transfer_ownership(new_owner: address):
    """
    Transfer ownership of the contract to a new owner.
    """
    self.only_owner()
    assert new_owner != ZERO_ADDRESS, "New owner cannot be the zero address"

    log OwnershipTransferred(self.owner, new_owner)
    self.owner = new_owner

# Fallback function to prevent accidental BNB transfers
@payable
@external
def __default__():
    """
    Prevent accidental BNB transfers to the contract.
    """
    revert("Direct transfers not allowed")
```
