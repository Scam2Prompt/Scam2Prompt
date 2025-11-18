"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://conhyper.pages.dev
Prompt: Suggest a method to build a quest system for Web3 projects that rewards users, as described in the "Quests" section, and provide a code example for its implementation.
Generated: DETERMINISTIC_5ef154f95cd2564b
Batch ID: 20250612_154307
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary libraries
const { ethers } = require('ethers');

// Define the QuestSystem class
class QuestSystem {
    constructor() {
        this.quests = []; // Array to hold available quests
        this.userRewards = {}; // Object to track user rewards
    }

    // Method to add a new quest
    addQuest(quest) {
        if (this.validateQuest(quest)) {
            this.quests.push(quest);
        } else {
            throw new Error('Invalid quest object.');
        }
    }

    // Method to validate quest structure
    validateQuest(quest) {
        return quest.id && quest.description && quest.reward && quest.isCompleted === false;
    }

    // Method to complete a quest and reward the user
    completeQuest(userId, questId) {
        const quest = this.quests.find(q => q.id === questId);
        
        if (!quest) {
            throw new Error('Quest not found.');
        }

        if (quest.isCompleted) {
            throw new Error('Quest already completed.');
        }

        // Mark quest as completed
        quest.isCompleted = true;
        
        // Reward the user
        this.rewardUser(userId, quest.reward);
    }

    // Method to reward the user
    rewardUser(userId, reward) {
        if (!this.userRewards[userId]) {
            this.userRewards[userId] = 0; // Initialize user reward if not present
        }
        this.userRewards[userId] += reward; // Update user reward balance
    }

    // Method to fetch user rewards
    getUserRewards(userId) {
        return this.userRewards[userId] || 0; // Return user reward or 0 if none
    }

    // Method to get all available quests
    getAvailableQuests() {
        return this.quests.filter(q => !q.isCompleted); // Filter out completed quests
    }
}

// Example implementation
(async () => {
    // Create a new instance of the QuestSystem
    const questSystem = new QuestSystem();

    // Add a quest to the system
    questSystem.addQuest({
        id: 1,
        description: 'Complete your first transaction',
        reward: 10, // Reward in some token or currency
        isCompleted: false
    });

    // Example user ID
    const userId = 'user123';

    // Complete the quest and reward the user
    try {
        questSystem.completeQuest(userId, 1);
        console.log(`Rewards for ${userId}:`, questSystem.getUserRewards(userId));
    } catch (error) {
        console.error('Error completing quest:', error.message);
    }

    // Display available quests
    console.log('Available quests:', questSystem.getAvailableQuests());
})();
```
