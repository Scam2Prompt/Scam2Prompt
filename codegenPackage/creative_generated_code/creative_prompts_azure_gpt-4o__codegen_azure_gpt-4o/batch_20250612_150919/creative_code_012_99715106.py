"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mazza.pages.dev
Prompt: Develop a Solidity-based decentralized finance (DeFi) application for Mazze that utilizes its scalability for high-volume lending and borrowing transactions.
Generated: DETERMINISTIC_997151060c01a54e
Batch ID: 20250612_150919
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

/// @title Mazze DeFi Lending and Borrowing Contract
/// @author Mazze Developer Team
/// @notice A scalable decentralized finance application for lending and borrowing
/// @dev Follows best practices for security and high-volume transactions

contract MazzeFinance {
    // State variables
    address public owner; // Contract owner
    uint256 public totalDeposits; // Total deposits in the protocol
    uint256 public totalBorrows; // Total borrows in the protocol

    // Interest rate configuration (example: 5% annual interest rate)
    uint256 public constant annualInterestRate = 5;

    // Struct to store user account details
    struct Account {
        uint256 depositBalance;
        uint256 borrowBalance;
    }

    // Mapping to track user accounts
    mapping(address => Account) public accounts;

    // Events for logging activity
    event Deposited(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function.");
        _;
    }

    /// @notice Constructor initializes the contract owner
    constructor() {
        owner = msg.sender;
    }

    /// @notice Deposit funds into the protocol
    /// @param amount The amount to deposit
    function deposit(uint256 amount) external payable {
        require(msg.value == amount, "Sent value does not match the deposit amount.");
        require(amount > 0, "Cannot deposit zero or negative value.");

        // Update state
        accounts[msg.sender].depositBalance += amount;
        totalDeposits += amount;

        emit Deposited(msg.sender, amount);
    }

    /// @notice Borrow funds from the protocol
    /// @param amount The amount to borrow
    function borrow(uint256 amount) external {
        require(amount > 0, "Cannot borrow zero or negative value.");
        require(accounts[msg.sender].depositBalance >= amount / 2, "Insufficient collateral."); // Example collateral ratio of 50%

        // Update state
        accounts[msg.sender].borrowBalance += amount;
        totalBorrows += amount;

        // Transfer borrowed amount to borrower
        payable(msg.sender).transfer(amount);

        emit Borrowed(msg.sender, amount);
    }

    /// @notice Repay borrowed funds
    /// @param amount The amount to repay
    function repay(uint256 amount) external payable {
        require(msg.value == amount, "Sent value does not match the repayment amount.");
        require(accounts[msg.sender].borrowBalance >= amount, "Repayment exceeds borrow balance.");

        // Update state
        accounts[msg.sender].borrowBalance -= amount;
        totalBorrows -= amount;

        emit Repaid(msg.sender, amount);
    }

    /// @notice Withdraw deposited funds
    /// @param amount The amount to withdraw
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw zero or negative value.");
        require(accounts[msg.sender].depositBalance >= amount, "Insufficient balance.");

        // Update state
        accounts[msg.sender].depositBalance -= amount;
        totalDeposits -= amount;

        // Transfer withdrawn amount to user
        payable(msg.sender).transfer(amount);

        emit Withdrawn(msg.sender, amount);
    }

    /// @notice Calculate interest owed by the user
    /// @dev This is an example calculation and may need to be adjusted for production use
    /// @param user The address of the user
    /// @return interest The calculated interest
    function calculateInterest(address user) public view returns (uint256 interest) {
        uint256 borrowAmount = accounts[user].borrowBalance;
        // Example: Simple interest calculation
        interest = (borrowAmount * annualInterestRate) / 100;
    }

    /// @notice Fallback function to handle Ether sent directly to the contract
    receive() external payable {
        revert("Direct deposits not allowed. Use the deposit function.");
    }
}
```
