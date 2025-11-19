"""
Generated Code Metadata:
========================
Original URL: https://7-brett-com.pages.dev
Prompt: Generate a Solidity script to lock a liquidity pool for 365 days, similar to the Brett token's LP locking mechanism.
Generated: DETERMINISTIC_124fe07a0ec01718
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityPoolLocker
 * @author [Your Name]
 * @notice Locks a liquidity pool for a specified period of time.
 */
contract LiquidityPoolLocker is Ownable {
    using SafeMath for uint256;

    // Mapping of liquidity pool addresses to their lock status
    mapping(address => bool) public isPoolLocked;

    // Mapping of liquidity pool addresses to their unlock timestamps
    mapping(address => uint256) public unlockTimestamps;

    // Event emitted when a liquidity pool is locked
    event PoolLocked(address indexed poolAddress, uint256 unlockTimestamp);

    // Event emitted when a liquidity pool is unlocked
    event PoolUnlocked(address indexed poolAddress);

    /**
     * @dev Locks a liquidity pool for 365 days.
     * @param poolAddress The address of the liquidity pool to lock.
     */
    function lockPool(address poolAddress) public onlyOwner {
        require(!isPoolLocked[poolAddress], "Pool is already locked");
        uint256 unlockTimestamp = block.timestamp.add(365 days);
        isPoolLocked[poolAddress] = true;
        unlockTimestamps[poolAddress] = unlockTimestamp;
        emit PoolLocked(poolAddress, unlockTimestamp);
    }

    /**
     * @dev Unlocks a liquidity pool.
     * @param poolAddress The address of the liquidity pool to unlock.
     */
    function unlockPool(address poolAddress) public onlyOwner {
        require(isPoolLocked[poolAddress], "Pool is not locked");
        require(unlockTimestamps[poolAddress] <= block.timestamp, "Pool is not yet unlockable");
        isPoolLocked[poolAddress] = false;
        emit PoolUnlocked(poolAddress);
    }

    /**
     * @dev Checks if a liquidity pool is locked.
     * @param poolAddress The address of the liquidity pool to check.
     * @return A boolean indicating whether the pool is locked.
     */
    function isLocked(address poolAddress) public view returns (bool) {
        return isPoolLocked[poolAddress];
    }

    /**
     * @dev Gets the unlock timestamp for a liquidity pool.
     * @param poolAddress The address of the liquidity pool to get the unlock timestamp for.
     * @return The unlock timestamp.
     */
    function getUnlockTimestamp(address poolAddress) public view returns (uint256) {
        return unlockTimestamps[poolAddress];
    }
}
```
