"""
Generated Code Metadata:
========================
Original URL: https://moonbags.pages.dev
Prompt: Develop a smart contract in Solidity that locks 20% of presale funds into a liquidity pool for two years, as described in MoonBag's liquidity strategy.
Generated: DETERMINISTIC_6600cbd6d1562369
Batch ID: 20250612_152249
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract LiquidityLock is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The token to be locked
    address public liquidityPool; // Address of the liquidity pool
    uint256 public lockAmount; // Amount to lock
    uint256 public unlockTime; // Time when the funds can be unlocked

    // Events
    event LiquidityLocked(uint256 amount, uint256 unlockTime);
    event LiquidityUnlocked(uint256 amount);

    // Constructor to initialize the contract
    constructor(IERC20 _token, address _liquidityPool) {
        token = _token;
        liquidityPool = _liquidityPool;
    }

    // Function to lock 20% of presale funds into the liquidity pool
    function lockLiquidity(uint256 presaleAmount) external onlyOwner {
        require(presaleAmount > 0, "Presale amount must be greater than zero");
        
        // Calculate 20% of the presale amount
        lockAmount = presaleAmount.mul(20).div(100);
        require(lockAmount > 0, "Lock amount must be greater than zero");

        // Transfer tokens to the liquidity pool
        require(token.transferFrom(msg.sender, liquidityPool, lockAmount), "Token transfer failed");

        // Set unlock time to two years from now
        unlockTime = block.timestamp + 730 days;

        emit LiquidityLocked(lockAmount, unlockTime);
    }

    // Function to unlock liquidity after the lock period
    function unlockLiquidity() external onlyOwner {
        require(block.timestamp >= unlockTime, "Liquidity is still locked");

        // Transfer the locked tokens back to the owner
        require(token.transfer(msg.sender, lockAmount), "Token transfer failed");

        emit LiquidityUnlocked(lockAmount);
        
        // Reset lock amount and unlock time
        lockAmount = 0;
        unlockTime = 0;
    }

    // Function to check the current lock status
    function getLockStatus() external view returns (uint256 amountLocked, uint256 timeRemaining) {
        amountLocked = lockAmount;
        if (block.timestamp < unlockTime) {
            timeRemaining = unlockTime - block.timestamp;
        } else {
            timeRemaining = 0;
        }
    }
}
```
