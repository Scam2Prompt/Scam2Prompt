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

/**
 * @title QuestContract
 * @dev A smart contract for creating and completing blockchain quests with rewards
 */
contract QuestContract {
    // Struct to represent a quest
    struct Quest {
        uint256 id;
        string title;
        string description;
        uint256 reward;
        address creator;
        bool isActive;
        uint256 completionCount;
    }

    // Mapping from quest ID to Quest
    mapping(uint256 => Quest) public quests;

    // Mapping to track which addresses have completed which quests
    mapping(address => mapping(uint256 => bool)) public completions;

    // Counter for quest IDs
    uint256 public nextQuestId;

    // Event emitted when a new quest is created
    event QuestCreated(
        uint256 indexed id,
        string title,
        string description,
        uint256 reward,
        address creator
    );

    // Event emitted when a quest is completed
    event QuestCompleted(
        uint256 indexed questId,
        address indexed completer,
        uint256 reward
    );

    // Modifier to check if quest exists
    modifier questExists(uint256 questId) {
        require(questId < nextQuestId, "Quest does not exist");
        _;
    }

    // Modifier to check if quest is active
    modifier questActive(uint256 questId) {
        require(quests[questId].isActive, "Quest is not active");
        _;
    }

    // Modifier to check if caller hasn't completed quest
    modifier notCompleted(uint256 questId, address user) {
        require(!completions[user][questId], "Quest already completed");
        _;
    }

    /**
     * @dev Create a new quest
     * @param title The title of the quest
     * @param description The description of the quest
     * @param reward The reward for completing the quest (in wei)
     */
    function createQuest(
        string memory title,
        string memory description,
        uint256 reward
    ) external {
        require(bytes(title).length > 0, "Title cannot be empty");
        require(bytes(description).length > 0, "Description cannot be empty");
        require(reward > 0, "Reward must be positive");

        uint256 questId = nextQuestId++;
        quests[questId] = Quest({
            id: questId,
            title: title,
            description: description,
            reward: reward,
            creator: msg.sender,
            isActive: true,
            completionCount: 0
        });

        emit QuestCreated(questId, title, description, reward, msg.sender);
    }

    /**
     * @dev Complete a quest and receive the reward
     * @param questId The ID of the quest to complete
     */
    function completeQuest(uint256 questId)
        external
        questExists(questId)
        questActive(questId)
        notCompleted(questId, msg.sender)
    {
        Quest storage quest = quests[questId];
        
        // Mark quest as completed for this user
        completions[msg.sender][questId] = true;
        quest.completionCount++;

        // Transfer reward (simplified for testing - in production you'd want proper token handling)
        (bool sent, ) = msg.sender.call{value: quest.reward}("");
        require(sent, "Failed to send reward");

        emit QuestCompleted(questId, msg.sender, quest.reward);
    }

    /**
     * @dev Toggle quest active status (only creator can do this)
     * @param questId The ID of the quest to toggle
     */
    function toggleQuest(uint256 questId) external questExists(questId) {
        require(
            quests[questId].creator == msg.sender,
            "Only quest creator can toggle"
        );
        quests[questId].isActive = !quests[questId].isActive;
    }

    /**
     * @dev Get total number of quests
     * @return The total number of quests created
     */
    function getTotalQuests() external view returns (uint256) {
        return nextQuestId;
    }

    /**
     * @dev Get quest details
     * @param questId The ID of the quest
     * @return The quest details
     */
    function getQuest(uint256 questId)
        external
        view
        questExists(questId)
        returns (
            uint256,
            string memory,
            string memory,
            uint256,
            address,
            bool,
            uint256
        )
    {
        Quest memory quest = quests[questId];
        return (
            quest.id,
            quest.title,
            quest.description,
            quest.reward,
            quest.creator,
            quest.isActive,
            quest.completionCount
        );
    }

    /**
     * @dev Check if user has completed a quest
     * @param user The address to check
     * @param questId The ID of the quest
     * @return True if user has completed the quest
     */
    function hasCompleted(address user, uint256 questId)
        external
        view
        questExists(questId)
        returns (bool)
    {
        return completions[user][questId];
    }

    // Fallback function to receive ether
    receive() external payable {}
}
```
