"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinuairdrop.pages.dev
Prompt: Generate Solidity code for a smart contract that supports locking $AI tokens in the Diamond Hands app, including functionality for calculating multipliers based on lock duration.
Generated: DETERMINISTIC_d0d97deeeda5db50
Batch ID: 20250612_153401
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

// Importing the ERC20 interface for $AI token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// DiamondHands contract to lock $AI tokens with multipliers based on duration
contract DiamondHands {
    // Struct to hold lock details
    struct Lock {
        uint256 amount;          // Amount of tokens locked
        uint256 unlockTime;     // Time when tokens can be unlocked
        uint256 multiplier;      // Multiplier based on lock duration
    }

    // Mapping from user address to their locks
    mapping(address => Lock[]) private userLocks;

    // Reference to the $AI token contract
    IERC20 public aiToken;

    // Events for logging actions
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to set the $AI token contract address
    constructor(address _aiTokenAddress) {
        require(_aiTokenAddress != address(0), "Invalid token address");
        aiToken = IERC20(_aiTokenAddress);
    }

    // Function to lock tokens with a specified duration
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than zero");
        require(duration >= 1 weeks && duration <= 52 weeks, "Duration must be between 1 week and 52 weeks");

        // Transfer tokens from user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + duration;
        // Calculate multiplier based on duration
        uint256 multiplier = calculateMultiplier(duration);

        // Create a new lock
        userLocks[msg.sender].push(Lock(amount, unlockTime, multiplier));

        // Emit event for locking tokens
        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    // Function to unlock tokens after the lock duration
    function unlockTokens(uint256 lockIndex) external {
        Lock storage userLock = userLocks[msg.sender][lockIndex];

        require(userLock.amount > 0, "No tokens locked at this index");
        require(block.timestamp >= userLock.unlockTime, "Tokens are still locked");

        // Calculate the total amount to unlock based on the multiplier
        uint256 totalAmount = userLock.amount * userLock.multiplier;

        // Reset the user's lock
        userLock.amount = 0;

        // Transfer the unlocked tokens back to the user
        require(aiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Emit event for unlocking tokens
        emit TokensUnlocked(msg.sender, totalAmount);
    }

    // Internal function to calculate multiplier based on lock duration
    function calculateMultiplier(uint256 duration) internal pure returns (uint256) {
        if (duration >= 1 weeks && duration < 4 weeks) {
            return 1; // 1x multiplier for locks less than 1 month
        } else if (duration >= 4 weeks && duration < 12 weeks) {
            return 2; // 2x multiplier for locks between 1 month and 3 months
        } else {
            return 3; // 3x multiplier for locks of 3 months or more
        }
    }

    // Function to get the number of locks for a user
    function getUserLocksCount() external view returns (uint256) {
        return userLocks[msg.sender].length;
    }

    // Function to get lock details for a specific index
    function getUserLock(address user, uint256 lockIndex) external view returns (Lock memory) {
        return userLocks[user][lockIndex];
    }
}
```
