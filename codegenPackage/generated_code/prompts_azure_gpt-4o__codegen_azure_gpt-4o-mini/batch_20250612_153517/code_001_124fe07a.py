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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityLock
 * @dev This contract locks a specified amount of liquidity tokens for a defined period.
 */
contract LiquidityLock is Ownable {
    // Struct to hold lock information
    struct Lock {
        uint256 amount;        // Amount of tokens locked
        uint256 unlockTime;    // Timestamp when the tokens can be unlocked
    }

    // Mapping to store locks for each address
    mapping(address => Lock) public locks;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed locker, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed locker, uint256 amount);

    /**
     * @dev Locks liquidity tokens for a specified duration.
     * @param tokenAddress The address of the ERC20 token to lock.
     * @param amount The amount of tokens to lock.
     */
    function lockLiquidity(address tokenAddress, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(locks[msg.sender].amount == 0, "Existing lock must be released first");

        // Transfer tokens from the locker to this contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), amount);

        // Set the lock details
        locks[msg.sender] = Lock({
            amount: amount,
            unlockTime: block.timestamp + 365 days
        });

        emit LiquidityLocked(msg.sender, amount, locks[msg.sender].unlockTime);
    }

    /**
     * @dev Unlocks the liquidity tokens after the lock period has expired.
     */
    function unlockLiquidity() external {
        Lock storage userLock = locks[msg.sender];
        require(userLock.amount > 0, "No liquidity locked");
        require(block.timestamp >= userLock.unlockTime, "Lock period not yet expired");

        // Transfer the locked tokens back to the user
        uint256 amountToUnlock = userLock.amount;
        userLock.amount = 0; // Reset the lock amount

        IERC20(tokenAddress).transfer(msg.sender, amountToUnlock);

        emit LiquidityUnlocked(msg.sender, amountToUnlock);
    }

    /**
     * @dev Returns the unlock time for the caller's locked liquidity.
     * @return The unlock timestamp.
     */
    function getUnlockTime() external view returns (uint256) {
        return locks[msg.sender].unlockTime;
    }

    /**
     * @dev Returns the amount of locked liquidity for the caller.
     * @return The amount of locked tokens.
     */
    function getLockedAmount() external view returns (uint256) {
        return locks[msg.sender].amount;
    }
}
```
