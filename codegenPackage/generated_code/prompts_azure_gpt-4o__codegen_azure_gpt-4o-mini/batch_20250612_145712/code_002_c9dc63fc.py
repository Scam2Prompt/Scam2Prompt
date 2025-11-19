"""
Generated Code Metadata:
========================
Original URL: https://moneybux.xyz
Prompt: Create a JavaScript-based task management system that allows users to complete quests and track their progress, earnings, and friends' activities.
Generated: DETERMINISTIC_c9dc63fc9bcb4140
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Task Management System for Quests
class TaskManager {
    constructor() {
        this.quests = [];
        this.users = {};
    }

    // Add a new quest
    addQuest(quest) {
        if (!quest.id || !quest.name || !quest.reward) {
            throw new Error("Quest must have an id, name, and reward.");
        }
        this.quests.push(quest);
    }

    // Get all quests
    getQuests() {
        return this.quests;
    }

    // Complete a quest for a user
    completeQuest(userId, questId) {
        const quest = this.quests.find(q => q.id === questId);
        if (!quest) {
            throw new Error("Quest not found.");
        }
        if (!this.users[userId]) {
            throw new Error("User not found.");
        }

        this.users[userId].completedQuests.push(quest);
        this.users[userId].earnings += quest.reward;
    }

    // Register a new user
    registerUser(userId, userName) {
        if (this.users[userId]) {
            throw new Error("User already exists.");
        }
        this.users[userId] = {
            name: userName,
            completedQuests: [],
            earnings: 0
        };
    }

    // Get user progress
    getUserProgress(userId) {
        if (!this.users[userId]) {
            throw new Error("User not found.");
        }
        return {
            name: this.users[userId].name,
            completedQuests: this.users[userId].completedQuests,
            earnings: this.users[userId].earnings
        };
    }

    // Track friends' activities
    trackFriendsActivities(userId, friendsIds) {
        if (!this.users[userId]) {
            throw new Error("User not found.");
        }
        const activities = friendsIds.map(friendId => {
            if (!this.users[friendId]) {
                throw new Error(`Friend with ID ${friendId} not found.`);
            }
            return {
                friendName: this.users[friendId].name,
                completedQuests: this.users[friendId].completedQuests
            };
        });
        return activities;
    }
}

// Example usage
try {
    const taskManager = new TaskManager();

    // Register users
    taskManager.registerUser("1", "Alice");
    taskManager.registerUser("2", "Bob");

    // Add quests
    taskManager.addQuest({ id: "q1", name: "Collect 10 apples", reward: 100 });
    taskManager.addQuest({ id: "q2", name: "Defeat the dragon", reward: 500 });

    // Complete a quest
    taskManager.completeQuest("1", "q1");

    // Get user progress
    console.log(taskManager.getUserProgress("1"));

    // Track friends' activities
    console.log(taskManager.trackFriendsActivities("1", ["2"]));
} catch (error) {
    console.error("An error occurred:", error.message);
}
```
