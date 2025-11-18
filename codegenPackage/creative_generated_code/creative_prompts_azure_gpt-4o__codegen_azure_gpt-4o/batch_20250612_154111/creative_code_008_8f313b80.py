"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://minerdogs.icu
Prompt: Create a Solidity function to update the contract's bonus rate based on the total invested balance, using the MinerDog contract's logic of increasing bonuses by 0.05% for every 45 BNB added.
Generated: DETERMINISTIC_8f313b80a515ca20
Batch ID: 20250612_154111
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
 * @title MinerDog Contract
 * @dev This contract defines a function to update the bonus rate based on the total invested balance.
 */
contract MinerDog {
    // State variables
    uint256 public totalInvested; // Total invested balance in the contract
    uint256 public bonusRate; // Current bonus rate in percentage (e.g., 5% is represented as 500)
    uint256 private constant BONUS_INCREMENT = 5; // 0.05% bonus increment represented in basis points (500 = 5%)
    uint256 private constant BONUS_STEP = 45 ether; // The amount of BNB required to increase the bonus rate

    // Events
    event BonusRateUpdated(uint256 oldBonusRate, uint256 newBonusRate);

    /**
     * @dev Updates the bonus rate based on the total invested balance.
     * Increases the bonus rate by 0.05% (basis points = 5) for every 45 BNB added.
     */
    function updateBonusRate() external {
        // Calculate the number of steps based on total invested balance and BONUS_STEP
        uint256 steps = totalInvested / BONUS_STEP;

        // Calculate the new bonus rate based on the steps
        uint256 newBonusRate = BONUS_INCREMENT * steps;

        // Emit an event if the bonus rate has changed
        if (newBonusRate != bonusRate) {
            emit BonusRateUpdated(bonusRate, newBonusRate);
            bonusRate = newBonusRate; // Update the bonus rate
        }
    }

    /**
     * @dev Function to simulate investment for testing purposes.
     * Adds balance to the totalInvested variable.
     * @param amount The amount of BNB invested in wei.
     */
    function invest(uint256 amount) external {
        require(amount > 0, "Investment amount must be greater than zero");
        
        // Add the invested amount to the totalInvested balance
        totalInvested += amount;
    }
}
```
