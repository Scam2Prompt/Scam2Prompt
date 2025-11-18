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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the lending and borrowing functionality
interface IDeFiPlatform {
    function lend(uint256 amount) external;
    function borrow(uint256 amount) external;
}

// Main contract for the DeFi application
contract MazzeDeFi is Ownable, IDeFiPlatform {
    using SafeMath for uint256;

    // Mapping to hold user balances
    mapping(address => uint256) private balances;
    
    // Mapping to track borrowed amounts
    mapping(address => uint256) private borrowedAmounts;

    // The underlying ERC20 token used for lending and borrowing
    IERC20 public token;

    // Events for lending and borrowing actions
    event Lent(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);

    // Constructor to initialize the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to lend tokens to the protocol
    function lend(uint256 amount) external override {
        require(amount > 0, "Amount should be greater than zero");
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update user balance
        balances[msg.sender] = balances[msg.sender].add(amount);
        
        emit Lent(msg.sender, amount);
    }

    // Function to borrow tokens from the protocol
    function borrow(uint256 amount) external override {
        require(amount > 0, "Amount should be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient collateral");

        // Update borrowed amounts
        borrowedAmounts[msg.sender] = borrowedAmounts[msg.sender].add(amount);

        // Transfer tokens to the borrower
        require(token.transfer(msg.sender, amount), "Transfer failed");

        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed tokens
    function repay(uint256 amount) external {
        require(amount > 0, "Amount should be greater than zero");
        require(borrowedAmounts[msg.sender] >= amount, "Repayment exceeds borrowed amount");

        // Update borrowed amounts
        borrowedAmounts[msg.sender] = borrowedAmounts[msg.sender].sub(amount);

        // Transfer tokens back to the contract
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");
    }

    // Function to check the balance of a user
    function balanceOf(address user) external view returns (uint256) {
        return balances[user];
    }

    // Function to check the borrowed amount of a user
    function borrowedAmountOf(address user) external view returns (uint256) {
        return borrowedAmounts[user];
    }

    // Function to withdraw lent tokens by the owner (for maintenance)
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount should be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        require(token.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
