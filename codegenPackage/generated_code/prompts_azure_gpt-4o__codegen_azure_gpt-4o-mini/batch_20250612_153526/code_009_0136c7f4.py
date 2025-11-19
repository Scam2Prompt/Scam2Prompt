"""
Generated Code Metadata:
========================
Original URL: https://brett-dvf.pages.dev
Prompt: Create a Solidity contract that locks liquidity for 365 days, similar to BRETT's LP locking mechanism. Include comments explaining each step.
Generated: DETERMINISTIC_0136c7f4e6584577
Batch ID: 20250612_153526
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
 * @dev A contract to lock liquidity for a specified duration (365 days).
 */
contract LiquidityLock is Ownable {
    // The token that is being locked
    IERC20 public token;

    // The address where the liquidity is locked
    address public liquidityAddress;

    // The timestamp when the liquidity will be unlocked
    uint256 public unlockTime;

    // Event emitted when liquidity is locked
    event LiquidityLocked(address indexed liquidityAddress, uint256 amount, uint256 unlockTime);

    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(address indexed liquidityAddress, uint256 amount);

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _token The address of the ERC20 token to be locked.
     */
    constructor(IERC20 _token) {
        token = _token;
    }

    /**
     * @dev Locks the specified amount of tokens for 365 days.
     * @param amount The amount of tokens to lock.
     * @param _liquidityAddress The address where the liquidity is held.
     */
    function lockLiquidity(uint256 amount, address _liquidityAddress) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(_liquidityAddress != address(0), "Invalid liquidity address");
        require(unlockTime == 0, "Liquidity already locked");

        // Transfer tokens from the owner to this contract
        token.transferFrom(msg.sender, address(this), amount);

        // Set the liquidity address and unlock time
        liquidityAddress = _liquidityAddress;
        unlockTime = block.timestamp + 365 days;

        emit LiquidityLocked(liquidityAddress, amount, unlockTime);
    }

    /**
     * @dev Unlocks the liquidity after the lock period has expired.
     */
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Liquidity is still locked");

        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to unlock");

        // Transfer the locked tokens back to the liquidity address
        token.transfer(liquidityAddress, balance);

        // Reset the unlock time and liquidity address
        unlockTime = 0;
        liquidityAddress = address(0);

        emit LiquidityUnlocked(liquidityAddress, balance);
    }

    /**
     * @dev Returns the current balance of the contract.
     * @return The balance of the locked tokens.
     */
    function getLockedBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
