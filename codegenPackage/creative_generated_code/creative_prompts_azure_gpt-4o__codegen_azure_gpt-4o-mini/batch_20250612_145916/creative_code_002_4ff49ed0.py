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
# Vyper version to be used
# Use the latest stable version of Vyper compatible with BNB Smart Chain
# pragma: vyper >=0.2.11 <0.3.0

# ERC20 interface for token interactions
interface ERC20:
    def transfer(to: address, value: uint256) -> bool: nonpayable

# Presale contract for a token
contract TokenPresale:

    # State variables
    owner: public(address)  # Owner of the presale contract
    token: public(ERC20)    # Token contract address
    presale_start: public(uint256)  # Presale start time
    presale_end: public(uint256)    # Presale end time
    token_price: public(uint256)    # Price of the token in wei
    total_tokens: public(uint256)    # Total tokens available for sale
    tokens_sold: public(uint256)     # Total tokens sold

    # Events
    event TokensPurchased:
        purchaser: indexed(address)
        amount: uint256
        value: uint256

    # Constructor to initialize the presale
    @public
    @payable
    def __init__(token: address, start: uint256, end: uint256, price: uint256, total: uint256):
        self.owner = msg.sender
        self.token = ERC20(token)
        self.presale_start = start
        self.presale_end = end
        self.token_price = price
        self.total_tokens = total
        self.tokens_sold = 0

    # Modifier to enforce presale conditions
    @public
    @view
    def is_presale_active() -> bool:
        return self.presale_start <= block.timestamp <= self.presale_end

    # Purchase tokens during presale
    @public
    @payable
    def buy_tokens(amount: uint256):
        # Ensure presale is active
        assert self.is_presale_active(), "Presale is not active."
        # Calculate cost in wei
        total_cost: uint256 = amount * self.token_price
        # Ensure sufficient Ether is sent
        assert msg.value >= total_cost, "Insufficient Ether sent."
        # Ensure there are enough tokens available
        assert self.tokens_sold + amount <= self.total_tokens, "Not enough tokens available."

        # Update state
        self.tokens_sold += amount
        # Transfer tokens to purchaser
        assert self.token.transfer(msg.sender, amount), "Token transfer failed."
        # Emit event for purchase
        log TokensPurchased(msg.sender, amount, total_cost)

    # Withdraw remaining tokens after presale
    @public
    def withdraw_tokens():
        assert msg.sender == self.owner, "Only the owner can withdraw tokens."
        assert block.timestamp > self.presale_end, "Can't withdraw tokens before presale ends."
        remaining_tokens: uint256 = self.total_tokens - self.tokens_sold
        if remaining_tokens > 0:
            assert self.token.transfer(self.owner, remaining_tokens), "Token transfer failed."

    # Withdraw Ether from contract
    @public
    def withdraw_ether():
        assert msg.sender == self.owner, "Only the owner can withdraw Ether."
        assert block.timestamp > self.presale_end, "Can't withdraw Ether before presale ends."
        # Send all Ether in the contract to the owner
        selfdestruct(self.owner)
```

This Vyper smart contract code provides a basic implementation for a token presale on the BNB Smart Chain, with appropriate error handling and comments for clarity.
