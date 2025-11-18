"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://usdc.name
Prompt: Generate Solidity code for a smart contract that integrates USDC for DeFi lending and borrowing functionality.
Generated: DETERMINISTIC_b7c864daf755ae66
Batch ID: 20250612_154002
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

// Importing the interface for ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// A simple DeFi lending and borrowing contract
contract DeFiLending {

    // Define events for lending and borrowing actions
    event Lend(address indexed lender, uint256 amount);
    event Borrow(address indexed borrower, uint256 amount);
    event Repay(address indexed borrower, uint256 amount);

    // USDC token contract instance
    IERC20 public usdc;

    // Mapping to track lent amounts per user
    mapping(address => uint256) public lentAmounts;

    // Mapping to track borrowed amounts per user
    mapping(address => uint256) public borrowedAmounts;

    // Constructor to initialize USDC token address
    constructor(address _usdcAddress) {
        require(_usdcAddress != address(0), "USDC address cannot be zero.");
        usdc = IERC20(_usdcAddress);
    }

    // Function for users to lend USDC
    function lend(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");

        // Transfer USDC from lender to contract
        bool success = usdc.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed.");

        // Update the lent amount for the lender
        lentAmounts[msg.sender] += amount;

        emit Lend(msg.sender, amount);
    }

    // Function for users to borrow USDC
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(lentAmounts[msg.sender] > 0, "No funds available to borrow.");

        // Update the borrowed amount for the borrower
        borrowedAmounts[msg.sender] += amount;

        // Transfer USDC from the contract to the borrower
        bool success = usdc.transfer(msg.sender, amount);
        require(success, "Transfer failed.");

        emit Borrow(msg.sender, amount);
    }

    // Function for users to repay borrowed USDC
    function repay(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero.");
        require(borrowedAmounts[msg.sender] >= amount, "Repay amount exceeds borrowed amount.");

        // Transfer USDC from borrower to contract
        bool success = usdc.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed.");

        // Update the borrowed amount for the borrower
        borrowedAmounts[msg.sender] -= amount;

        emit Repay(msg.sender, amount);
    }

    // Function to view the lent amount of a user
    function viewLentAmount(address user) external view returns (uint256) {
        return lentAmounts[user];
    }

    // Function to view the borrowed amount of a user
    function viewBorrowedAmount(address user) external view returns (uint256) {
        return borrowedAmounts[user];
    }
}
```
