"""
Generated Code Metadata:
========================
Original URL: https://mantadev.pages.dev
Prompt: Create a function in Solidity that calculates the total KARMA earned based on quests completed and multipliers applied in the MANTRA Zone.
Generated: DETERMINISTIC_573a7faf86134506
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

/**
 * @title KARMA Calculator for MANTRA Zone
 * @author [Your Name]
 * @notice Calculates the total KARMA earned based on quests completed and multipliers applied.
 */
contract KarmCalculator {
    /**
     * @dev Struct to represent a Quest with its KARMA reward and multiplier.
     */
    struct Quest {
        uint256 karmaReward;
        uint256 multiplier;
    }

    /**
     * @dev Mapping of quest IDs to their respective Quest structs.
     */
    mapping(uint256 => Quest) public quests;

    /**
     * @dev Function to add a new quest to the quests mapping.
     * @param _questId The ID of the quest.
     * @param _karmaReward The KARMA reward for the quest.
     * @param _multiplier The multiplier for the quest.
     */
    function addQuest(uint256 _questId, uint256 _karmaReward, uint256 _multiplier) public {
        require(_karmaReward > 0, "KARMA reward must be greater than 0");
        require(_multiplier > 0, "Multiplier must be greater than 0");
        quests[_questId] = Quest(_karmaReward, _multiplier);
    }

    /**
     * @dev Function to calculate the total KARMA earned based on quests completed.
     * @param _questIds Array of quest IDs completed.
     * @return The total KARMA earned.
     */
    function calculateKarma(uint256[] memory _questIds) public view returns (uint256) {
        uint256 totalKarma = 0;
        for (uint256 i = 0; i < _questIds.length; i++) {
            uint256 questId = _questIds[i];
            require(quests[questId].karmaReward > 0, "Quest not found");
            uint256 questKarma = quests[questId].karmaReward * quests[questId].multiplier;
            totalKarma += questKarma;
        }
        return totalKarma;
    }

    /**
     * @dev Function to update the KARMA reward for a specific quest.
     * @param _questId The ID of the quest.
     * @param _newKarmaReward The new KARMA reward for the quest.
     */
    function updateKarmaReward(uint256 _questId, uint256 _newKarmaReward) public {
        require(quests[_questId].karmaReward > 0, "Quest not found");
        require(_newKarmaReward > 0, "KARMA reward must be greater than 0");
        quests[_questId].karmaReward = _newKarmaReward;
    }

    /**
     * @dev Function to update the multiplier for a specific quest.
     * @param _questId The ID of the quest.
     * @param _newMultiplier The new multiplier for the quest.
     */
    function updateMultiplier(uint256 _questId, uint256 _newMultiplier) public {
        require(quests[_questId].multiplier > 0, "Quest not found");
        require(_newMultiplier > 0, "Multiplier must be greater than 0");
        quests[_questId].multiplier = _newMultiplier;
    }
}
```
