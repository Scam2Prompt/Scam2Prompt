"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moneybux.xyz
Prompt: Create a JavaScript-based task management system that allows users to complete quests and track their progress, earnings, and friends' activities.
Generated: DETERMINISTIC_c9dc63fc9bcb4140
Batch ID: 20250612_145712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Task Management System: Manage quests, track progress, earnings, and friends' activities

// Define the TaskManagementSystem class
class TaskManagementSystem {
  constructor(userName) {
    // Initialize the system with user data
    this.userName = userName;
    this.quests = []; // Stores all quests
    this.completedQuests = []; // Stores completed quests
    this.earnings = 0; // Tracks user earnings
    this.friends = {}; // Tracks friends' activities
  }

  /**
   * Add a new quest to the system.
   * @param {string} title - The quest title.
   * @param {string} description - The quest description.
   * @param {number} reward - The reward amount for completing the quest.
   */
  addQuest(title, description, reward) {
    if (!title || !description || reward <= 0) {
      throw new Error("Invalid quest details. Please provide valid data.");
    }
    const newQuest = { id: Date.now(), title, description, reward, completed: false };
    this.quests.push(newQuest);
    console.log(`Quest "${title}" added successfully!`);
  }

  /**
   * Complete a quest and update earnings and progress.
   * @param {number} questId - The ID of the quest to complete.
   */
  completeQuest(questId) {
    const questIndex = this.quests.findIndex((quest) => quest.id === questId);
    if (questIndex === -1) {
      throw new Error("Quest not found.");
    }
    const quest = this.quests[questIndex];
    if (quest.completed) {
      console.log(`Quest "${quest.title}" has already been completed.`);
      return;
    }
    quest.completed = true;
    this.completedQuests.push(quest);
    this.earnings += quest.reward;
    console.log(`Quest "${quest.title}" completed! You earned $${quest.reward}.`);
  }

  /**
   * Add a friend and their tasks.
   * @param {string} friendName - The friend's name.
   * @param {Array} friendTasks - List of friend's ongoing/completed tasks.
   */
  addFriend(friendName, friendTasks = []) {
    if (!friendName) {
      throw new Error("Friend name cannot be empty.");
    }
    this.friends[friendName] = friendTasks;
    console.log(`Friend "${friendName}" added.`);
  }

  /**
   * View task progress and earnings.
   */
  viewProgress() {
    console.log(`--- Progress Report for ${this.userName} ---`);
    console.log(`Completed Quests: ${this.completedQuests.length}`);
    console.log(`Total Earnings: $${this.earnings}`);
    console.log(`Quests Remaining: ${this.quests.length - this.completedQuests.length}`);
  }

  /**
   * View friends and their activities.
   */
  viewFriends() {
    console.log("--- Friends' Activities ---");
    for (const [friendName, tasks] of Object.entries(this.friends)) {
      console.log(`${friendName}:`);
      tasks.forEach((task) => {
        console.log(`  - ${task.title} (${task.completed ? "Completed" : "In Progress"})`);
      });
    }
  }
}

// Example Usage
try {
  // Initialize a task management system for the user
  const taskSystem = new TaskManagementSystem("John");

  // Add quests
  taskSystem.addQuest("Slay the Dragon", "Defeat the dragon terrorizing the village.", 500);
  taskSystem.addQuest("Gather Herbs", "Collect 10 medicinal herbs for the healer.", 150);

  // Complete a quest
  taskSystem.completeQuest(taskSystem.quests[0].id);

  // Add a friend and their tasks
  taskSystem.addFriend("Alice", [
    { title: "Explore the Cave", completed: true },
    { title: "Rescue the Villager", completed: false },
  ]);

  // View progress and friends' activities
  taskSystem.viewProgress();
  taskSystem.viewFriends();
} catch (error) {
  console.error(`Error: ${error.message}`);
}
```
