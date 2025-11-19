"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safemoon.network
Prompt: Describe the anti-whale measures used by SafeMoon and how to integrate similar features into a new blockchain project.
Generated: DETERMINISTIC_4e307d184dcd4e07
Batch ID: 20250612_161441
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
 * @title AntiWhaleToken
 * @dev Example of integrating anti-whale measures into a token smart contract.
 * Anti-whale measures are designed to limit large transactions to prevent market manipulation.
 */
contract AntiWhaleToken {
    string public name = "AntiWhaleToken";
    string public symbol = "AWT";
    uint8 public decimals = 18;
    uint256 public totalSupply = 1_000_000 * (10 ** uint256(decimals)); // 1 million tokens

    mapping(address => uint256) public balanceOf;
    mapping(address => mapping(address => uint256)) public allowance;

    // Anti-whale settings
    uint256 public maxTransactionAmount; // Maximum amount allowed per transaction
    uint256 public maxWalletAmount; // Maximum amount allowed per wallet

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    // Constructor: Initializes the contract with the deployer as the balance owner
    constructor(uint256 _maxTransactionAmount, uint256 _maxWalletAmount) {
        require(_maxTransactionAmount > 0, "Max transaction amount must be greater than 0");
        require(_maxWalletAmount > 0, "Max wallet amount must be greater than 0");

        balanceOf[msg.sender] = totalSupply; // Assign total supply to the deployer
        maxTransactionAmount = _maxTransactionAmount;
        maxWalletAmount = _maxWalletAmount;
    }

    // Transfer function with anti-whale logic
    function transfer(address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is prohibited");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(amount <= maxTransactionAmount, "Transfer amount exceeds the maximum transaction limit");
        require(balanceOf[to] + amount <= maxWalletAmount, "Recipient wallet exceeds the maximum wallet limit");

        // Perform the transfer
        _transfer(msg.sender, to, amount);
        return true;
    }

    // Transfer function (internal)
    function _transfer(address from, address to, uint256 amount) internal {
        require(balanceOf[from] >= amount, "Insufficient balance");

        balanceOf[from] -= amount;
        balanceOf[to] += amount;

        emit Transfer(from, to, amount);
    }

    // Approve function
    function approve(address spender, uint256 amount) public returns (bool) {
        require(spender != address(0), "Approval to the zero address is prohibited");

        allowance[msg.sender][spender] = amount;
        emit Approval(msg.sender, spender, amount);
        return true;
    }

    // TransferFrom function with anti-whale logic
    function transferFrom(address from, address to, uint256 amount) public returns (bool) {
        require(to != address(0), "Transfer to the zero address is prohibited");
        require(amount > 0, "Transfer amount must be greater than zero");
        require(amount <= maxTransactionAmount, "Transfer amount exceeds the maximum transaction limit");
        require(balanceOf[to] + amount <= maxWalletAmount, "Recipient wallet exceeds the maximum wallet limit");
        require(allowance[from][msg.sender] >= amount, "Transfer amount exceeds allowance");

        // Perform the transfer
        _transfer(from, to, amount);

        // Update the allowance
        allowance[from][msg.sender] -= amount;

        return true;
    }

    // Function to update anti-whale settings (restricted to contract owner)
    function updateAntiWhaleSettings(uint256 _maxTransactionAmount, uint256 _maxWalletAmount) external {
        require(msg.sender == address(this), "Only contract owner can update anti-whale settings");
        require(_maxTransactionAmount > 0, "Max transaction amount must be greater than 0");
        require(_maxWalletAmount > 0, "Max wallet amount must be greater than 0");

        maxTransactionAmount = _maxTransactionAmount;
        maxWalletAmount = _maxWalletAmount;
    }
}
```
