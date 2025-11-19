"""
Generated Code Metadata:
========================
Original URL: https://claim-73f.pages.dev
Prompt: Describe how to create a smart contract for a binary options trade on the Vyper DEX, including the logic for determining profit based on asset price movements.
Generated: DETERMINISTIC_d929a1eeaed5d92f
Batch ID: 20250612_161042
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
from vyper import v1_0_0

# Define the smart contract for binary options trading
@public
contract BinaryOptions:
    # Define state variables
    owner: public(address)
    asset_price: public(uint256)
    strike_price: public(uint256)
    expiration_time: public(uint256)
    is_settled: public(bool)
    payout: public(uint256)

    # Event to log the trade outcome
    event TradeSettled(success: bool, payout: uint256)

    # Constructor to initialize the contract
    @public
    @payable
    def __init__(self, _strike_price: uint256, _expiration_time: uint256):
        self.owner = msg.sender
        self.strike_price = _strike_price
        self.expiration_time = block.timestamp + _expiration_time
        self.is_settled = False
        self.payout = 0

    # Function to set the current asset price
    @public
    @only_owner
    def set_asset_price(_price: uint256):
        # Ensure the contract is not yet settled
        assert not self.is_settled, "Contract already settled"
        self.asset_price = _price

    # Function to settle the trade based on asset price
    @public
    def settle_trade():
        # Ensure the contract is not already settled
        assert not self.is_settled, "Contract already settled"
        # Ensure the current time is past the expiration time
        assert block.timestamp >= self.expiration_time, "Trade not yet expired"

        # Determine the outcome of the trade
        if self.asset_price >= self.strike_price:
            self.payout = msg.value * 2  # Winner gets double their stake
            log.TradeSettled(True, self.payout)
        else:
            self.payout = 0  # Loser gets nothing
            log.TradeSettled(False, self.payout)

        # Mark the contract as settled
        self.is_settled = True

    # Function to withdraw payout
    @public
    @only_owner
    def withdraw():
        # Ensure the contract is settled
        assert self.is_settled, "Contract not settled"
        # Ensure there is a payout to withdraw
        assert self.payout > 0, "No payout available"

        # Transfer the payout to the owner
        send(self.owner, self.payout)
        self.payout = 0  # Reset payout after withdrawal

    # Modifier to restrict access to the owner
    @public
    @constant
    def only_owner():
        assert msg.sender == self.owner, "Only the owner can call this function"
```

This code defines a simple binary options trading smart contract using Vyper. It includes functions to set the asset price, settle the trade based on the asset price at expiration, and withdraw the payout. Proper error handling and access control are implemented to ensure the contract operates securely.
