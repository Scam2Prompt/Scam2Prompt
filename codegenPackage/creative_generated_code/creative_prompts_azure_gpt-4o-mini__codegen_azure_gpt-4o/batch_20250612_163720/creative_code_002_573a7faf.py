"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Create a function in Solidity that calculates the total KARMA earned based on quests completed and multipliers applied in the MANTRA Zone.
Generated: DETERMINISTIC_573a7faf86134506
Batch ID: 20250612_163720
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
 * @title KARMA Calculator
 * @dev This contract provides a function to calculate KARMA earned based on quests and multipliers.
 */
contract KarmaCalculator {
    // Event emitted when KARMA is calculated
    event KarmaCalculated(address indexed user, uint256 totalKarma);

    /**
     * @notice Calculates the total KARMA earned based on quests completed and multipliers applied.
     * @param questsCompleted Array of integers representing the base KARMA for each quest completed.
     * @param multipliers Array of integers representing the multipliers for each quest.
     * @return totalKarma Total KARMA earned.
     */
    function calculateKarma(uint256[] memory questsCompleted, uint256[] memory multipliers)
        public
        pure
        returns (uint256 totalKarma)
    {
        // Ensure the input arrays are of the same length
        require(questsCompleted.length == multipliers.length, "Input arrays must have the same length");

        // Initialize total KARMA to zero
        totalKarma = 0;

        // Iterate through the quests and apply multipliers to calculate total KARMA
        for (uint256 i = 0; i < questsCompleted.length; i++) {
            // Ensure the values are positive
            require(questsCompleted[i] > 0, "Quest base KARMA must be positive");
            require(multipliers[i] > 0, "Multiplier must be positive");

            // Add the calculated KARMA for each quest to the total
            totalKarma += questsCompleted[i] * multipliers[i];
        }

        // Emit an event with the calculated KARMA
        emit KarmaCalculated(msg.sender, totalKarma);

        return totalKarma;
    }
}
```
