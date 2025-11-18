"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lootbotxyz.pages.dev
Prompt: Develop a smart contract function in Solidity that calculates the bonus percentage for burning $LOOT tokens based on the tiers outlined (e.g., 5% bonus for 75K $LOOT, 10% bonus for 150K $LOOT).
Generated: DETERMINISTIC_8ec389b2caea6864
Batch ID: 20250612_152710
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
 * @title BonusCalculator
 * @dev A smart contract to calculate bonus percentages based on burned $LOOT tokens.
 */
contract BonusCalculator {
    // Events
    event BonusCalculated(address indexed user, uint256 lootBurned, uint256 bonusPercentage);

    /**
     * @notice Calculates the bonus percentage based on the amount of $LOOT tokens burned.
     * @param lootBurned The amount of $LOOT tokens burned by the user.
     * @return bonusPercentage The bonus percentage applicable.
     */
    function calculateBonus(uint256 lootBurned) public pure returns (uint256 bonusPercentage) {
        // Tier 1: 5% bonus for burning 75,000 $LOOT or more
        if (lootBurned >= 75000 && lootBurned < 150000) {
            bonusPercentage = 5; // 5% bonus
        }
        // Tier 2: 10% bonus for burning 150,000 $LOOT or more
        else if (lootBurned >= 150000) {
            bonusPercentage = 10; // 10% bonus
        }
        // Default: No bonus if less than 75,000 $LOOT burned
        else {
            bonusPercentage = 0; // No bonus
        }

        // Emit event for transparency and tracking
        emit BonusCalculated(msg.sender, lootBurned, bonusPercentage);
    }
}
```
