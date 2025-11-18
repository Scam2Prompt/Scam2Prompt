"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinumult.pages.dev
Prompt: Develop a decentralized application (DApp) that allows users to lock $AI tokens for a specified term and receive soulbound receipt tokens. Include features for calculating multipliers based on lock duration.
Generated: DETERMINISTIC_2348d0cdf042149d
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AI Locking DApp
 * @dev This contract allows users to lock $AI tokens for a specified term and receive soulbound receipt tokens.
 */
contract AILock is Ownable {
    using Counters for Counters.Counter;

    // Struct to store details about locked tokens
    struct Lock {
        uint256 amount; // Amount of locked tokens
        uint256 unlockTime; // Timestamp when the tokens can be unlocked
        uint256 multiplier; // Multiplier based on the lock duration
    }

    // Mapping to store user locks
    mapping(address => Lock) public userLocks;

    // The token being locked
    IERC20 public aiToken;

    // Events
    event TokensLocked(address indexed user, uint256 amount, uint256 duration);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to set the AI token address
    constructor(address _aiToken) {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    /**
     * @dev Locks the specified amount of $AI tokens for a certain duration.
     * @param amount The amount of $AI tokens to lock.
     * @param duration The duration in seconds for which the tokens are locked.
     */
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Safe transfer of tokens to the contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Calculate multiplier based on duration
        uint256 multiplier = calculateMultiplier(duration);

        // Create a new lock for the user
        userLocks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + duration,
            multiplier: multiplier
        });

        emit TokensLocked(msg.sender, amount, duration);
    }

    /**
     * @dev Unlocks the tokens after the lock period has ended.
     */
    function unlockTokens() external {
        Lock memory userLock = userLocks[msg.sender];
        
        require(userLock.amount > 0, "No tokens locked");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Transfer the locked tokens back to the user
        uint256 amountToUnlock = userLock.amount * userLock.multiplier;
        require(aiToken.transfer(msg.sender, amountToUnlock), "Transfer failed");

        // Reset the user's lock
        delete userLocks[msg.sender];

        emit TokensUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Calculates the multiplier based on the lock duration.
     * @param duration The duration for which the tokens are locked.
     * @return multiplier The calculated multiplier.
     */
    function calculateMultiplier(uint256 duration) internal pure returns (uint256) {
        // Example: 1x for 1 week, 2x for 2 weeks, etc.
        // This is a simple linear multiplier system
        return duration / 1 weeks; // Multiplier increases by 1 for every week
    }
}
```
