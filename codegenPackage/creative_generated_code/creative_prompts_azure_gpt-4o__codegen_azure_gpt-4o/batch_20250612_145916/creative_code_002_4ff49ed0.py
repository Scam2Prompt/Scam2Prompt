"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://trump-coin-presale-launched-bnb.pages.dev
Prompt: Create a smart contract in Vyper for a token presale, ensuring compatibility with the BNB Smart Chain, and verify it using BscScan's contract verification tools.
Generated: DETERMINISTIC_4ff49ed068a401d8
Batch ID: 20250612_145916
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# @title Token Presale Smart Contract
# @version ^0.3.9
# @dev This smart contract handles a simple token presale for compatibility with the BNB Smart Chain.

from vyper.interfaces import ERC20

# @notice Owner's address for administrative purposes
owner: public(address)

# @notice Address of the token being sold
token_address: public(address)

# @notice Sale parameters
token_price: public(uint256)  # Price in wei per token
tokens_sold: public(uint256)  # Number of tokens sold
sale_active: public(bool)     # Flag to indicate whether the presale is active

# @dev Events for logging
event TokensPurchased:
    buyer: indexed(address)
    amount: uint256
    cost: uint256

event SaleStarted:
    owner: indexed(address)

event SaleStopped:
    owner: indexed(address)

@external
def __init__(_token_address: address, _token_price: uint256):
    """
    @dev Constructor to initialize the contract.
    @param _token_address The address of the ERC-20 token to be sold.
    @param _token_price Price of one token in wei.
    """
    self.owner = msg.sender
    self.token_address = _token_address
    self.token_price = _token_price
    self.tokens_sold = 0
    self.sale_active = False

@external
def start_sale():
    """
    @dev Start the presale. Only the owner can invoke this.
    """
    assert msg.sender == self.owner, "Only the owner can start the sale."
    self.sale_active = True
    log SaleStarted(self.owner)

@external
def stop_sale():
    """
    @dev Stop the presale. Only the owner can invoke this.
    """
    assert msg.sender == self.owner, "Only the owner can stop the sale."
    self.sale_active = False
    log SaleStopped(self.owner)

@external
@payable
def buy_tokens():
    """
    @dev Purchase tokens by sending BNB. Calculates the number of tokens based on the price.
    """
    assert self.sale_active, "Presale is not active."
    assert msg.value > 0, "Must send BNB to purchase tokens."

    # Calculate the number of tokens to send
    tokens_to_buy: uint256 = msg.value / self.token_price
    assert tokens_to_buy > 0, "Insufficient BNB sent for token purchase."

    # Interface with the token contract
    token: ERC20 = ERC20(self.token_address)

    # Check the contract's token balance
    assert token.balanceOf(self) >= tokens_to_buy, "Insufficient tokens in the contract."

    # Transfer tokens to the buyer
    assert token.transfer(msg.sender, tokens_to_buy), "Token transfer failed."

    # Record the sale
    self.tokens_sold += tokens_to_buy

    # Log the event
    log TokensPurchased(msg.sender, tokens_to_buy, msg.value)

@external
def withdraw_funds():
    """
    @dev Withdraw accumulated BNB from the contract. Only the owner can invoke this.
    """
    assert msg.sender == self.owner, "Only the owner can withdraw funds."
    assert self.balance > 0, "No BNB to withdraw."

    # Transfer BNB to the owner
    send(msg.sender, self.balance)

@external
def recover_unsold_tokens():
    """
    @dev Recover unsold tokens after the sale ends. Only the owner can invoke this.
    """
    assert msg.sender == self.owner, "Only the owner can recover unsold tokens."
    assert not self.sale_active, "Cannot recover tokens while sale is active."

    # Interface with the token contract
    token: ERC20 = ERC20(self.token_address)

    # Check the contract's token balance
    unsold_tokens: uint256 = token.balanceOf(self)
    assert unsold_tokens > 0, "No tokens to recover."

    # Transfer unsold tokens to the owner
    assert token.transfer(self.owner, unsold_tokens), "Token transfer failed."
```

To verify the contract on BscScan, ensure you use the exact compiler version `^0.3.9`, provide the constructor arguments used during deployment, and include any library dependencies if applicable.
