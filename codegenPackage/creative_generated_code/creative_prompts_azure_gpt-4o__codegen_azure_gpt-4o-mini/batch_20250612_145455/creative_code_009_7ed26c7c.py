"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogg.pages.dev
Prompt: Write a Solidity function to resolve high gas bugs during $MOG token transactions, optimizing for lower transaction fees.
Generated: DETERMINISTIC_7ed26c7c3d1be395
Batch ID: 20250612_145455
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

contract MOGToken {
    // Event emitted when tokens are transferred
    event Transfer(address indexed from, address indexed to, uint256 value);

    // Mapping from addresses to their balance
    mapping(address => uint256) private balances;

    // Total supply of the token
    uint256 private totalSupply;

    // Constructor to initialize total supply and allocate to the contract creator
    constructor(uint256 initialSupply) {
        totalSupply = initialSupply * (10 ** 18); // Assuming token has 18 decimals
        balances[msg.sender] = totalSupply; // Allocate initial supply to the contract creator
    }

    // Function to get the balance of an address
    function balanceOf(address account) public view returns (uint256) {
        require(account != address(0), "Address cannot be zero");
        return balances[account];
    }

    // Optimized transfer function to minimize gas costs
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is not allowed");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Using unchecked to save gas; balances are checked before
        unchecked {
            balances[msg.sender] -= amount;
            balances[to] += amount;
        }

        emit Transfer(msg.sender, to, amount);
        return true;
    }

    // Function to retrieve the total supply of tokens
    function getTotalSupply() public view returns (uint256) {
        return totalSupply;
    }

    // Function to approve spending of tokens by a delegated address
    function approve(address spender, uint256 amount) public returns (bool) {
        // Approve logic should be implemented here if required
        return true;
    }

    // Function to transfer tokens from one account to another on behalf of the owner
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        // Transfer logic with allowance checks should be implemented here if required
        return true;
    }
}
```
