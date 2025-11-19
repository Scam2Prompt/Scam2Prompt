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

// Importing required OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CommunityQuest contract to implement a quest feature in a dApp
contract CommunityQuest is Ownable {
    // Token contract for $SMOG
    IERC20 public smogToken;

    // Struct to represent a Quest
    struct Quest {
        string description;
        uint256 reward; // Amount of $SMOG tokens rewarded for completing the quest
        bool isCompleted; // Status of the quest
        address[] participants; // List of participants who completed the quest
    }

    // Mapping to store quests
    mapping(uint256 => Quest) public quests;
    uint256 public questCount; // Counter for quests

    // Event emitted when a new quest is created
    event QuestCreated(uint256 indexed questId, string description, uint256 reward);

    // Event emitted when a quest is completed
    event QuestCompleted(uint256 indexed questId, address indexed participant);

    // Constructor to initialize the $SMOG token contract address
    constructor(address _smogToken) {
        require(_smogToken != address(0), "Invalid token address");
        smogToken = IERC20(_smogToken);
    }

    // Function to create a new quest
    function createQuest(string calldata _description, uint256 _reward) external onlyOwner {
        require(_reward > 0, "Reward must be greater than 0");
        
        quests[questCount] = Quest({
            description: _description,
            reward: _reward,
            isCompleted: false,
            participants: new address[](0)
        });

        emit QuestCreated(questCount, _description, _reward);
        questCount++;
    }

    // Function to complete a quest
    function completeQuest(uint256 _questId) external {
        Quest storage quest = quests[_questId];
        
        require(_questId < questCount, "Quest does not exist");
        require(!quest.isCompleted, "Quest already completed");

        // Mark the quest as completed
        quest.isCompleted = true;
        quest.participants.push(msg.sender);

        // Transfer the reward to the participant
        require(smogToken.balanceOf(address(this)) >= quest.reward, "Not enough token balance in contract");
        smogToken.transfer(msg.sender, quest.reward);

        emit QuestCompleted(_questId, msg.sender);
    }

    // Function to retrieve quest details
    function getQuest(uint256 _questId) external view returns (string memory, uint256, bool, address[] memory) {
        require(_questId < questCount, "Quest does not exist");
        Quest storage quest = quests[_questId];
        return (quest.description, quest.reward, quest.isCompleted, quest.participants);
    }

    // Function to withdraw tokens from the contract (only for owner)
    function withdrawTokens(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be greater than 0");
        require(smogToken.balanceOf(address(this)) >= _amount, "Not enough tokens in contract");
        
        smogToken.transfer(msg.sender, _amount);
    }
}
```
