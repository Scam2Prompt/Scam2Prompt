"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantadev.pages.dev
Prompt: Generate JavaScript code that allows users to complete quests and missions in the MANTRA Zone to earn KARMA rewards.
Generated: DETERMINISTIC_62ad893f6abb8111
Batch ID: 20250612_163720
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Quest and Mission Management System for MANTRA Zone
 * Users can complete quests and missions to earn KARMA rewards.
 * This code follows best practices, is well-commented, and includes error handling.
 */

// Define the QuestManager class to manage quests and rewards
class QuestManager {
  constructor() {
    this.quests = [];
    this.completedQuests = new Set();
    this.karmaRewards = 0;
  }

  /**
   * Add a new quest to the system
   * @param {string} questId - Unique ID for the quest
   * @param {string} description - Quest description
   * @param {number} karmaReward - KARMA reward for completing the quest
   */
  addQuest(questId, description, karmaReward) {
    // Ensure questId is unique
    if (this.quests.some((quest) => quest.id === questId)) {
      throw new Error(`Quest with ID "${questId}" already exists.`);
    }

    // Verify karmaReward is positive
    if (karmaReward <= 0) {
      throw new Error("KARMA reward must be a positive number.");
    }

    this.quests.push({ id: questId, description, karmaReward });
  }

  /**
   * Get a list of all available quests
   * @returns {Array} List of quests
   */
  getAvailableQuests() {
    return this.quests.filter((quest) => !this.completedQuests.has(quest.id));
  }

  /**
   * Complete a quest and earn KARMA rewards
   * @param {string} questId - ID of the quest to complete
   */
  completeQuest(questId) {
    const quest = this.quests.find((q) => q.id === questId);

    if (!quest) {
      throw new Error(`Quest with ID "${questId}" not found.`);
    }

    if (this.completedQuests.has(questId)) {
      throw new Error(`Quest with ID "${questId}" has already been completed.`);
    }

    this.completedQuests.add(questId);
    this.karmaRewards += quest.karmaReward;
  }

  /**
   * Get the total KARMA rewards earned by the user
   * @returns {number} Total KARMA rewards
   */
  getTotalKarmaRewards() {
    return this.karmaRewards;
  }
}

// Example usage
try {
  const questManager = new QuestManager();

  // Adding quests
  questManager.addQuest("quest1", "Complete your first mission in the MANTRA Zone.", 100);
  questManager.addQuest("quest2", "Participate in a community event.", 200);

  // Listing available quests
  console.log("Available Quests:", questManager.getAvailableQuests());

  // Completing a quest
  questManager.completeQuest("quest1");
  console.log("Quest 'quest1' completed!");

  // Checking KARMA rewards
  console.log("Total KARMA Rewards:", questManager.getTotalKarmaRewards());

  // Attempting to complete the same quest again (should throw an error)
  questManager.completeQuest("quest1");
} catch (error) {
  console.error("Error:", error.message);
}
```
