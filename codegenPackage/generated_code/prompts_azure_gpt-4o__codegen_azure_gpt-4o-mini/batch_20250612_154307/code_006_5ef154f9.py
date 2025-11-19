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

```javascript
// Import necessary libraries
const { ethers } = require("ethers");

// Define the QuestSystem contract
class QuestSystem {
    constructor() {
        this.quests = []; // Array to hold quests
        this.userRewards = {}; // Object to track user rewards
    }

    // Method to create a new quest
    createQuest(title, description, reward) {
        // Validate input parameters
        if (!title || !description || !reward) {
            throw new Error("Invalid quest parameters");
        }

        const quest = {
            id: this.quests.length + 1,
            title,
            description,
            reward,
            completedBy: new Set(), // Track users who completed the quest
        };

        this.quests.push(quest);
        return quest;
    }

    // Method for a user to complete a quest
    completeQuest(userId, questId) {
        // Validate input parameters
        if (!userId || !questId) {
            throw new Error("User ID and Quest ID are required");
        }

        const quest = this.quests.find(q => q.id === questId);
        if (!quest) {
            throw new Error("Quest not found");
        }

        // Check if the user has already completed the quest
        if (quest.completedBy.has(userId)) {
            throw new Error("Quest already completed by this user");
        }

        // Mark the quest as completed by the user
        quest.completedBy.add(userId);
        this.rewardUser(userId, quest.reward);
        return `Quest "${quest.title}" completed! Reward: ${quest.reward}`;
    }

    // Method to reward a user
    rewardUser(userId, reward) {
        // Initialize user rewards if not already done
        if (!this.userRewards[userId]) {
            this.userRewards[userId] = 0;
        }

        // Update user rewards
        this.userRewards[userId] += reward;
    }

    // Method to get user rewards
    getUserRewards(userId) {
        return this.userRewards[userId] || 0;
    }

    // Method to get all quests
    getAllQuests() {
        return this.quests;
    }
}

// Example usage
(async () => {
    try {
        const questSystem = new QuestSystem();

        // Create quests
        questSystem.createQuest("First Quest", "Complete the first task", 10);
        questSystem.createQuest("Second Quest", "Complete the second task", 20);

        // User completes a quest
        console.log(questSystem.completeQuest("user1", 1));

        // Get user rewards
        console.log(`User1 Rewards: ${questSystem.getUserRewards("user1")}`);

        // Get all quests
        console.log(questSystem.getAllQuests());
    } catch (error) {
        console.error("Error:", error.message);
    }
})();
```
