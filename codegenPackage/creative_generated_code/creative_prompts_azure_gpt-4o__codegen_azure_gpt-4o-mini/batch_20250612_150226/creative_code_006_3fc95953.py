"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushdtoken.pages.dev
Prompt: Develop a Solidity contract for locking liquidity in a blockchain-based marketplace like Pushd, ensuring liquidity is locked for 20 years to prevent rug pulls.
Generated: DETERMINISTIC_3fc959534b06c02b
Batch ID: 20250612_150226
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
 * @title LiquidityLocker
 * @dev This contract locks liquidity for a specified duration (20 years) to prevent rug pulls.
 */
contract LiquidityLocker {
    // State variables
    address public owner;             // Address of the contract owner
    uint256 public lockEndTime;       // Time until liquidity can be unlocked
    bool public liquidityLocked;       // Status of liquidity lock

    // Event emitted when liquidity is locked
    event LiquidityLocked(uint256 amount, uint256 lockEndTime);
    // Event emitted when liquidity is unlocked
    event LiquidityUnlocked(uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Modifier to check if liquidity is currently locked
    modifier whenLocked() {
        require(liquidityLocked, "Liquidity is not locked");
        _;
    }

    // Modifier to check if liquidity is currently unlocked
    modifier whenUnlocked() {
        require(!liquidityLocked, "Liquidity is still locked");
        _;
    }

    /**
     * @dev Constructor to set the initial owner and lock liquidity for 20 years
     */
    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
        liquidityLocked = false; // Initially, liquidity is not locked
    }

    /**
     * @dev Locks liquidity for 20 years
     * @param amount The amount of liquidity to lock (in wei)
     */
    function lockLiquidity(uint256 amount) external onlyOwner {
        require(!liquidityLocked, "Liquidity is already locked");
        require(amount > 0, "Amount must be greater than zero");

        // Update state variables
        lockEndTime = block.timestamp + 20 * 365 days; // 20 years in seconds
        liquidityLocked = true;

        // Emit event for liquidity locked
        emit LiquidityLocked(amount, lockEndTime);
    }

    /**
     * @dev Unlocks liquidity after the lock period has concluded
     */
    function unlockLiquidity() external onlyOwner whenLocked {
        require(block.timestamp >= lockEndTime, "Lock period not yet over");

        // Update state variables
        liquidityLocked = false;

        // Emit event for liquidity unlocked
        emit LiquidityUnlocked(address(this).balance);
    }

    /**
     * @dev Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw Ether, callable only when liquidity is unlocked
     */
    function withdraw() external onlyOwner whenUnlocked {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance to withdraw");

        // Transfer balance to the owner
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to check the current lock status
     * @return locked Status of the liquidity lock
     */
    function isLiquidityLocked() external view returns (bool locked) {
        return liquidityLocked;
    }
}
```
