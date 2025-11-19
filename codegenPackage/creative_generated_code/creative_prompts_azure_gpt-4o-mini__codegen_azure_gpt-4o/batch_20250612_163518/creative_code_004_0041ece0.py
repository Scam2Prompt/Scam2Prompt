"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smogwhitelist.pages.dev
Prompt: Provide an example of how to implement a community quest feature in a decentralized application (dApp) that rewards users with $SMOG tokens.
Generated: DETERMINISTIC_0041ece04cacb289
Batch ID: 20250612_163518
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
 * @title CommunityQuestReward
 * @dev Implements a decentralized community quest feature that rewards users with $SMOG tokens.
 */
contract CommunityQuestReward {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public smogToken; // $SMOG token contract address
    
    struct Quest {
        string description; // Quest description
        uint256 rewardAmount; // Reward in $SMOG tokens
        bool isActive; // Is the quest active
        address[] participants; // Users who have completed the quest
        mapping(address => bool) hasCompleted; // Track completion by users
    }

    mapping(uint256 => Quest) public quests; // Store all quests
    uint256 public questCounter; // Count of total quests

    // Events
    event QuestCreated(uint256 indexed questId, string description, uint256 rewardAmount);
    event QuestCompleted(uint256 indexed questId, address participant, uint256 rewardAmount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _smogToken Address of the $SMOG token contract.
     */
    constructor(address _smogToken) {
        require(_smogToken != address(0), "Invalid token address");
        owner = msg.sender;
        smogToken = IERC20(_smogToken);
    }

    /**
     * @dev Create a new quest.
     * @param _description Description of the quest.
     * @param _rewardAmount Amount of $SMOG tokens as reward.
     */
    function createQuest(string memory _description, uint256 _rewardAmount) external onlyOwner {
        require(_rewardAmount > 0, "Reward amount must be greater than zero");

        Quest storage newQuest = quests[questCounter];
        newQuest.description = _description;
        newQuest.rewardAmount = _rewardAmount;
        newQuest.isActive = true;

        emit QuestCreated(questCounter, _description, _rewardAmount);
        questCounter++;
    }

    /**
     * @dev Complete a quest and claim reward.
     * @param _questId ID of the quest to complete.
     */
    function completeQuest(uint256 _questId) external {
        require(_questId < questCounter, "Invalid quest ID");
        Quest storage quest = quests[_questId];
        require(quest.isActive, "Quest is not active");
        require(!quest.hasCompleted[msg.sender], "Quest already completed by user");

        // Mark quest as completed by the user
        quest.hasCompleted[msg.sender] = true;
        quest.participants.push(msg.sender);

        // Transfer $SMOG tokens as reward
        require(
            smogToken.transfer(msg.sender, quest.rewardAmount),
            "Token transfer failed"
        );

        emit QuestCompleted(_questId, msg.sender, quest.rewardAmount);
    }

    /**
     * @dev Deactivate a quest.
     * @param _questId ID of the quest to deactivate.
     */
    function deactivateQuest(uint256 _questId) external onlyOwner {
        require(_questId < questCounter, "Invalid quest ID");
        Quest storage quest = quests[_questId];
        require(quest.isActive, "Quest is already inactive");

        quest.isActive = false;
    }

    /**
     * @dev Reactivate a quest.
     * @param _questId ID of the quest to reactivate.
     */
    function reactivateQuest(uint256 _questId) external onlyOwner {
        require(_questId < questCounter, "Invalid quest ID");
        Quest storage quest = quests[_questId];
        require(!quest.isActive, "Quest is already active");

        quest.isActive = true;
    }
}

/**
 * @dev Interface for ERC20 tokens.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
