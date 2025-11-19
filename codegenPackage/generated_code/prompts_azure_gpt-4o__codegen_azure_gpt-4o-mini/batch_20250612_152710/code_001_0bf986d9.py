"""
Generated Code Metadata:
========================
Original URL: https://claimanyinu.pages.dev
Prompt: Generate Solidity code for a smart contract that supports locking $AI tokens for a specified duration, with multipliers based on lock duration as described in the Diamond Hands app.
Generated: DETERMINISTIC_0bf986d9d0a24e80
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for locking AI tokens with multipliers based on lock duration
contract AITokenLocker is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
        uint256 multiplier;     // Multiplier based on lock duration
    }

    // Mapping to track user locks
    mapping(address => Lock[]) public userLocks;

    // Reference to the AI token contract
    IERC20 public aiToken;

    // Events for logging
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to set the AI token address
    constructor(IERC20 _aiToken) {
        aiToken = _aiToken;
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Calculate unlock time and multiplier based on duration
        uint256 unlockTime = block.timestamp + duration;
        uint256 multiplier = calculateMultiplier(duration);

        // Transfer tokens from user to this contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store the lock information
        userLocks[msg.sender].push(Lock(amount, unlockTime, multiplier));

        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        uint256 totalUnlocked = 0;

        // Iterate through user's locks
        for (uint256 i = 0; i < userLocks[msg.sender].length; i++) {
            Lock storage userLock = userLocks[msg.sender][i];

            // Check if the lock is expired
            if (block.timestamp >= userLock.unlockTime) {
                totalUnlocked += userLock.amount * userLock.multiplier;

                // Remove the lock (optional: can be optimized)
                delete userLocks[msg.sender][i];
            }
        }

        require(totalUnlocked > 0, "No tokens available for unlock");

        // Transfer unlocked tokens back to the user
        require(aiToken.transfer(msg.sender, totalUnlocked), "Token transfer failed");

        emit TokensUnlocked(msg.sender, totalUnlocked);
    }

    // Function to calculate multiplier based on lock duration
    function calculateMultiplier(uint256 duration) internal pure returns (uint256) {
        if (duration >= 30 days) {
            return 3; // 3x multiplier for 30 days or more
        } else if (duration >= 14 days) {
            return 2; // 2x multiplier for 14 days or more
        } else {
            return 1; // 1x multiplier for less than 14 days
        }
    }

    // Function to withdraw tokens in case of emergency (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(aiToken.transfer(msg.sender, amount), "Token transfer failed");
    }
}
```
