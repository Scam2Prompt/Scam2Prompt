"""
Generated Code Metadata:
========================
Original URL: https://bonk-rewarded.pages.dev
Prompt: Generate a smart contract code snippet in Solidity to implement a similar locking mechanism for $BONK tokens, with a rewards multiplier based on the lock duration.
Generated: DETERMINISTIC_1dd6fd84ac32f5af
Batch ID: 20250622_205603
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
 * @title BONKTokenLock
 * @dev A smart contract to lock BONK tokens with a rewards multiplier based on lock duration.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract BONKTokenLock {
    // Address of the BONK token contract
    IERC20 public immutable bonkToken;

    // Struct to store lock details
    struct Lock {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when tokens can be unlocked
        uint256 multiplier; // Rewards multiplier based on lock duration
    }

    // Mapping of user address to their lock details
    mapping(address => Lock) public locks;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the BONK token address
    constructor(address _bonkToken) {
        require(_bonkToken != address(0), "Invalid BONK token address");
        bonkToken = IERC20(_bonkToken);
    }

    /**
     * @dev Lock BONK tokens for a specified duration.
     * @param amount Amount of BONK tokens to lock.
     * @param lockDuration Duration in seconds to lock the tokens.
     */
    function lockTokens(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");
        require(locks[msg.sender].amount == 0, "Tokens already locked");

        // Calculate unlock time and rewards multiplier
        uint256 unlockTime = block.timestamp + lockDuration;
        uint256 multiplier = calculateMultiplier(lockDuration);

        // Transfer BONK tokens from the user to the contract
        require(bonkToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store lock details
        locks[msg.sender] = Lock(amount, unlockTime, multiplier);

        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    /**
     * @dev Unlock BONK tokens and claim rewards.
     */
    function unlockTokens() external {
        Lock memory userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Calculate reward based on multiplier
        uint256 reward = userLock.amount * userLock.multiplier / 100;

        // Transfer locked tokens and reward to the user
        require(bonkToken.transfer(msg.sender, userLock.amount + reward), "Token transfer failed");

        // Clear lock details
        delete locks[msg.sender];

        emit TokensUnlocked(msg.sender, userLock.amount, reward);
    }

    /**
     * @dev Calculate rewards multiplier based on lock duration.
     * @param lockDuration Duration in seconds to lock the tokens.
     * @return multiplier Rewards multiplier as a percentage.
     */
    function calculateMultiplier(uint256 lockDuration) public pure returns (uint256) {
        if (lockDuration >= 365 days) {
            return 50; // 50% reward for 1 year or more
        } else if (lockDuration >= 180 days) {
            return 25; // 25% reward for 6 months or more
        } else if (lockDuration >= 90 days) {
            return 10; // 10% reward for 3 months or more
        } else {
            return 5; // 5% reward for less than 3 months
        }
    }
}
```
