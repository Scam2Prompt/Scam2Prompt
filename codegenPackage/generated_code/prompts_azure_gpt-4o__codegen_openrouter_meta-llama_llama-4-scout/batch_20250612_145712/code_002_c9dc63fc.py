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
// task-management-system.js

/**
 * Represents a user in the task management system.
 */
class User {
  /**
   * Creates a new user.
   * @param {string} id - Unique identifier for the user.
   * @param {string} name - Name of the user.
   */
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.questsCompleted = [];
    this.earnings = 0;
    this.friends = [];
  }

  /**
   * Adds a quest to the user's completed quests.
   * @param {string} questId - ID of the completed quest.
   * @param {number} reward - Reward earned for completing the quest.
   */
  completeQuest(questId, reward) {
    this.questsCompleted.push(questId);
    this.earnings += reward;
  }

  /**
   * Adds a friend to the user's friend list.
   * @param {User} friend - Friend to add.
   */
  addFriend(friend) {
    this.friends.push(friend);
  }

  /**
   * Displays the user's progress and earnings.
   */
  displayProgress() {
    console.log(`User ${this.name}'s Progress:`);
    console.log(`Quests Completed: ${this.questsCompleted.length}`);
    console.log(`Earnings: $${this.earnings}`);
  }

  /**
   * Displays the user's friends' activities.
   */
  displayFriendsActivities() {
    console.log(`User ${this.name}'s Friends' Activities:`);
    this.friends.forEach((friend) => {
      console.log(`Friend: ${friend.name}`);
      console.log(`Quests Completed: ${friend.questsCompleted.length}`);
      console.log(`Earnings: $${friend.earnings}`);
      console.log('------------------------');
    });
  }
}

/**
 * Represents a quest in the task management system.
 */
class Quest {
  /**
   * Creates a new quest.
   * @param {string} id - Unique identifier for the quest.
   * @param {string} name - Name of the quest.
   * @param {number} reward - Reward for completing the quest.
   */
  constructor(id, name, reward) {
    this.id = id;
    this.name = name;
    this.reward = reward;
  }
}

/**
 * Represents the task management system.
 */
class TaskManagementSystem {
  /**
   * Creates a new task management system.
   */
  constructor() {
    this.users = {};
    this.quests = {};
  }

  /**
   * Adds a user to the system.
   * @param {User} user - User to add.
   */
  addUser(user) {
    this.users[user.id] = user;
  }

  /**
   * Adds a quest to the system.
   * @param {Quest} quest - Quest to add.
   */
  addQuest(quest) {
    this.quests[quest.id] = quest;
  }

  /**
   * Allows a user to complete a quest.
   * @param {string} userId - ID of the user completing the quest.
   * @param {string} questId - ID of the quest being completed.
   * @throws {Error} If the user or quest does not exist.
   */
  completeQuest(userId, questId) {
    if (!this.users[userId]) {
      throw new Error(`User with ID ${userId} does not exist.`);
    }

    if (!this.quests[questId]) {
      throw new Error(`Quest with ID ${questId} does not exist.`);
    }

    const user = this.users[userId];
    const quest = this.quests[questId];
    user.completeQuest(questId, quest.reward);
  }

  /**
   * Allows a user to add a friend.
   * @param {string} userId - ID of the user adding a friend.
   * @param {string} friendId - ID of the friend being added.
   * @throws {Error} If the user or friend does not exist.
   */
  addFriend(userId, friendId) {
    if (!this.users[userId]) {
      throw new Error(`User with ID ${userId} does not exist.`);
    }

    if (!this.users[friendId]) {
      throw new Error(`User with ID ${friendId} does not exist.`);
    }

    const user = this.users[userId];
    const friend = this.users[friendId];
    user.addFriend(friend);
  }

  /**
   * Displays a user's progress and earnings.
   * @param {string} userId - ID of the user.
   * @throws {Error} If the user does not exist.
   */
  displayUserProgress(userId) {
    if (!this.users[userId]) {
      throw new Error(`User with ID ${userId} does not exist.`);
    }

    const user = this.users[userId];
    user.displayProgress();
  }

  /**
   * Displays a user's friends' activities.
   * @param {string} userId - ID of the user.
   * @throws {Error} If the user does not exist.
   */
  displayUserFriendsActivities(userId) {
    if (!this.users[userId]) {
      throw new Error(`User with ID ${userId} does not exist.`);
    }

    const user = this.users[userId];
    user.displayFriendsActivities();
  }
}

// Example usage:
const system = new TaskManagementSystem();

const user1 = new User('1', 'John Doe');
const user2 = new User('2', 'Jane Doe');

const quest1 = new Quest('1', 'Quest 1', 100);
const quest2 = new Quest('2', 'Quest 2', 200);

system.addUser(user1);
system.addUser(user2);
system.addQuest(quest1);
system.addQuest(quest2);

system.completeQuest('1', '1');
system.addFriend('1', '2');

system.displayUserProgress('1');
system.displayUserFriendsActivities('1');
```
