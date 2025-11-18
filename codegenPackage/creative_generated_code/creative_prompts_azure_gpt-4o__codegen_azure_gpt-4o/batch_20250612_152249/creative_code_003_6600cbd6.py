"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbags.pages.dev
Prompt: Develop a smart contract in Solidity that locks 20% of presale funds into a liquidity pool for two years, as described in MoonBag's liquidity strategy.
Generated: DETERMINISTIC_6600cbd6d1562369
Batch ID: 20250612_152249
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
 * @title MoonBagLiquidityLock
 * @dev A smart contract to lock 20% of presale funds into a liquidity pool for two years.
 */
contract MoonBagLiquidityLock {
    // State variables
    address public owner; // Owner of the contract
    uint256 public unlockTimestamp; // Timestamp when funds can be unlocked
    uint256 public lockedFunds; // Amount of funds locked
    address public liquidityPool; // Address of the liquidity pool

    event FundsLocked(address indexed liquidityPool, uint256 amount, uint256 unlockTimestamp);
    event FundsReleased(address indexed liquidityPool, uint256 amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    constructor(address _liquidityPool) {
        require(_liquidityPool != address(0), "Liquidity pool address cannot be zero");
        owner = msg.sender; // Assign owner
        liquidityPool = _liquidityPool; // Assign liquidity pool
        unlockTimestamp = block.timestamp + 2 * 365 days; // Lock duration: 2 years
    }

    /**
     * @dev Lock 20% of presale funds into the liquidity pool.
     * @param totalPresaleFunds The total amount of presale funds raised.
     */
    function lockFunds(uint256 totalPresaleFunds) external onlyOwner {
        require(lockedFunds == 0, "Funds have already been locked"); // Prevent double locking
        require(totalPresaleFunds > 0, "Presale funds must be greater than zero");

        // Calculate 20% of total presale funds
        uint256 amountToLock = (totalPresaleFunds * 20) / 100;

        // Transfer funds to this contract
        lockedFunds = amountToLock;

        emit FundsLocked(liquidityPool, lockedFunds, unlockTimestamp);
    }

    /**
     * @dev Release locked funds after the two-year period.
     */
    function releaseFunds() external onlyOwner {
        require(block.timestamp >= unlockTimestamp, "Funds are still locked");
        require(lockedFunds > 0, "No funds to release");

        uint256 amountToRelease = lockedFunds;

        // Reset locked funds to prevent re-entry
        lockedFunds = 0;

        // Transfer funds to the liquidity pool
        (bool success, ) = liquidityPool.call{value: amountToRelease}("");
        require(success, "Failed to transfer funds to liquidity pool");

        emit FundsReleased(liquidityPool, amountToRelease);
    }

    // Accept ETH deposits to the contract
    receive() external payable {}

    fallback() external payable {}
}
```
