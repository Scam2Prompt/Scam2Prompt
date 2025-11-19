"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://taskchainclaim.web.app
Prompt: Develop a smart contract in Solidity for managing the distribution of rewards in the TaskChain ecosystem based on completed quests.
Generated: DETERMINISTIC_92840c27e9216a19
Batch ID: 20250612_161420
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
 * @title TaskChainRewardDistributor
 * @dev Smart contract to manage reward distribution for TaskChain ecosystem based on completed quests.
 */
contract TaskChainRewardDistributor {
    // Address of the contract owner
    address public owner;

    // Struct to hold quest details
    struct Quest {
        string questName;
        uint256 rewardAmount;
        bool isActive; // Whether the quest is active
        bool isClaimed; // Whether the reward is claimed
    }

    // Mapping from quest ID to Quest struct
    mapping(uint256 => Quest) public quests;

    // Mapping from user address to their completed quests
    mapping(address => uint256[]) public userCompletedQuests;

    // Event emitted when a quest is created
    event QuestCreated(uint256 indexed questId, string questName, uint256 rewardAmount);

    // Event emitted when a reward is claimed
    event RewardClaimed(address indexed user, uint256 indexed questId, uint256 rewardAmount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action.");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new quest.
     * @param questId Unique ID of the quest.
     * @param questName Name of the quest.
     * @param rewardAmount Amount of reward for completing the quest.
     */
    function createQuest(
        uint256 questId,
        string memory questName,
        uint256 rewardAmount
    ) external onlyOwner {
        require(quests[questId].rewardAmount == 0, "Quest ID already exists.");

        quests[questId] = Quest({
            questName: questName,
            rewardAmount: rewardAmount,
            isActive: true,
            isClaimed: false
        });

        emit QuestCreated(questId, questName, rewardAmount);
    }

    /**
     * @dev Function to mark a quest as completed for a user.
     * @param questId ID of the quest completed.
     */
    function markQuestAsCompleted(uint256 questId) external {
        require(quests[questId].isActive, "Quest is not active.");
        require(!quests[questId].isClaimed, "Reward for this quest is already claimed.");

        userCompletedQuests[msg.sender].push(questId);
    }

    /**
     * @dev Function to claim a reward for a completed quest.
     * @param questId ID of the quest reward being claimed.
     */
    function claimReward(uint256 questId) external {
        require(quests[questId].isActive, "Quest is not active.");
        require(!quests[questId].isClaimed, "Reward for this quest is already claimed.");
        require(isQuestCompletedByUser(msg.sender, questId), "User has not completed this quest.");

        // Mark the reward as claimed
        quests[questId].isClaimed = true;

        // Transfer the reward (simplified logic here for demonstration purposes)
        payable(msg.sender).transfer(quests[questId].rewardAmount);

        emit RewardClaimed(msg.sender, questId, quests[questId].rewardAmount);
    }

    /**
     * @dev Function to check if a quest is completed by a user.
     * @param user Address of the user.
     * @param questId ID of the quest.
     * @return Whether the quest is completed by the user.
     */
    function isQuestCompletedByUser(address user, uint256 questId) public view returns (bool) {
        uint256[] memory completedQuests = userCompletedQuests[user];
        for (uint256 i = 0; i < completedQuests.length; i++) {
            if (completedQuests[i] == questId) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Fallback function to accept Ether deposits.
     * Required for the contract to have balance for reward distribution.
     */
    receive() external payable {}

    /**
     * @dev Function to withdraw all Ether from the contract (restricted to owner).
     */
    function withdrawEther() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }
}
```
