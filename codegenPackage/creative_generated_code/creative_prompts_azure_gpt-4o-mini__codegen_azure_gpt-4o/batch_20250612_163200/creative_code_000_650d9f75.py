"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Write a smart contract using Solidity for the Mazze blockchain that implements a basic token transfer functionality, ensuring EVM compatibility.
Generated: DETERMINISTIC_650d9f75a69595e2
Batch ID: 20250612_163200
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
 * @title BasicToken
 * @dev Implementation of a basic ERC20-like token for Mazze blockchain with transfer functionality.
 *      This contract ensures compatibility with the Ethereum Virtual Machine (EVM).
 */
contract BasicToken {
    // Mapping to hold balances of each address
    mapping(address => uint256) private balances;

    // Total supply of the token
    uint256 private totalSupply;

    // Event emitted when a transfer occurs
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Constructor to initialize the total supply and assign it to the contract deployer
    constructor(uint256 _initialSupply) {
        require(_initialSupply > 0, "Initial supply must be greater than 0");
        totalSupply = _initialSupply;
        balances[msg.sender] = _initialSupply; // Assign all tokens to the deployer
        emit Transfer(address(0), msg.sender, _initialSupply); // Emit a transfer event (minting)
    }

    /**
     * @dev Function to get the total supply of tokens
     * @return Total supply of the token
     */
    function getTotalSupply() external view returns (uint256) {
        return totalSupply;
    }

    /**
     * @dev Function to check the balance of a given address
     * @param account The address to query the balance of
     * @return The balance of the specified address
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Function to transfer tokens to another address
     * @param recipient The address to transfer tokens to
     * @param amount The amount of tokens to transfer
     * @return A boolean indicating whether the transfer was successful
     */
    function transfer(address recipient, uint256 amount) external returns (bool) {
        require(recipient != address(0), "Transfer to the zero address is not allowed");
        require(amount > 0, "Transfer amount must be greater than 0");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Deduct tokens from the sender's balance
        balances[msg.sender] -= amount;

        // Add tokens to the recipient's balance
        balances[recipient] += amount;

        // Emit the transfer event
        emit Transfer(msg.sender, recipient, amount);

        return true;
    }
}
```
