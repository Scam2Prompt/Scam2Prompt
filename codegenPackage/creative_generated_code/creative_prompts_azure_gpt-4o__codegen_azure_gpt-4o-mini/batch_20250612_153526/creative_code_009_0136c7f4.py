"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://brett-dvf.pages.dev
Prompt: Create a Solidity contract that locks liquidity for 365 days, similar to BRETT's LP locking mechanism. Include comments explaining each step.
Generated: DETERMINISTIC_0136c7f4e6584577
Batch ID: 20250612_153526
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
 * @dev A contract to lock liquidity for a specified duration (365 days).
 */
contract LiquidityLock is Ownable {
    // The token to be locked
    IERC20 public liquidityToken;

    // The address where the tokens are locked
    address public lockAddress;

    // The timestamp until which the liquidity is locked
    uint256 public unlockTime;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed token, address indexed locker, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is released
    event LiquidityReleased(address indexed token, address indexed locker, uint256 amount);

    /**
     * @dev Constructor that sets the token to be locked.
     * @param _liquidityToken The address of the ERC20 token to lock.
     */
    constructor(IERC20 _liquidityToken) {
        liquidityToken = _liquidityToken;
    }

    /**
     * @dev Locks the specified amount of tokens for 365 days.
     * @param amount The amount of tokens to lock.
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(unlockTime == 0, "Liquidity is already locked");

        // Transfer tokens from the owner's account to the contract
        require(liquidityToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Set the unlock time to 365 days from now
        unlockTime = block.timestamp + 365 days;

        // Emit an event for the liquidity lock
        emit LiquidityLocked(address(liquidityToken), msg.sender, amount, unlockTime);
    }

    /**
     * @dev Releases the locked liquidity after 365 days.
     */
    function releaseLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Liquidity is still locked");
        require(lockAddress == address(this), "No liquidity to release");
        
        uint256 balance = liquidityToken.balanceOf(address(this));
        require(balance > 0, "No liquidity to release");

        // Transfer the tokens back to the owner
        require(liquidityToken.transfer(msg.sender, balance), "Token transfer failed");

        // Emit an event for the liquidity release
        emit LiquidityReleased(address(liquidityToken), msg.sender, balance);

        // Reset the unlock time and lock address
        unlockTime = 0;
        lockAddress = address(0);
    }

    /**
     * @dev Returns the current status of the liquidity lock.
     * @return locked Whether liquidity is locked.
     * @return unlockTime The time when liquidity will be unlocked.
     */
    function getLockStatus() external view returns (bool locked, uint256 unlockUntil) {
        locked = (unlockTime > block.timestamp);
        unlockUntil = unlockTime;
    }
}
```
