"""
Generated Code Metadata:
========================
Original URL: https://hamsterboost.io
Prompt: Create a smart contract example in Solidity that could be used for blockchain testing quests, similar to those described on Hamster Boost.
Generated: DETERMINISTIC_abbf8618b3ec0647
Batch ID: 20250612_154339
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

/// @title Blockchain Testing Quest Smart Contract
/// @author Your Name
/// @notice This contract allows users to create and participate in testing quests
/// @dev This contract is designed for educational purposes and should be audited before production use

contract TestingQuest {
    // Struct to represent a quest
    struct Quest {
        uint256 id;
        string description;
        address creator;
        uint256 reward;
        bool completed;
    }

    // Mapping to store quests by their ID
    mapping(uint256 => Quest) public quests;
    // Counter for quest IDs
    uint256 public questCount;

    // Event emitted when a new quest is created
    event QuestCreated(uint256 indexed questId, string description, address indexed creator, uint256 reward);
    // Event emitted when a quest is completed
    event QuestCompleted(uint256 indexed questId, address indexed completer);

    /// @notice Create a new quest
    /// @param _description The description of the quest
    /// @param _reward The reward for completing the quest
    /// @dev The reward must be greater than zero
    function createQuest(string calldata _description, uint256 _reward) external {
        require(_reward > 0, "Reward must be greater than zero");

        questCount++;
        quests[questCount] = Quest(questCount, _description, msg.sender, _reward, false);

        emit QuestCreated(questCount, _description, msg.sender, _reward);
    }

    /// @notice Complete a quest
    /// @param _questId The ID of the quest to complete
    /// @dev Only the creator of the quest can mark it as completed
    function completeQuest(uint256 _questId) external {
        Quest storage quest = quests[_questId];
        require(quest.id != 0, "Quest does not exist");
        require(!quest.completed, "Quest already completed");
        require(msg.sender == quest.creator, "Only the creator can complete the quest");

        quest.completed = true;

        // Transfer the reward to the quest creator
        payable(quest.creator).transfer(quest.reward);

        emit QuestCompleted(_questId, msg.sender);
    }

    /// @notice Fallback function to accept Ether
    receive() external payable {}

    /// @notice Withdraw contract balance to the owner
    /// @dev Only the contract owner can withdraw funds
    function withdraw() external {
        // Only the contract deployer can withdraw funds
        require(msg.sender == address(this), "Only contract owner can withdraw");
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
