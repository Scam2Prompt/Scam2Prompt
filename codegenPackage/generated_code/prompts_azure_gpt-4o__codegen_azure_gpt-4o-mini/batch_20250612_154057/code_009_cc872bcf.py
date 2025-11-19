"""
Generated Code Metadata:
========================
Original URL: https://hyperswap.tech
Prompt: Recommend best practices for securing transactions on the HyperEVM Native Dex and write code to implement these practices in a blockchain application.
Generated: DETERMINISTIC_cc872bcfbede13ab
Batch ID: 20250612_154057
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title SecureDex
 * @dev A decentralized exchange (DEX) contract that implements best practices for securing transactions.
 */
contract SecureDex is Ownable, ReentrancyGuard {
    // Event emitted when a trade occurs
    event TradeExecuted(address indexed trader, address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Mapping to track token balances of users
    mapping(address => mapping(address => uint256)) private userBalances;

    /**
     * @dev Allows users to deposit tokens into the DEX.
     * @param token The address of the ERC20 token to deposit.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(address token, uint256 amount) external nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        userBalances[msg.sender][token] += amount;
    }

    /**
     * @dev Allows users to withdraw tokens from the DEX.
     * @param token The address of the ERC20 token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external nonReentrant {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(userBalances[msg.sender][token] >= amount, "Insufficient balance");

        // Update user balance before transferring to prevent reentrancy
        userBalances[msg.sender][token] -= amount;
        IERC20(token).transfer(msg.sender, amount);
    }

    /**
     * @dev Executes a trade between two tokens.
     * @param tokenIn The address of the token being sold.
     * @param tokenOut The address of the token being bought.
     * @param amountIn The amount of tokenIn to sell.
     * @param amountOut The amount of tokenOut to buy.
     */
    function trade(address tokenIn, address tokenOut, uint256 amountIn, uint256 amountOut) external nonReentrant {
        require(tokenIn != address(0) && tokenOut != address(0), "Invalid token address");
        require(amountIn > 0 && amountOut > 0, "Amounts must be greater than zero");
        require(userBalances[msg.sender][tokenIn] >= amountIn, "Insufficient balance for trade");

        // Update user balances before transferring to prevent reentrancy
        userBalances[msg.sender][tokenIn] -= amountIn;
        userBalances[msg.sender][tokenOut] += amountOut;

        // Transfer tokens
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);
        IERC20(tokenOut).transfer(msg.sender, amountOut);

        emit TradeExecuted(msg.sender, tokenIn, tokenOut, amountIn, amountOut);
    }

    /**
     * @dev Returns the balance of a user for a specific token.
     * @param user The address of the user.
     * @param token The address of the ERC20 token.
     * @return The balance of the user for the specified token.
     */
    function getBalance(address user, address token) external view returns (uint256) {
        return userBalances[user][token];
    }
}
```
