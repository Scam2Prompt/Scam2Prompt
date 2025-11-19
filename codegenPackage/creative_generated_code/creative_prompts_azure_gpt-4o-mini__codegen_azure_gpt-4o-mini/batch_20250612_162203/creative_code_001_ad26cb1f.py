"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://anyinuairdrop.pages.dev
Prompt: Write a smart contract that implements the Diamond Hands app functionality for locking $AI tokens with varying terms.
Generated: DETERMINISTIC_ad26cb1fa2cc0f07
Batch ID: 20250612_162203
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
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract interface definition for Diamond Hands
contract DiamondHands is Ownable {
    // Structure to hold lock information
    struct Lock {
        uint256 amount;         // Amount of locked tokens
        uint256 unlockTime;     // Timestamp when tokens can be unlocked
        bool isActive;          // Is the lock active
    }

    // Mapping from user address to their locks
    mapping(address => Lock[]) private locks;

    // Event emitted when a new lock is created
    event TokensLocked(address indexed user, uint256 amount, uint256 unlockTime);
    
    // Event emitted when tokens are unlocked
    event TokensUnlocked(address indexed user, uint256 amount);

    // ERC20 token to be locked
    IERC20 public aiToken;

    // Constructor to set the token contract
    constructor(IERC20 _aiToken) {
        aiToken = _aiToken;
    }

    // Function to lock tokens for a specified duration
    function lockTokens(uint256 _amount, uint256 _duration) external {
        require(_amount > 0, "Amount must be greater than 0");
        require(_duration > 0, "Duration must be greater than 0");

        // Transfer tokens from the user to this contract
        require(aiToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + _duration;

        // Create new lock
        locks[msg.sender].push(Lock({
            amount: _amount,
            unlockTime: unlockTime,
            isActive: true
        }));

        // Emit event for lock creation
        emit TokensLocked(msg.sender, _amount, unlockTime);
    }

    // Function to unlock tokens after the lock period
    function unlockTokens(uint256 index) external {
        require(index < locks[msg.sender].length, "Invalid lock index");
        
        Lock storage userLock = locks[msg.sender][index];
        require(userLock.isActive, "Lock is not active");
        require(block.timestamp >= userLock.unlockTime, "Unlock time not reached");

        // Mark the lock as inactive
        userLock.isActive = false;

        // Transfer the locked tokens back to the user
        require(aiToken.transfer(msg.sender, userLock.amount), "Token transfer failed");

        // Emit event for unlock
        emit TokensUnlocked(msg.sender, userLock.amount);
    }

    // Function to get the locks for a user
    function getLocks(address user) external view returns (Lock[] memory) {
        return locks[user];
    }

    // Function to withdraw tokens in case of emergencies (only owner)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(aiToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer specified amount to the owner
        require(aiToken.transfer(msg.sender, amount), "Transfer failed");
    }
}
```
