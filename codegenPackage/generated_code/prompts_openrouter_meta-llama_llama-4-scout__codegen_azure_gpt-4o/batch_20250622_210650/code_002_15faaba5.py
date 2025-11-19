"""
Generated Code Metadata:
========================
Original URL: https://kangamoon-zealyreward.pages.dev
Prompt: Generate a JavaScript code snippet to implement a simple quest completion system, like the one on Kangamoon, that awards XP for tasks such as inviting friends to join Zealy.
Generated: DETERMINISTIC_15faaba5226dc92d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quest Completion System
// This script implements a simple quest completion system that awards XP for completing tasks like inviting friends.

class QuestCompletionSystem {
  constructor() {
    // Initialize the system with default values
    this.quests = {}; // Stores quest details
    this.userXP = {}; // Stores user XP
  }

  /**
   * Adds a new quest to the system.
   * @param {string} questId - Unique identifier for the quest.
   * @param {string} description - Description of the quest.
   * @param {number} xpReward - XP awarded for completing the quest.
   */
  addQuest(questId, description, xpReward) {
    if (!questId || !description || !xpReward || xpReward <= 0) {
      throw new Error("Invalid quest details provided.");
    }
    this.quests[questId] = { description, xpReward, completedBy: [] };
  }

  /**
   * Marks a quest as completed by a user and awards XP.
   * @param {string} userId - Unique identifier for the user.
   * @param {string} questId - Unique identifier for the quest.
   */
  completeQuest(userId, questId) {
    if (!userId || !questId) {
      throw new Error("User ID and Quest ID are required.");
    }

    const quest = this.quests[questId];
    if (!quest) {
      throw new Error("Quest not found.");
    }

    if (quest.completedBy.includes(userId)) {
      throw new Error("Quest already completed by this user.");
    }

    // Mark quest as completed by the user
    quest.completedBy.push(userId);

    // Award XP to the user
    this.userXP[userId] = (this.userXP[userId] || 0) + quest.xpReward;
  }

  /**
   * Retrieves the XP of a user.
   * @param {string} userId - Unique identifier for the user.
   * @returns {number} - The user's total XP.
   */
  getUserXP(userId) {
    if (!userId) {
      throw new Error("User ID is required.");
    }
    return this.userXP[userId] || 0;
  }

  /**
   * Retrieves the details of a quest.
   * @param {string} questId - Unique identifier for the quest.
   * @returns {object} - The quest details.
   */
  getQuestDetails(questId) {
    if (!questId) {
      throw new Error("Quest ID is required.");
    }
    const quest = this.quests[questId];
    if (!quest) {
      throw new Error("Quest not found.");
    }
    return quest;
  }
}

// Example usage:

try {
  const questSystem = new QuestCompletionSystem();

  // Add quests
  questSystem.addQuest("invite_friends", "Invite friends to join Zealy", 100);
  questSystem.addQuest("complete_profile", "Complete your profile", 50);

  // Complete quests
  questSystem.completeQuest("user123", "invite_friends");
  questSystem.completeQuest("user123", "complete_profile");

  // Retrieve user XP
  console.log("User XP:", questSystem.getUserXP("user123")); // Output: User XP: 150

  // Retrieve quest details
  console.log("Quest Details:", questSystem.getQuestDetails("invite_friends"));
} catch (error) {
  console.error("Error:", error.message);
}
```
