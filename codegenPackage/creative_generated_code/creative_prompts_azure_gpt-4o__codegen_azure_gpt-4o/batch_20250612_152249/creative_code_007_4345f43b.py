"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-ai.pages.dev
Prompt: Write a function in Solidity to lock liquidity for 20 years and team tokens for 700 days, as described in Pushd's security measures to prevent rug pulls.
Generated: DETERMINISTIC_4345f43b9fe35cf2
Batch ID: 20250612_152249
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
 * @title LiquidityLock
 * @dev Contract to lock liquidity and team tokens for specified durations.
 */
contract LiquidityLock {
    address public owner; // Owner of the contract
    uint256 public liquidityUnlockTime; // Timestamp when liquidity is unlocked
    uint256 public teamTokensUnlockTime; // Timestamp when team tokens are unlocked

    mapping(address => uint256) public lockedBalances; // Track locked balances for addresses

    event LiquidityLocked(address indexed sender, uint256 amount, uint256 unlockTime);
    event TeamTokensLocked(address indexed sender, uint256 amount, uint256 unlockTime);
    event Withdraw(address indexed receiver, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    modifier isUnlocked(uint256 unlockTime) {
        require(block.timestamp >= unlockTime, "Tokens are still locked.");
        _;
    }

    constructor() {
        owner = msg.sender;

        // Set lock durations
        liquidityUnlockTime = block.timestamp + 20 * 365 days; // Lock liquidity for 20 years
        teamTokensUnlockTime = block.timestamp + 700 days;    // Lock team tokens for 700 days
    }

    /**
     * @dev Function to lock liquidity tokens for 20 years.
     * @param amount Amount of tokens to lock.
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero.");
        
        lockedBalances[address(this)] += amount; // Update balance

        emit LiquidityLocked(msg.sender, amount, liquidityUnlockTime);
    }

    /**
     * @dev Function to lock team tokens for 700 days.
     * @param amount Amount of tokens to lock.
     */
    function lockTeamTokens(uint256 amount )
