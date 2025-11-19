"""
Generated Code Metadata:
========================
Original URL: https://mbdfinancials-mg.pages.dev
Prompt: Write a smart contract in Solidity for managing decentralized financial transactions within the MBD Financial District, ensuring compatibility with BRC-20 tokens.
Generated: DETERMINISTIC_2e1b5aa996e1f4f2
Batch ID: 20250612_151255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the interface for BRC-20 tokens
interface IBRC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

// Smart contract for managing decentralized financial transactions
contract MBDFinancialDistrict {
    // State variables
    address public owner;
    IBRC20 public brc20Token;

    // Event declarations
    event TransactionExecuted(address indexed from, address indexed to, uint256 amount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract with the BRC-20 token address
    constructor(address _brc20Token) {
        require(_brc20Token != address(0), "Invalid token address");
        brc20Token = IBRC20(_brc20Token);
        owner = msg.sender;
    }

    // Function to execute a transaction
    function executeTransaction(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        require(brc20Token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer BRC-20 tokens to the recipient
        bool success = brc20Token.transfer(recipient, amount);
        require(success, "Token transfer failed");

        emit TransactionExecuted(msg.sender, recipient, amount);
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(brc20Token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer BRC-20 tokens to the owner
        bool success = brc20Token.transfer(owner, amount);
        require(success, "Token transfer failed");
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    // Function to check the contract's BRC-20 token balance
    function getTokenBalance() external view returns (uint256) {
        return brc20Token.balanceOf(address(this));
    }
}
```
