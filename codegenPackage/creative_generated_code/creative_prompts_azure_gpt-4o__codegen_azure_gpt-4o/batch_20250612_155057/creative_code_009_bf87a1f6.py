"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethevista.app
Prompt: Write a Solidity contract that integrates Ethervista's "Hardlock" feature for locking liquidity with customizable parameters.
Generated: DETERMINISTIC_bf87a1f65be7edf2
Batch ID: 20250612_155057
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
 * @title HardlockLiquidity
 * @dev A Solidity contract to lock liquidity using Ethervista's "Hardlock" feature,
 * with customizable parameters for lock duration and recipient.
 */
contract HardlockLiquidity {
    // Struct definition for a liquidity lock
    struct LiquidityLock {
        address token;        // Address of the token being locked
        uint256 amount;       // Amount of tokens locked
        uint256 unlockTime;   // Timestamp when tokens can be unlocked
        address owner;        // Owner of the locked tokens
    }

    // Mapping to store all liquidity locks by ID
    mapping(uint256 => LiquidityLock) public locks;
    uint256 public nextLockId; // Incremental ID for newly created locks

    // Event emitted when liquidity is locked
    event LiquidityLocked(
        uint256 indexed lockId,
        address indexed token,
        uint256 amount,
        uint256 unlockTime,
        address indexed owner
    );

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(uint256 indexed lockId, address indexed owner);

    /**
     * @dev Locks liquidity for a specified duration.
     * @param token The address of the token to lock.
     * @param amount The amount of tokens to lock.
     * @param lockDuration The duration in seconds to lock the tokens.
     */
    function lockLiquidity(
        address token,
        uint256 amount,
        uint256 lockDuration
    ) external {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        require(lockDuration > 0, "Lock duration must be greater than zero");

        uint256 unlockTime = block.timestamp + lockDuration;

        // Transfer tokens from the sender to this contract
        require(
            IERC20(token).transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        // Create a new liquidity lock
        locks[nextLockId] = LiquidityLock({
            token: token,
            amount: amount,
            unlockTime: unlockTime,
            owner: msg.sender
        });

        // Emit an event for the new lock
        emit LiquidityLocked(nextLockId, token, amount, unlockTime, msg.sender);

        // Increment the lock ID for the next lock
        nextLockId++;
    }

    /**
     * @dev Unlocks liquidity once the lock duration has expired.
     * @param lockId The ID of the lock to unlock.
     */
    function unlockLiquidity(uint256 lockId) external {
        LiquidityLock storage lock = locks[lockId];

        require(lock.owner == msg.sender, "Not the owner of this lock");
        require(block.timestamp >= lock.unlockTime, "Lock duration not yet expired");
        require(lock.amount > 0, "No tokens to unlock");

        uint256 amount = lock.amount;
        address token = lock.token;

        // Reset the lock
        lock.amount = 0;

        // Transfer the tokens back to the owner
        require(IERC20(token).transfer(msg.sender, amount), "Token transfer failed");

        // Emit an event for the unlock
        emit LiquidityUnlocked(lockId, msg.sender);
    }

    /**
     * @dev Returns information about a liquidity lock.
     * @param lockId The ID of the lock to query.
     * @return token The address of the token locked.
     * @return amount The amount of tokens locked.
     * @return unlockTime The timestamp when the lock expires.
     * @return owner The owner of the lock.
     */
    function getLock(uint256 lockId)
        external
        view
        returns (
            address token,
            uint256 amount,
            uint256 unlockTime,
            address owner
        )
    {
        LiquidityLock storage lock = locks[lockId];
        return (lock.token, lock.amount, lock.unlockTime, lock.owner);
    }
}

// Interface for interacting with ERC20 tokens
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
