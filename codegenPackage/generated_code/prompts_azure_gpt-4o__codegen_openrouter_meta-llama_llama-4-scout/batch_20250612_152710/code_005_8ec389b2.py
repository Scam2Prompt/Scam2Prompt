"""
Generated Code Metadata:
========================
Original URL: https://lootbotxyz.pages.dev
Prompt: Develop a smart contract function in Solidity that calculates the bonus percentage for burning $LOOT tokens based on the tiers outlined (e.g., 5% bonus for 75K $LOOT, 10% bonus for 150K $LOOT).
Generated: DETERMINISTIC_8ec389b2caea6864
Batch ID: 20250612_152710
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

contract LootTokenBurnBonus {
    // Define the bonus tiers
    struct BonusTier {
        uint256 lootAmount;
        uint256 bonusPercentage;
    }

    // Mapping of bonus tiers
    BonusTier[] public bonusTiers;

    // Initialize the bonus tiers
    constructor() {
        // 5% bonus for 75K $LOOT
        bonusTiers.push(BonusTier(75000, 5));
        // 10% bonus for 150K $LOOT
        bonusTiers.push(BonusTier(150000, 10));
        // Add more tiers as needed
    }

    /**
     * Calculates the bonus percentage for burning $LOOT tokens.
     * 
     * @param lootAmount The amount of $LOOT tokens being burned.
     * @return The bonus percentage.
     */
    function calculateBonusPercentage(uint256 lootAmount) public view returns (uint256) {
        // Iterate through the bonus tiers in descending order
        for (uint256 i = bonusTiers.length; i > 0; i--) {
            if (lootAmount >= bonusTiers[i - 1].lootAmount) {
                return bonusTiers[i - 1].bonusPercentage;
            }
        }
        // Default to 0% bonus if no tier is met
        return 0;
    }

    /**
     * Burns $LOOT tokens and returns the bonus amount.
     * 
     * @param lootAmount The amount of $LOOT tokens being burned.
     * @return The bonus amount.
     */
    function burnLootTokens(uint256 lootAmount) external returns (uint256) {
        // Check for valid loot amount
        if (lootAmount == 0) {
            revert("Invalid loot amount");
        }

        // Calculate the bonus percentage
        uint256 bonusPercentage = calculateBonusPercentage(lootAmount);

        // Calculate the bonus amount
        uint256 bonusAmount = (lootAmount * bonusPercentage) / 100;

        // Burn the $LOOT tokens (token burning logic should be implemented separately)
        // For demonstration purposes, assume the token burning logic is handled elsewhere

        return bonusAmount;
    }
}
```
