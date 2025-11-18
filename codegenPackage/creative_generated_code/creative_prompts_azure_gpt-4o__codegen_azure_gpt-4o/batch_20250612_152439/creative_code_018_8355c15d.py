"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinu-gateway.pages.dev
Prompt: Write a Solidity contract to implement a community collar ranking system for $AI holders based on the amount and duration of locked tokens.
Generated: DETERMINISTIC_8355c15d6f2aa9e3
Batch ID: 20250612_152439
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
 * @title Community Collar Ranking System for $AI Holders
 * @dev This contract allows $AI holders to lock their tokens and calculates their rank based on the amount and duration of locked tokens.
 */
contract CollarRanking {

    // Event emitted whenever a user locks tokens
    event TokensLocked(address indexed user, uint256 amount, uint256 duration, uint256 unlockTime);

    // Event emitted whenever a user withdraws locked tokens
    event TokensWithdrawn(address indexed user, uint256 amount);

    // Struct to store lock details
    struct Lock {
        uint256 amount;      // Amount of tokens locked
        uint256 unlockTime;  // Timestamp when tokens can be unlocked
        uint256 duration;    // Lock duration in seconds
    }

    // Mapping to track the locked tokens of each user
    mapping(address => Lock) public locks;

    // ERC20 token contract address for $AI tokens
    IERC20 public aiToken;

    /**
     * @dev Constructor to set the $AI token contract address.
     * @param _aiToken Address of the $AI ERC20 token contract.
     */
    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    /**
     * @dev Function to lock $AI tokens for a specific duration.
     * @param amount Amount of tokens to lock.
     * @param duration Lock duration in seconds.
     */
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Lock amount must be greater than zero");
        require(duration > 0, "Lock duration must be greater than zero");

        // Ensure no existing lock overlaps
        require(locks[msg.sender].amount == 0, "Existing lock must be withdrawn first");

        // Transfer tokens from user to contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + duration;

        // Store lock details
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: unlockTime,
            duration: duration
        });

        // Emit event
        emit TokensLocked(msg.sender, amount, duration, unlockTime);
    }

    /**
     * @dev Function to withdraw locked $AI tokens after the lock duration ends.
     */
    function withdrawTokens() external {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Lock duration not yet completed");

        // Clear user's lock
        delete locks[msg.sender];

        // Transfer tokens back to user
        require(aiToken.transfer(msg.sender, userLock.amount), "Token transfer failed");

        // Emit event
        emit TokensWithdrawn(msg.sender, userLock.amount);
    }

    /**
     * @dev Function to fetch user's rank based on locked amount and duration.
     * @return rank Calculated rank based on the lock details.
     */
    function getRank(address user) external view returns (uint256 rank) {
        Lock memory userLock = locks[user];
        if (userLock.amount == 0) {
            return 0; // No rank for users without locked tokens
        }
        // Rank is calculated as locked amount multiplied by lock duration
        rank = userLock.amount * userLock.duration;
    }
}

// Interface for ERC20 token standard
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
