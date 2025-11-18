"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hamsterboost.io
Prompt: Create a smart contract example in Solidity that could be used for blockchain testing quests, similar to those described on Hamster Boost.
Generated: DETERMINISTIC_abbf8618b3ec0647
Batch ID: 20250612_154339
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

/// @title Blockchain Testing Quest Contract
/// @notice This contract allows users to create and participate in quests for testing on the blockchain
/// @dev The contract includes functionalities for quest creation, participation, and rewards distribution
contract QuestContract {
    // Struct to represent a Quest
    struct Quest {
        string description; // Description of the quest
        address creator; // Address of the quest creator
        uint256 reward; // Reward for completing the quest
        uint256 participantsCount; // Count of participants in the quest
        bool isActive; // Status of the quest
    }

    // Mapping to store quests by their ID
    mapping(uint256 => Quest) public quests;
    uint256 public questCount; // Total number of quests created

    // Event emitted when a quest is created
    event QuestCreated(uint256 indexed questId, string description, address indexed creator, uint256 reward);

    // Event emitted when a user participates in a quest
    event QuestParticipated(uint256 indexed questId, address indexed participant);

    // Modifier to check if the quest is active
    modifier onlyActiveQuest(uint256 _questId) {
        require(quests[_questId].isActive, "Quest is not active");
        _;
    }

    /// @notice Creates a new quest
    /// @param _description Description of the quest
    /// @param _reward Reward for completing the quest
    function createQuest(string calldata _description, uint256 _reward) external {
        require(_reward > 0, "Reward must be greater than zero");

        questCount++;
        quests[questCount] = Quest({
            description: _description,
            creator: msg.sender,
            reward: _reward,
            participantsCount: 0,
            isActive: true
        });

        emit QuestCreated(questCount, _description, msg.sender, _reward);
    }

    /// @notice Allows a user to participate in a quest
    /// @param _questId The ID of the quest to participate in
    function participateInQuest(uint256 _questId) external onlyActiveQuest(_questId) {
        quests[_questId].participantsCount++;
        emit QuestParticipated(_questId, msg.sender);
    }

    /// @notice Completes a quest and provides rewards to the participants
    /// @param _questId The ID of the quest to complete
    /// @dev Only the creator of the quest can complete it
    function completeQuest(uint256 _questId) external {
        Quest storage quest = quests[_questId];
        require(msg.sender == quest.creator, "Only the quest creator can complete the quest");
        require(quest.isActive, "Quest must be active to complete");

        quest.isActive = false; // Mark the quest as inactive

        // Note: Here you might implement the logic to reward participants, such as transferring tokens
        // For demonstration, we are just resetting the quest
    }

    /// @notice Returns the details of a specific quest
    /// @param _questId The ID of the quest to retrieve
    /// @return The details of the quest
    function getQuest(uint256 _questId) external view returns (Quest memory) {
        return quests[_questId];
    }
}
```
