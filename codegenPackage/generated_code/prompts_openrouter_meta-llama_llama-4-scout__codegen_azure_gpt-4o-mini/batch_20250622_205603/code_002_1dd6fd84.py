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

// Interface for the ERC20 token
interface IBONK {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for locking BONK tokens with a rewards multiplier
contract BONKLock {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Time when tokens can be unlocked
        uint256 multiplier;     // Rewards multiplier based on lock duration
    }

    // Mapping of user addresses to their locks
    mapping(address => Lock) public locks;

    // The BONK token contract
    IBONK public bonkToken;

    // Events for logging
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to set the BONK token address
    constructor(address _bonkToken) {
        bonkToken = IBONK(_bonkToken);
    }

    // Function to lock tokens
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(bonkToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");
        require(locks[msg.sender].amount == 0, "Existing lock must be unlocked first");

        // Calculate unlock time and multiplier based on duration
        uint256 unlockTime = block.timestamp + duration;
        uint256 multiplier = calculateMultiplier(duration);

        // Transfer tokens to the contract
        require(bonkToken.transfer(address(this), amount), "Token transfer failed");

        // Store lock information
        locks[msg.sender] = Lock(amount, unlockTime, multiplier);

        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    // Function to unlock tokens and claim rewards
    function unlockTokens() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Calculate rewards based on the multiplier
        uint256 rewards = userLock.amount * userLock.multiplier / 100; // Assuming multiplier is in percentage

        // Reset the user's lock
        uint256 amountToUnlock = userLock.amount;
        delete locks[msg.sender];

        // Transfer locked tokens and rewards back to the user
        require(bonkToken.transfer(msg.sender, amountToUnlock + rewards), "Token transfer failed");

        emit TokensUnlocked(msg.sender, amountToUnlock, rewards);
    }

    // Function to calculate the rewards multiplier based on lock duration
    function calculateMultiplier(uint256 duration) internal pure returns (uint256) {
        if (duration >= 30 days) {
            return 20; // 20% for 30 days or more
        } else if (duration >= 14 days) {
            return 10; // 10% for 14 days or more
        } else if (duration >= 7 days) {
            return 5; // 5% for 7 days or more
        } else {
            return 0; // No multiplier for less than 7 days
        }
    }
}
```
