"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimanyinu.pages.dev
Prompt: Generate Solidity code for a smart contract that supports locking $AI tokens for a specified duration, with multipliers based on lock duration as described in the Diamond Hands app.
Generated: DETERMINISTIC_0bf986d9d0a24e80
Batch ID: 20250612_152710
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

// Import OpenZeppelin's ERC20 interface and Ownable contract
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the Lock contract
contract AITokenLock is Ownable {
    // Token interface for the $AI token
    IERC20 public aiToken;

    // Struct to hold lock information
    struct LockInfo {
        uint256 amount;         // Amount of locked tokens
        uint256 unlockTime;     // Time when tokens can be unlocked
        uint256 multiplier;     // Multiplier based on lock duration
    }

    // Mapping from user addresses to their lock information
    mapping(address => LockInfo) public locks;

    // Events for logging actions
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime, uint256 multiplier);
    event TokensUnlocked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with the $AI token address
    constructor(IERC20 _aiToken) {
        require(address(_aiToken) != address(0), "Invalid token address");
        aiToken = _aiToken;
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than zero");
        require(_duration >= 7 days, "Minimum lock duration is 7 days");
        require(_duration <= 365 days, "Maximum lock duration is 365 days");

        // Calculate unlock time and multiplier based on duration
        uint256 unlockTime = block.timestamp + _duration;
        uint256 multiplier = calculateMultiplier(_duration);

        // Transfer tokens from user to the contract
        require(aiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's lock information
        locks[msg.sender] = LockInfo({
            amount: _amount,
            unlockTime: unlockTime,
            multiplier: multiplier
        });

        emit TokensLocked(msg.sender, _amount, unlockTime, multiplier);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens() external {
        LockInfo memory lockInfo = locks[msg.sender];

        require(lockInfo.amount > 0, "No tokens locked");
        require(block.timestamp >= lockInfo.unlockTime, "Tokens are still locked");

        // Calculate the total amount including the multiplier
        uint256 totalAmount = lockInfo.amount * lockInfo.multiplier;

        // Reset lock information
        delete locks[msg.sender];

        // Transfer tokens back to the user
        require(aiToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, totalAmount);
    }

    // Internal function to calculate multiplier based on duration
    function calculateMultiplier(uint256 _duration) internal pure returns (uint256) {
        if (_duration < 30 days) {
            return 1; // 1x multiplier for less than 30 days
        } else if (_duration < 90 days) {
            return 2; // 2x multiplier for 30 to 90 days
        } else if (_duration < 365 days) {
            return 3; // 3x multiplier for 90 to 365 days
        } else {
            return 4; // 4x multiplier for exactly 365 days
        }
    }
}
```
