"""
Generated Code Metadata:
========================
Original URL: https://smogwhitelist.pages.dev
Prompt: Provide an example of how to implement a community quest feature in a decentralized application (dApp) that rewards users with $SMOG tokens.
Generated: DETERMINISTIC_0041ece04cacb289
Batch ID: 20250612_163518
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
 * @title CommunityQuest
 * @dev A decentralized application (dApp) contract for managing community quests and rewarding users with $SMOG tokens.
 */
contract CommunityQuest {
    // Token interface for $SMOG token
    interface ISmogToken {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // Address of the $SMOG token contract
    address public smogTokenAddress;

    // Struct to represent a quest
    struct Quest {
        string description; // Description of the quest
        uint256 reward;     // Reward in $SMOG tokens
        bool isActive;      // Status of the quest
    }

    // Mapping to store quests by ID
    mapping(uint256 => Quest) public quests;

    // Mapping to track quest completion by user
    mapping(uint256 => mapping(address => bool)) public questCompletion;

    // Counter for quest IDs
    uint256 public questCounter;

    // Owner of the contract
    address public owner;

    // Events
    event QuestCreated(uint256 questId, string description, uint256 reward);
    event QuestCompleted(uint256 questId, address user, uint256 reward);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _smogTokenAddress Address of the $SMOG token contract.
     */
    constructor(address _smogTokenAddress) {
        require(_smogTokenAddress != address(0), "Invalid token address");
        smogTokenAddress = _smogTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new quest.
     * @param _description Description of the quest.
     * @param _reward Reward in $SMOG tokens for completing the quest.
     */
    function createQuest(string memory _description, uint256 _reward) external onlyOwner {
        require(bytes(_description).length > 0, "Description cannot be empty");
        require(_reward > 0, "Reward must be greater than zero");

        questCounter++;
        quests[questCounter] = Quest({
            description: _description,
            reward: _reward,
            isActive: true
        });

        emit QuestCreated(questCounter, _description, _reward);
    }

    /**
     * @dev Function to complete a quest and claim the reward.
     * @param _questId ID of the quest to complete.
     */
    function completeQuest(uint256 _questId) external {
        Quest storage quest = quests[_questId];
        require(quest.isActive, "Quest is not active");
        require(!questCompletion[_questId][msg.sender], "Quest already completed by user");

        // Mark the quest as completed for the user
        questCompletion[_questId][msg.sender] = true;

        // Transfer the reward to the user
        ISmogToken smogToken = ISmogToken(smogTokenAddress);
        require(smogToken.transfer(msg.sender, quest.reward), "Token transfer failed");

        emit QuestCompleted(_questId, msg.sender, quest.reward);
    }

    /**
     * @dev Function to deactivate a quest.
     * @param _questId ID of the quest to deactivate.
     */
    function deactivateQuest(uint256 _questId) external onlyOwner {
        Quest storage quest = quests[_questId];
        require(quest.isActive, "Quest is already inactive");

        quest.isActive = false;
    }

    /**
     * @dev Function to update the $SMOG token contract address.
     * @param _newSmogTokenAddress New address of the $SMOG token contract.
     */
    function updateSmogTokenAddress(address _newSmogTokenAddress) external onlyOwner {
        require(_newSmogTokenAddress != address(0), "Invalid token address");
        smogTokenAddress = _newSmogTokenAddress;
    }
}
```
