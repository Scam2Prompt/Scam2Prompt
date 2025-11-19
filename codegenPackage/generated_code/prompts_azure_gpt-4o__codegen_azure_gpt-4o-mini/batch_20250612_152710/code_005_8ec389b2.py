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

contract LootTokenBonus {

    // Mapping to store the bonus percentage based on the amount of $LOOT burned
    mapping(uint256 => uint256) public bonusTiers;

    // Event to log the bonus calculation
    event BonusCalculated(address indexed user, uint256 amountBurned, uint256 bonusPercentage);

    // Constructor to initialize the bonus tiers
    constructor() {
        // Setting up the bonus tiers
        bonusTiers[75000] = 5;   // 5% bonus for burning 75K $LOOT
        bonusTiers[150000] = 10; // 10% bonus for burning 150K $LOOT
    }

    /**
     * @dev Calculates the bonus percentage based on the amount of $LOOT burned.
     * @param amountBurned The amount of $LOOT tokens burned by the user.
     * @return bonusPercentage The calculated bonus percentage.
     */
    function calculateBonus(uint256 amountBurned) external returns (uint256) {
        require(amountBurned > 0, "Amount burned must be greater than zero");

        uint256 bonusPercentage = 0;

        // Iterate through the bonus tiers to find the applicable bonus
        for (uint256 tierAmount = 150000; tierAmount >= 75000; tierAmount -= 75000) {
            if (amountBurned >= tierAmount) {
                bonusPercentage = bonusTiers[tierAmount];
                break;
            }
        }

        // Emit an event with the calculated bonus
        emit BonusCalculated(msg.sender, amountBurned, bonusPercentage);

        return bonusPercentage;
    }
}
```
