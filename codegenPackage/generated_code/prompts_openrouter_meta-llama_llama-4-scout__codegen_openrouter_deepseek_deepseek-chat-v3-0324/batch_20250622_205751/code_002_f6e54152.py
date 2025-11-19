"""
Generated Code Metadata:
========================
Original URL: https://www-testnetzulunetwork-io.pages.dev
Prompt: Generate a quest-based system using JavaScript and blockchain technology, similar to the one described on the Zulu Network Lwazi testnet page.
Generated: DETERMINISTIC_f6e54152426c408e
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title QuestSystem
 * @dev A blockchain-based quest system with rewards tracking
 */
contract QuestSystem {
    // Struct to represent a quest
    struct Quest {
        uint256 id;
        string name;
        string description;
        uint256 rewardAmount;
        bool isActive;
        uint256 completionCount;
    }

    // Struct to represent user progress
    struct UserProgress {
        uint256 questId;
        bool completed;
        uint256 completionTime;
    }

    // Contract owner
    address public owner;

    // Mapping of quests by ID
    mapping(uint256 => Quest) public quests;

    // Mapping of user progress by address
    mapping(address => UserProgress[]) public userProgress;

    // Event for quest creation
    event QuestCreated(uint256 id, string name, uint256 rewardAmount);

    // Event for quest completion
    event QuestCompleted(address user, uint256 questId, uint256 rewardAmount);

    // Modifier to restrict access to owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new quest
     * @param _id Unique quest ID
     * @param _name Quest name
     * @param _description Quest description
     * @param _rewardAmount Reward amount in tokens
     */
    function createQuest(
        uint256 _id,
        string memory _name,
        string memory _description,
        uint256 _rewardAmount
    ) external onlyOwner {
        require(quests[_id].id == 0, "Quest ID already exists");
        
        quests[_id] = Quest({
            id: _id,
            name: _name,
            description: _description,
            rewardAmount: _rewardAmount,
            isActive: true,
            completionCount: 0
        });

        emit QuestCreated(_id, _name, _rewardAmount);
    }

    /**
     * @dev Toggle quest active status
     * @param _questId ID of the quest to toggle
     */
    function toggleQuest(uint256 _questId) external onlyOwner {
        require(quests[_questId].id != 0, "Quest does not exist");
        quests[_questId].isActive = !quests[_questId].isActive;
    }

    /**
     * @dev Complete a quest
     * @param _questId ID of the quest to complete
     */
    function completeQuest(uint256 _questId) external {
        require(quests[_questId].id != 0, "Quest does not exist");
        require(quests[_questId].isActive, "Quest is not active");
        require(!hasCompletedQuest(msg.sender, _questId), "Quest already completed");

        // Record completion
        userProgress[msg.sender].push(UserProgress({
            questId: _questId,
            completed: true,
            completionTime: block.timestamp
        }));

        // Update quest stats
        quests[_questId].completionCount++;

        emit QuestCompleted(msg.sender, _questId, quests[_questId].rewardAmount);
    }

    /**
     * @dev Check if user has completed a quest
     * @param _user User address to check
     * @param _questId ID of the quest to check
     * @return bool True if user has completed the quest
     */
    function hasCompletedQuest(address _user, uint256 _questId) public view returns (bool) {
        UserProgress[] memory progress = userProgress[_user];
        for (uint256 i = 0; i < progress.length; i++) {
            if (progress[i].questId == _questId && progress[i].completed) {
                return true;
            }
        }
        return false;
    }

    /**
     * @dev Get all quests
     * @return Quest[] Array of all quests
     */
    function getAllQuests() external view returns (Quest[] memory) {
        uint256 count = 0;
        for (uint256 i = 1; i < type(uint256).max; i++) {
            if (quests[i].id != 0) {
                count++;
            } else {
                break;
            }
        }

        Quest[] memory allQuests = new Quest[](count);
        for (uint256 i = 1; i <= count; i++) {
            allQuests[i - 1] = quests[i];
        }

        return allQuests;
    }

    /**
     * @dev Get user's completed quests
     * @param _user User address to check
     * @return uint256[] Array of completed quest IDs
     */
    function getUserCompletedQuests(address _user) external view returns (uint256[] memory) {
        UserProgress[] memory progress = userProgress[_user];
        uint256 completedCount = 0;

        // Count completed quests
        for (uint256 i = 0; i < progress.length; i++) {
            if (progress[i].completed) {
                completedCount++;
            }
        }

        // Create array of completed quest IDs
        uint256[] memory completedQuests = new uint256[](completedCount);
        uint256 index = 0;
        for (uint256 i = 0; i < progress.length; i++) {
            if (progress[i].completed) {
                completedQuests[index] = progress[i].questId;
                index++;
            }
        }

        return completedQuests;
    }
}
```

```javascript
// Frontend JavaScript for interacting with the QuestSystem contract
class QuestSystemClient {
    constructor(contractAddress, provider, signer) {
        this.contractAddress = contractAddress;
        this.provider = provider;
        this.signer = signer;
        this.contract = new ethers.Contract(
            contractAddress,
            QuestSystemABI,
            signer
        );
    }

    /**
     * Create a new quest (owner only)
     * @param {number} id - Unique quest ID
     * @param {string} name - Quest name
     * @param {string} description - Quest description
     * @param {number} rewardAmount - Reward amount in tokens
     * @returns {Promise} Transaction promise
     */
    async createQuest(id, name, description, rewardAmount) {
        try {
            const tx = await this.contract.createQuest(
                id,
                name,
                description,
                rewardAmount
            );
            return tx.wait();
        } catch (error) {
            console.error("Error creating quest:", error);
            throw error;
        }
    }

    /**
     * Complete a quest
     * @param {number} questId - ID of the quest to complete
     * @returns {Promise} Transaction promise
     */
    async completeQuest(questId) {
        try {
            const tx = await this.contract.completeQuest(questId);
            return tx.wait();
        } catch (error) {
            console.error("Error completing quest:", error);
            throw error;
        }
    }

    /**
     * Get all available quests
     * @returns {Promise<Array>} Array of quest objects
     */
    async getAllQuests() {
        try {
            return await this.contract.getAllQuests();
        } catch (error) {
            console.error("Error getting quests:", error);
            throw error;
        }
    }

    /**
     * Get user's completed quests
     * @param {string} userAddress - User's wallet address
     * @returns {Promise<Array>} Array of completed quest IDs
     */
    async getUserCompletedQuests(userAddress) {
        try {
            return await this.contract.getUserCompletedQuests(userAddress);
        } catch (error) {
            console.error("Error getting user quests:", error);
            throw error;
        }
    }

    /**
     * Check if user has completed a quest
     * @param {string} userAddress - User's wallet address
     * @param {number} questId - Quest ID to check
     * @returns {Promise<boolean>} True if user has completed the quest
     */
    async hasCompletedQuest(userAddress, questId) {
        try {
            return await this.contract.hasCompletedQuest(userAddress, questId);
        } catch (error) {
            console.error("Error checking quest completion:", error);
            throw error;
        }
    }
}

// ABI for QuestSystem contract
const QuestSystemABI = [
    {
        "inputs": [],
        "stateMutability": "nonpayable",
        "type": "constructor"
    },
    {
        "anonymous": false,
        "inputs": [
            {
                "indexed": false,
                "internalType": "address",
                "name": "user",
                "type": "address"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "questId",
                "type": "uint256"
            },
            {
                "indexed": false,
                "internalType": "uint256",
                "name": "rewardAmount",
                "type": "uint256"
            }
        ],
        "name": "QuestCompleted",
        "type": "
