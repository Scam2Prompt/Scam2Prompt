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

contract KarmaCalculator {
    // State variable to store the total KARMA
    uint256 public totalKarma;

    // Event to log the KARMA earned
    event KarmaEarned(address indexed user, uint256 karmaAmount);

    /**
     * @dev Calculates the total KARMA earned based on quests completed and multipliers.
     * @param questsCompleted The number of quests completed.
     * @param multiplier The multiplier applied to the quests.
     * @return The total KARMA earned.
     */
    function calculateKarma(uint256 questsCompleted, uint256 multiplier) external returns (uint256) {
        // Input validation
        require(questsCompleted > 0, "You must complete at least one quest.");
        require(multiplier > 0, "Multiplier must be greater than zero.");
        
        // Calculate the KARMA earned
        uint256 karmaEarned = questsCompleted * multiplier;

        // Update total KARMA
        totalKarma += karmaEarned;

        // Emit an event to log the KARMA earned
        emit KarmaEarned(msg.sender, karmaEarned);

        // Return the calculated KARMA
        return karmaEarned;
    }
}
```
