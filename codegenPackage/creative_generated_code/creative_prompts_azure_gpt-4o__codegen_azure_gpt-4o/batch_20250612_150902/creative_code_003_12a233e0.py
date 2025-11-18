"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-org.pages.dev
Prompt: Create a function in Solidity for a smart contract that locks liquidity for a specified period, similar to MoonBag's liquidity mechanism.
Generated: DETERMINISTIC_12a233e00b05454b
Batch ID: 20250612_150902
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
 * @title LiquidityLocker
 * @dev A smart contract that locks liquidity for a specified period.
 */
contract LiquidityLocker {
    // Struct to represent a locked liquidity entry
    struct LiquidityLock {
        uint256 amount; // Amount of tokens locked
        uint256 unlockTime; // Timestamp when the lock expires
        address tokenAddress; // ERC20 token address for the liquidity lock
        address owner; // Owner of the locked tokens
    }

    // Mapping to store liquidity locks by ID
    mapping(uint256 => LiquidityLock) public liquidityLocks;

    // Counter for tracking lock IDs
    uint256 public lockIdCounter;

    // Event emitted when liquidity is locked
    event LiquidityLocked(
        uint256 lockId,
        address indexed owner,
        address indexed tokenAddress,
        uint256 amount,
        uint256 unlockTime
    );

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(
        uint256 lockId,
        address indexed owner,
        address indexed tokenAddress,
        uint256 amount
    );

    /**
     * @dev Locks liquidity by transferring tokens to the contract and storing lock information.
     * @param tokenAddress The address of the ERC20 token to lock.
     * @param amount The amount of tokens to lock.
     * @param lockDuration The duration (in seconds) to lock the tokens.
     */
    function lockLiquidity(
        address tokenAddress,
        uint256 amount,
        uint256 lockDuration
    ) external {
        require(tokenAddress != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        // Increment lock ID counter
        lockIdCounter++;

        // Calculate unlock time
        uint256 unlockTime = block.timestamp + lockDuration;

        // Create LiquidityLock entry
        LiquidityLock memory newLock = LiquidityLock({
            amount: amount,
            unlockTime: unlockTime,
            tokenAddress: tokenAddress,
            owner: msg.sender
        });

        // Store the lock in the mapping
        liquidityLocks[lockIdCounter] = newLock;

        // Transfer tokens from sender to contract
        bool success = IERC20(tokenAddress).transferFrom(
            msg.sender,
            address(this),
            amount
        );
        require(success, "Token transfer failed");

        // Emit LiquidityLocked event
        emit LiquidityLocked(lockIdCounter, msg.sender, tokenAddress, amount, unlockTime);
    }

    /**
     * @dev Unlocks liquidity if the lock period has expired.
     * @param lockId The ID of the liquidity lock to unlock.
     */
    function unlockLiquidity(uint256 lockId) external {
        // Retrieve the lock from the mapping
        LiquidityLock storage lock = liquidityLocks[lockId];

        require(lock.owner == msg.sender, "Only owner can unlock liquidity");
        require(block.timestamp >= lock.unlockTime, "Lock period not expired");

        // Store relevant details before deletion
        uint256 amount = lock.amount;
        address tokenAddress = lock.tokenAddress;

        // Remove the lock entry
        delete liquidityLocks[lockId];

        // Transfer tokens back to the owner
        bool success = IERC20(tokenAddress).transfer(lock.owner, amount);
        require(success, "Token transfer failed");

        // Emit LiquidityUnlocked event
        emit LiquidityUnlocked(lockId, lock.owner, tokenAddress, amount);
    }
}

// Minimal ERC20 interface to interact with tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
