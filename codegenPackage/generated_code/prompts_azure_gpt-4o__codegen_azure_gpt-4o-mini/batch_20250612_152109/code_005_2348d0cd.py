"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Develop a decentralized application (DApp) that allows users to lock $AI tokens for a specified term and receive soulbound receipt tokens. Include features for calculating multipliers based on lock duration.
Generated: DETERMINISTIC_2348d0cdf042149d
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/Counters.sol";

// Soulbound receipt token contract
contract SoulboundReceipt {
    // Mapping to track soulbound tokens for each user
    mapping(address => bool) public hasSoulboundToken;

    // Function to mint a soulbound token
    function mintSoulboundToken(address user) external {
        require(!hasSoulboundToken[user], "User already has a soulbound token");
        hasSoulboundToken[user] = true;
    }
}

// Main DApp contract for locking $AI tokens
contract TokenLock is Ownable {
    using Counters for Counters.Counter;

    // Struct to hold lock information
    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        uint256 multiplier;
    }

    // Mapping to track user locks
    mapping(address => Lock[]) public userLocks;

    // Reference to the $AI token contract
    IERC20 public aiToken;
    SoulboundReceipt public soulboundReceipt;

    // Events for logging
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $AI token address
    constructor(address _aiToken, address _soulboundReceipt) {
        aiToken = IERC20(_aiToken);
        soulboundReceipt = SoulboundReceipt(_soulboundReceipt);
    }

    // Function to lock tokens
    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(duration > 0, "Duration must be greater than 0");

        // Calculate unlock time and multiplier
        uint256 unlockTime = block.timestamp + duration;
        uint256 multiplier = calculateMultiplier(duration);

        // Transfer tokens from user to this contract
        require(aiToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Store lock information
        userLocks[msg.sender].push(Lock(amount, unlockTime, multiplier));

        // Mint soulbound token for the user
        soulboundReceipt.mintSoulboundToken(msg.sender);

        emit TokensLocked(msg.sender, amount, unlockTime, multiplier);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        uint256 totalAmount = 0;

        // Iterate through user's locks
        for (uint256 i = 0; i < userLocks[msg.sender].length; i++) {
            Lock storage userLock = userLocks[msg.sender][i];
            if (block.timestamp >= userLock.unlockTime) {
                totalAmount += userLock.amount * userLock.multiplier; // Apply multiplier
                delete userLocks[msg.sender][i]; // Remove the lock
            }
        }

        require(totalAmount > 0, "No tokens to unlock");

        // Transfer unlocked tokens back to the user
        require(aiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, totalAmount);
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
}
```
