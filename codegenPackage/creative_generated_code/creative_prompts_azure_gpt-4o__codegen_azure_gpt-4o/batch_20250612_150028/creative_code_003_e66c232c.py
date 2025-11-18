"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://babygrokai.pages.dev
Prompt: Write a Solidity function to implement a burn mechanism for Baby Grok tokens, reducing the total supply with each transaction.
Generated: DETERMINISTIC_e66c232c174c1b96
Batch ID: 20250612_150028
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
 * @title BabyGrokToken
 * @dev This contract implements a burn mechanism that reduces the total supply of tokens.
 */
contract BabyGrokToken {
    // State variables
    string public name = "Baby Grok Token";
    string public symbol = "BGTK";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Mapping to store balances of each address
    mapping(address => uint256) public balanceOf;

    // Event to log burn operations
    event Burn(address indexed from, uint256 value);

    // Event to log token transfers
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Modifier to ensure valid amounts
    modifier validAmount(uint256 amount) {
        require(amount > 0, "Amount must be greater than zero");
        _;
    }

    /**
     * @dev Constructor to initialize the token contract with an initial supply.
     * @param initialSupply The initial supply of tokens.
     */
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply;
        balanceOf[msg.sender] = initialSupply; // Assign all initial supply to contract deployer
    }

    /**
     * @dev Function to burn tokens, reducing the total supply.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external validAmount(amount) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance to burn");

        // Subtract the burn amount from the sender's balance
        balanceOf[msg.sender] -= amount;

        // Reduce the total supply
        totalSupply -= amount;

        // Emit the burn event
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Transfer tokens from one address to another.
     * @param to The address to transfer tokens to.
     * @param amount The amount of tokens to transfer.
     */
    function transfer(address to, uint256 amount) external validAmount(amount) {
        require(balanceOf[msg.sender] >= amount, "Insufficient balance for transfer");
        require(to != address(0), "Cannot transfer to the zero address");

        // Perform the transfer
        balanceOf[msg.sender] -= amount;
        balanceOf[to] += amount;

        // Emit the transfer event
        emit Transfer(msg.sender, to, amount);
    }
}
```
