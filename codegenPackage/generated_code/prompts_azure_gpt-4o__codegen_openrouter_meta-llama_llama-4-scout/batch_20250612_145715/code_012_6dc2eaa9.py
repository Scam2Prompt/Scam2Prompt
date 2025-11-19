"""
Generated Code Metadata:
========================
Original URL: https://everlodge-claimv2.pages.dev
Prompt: Write a Solidity contract that includes functionality for locking liquidity pools, similar to Everlodge's roadmap for Uniswap listings.
Generated: DETERMINISTIC_6dc2eaa98962e232
Batch ID: 20250612_145715
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title LiquidityPoolLocker
 * @author [Your Name]
 * @notice A contract for locking liquidity pools, inspired by Everlodge's roadmap for Uniswap listings.
 */
contract LiquidityPoolLocker is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of liquidity pool addresses to their lock status
    mapping(address => bool) public lockedPools;

    // Mapping of liquidity pool addresses to their unlock timestamps
    mapping(address => uint256) public unlockTimestamps;

    // Event emitted when a liquidity pool is locked
    event PoolLocked(address indexed poolAddress, uint256 unlockTimestamp);

    // Event emitted when a liquidity pool is unlocked
    event PoolUnlocked(address indexed poolAddress);

    // Error thrown when attempting to lock an already locked pool
    error PoolAlreadyLocked();

    // Error thrown when attempting to unlock an unlocked pool
    error PoolNotLocked();

    // Error thrown when unlock timestamp is in the past
    error UnlockTimestampInThePast();

    /**
     * @notice Locks a liquidity pool for a specified duration.
     * @param poolAddress The address of the liquidity pool to lock.
     * @param unlockTimestamp The timestamp at which the pool will be unlocked.
     */
    function lockPool(address poolAddress, uint256 unlockTimestamp) external nonReentrant {
        if (lockedPools[poolAddress]) {
            revert PoolAlreadyLocked();
        }

        if (unlockTimestamp <= block.timestamp) {
            revert UnlockTimestampInThePast();
        }

        lockedPools[poolAddress] = true;
        unlockTimestamps[poolAddress] = unlockTimestamp;

        emit PoolLocked(poolAddress, unlockTimestamp);
    }

    /**
     * @notice Unlocks a liquidity pool.
     * @param poolAddress The address of the liquidity pool to unlock.
     */
    function unlockPool(address poolAddress) external nonReentrant {
        if (!lockedPools[poolAddress]) {
            revert PoolNotLocked();
        }

        if (unlockTimestamps[poolAddress] > block.timestamp) {
            revert UnlockTimestampInThePast();
        }

        lockedPools[poolAddress] = false;
        delete unlockTimestamps[poolAddress];

        emit PoolUnlocked(poolAddress);
    }

    /**
     * @notice Checks if a liquidity pool is locked.
     * @param poolAddress The address of the liquidity pool to check.
     * @return A boolean indicating whether the pool is locked.
     */
    function isPoolLocked(address poolAddress) external view returns (bool) {
        return lockedPools[poolAddress];
    }

    /**
     * @notice Retrieves the unlock timestamp for a liquidity pool.
     * @param poolAddress The address of the liquidity pool.
     * @return The unlock timestamp.
     */
    function getUnlockTimestamp(address poolAddress) external view returns (uint256) {
        return unlockTimestamps[poolAddress];
    }
}
```
