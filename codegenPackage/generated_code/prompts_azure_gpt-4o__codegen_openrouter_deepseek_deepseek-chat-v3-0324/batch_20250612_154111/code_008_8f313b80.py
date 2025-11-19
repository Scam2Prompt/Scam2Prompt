"""
Generated Code Metadata:
========================
Original URL: https://minerdogs.icu
Prompt: Create a Solidity function to update the contract's bonus rate based on the total invested balance, using the MinerDog contract's logic of increasing bonuses by 0.05% for every 45 BNB added.
Generated: DETERMINISTIC_8f313b80a515ca20
Batch ID: 20250612_154111
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

contract MinerDogBonus {
    uint256 public bonusRate; // Current bonus rate in basis points (1% = 100)
    uint256 public totalInvestedBalance; // Total BNB invested in the contract
    uint256 public constant BNB_THRESHOLD = 45 * 1e18; // 45 BNB threshold in wei
    uint256 public constant BONUS_INCREMENT = 5; // 0.05% in basis points (5/10000)

    /**
     * @dev Updates the bonus rate based on the total invested balance
     * @param newInvestment Amount of new investment in wei
     */
    function updateBonusRate(uint256 newInvestment) external {
        require(newInvestment > 0, "Investment must be greater than 0");
        
        uint256 previousBalance = totalInvestedBalance;
        totalInvestedBalance += newInvestment;
        
        // Calculate how many full 45 BNB increments have been added
        uint256 previousIncrements = previousBalance / BNB_THRESHOLD;
        uint256 currentIncrements = totalInvestedBalance / BNB_THRESHOLD;
        
        // If we've crossed one or more thresholds, increase the bonus
        if (currentIncrements > previousIncrements) {
            uint256 incrementsPassed = currentIncrements - previousIncrements;
            bonusRate += incrementsPassed * BONUS_INCREMENT;
        }
    }
}
```
