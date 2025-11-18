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

/**
 * @title QuestContract
 * @dev A simple smart contract for creating and completing blockchain testing quests.
 */
contract QuestContract {
    // Struct to represent a quest
    struct Quest {
        uint256 id;                 // Unique ID for the quest
        string name;                // Name of the quest
        string description;         // Description of the quest
        address creator;            // Address of the quest creator
        uint256 reward;             // Reward amount for completing the quest
        bool isCompleted;           // Flag to indicate if the quest is completed
    }

    // Mapping to store quests by their ID
    mapping(uint256 => Quest) public quests;

    // Counter to generate unique quest IDs
    uint256 private questCounter;

    // Event emitted when a new quest is created
    event QuestCreated(uint256 id, string name, address creator, uint256 reward);

    // Event emitted when a quest is completed
    event QuestCompleted(uint256 id, address completer);

    /**
     * @dev Function to create a new quest.
     * @param _name Name of the quest.
     * @param _description Description of the quest.
     * @param _reward Reward amount for completing the quest.
     */
    function createQuest(string memory _name, string memory _description, uint256 _reward) external {
        // Ensure the reward is greater than zero
        require(_reward > 0, "Reward must be greater than zero");

        // Increment the quest counter to generate a unique ID
        questCounter++;

        // Create the quest and store it in the mapping
        quests[questCounter] = Quest({
            id: questCounter,
            name: _name,
            description: _description,
            creator: msg.sender,
            reward: _reward,
            isCompleted: false
        });

        // Emit the QuestCreated event
        emit QuestCreated(questCounter, _name, msg.sender, _reward);
    }

    /**
     * @dev Function to complete a quest and claim its reward.
     * @param _questId ID of the quest to complete.
     */
    function completeQuest(uint256 _questId) external {
        // Retrieve the quest from the mapping
        Quest storage quest = quests[_questId];

        // Ensure the quest exists and has not already been completed
        require(quest.id != 0, "Quest does not exist");
        require(!quest.isCompleted, "Quest has already been completed");

        // Ensure the sender is not the quest creator
        require(msg.sender != quest.creator, "Quest creator cannot complete their own quest");

        // Mark the quest as completed
        quest.isCompleted = true;

        // Transfer the reward to the sender
        payable(msg.sender).transfer(quest.reward);

        // Emit the QuestCompleted event
        emit QuestCompleted(_questId, msg.sender);
    }

    /**
     * @dev Fallback function to accept Ether sent to the contract.
     */
    receive() external payable {
        // Accept Ether deposits for funding quest rewards
    }

    /**
     * @dev Function to retrieve the contract's balance.
     * @return The current Ether balance of the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
