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

/// @title LOOT Token Bonus Calculation
/// @notice This contract calculates bonus percentages based on the amount of $LOOT tokens burned
contract LootTokenBonus {

    // Define the bonus tiers
    enum BonusTier { None, FivePercent, TenPercent }

    /// @notice Calculates the bonus percentage based on the amount of LOOT burned
    /// @param amountBurned The amount of $LOOT tokens burned
    /// @return bonusPercentage The corresponding bonus percentage
    function calculateBonus(uint256 amountBurned) public pure returns (uint256 bonusPercentage) {
        // Validate the input amount
        require(amountBurned > 0, "Amount burned must be greater than zero");

        // Determine the bonus tier based on amount burned
        if (amountBurned >= 150000 * 10**18) {
            return 10; // 10% bonus for burning 150K or more LOOT
        } else if (amountBurned >= 75000 * 10**18) {
            return 5; // 5% bonus for burning 75K or more LOOT
        }

        return 0; // No bonus for amounts less than 75K LOOT
    }
}
```
