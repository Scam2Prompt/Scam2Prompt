"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metis-a7k.pages.dev
Prompt: Write a smart contract that awards Epic NFTs to users based on their performance in Metis quests.
Generated: DETERMINISTIC_6003796f90691472
Batch ID: 20250612_152511
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
 * @title EpicNFTRewarder
 * @dev A smart contract to award Epic NFTs to users based on their performance in Metis quests.
 */
contract EpicNFTRewarder {
    // Address of the owner (contract deployer)
    address public owner;

    // Struct to represent a Quest
    struct Quest {
        uint256 questId;
        string questName;
        uint256 performanceThreshold; // Performance score required to earn an NFT
    }

    // Mapping to store quests
    mapping(uint256 => Quest) public quests;

    // Mapping to track which users have earned an NFT for a specific quest
    mapping(uint256 => mapping(address => bool)) public questRewards;

    // Event emitted when a user earns an NFT
    event NFTAwarded(address indexed user, uint256 indexed questId, string questName);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Permission denied: Only owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to add a new quest.
     * @param questId Unique identifier for the quest.
     * @param questName Name of the quest.
     * @param performanceThreshold Performance score required to earn an NFT.
     */
    function addQuest(
        uint256 questId,
        string memory questName,
        uint256 performanceThreshold
    ) external onlyOwner {
        require(bytes(questName).length > 0, "Quest name cannot be empty");
        require(performanceThreshold > 0, "Performance threshold must be greater than zero");

        // Ensure questId is unique
        require(bytes(quests[questId].questName).length == 0, "Quest ID already exists");

        // Add the quest
        quests[questId] = Quest(questId, questName, performanceThreshold);
    }

    /**
     * @dev Function to award an Epic NFT to a user based on their performance in a quest.
     * @param questId The quest ID for which the user is being evaluated.
     * @param user The address of the user.
     * @param userPerformance The performance score of the user.
     */
    function awardNFT(
        uint256 questId,
        address user,
        uint256 userPerformance
    ) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(bytes(quests[questId].questName).length > 0, "Quest does not exist");
        require(!questRewards[questId][user], "User has already been awarded for this quest");

        Quest memory quest = quests[questId];

        // Check if the user's performance meets the threshold
        require(userPerformance >= quest.performanceThreshold, "User performance does not meet the required threshold");

        // Mark reward as given
        questRewards[questId][user] = true;

        // Emit event for awarding NFT
        emit NFTAwarded(user, quest.questId, quest.questName);
    }

    /**
     * @dev Function to check if a user has received an NFT for a specific quest.
     * @param questId The quest ID.
     * @param user The address of the user.
     * @return bool True if the user has received an NFT, false otherwise.
     */
    function hasUserReceivedNFT(uint256 questId, address user) external view returns (bool) {
        return questRewards[questId][user];
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
