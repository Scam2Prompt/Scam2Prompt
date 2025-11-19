"""
Generated Code Metadata:
========================
Original URL: https://conhyper.pages.dev
Prompt: Suggest a method to build a quest system for Web3 projects that rewards users, as described in the "Quests" section, and provide a code example for its implementation.
Generated: DETERMINISTIC_5ef154f95cd2564b
Batch ID: 20250612_154307
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract QuestSystem is Ownable, ReentrancyGuard {
    // Struct to represent a quest
    struct Quest {
        uint256 id;
        string name;
        string description;
        uint256 rewardAmount;
        address rewardToken;
        bool isActive;
        uint256 completionCount;
    }

    // Mapping from quest ID to Quest
    mapping(uint256 => Quest) public quests;

    // Mapping from user address to completed quest IDs
    mapping(address => uint256[]) private userCompletedQuests;

    // Counter for quest IDs
    uint256 private nextQuestId = 1;

    // Events
    event QuestCreated(
        uint256 indexed questId,
        string name,
        string description,
        uint256 rewardAmount,
        address rewardToken
    );
    event QuestCompleted(
        uint256 indexed questId,
        address indexed user,
        uint256 rewardAmount,
        address rewardToken
    );
    event QuestStatusChanged(uint256 indexed questId, bool isActive);

    /**
     * @dev Creates a new quest
     * @param name The name of the quest
     * @param description Description of the quest
     * @param rewardAmount Amount of tokens to reward
     * @param rewardToken Address of the ERC20 token used for rewards
     */
    function createQuest(
        string memory name,
        string memory description,
        uint256 rewardAmount,
        address rewardToken
    ) external onlyOwner {
        uint256 questId = nextQuestId++;
        quests[questId] = Quest({
            id: questId,
            name: name,
            description: description,
            rewardAmount: rewardAmount,
            rewardToken: rewardToken,
            isActive: true,
            completionCount: 0
        });

        emit QuestCreated(questId, name, description, rewardAmount, rewardToken);
    }

    /**
     * @dev Toggles the active status of a quest
     * @param questId ID of the quest to toggle
     */
    function toggleQuestStatus(uint256 questId) external onlyOwner {
        require(questId < nextQuestId, "Quest does not exist");
        quests[questId].isActive = !quests[questId].isActive;
        emit QuestStatusChanged(questId, quests[questId].isActive);
    }

    /**
     * @dev Completes a quest and rewards the user
     * @param questId ID of the quest to complete
     */
    function completeQuest(uint256 questId) external nonReentrant {
        require(questId < nextQuestId, "Quest does not exist");
        Quest storage quest = quests[questId];
        require(quest.isActive, "Quest is not active");
        require(!hasCompletedQuest(msg.sender, questId), "Already completed this quest");

        // Transfer reward tokens
        IERC20 token = IERC20(quest.rewardToken);
        require(
            token.balanceOf(address(this)) >= quest.rewardAmount,
            "Insufficient contract balance"
        );
        
        bool success = token.transfer(msg.sender, quest.rewardAmount);
        require(success, "Token transfer failed");

        // Update quest and user data
        quest.completionCount++;
        userCompletedQuests[msg.sender].push(questId);

        emit QuestCompleted(questId, msg.sender, quest.rewardAmount, quest.rewardToken);
    }

    /**
     * @dev Checks if a user has completed a specific quest
     * @param user Address of the user
     * @param questId ID of the quest
     * @return bool True if user has completed the quest
     */
    function hasCompletedQuest(address user, uint256 questId) public view returns (bool) {
        uint256[] storage completedQuests = userCompletedQuests[user];
        for (uint256 i = 0; i < completedQuests.length; i++) {
            if (completedQuests[i] == questId) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Gets all quest IDs completed by a user
     * @param user Address of the user
     * @return uint256[] Array of completed quest IDs
     */
    function getUserCompletedQuests(address user) external view returns (uint256[] memory) {
        return userCompletedQuests[user];
    }

    /**
     * @dev Withdraws ERC20 tokens from the contract (emergency only)
     * @param tokenAddress Address of the token contract
     * @param amount Amount to withdraw
     */
    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        bool success = token.transfer(owner(), amount);
        require(success, "Token transfer failed");
    }
}
```
