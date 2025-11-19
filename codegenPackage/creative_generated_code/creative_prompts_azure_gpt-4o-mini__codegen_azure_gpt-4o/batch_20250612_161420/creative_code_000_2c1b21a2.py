"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bigpump.pages.dev
Prompt: Generate a smart contract for a meme coin similar to Big Pump Token ($PUMP) on the BNB Chain with a total supply of 4,444,444,444,444.
Generated: DETERMINISTIC_2c1b21a272def51b
Batch ID: 20250612_161420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title MemeCoinContract
 * @dev A smart contract for a meme coin similar to Big Pump Token ($PUMP) on the BNB Chain.
 * Total supply: 4,444,444,444,444.
 */
contract MemeCoin {
    // Public variables to store token details
    string public name = "Big Pump Token";
    string public symbol = "PUMP";
    uint8 public decimals = 18; // Standard decimal precision
    uint256 public totalSupply = 4444444444444 * 10**uint256(decimals); // Total supply with decimal adjustments

    // Mapping for balances of users
    mapping(address => uint256) public balanceOf;
    // Mapping for allowances (used in ERC20 transfers)
    mapping(address => mapping(address => uint256)) public allowance;

    // Events to log activities
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    /**
     * @dev Constructor to initialize the token and assign total supply to the deployer.
     */
    constructor() {
        balanceOf[msg.sender] = totalSupply; // Assign the total supply to the contract creator
        emit Transfer(address(0), msg.sender, totalSupply); // Emit transfer event indicating minting
    }

    /**
     * @dev Internal function to handle safe math subtraction.
     * Reverts if subtraction leads to a negative result.
     */
    function _safeSubtract(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction results in negative value");
        return a - b;
    }

    /**
     * @dev Internal function to handle safe math addition.
     * Reverts if addition leads to overflow.
     */
    function _safeAdd(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition results in overflow");
        return c;
    }

    /**
     * @dev ERC20 Transfer function to move tokens to another address.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
     * @return success Returns true if transfer is successful.
     */
    function transfer(address to, uint256 value) public returns (bool success) {
        require(to != address(0), "Invalid address"); // Prevent transfer to zero address
        require(balanceOf[msg.sender] >= value, "Insufficient balance"); // Ensure the sender has enough tokens

        balanceOf[msg.sender] = _safeSubtract(balanceOf[msg.sender], value); // Deduct from sender's balance
        balanceOf[to] = _safeAdd(balanceOf[to], value); // Add to recipient's balance

        emit Transfer(msg.sender, to, value); // Emit transfer event
        return true;
    }

    /**
     * @dev ERC20 Approval function to set allowance for a spender.
     * @param spender Address allowed to spend the tokens.
     * @param value Amount of tokens allowed to be spent.
     * @return success Returns true if approval is successful.
     */
    function approve(address spender, uint256 value) public returns (bool success) {
        require(spender != address(0), "Invalid address"); // Prevent approval to zero address

        allowance[msg.sender][spender] = value; // Set the allowance
        emit Approval(msg.sender, spender, value); // Emit approval event
        return true;
    }

    /**
     * @dev ERC20 TransferFrom function to transfer tokens on behalf of another account.
     * @param from Address to transfer tokens from.
     * @param to Address to transfer tokens to.
     * @param value Amount of tokens to transfer.
     * @return success Returns true if transfer is successful.
     */
    function transferFrom(address from, address to, uint256 value) public returns (bool success) {
        require(to != address(0), "Invalid address"); // Prevent transfer to zero address
        require(value <= balanceOf[from], "Insufficient balance"); // Ensure the sender has enough tokens
        require(value <= allowance[from][msg.sender], "Allowance exceeded"); // Ensure allowance is sufficient

        balanceOf[from] = _safeSubtract(balanceOf[from], value); // Deduct from sender's balance
        balanceOf[to] = _safeAdd(balanceOf[to], value); // Add to recipient's balance
        allowance[from][msg.sender] = _safeSubtract(allowance[from][msg.sender], value); // Deduct from allowance

        emit Transfer(from, to, value); // Emit transfer event
        return true;
    }
}
```
