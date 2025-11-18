"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://galxe-backendserver.pages.dev
Prompt: Create a smart contract example for a Galxe Quest that rewards users for completing specific blockchain tasks.
Generated: DETERMINISTIC_1ddcfe4685aa09ca
Batch ID: 20250612_145715
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

/// @title Galxe Quest Smart Contract
/// @author Your Name
/// @notice This contract allows users to complete quests and earn rewards
/// @dev This contract uses OpenZeppelin's SafeERC20 for safe token transfers

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract GalxeQuest is Ownable {
    using SafeERC20 for IERC20;

    struct Quest {
        string description;
        uint256 rewardAmount;
        bool isCompleted;
    }

    // Mapping of quest IDs to Quest details
    mapping(uint256 => Quest) public quests;
    
    // Mapping to track user completions of quests
    mapping(address => mapping(uint256 => bool)) public userCompletedQuests;

    IERC20 public rewardToken;
    uint256 public questCounter;

    /// @dev Event emitted when a new quest is created
    event QuestCreated(uint256 questId, string description, uint256 rewardAmount);
    
    /// @dev Event emitted when a user completes a quest
    event QuestCompleted(address indexed user, uint256 questId);

    /// @param _rewardToken The address of the ERC20 token to be used as rewards
    constructor(IERC20 _rewardToken) {
        rewardToken = _rewardToken;
    }

    /// @notice Create a new quest
    /// @param description The description of the quest
    /// @param rewardAmount The amount of tokens to reward for completing the quest
    function createQuest(string memory description, uint256 rewardAmount) external onlyOwner {
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        quests[questCounter] = Quest({
            description: description,
            rewardAmount: rewardAmount,
            isCompleted: false
        });

        emit QuestCreated(questCounter, description, rewardAmount);
        questCounter++;
    }

    /// @notice User completes a quest and is rewarded
    /// @param questId The ID of the quest to be completed
    function completeQuest(uint256 questId) external {
        Quest storage quest = quests[questId];

        require(!quest.isCompleted, "Quest already completed");
        require(!userCompletedQuests[msg.sender][questId], "User already completed this quest");

        // Mark quest as completed
        quest.isCompleted = true;
        userCompletedQuests[msg.sender][questId] = true;

        // Transfer reward
        rewardToken.safeTransfer(msg.sender, quest.rewardAmount);

        emit QuestCompleted(msg.sender, questId);
    }

    /// @notice Withdraw tokens from the contract
    /// @param amount The amount of tokens to withdraw
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        rewardToken.safeTransfer(msg.sender, amount);
    }
}
```
