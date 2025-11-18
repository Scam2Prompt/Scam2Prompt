"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethevista.app
Prompt: Create a Solidity function that enforces a mandatory 5-day liquidity lock for new token launches, aligning with Ethervista's safeguards for user trust.
Generated: DETERMINISTIC_d10c60364114e77a
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

import "@openzeppelin/contracts/access/Ownable.sol";

contract LiquidityLock is Ownable {
    // Structure to hold lock information
    struct LockInfo {
        uint256 unlockTime; // The time when the lock will be lifted
        bool isLocked;      // Indicates if liquidity is currently locked
    }

    // Mapping from token address to its lock information
    mapping(address => LockInfo) public lockedTokens;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed token);

    // Modifier to check if the liquidity is still locked
    modifier onlyWhenLocked(address token) {
        require(lockedTokens[token].isLocked, "Liquidity is not locked.");
        require(block.timestamp < lockedTokens[token].unlockTime, "Liquidity lock has expired.");
        _;
    }

    // Modifier to check if the liquidity is unlocked
    modifier onlyWhenUnlocked(address token) {
        require(!lockedTokens[token].isLocked, "Liquidity is still locked.");
        _;
    }

    /**
     * @dev Locks liquidity for a specified token for a mandatory duration of 5 days.
     * @param token The address of the token to lock liquidity for.
     */
    function lockLiquidity(address token) external onlyOwner onlyWhenUnlocked(token) {
        // Set the lock information
        lockedTokens[token].unlockTime = block.timestamp + 5 days; // Set unlock time to 5 days from now
        lockedTokens[token].isLocked = true; // Mark the token as locked

        // Emit an event for locking liquidity
        emit LiquidityLocked(token, lockedTokens[token].unlockTime);
    }

    /**
     * @dev Unlocks liquidity for the specified token if the lock is expired.
     * @param token The address of the token to unlock liquidity for.
     */
    function unlockLiquidity(address token) external onlyOwner onlyWhenLocked(token) {
        // Check if the lock period has expired
        require(block.timestamp >= lockedTokens[token].unlockTime, "Liquidity lock is still active.");

        // Reset lock information
        lockedTokens[token].isLocked = false;

        // Emit an event for unlocking liquidity
        emit LiquidityUnlocked(token);
    }

    /**
     * @dev Checks if the specified token's liquidity is locked.
     * @param token The address of the token to check.
     * @return bool indicating if the liquidity is locked.
     */
    function isLiquidityLocked(address token) external view returns (bool) {
        return lockedTokens[token].isLocked;
    }

    /**
     * @dev Returns the unlock time of the specified token's liquidity.
     * @param token The address of the token to check.
     * @return uint256 representing the unlock time.
     */
    function getUnlockTime(address token) external view returns (uint256) {
        return lockedTokens[token].unlockTime;
    }
}
```
