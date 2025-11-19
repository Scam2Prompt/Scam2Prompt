"""
Generated Code Metadata:
========================
Original URL: https://hoststandart.ru
Prompt: "Generate a smart contract code in Solidity to create a simple DeFi lending platform similar to Belt Finance."
Generated: DETERMINISTIC_92ce212a00539df5
Batch ID: 20250622_212411
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Simple DeFi Lending Platform Contract
contract SimpleDeFiLending is Ownable {
    using SafeMath for uint256;

    // Struct to hold user information
    struct User {
        uint256 depositedAmount;
        uint256 borrowedAmount;
        uint256 interestRate; // Interest rate in basis points (1/100th of a percent)
    }

    // Mapping of user addresses to their information
    mapping(address => User) public users;

    // Token used for lending and borrowing
    IERC20 public token;

    // Events for logging actions
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);

    // Constructor to initialize the token
    constructor(IERC20 _token) {
        token = _token;
    }

    // Deposit tokens into the lending platform
    function deposit(uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");
        
        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), amount);
        
        // Update user information
        users[msg.sender].depositedAmount = users[msg.sender].depositedAmount.add(amount);
        
        emit Deposited(msg.sender, amount);
    }

    // Withdraw tokens from the lending platform
    function withdraw(uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(users[msg.sender].depositedAmount >= amount, "Insufficient balance to withdraw");

        // Update user information
        users[msg.sender].depositedAmount = users[msg.sender].depositedAmount.sub(amount);
        
        // Transfer tokens back to user
        token.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Borrow tokens from the lending platform
    function borrow(uint256 amount) external {
        require(amount > 0, "Borrow amount must be greater than zero");
        require(users[msg.sender].depositedAmount > 0, "No collateral deposited");
        
        // Update user information
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.add(amount);
        
        // Transfer tokens to user
        token.transfer(msg.sender, amount);
        
        emit Borrowed(msg.sender, amount);
    }

    // Repay borrowed tokens
    function repay(uint256 amount) external {
        require(amount > 0, "Repay amount must be greater than zero");
        require(users[msg.sender].borrowedAmount >= amount, "Repay amount exceeds borrowed amount");

        // Update user information
        users[msg.sender].borrowedAmount = users[msg.sender].borrowedAmount.sub(amount);
        
        // Transfer tokens from user to contract
        token.transferFrom(msg.sender, address(this), amount);
        
        emit Repaid(msg.sender, amount);
    }

    // Get user information
    function getUserInfo(address user) external view returns (uint256 depositedAmount, uint256 borrowedAmount) {
        User memory userInfo = users[user];
        return (userInfo.depositedAmount, userInfo.borrowedAmount);
    }
}
```
