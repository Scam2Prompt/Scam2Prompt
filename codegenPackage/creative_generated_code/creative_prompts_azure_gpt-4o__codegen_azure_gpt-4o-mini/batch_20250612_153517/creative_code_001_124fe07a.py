"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7-brett-com.pages.dev
Prompt: Generate a Solidity script to lock a liquidity pool for 365 days, similar to the Brett token's LP locking mechanism.
Generated: DETERMINISTIC_124fe07a0ec01718
Batch ID: 20250612_153517
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

/**
 * @title LiquidityLock
 * @dev This contract locks a specified amount of liquidity tokens 
 * for a predetermined duration (365 days).
 */
contract LiquidityLock is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;      // Amount of tokens locked
        uint256 unlockTime;  // Time when the tokens can be unlocked
    }

    // Mapping of liquidity token addresses to their respective locks
    mapping(address => Lock) public locks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, uint256 amount, uint256 unlockTime);
    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed token, uint256 amount);

    /**
     * @dev Locks the specified amount of liquidity tokens for 365 days.
     * @param token Address of the liquidity token to be locked.
     * @param amount Amount of tokens to lock.
     */
    function lockLiquidity(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer the tokens from the owner to the contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        
        // Set the lock details
        locks[token] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 365 days
        });

        emit LiquidityLocked(token, amount, locks[token].unlockTime);
    }

    /**
     * @dev Unlocks the liquidity tokens after the lock period has ended.
     * Only the owner can call this function.
     * @param token Address of the liquidity token to unlock.
     */
    function unlockLiquidity(address token) external onlyOwner {
        Lock storage lock = locks[token];
        
        // Check if the lock exists and if the unlock time has passed
        require(lock.amount > 0, "No liquidity locked");
        require(block.timestamp >= lock.unlockTime, "Lock period not expired");
        
        // Transfer the locked tokens back to the owner
        uint256 amountToUnlock = lock.amount;
        lock.amount = 0; // Set to zero to prevent re-entrancy
        IERC20(token).transfer(msg.sender, amountToUnlock);

        emit LiquidityUnlocked(token, amountToUnlock);
    }

    /**
     * @dev Returns the lock information for a specific token.
     * @param token Address of the liquidity token.
     * @return amount Amount of tokens locked.
     * @return unlockTime Time when the tokens can be unlocked.
     */
    function getLockInfo(address token) external view returns (uint256 amount, uint256 unlockTime) {
        Lock storage lock = locks[token];
        return (lock.amount, lock.unlockTime);
    }
}
```
