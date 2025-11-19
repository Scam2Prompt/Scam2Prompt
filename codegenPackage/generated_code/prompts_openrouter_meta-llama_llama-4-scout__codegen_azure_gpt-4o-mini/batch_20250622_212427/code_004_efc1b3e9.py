"""
Generated Code Metadata:
========================
Original URL: https://geoins.ru
Prompt: Develop a simple smart contract in Solidity that utilizes QiDao's collateralized stablecoin MAI for lending.
Generated: DETERMINISTIC_efc1b3e9985c61e2
Batch ID: 20250622_212427
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

// Importing the interface for the MAI token
interface IMaiToken {
    function transfer(address to, uint256 amount) external returns (bool);
    function transferFrom(address from, address to, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Simple lending contract using QiDao's MAI stablecoin
contract MaiLending {
    // State variables
    IMaiToken public maiToken; // MAI token contract
    address public owner; // Owner of the contract

    // Mapping to track user balances
    mapping(address => uint256) public userBalances;

    // Events for logging
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Loaned(address indexed user, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to set the MAI token address and the owner
    constructor(address _maiToken) {
        maiToken = IMaiToken(_maiToken);
        owner = msg.sender;
    }

    // Function to deposit MAI into the contract
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer MAI from the user to the contract
        require(maiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");
        
        // Update user balance
        userBalances[msg.sender] += amount;

        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw MAI from the contract
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender] >= amount, "Insufficient balance");

        // Update user balance
        userBalances[msg.sender] -= amount;

        // Transfer MAI back to the user
        require(maiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    // Function to loan MAI to a user
    function loan(uint256 amount) external onlyOwner {
        require(amount > 0, "Loan amount must be greater than zero");
        
        // Transfer MAI to the user
        require(maiToken.transfer(msg.sender, amount), "Transfer failed");

        emit Loaned(msg.sender, amount);
    }

    // Function to check the contract's MAI balance
    function contractBalance() external view returns (uint256) {
        return maiToken.balanceOf(address(this));
    }

    // Function to withdraw contract's MAI balance to the owner
    function withdrawContractBalance() external onlyOwner {
        uint256 balance = maiToken.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");

        // Transfer MAI to the owner
        require(maiToken.transfer(owner, balance), "Transfer failed");
    }
}
```
