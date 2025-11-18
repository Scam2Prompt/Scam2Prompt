"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://predelin.ru
Prompt: Write a Solidity smart contract to interact with Beethoven X's liquidity pools, enabling users to deposit and withdraw assets securely.
Generated: DETERMINISTIC_577661778558df45
Batch ID: 20250612_154829
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Beethoven X liquidity pool
interface IBeethovenXPool {
    function deposit(uint256 amount, address token) external;
    function withdraw(uint256 amount, address token) external;
}

contract BeethovenXLiquidityManager is Ownable, ReentrancyGuard {
    // The Beethoven X pool contract address
    IBeethovenXPool public pool;

    // Mapping to track user deposits
    mapping(address => mapping(address => uint256)) private userBalances;

    // Event emitted when a user deposits tokens
    event Deposited(address indexed user, address indexed token, uint256 amount);

    // Event emitted when a user withdraws tokens
    event Withdrawn(address indexed user, address indexed token, uint256 amount);

    // Constructor to set the Beethoven X pool address
    constructor(address poolAddress) {
        require(poolAddress != address(0), "Invalid pool address");
        pool = IBeethovenXPool(poolAddress);
    }

    // Function to deposit tokens into the Beethoven X liquidity pool
    function deposit(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Deposit amount must be greater than zero");
        require(token != address(0), "Invalid token address");

        // Transfer tokens from user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Update user balance
        userBalances[msg.sender][token] += amount;

        // Deposit tokens into the Beethoven X pool
        IERC20(token).approve(address(pool), amount);
        pool.deposit(amount, token);

        emit Deposited(msg.sender, token, amount);
    }

    // Function to withdraw tokens from the Beethoven X liquidity pool
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");

        // Withdraw tokens from the Beethoven X pool
        pool.withdraw(amount, token);

        // Update user balance
        userBalances[msg.sender][token] -= amount;

        // Transfer tokens back to the user
        IERC20(token).transfer(msg.sender, amount);

        emit Withdrawn(msg.sender, token, amount);
    }

    // Function to check the user's balance of a specific token
    function balanceOf(address user, address token) external view returns (uint256) {
        return userBalances[user][token];
    }

    // Function to set a new Beethoven X pool address (only owner)
    function setPoolAddress(address poolAddress) external onlyOwner {
        require(poolAddress != address(0), "Invalid pool address");
        pool = IBeethovenXPool(poolAddress);
    }
}
```
