"""
Generated Code Metadata:
========================
Original URL: https://meteora-app-git-deposit-one-tx-wowcats.vercel.app
Prompt: "Generate a smart contract code snippet for creating a multi-token pool on Meteora, including yield calculation based on 365d Yield / TVL."
Generated: DETERMINISTIC_21ff7dfdae5594b5
Batch ID: 20250622_204901
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

/**
 * @title MultiTokenPool
 * @dev A smart contract for creating a multi-token pool on Meteora with yield calculation.
 */
contract MultiTokenPool {
    // Struct to store token information
    struct TokenInfo {
        uint256 totalDeposited; // Total amount of tokens deposited
        uint256 yieldRate;      // Annual yield rate (percentage, e.g., 5 for 5%)
    }

    // Mapping to store token information by token address
    mapping(address => TokenInfo) public tokenPool;

    // Mapping to store user balances by token address and user address
    mapping(address => mapping(address => uint256)) public userBalances;

    // Event emitted when tokens are deposited
    event TokensDeposited(address indexed user, address indexed token, uint256 amount);

    // Event emitted when tokens are withdrawn
    event TokensWithdrawn(address indexed user, address indexed token, uint256 amount);

    // Event emitted when yield is claimed
    event YieldClaimed(address indexed user, address indexed token, uint256 yieldAmount);

    /**
     * @dev Deposit tokens into the pool.
     * @param token The address of the token to deposit.
     * @param amount The amount of tokens to deposit.
     */
    function deposit(address token, uint256 amount) external {
        require(amount > 0, "Deposit amount must be greater than zero");

        // Transfer tokens from the user to the contract
        require(
            IERC20(token).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Update user balance and total deposited for the token
        userBalances[token][msg.sender] += amount;
        tokenPool[token].totalDeposited += amount;

        emit TokensDeposited(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the pool.
     * @param token The address of the token to withdraw.
     * @param amount The amount of tokens to withdraw.
     */
    function withdraw(address token, uint256 amount) external {
        require(amount > 0, "Withdraw amount must be greater than zero");
        require(
            userBalances[token][msg.sender] >= amount,
            "Insufficient balance to withdraw"
        );

        // Update user balance and total deposited for the token
        userBalances[token][msg.sender] -= amount;
        tokenPool[token].totalDeposited -= amount;

        // Transfer tokens from the contract to the user
        require(
            IERC20(token).transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensWithdrawn(msg.sender, token, amount);
    }

    /**
     * @dev Claim yield for a specific token.
     * @param token The address of the token to claim yield for.
     */
    function claimYield(address token) external {
        uint256 userBalance = userBalances[token][msg.sender];
        require(userBalance > 0, "No balance to claim yield");

        // Calculate yield based on 365-day yield formula
        uint256 yieldRate = tokenPool[token].yieldRate;
        uint256 yieldAmount = (userBalance * yieldRate) / 100 / 365;

        // Transfer yield to the user
        require(
            IERC20(token).transfer(msg.sender, yieldAmount),
            "Yield transfer failed"
        );

        emit YieldClaimed(msg.sender, token, yieldAmount);
    }

    /**
     * @dev Set the annual yield rate for a specific token.
     * @param token The address of the token.
     * @param yieldRate The annual yield rate (percentage, e.g., 5 for 5%).
     */
    function setYieldRate(address token, uint256 yieldRate) external {
        // Only the contract owner can set the yield rate (add access control as needed)
        tokenPool[token].yieldRate = yieldRate;
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
