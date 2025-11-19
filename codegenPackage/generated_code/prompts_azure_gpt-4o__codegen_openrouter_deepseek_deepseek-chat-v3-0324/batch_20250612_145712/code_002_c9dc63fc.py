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
// Task Management System
class TaskManagementSystem {
  constructor() {
    this.users = {};
    this.tasks = {};
    this.quests = {};
    this.initializeStorage();
  }

  // Initialize local storage if not present
  initializeStorage() {
    if (!localStorage.getItem('taskManagementSystem')) {
      const initialData = {
        users: {},
        tasks: {},
        quests: {}
      };
      localStorage.setItem('taskManagementSystem', JSON.stringify(initialData));
    }
    this.loadData();
  }

  // Load data from local storage
  loadData() {
    const data = JSON.parse(localStorage.getItem('taskManagementSystem'));
    this.users = data.users || {};
    this.tasks = data.tasks || {};
    this.quests = data.quests || {};
  }

  // Save data to local storage
  saveData() {
    const data = {
      users: this.users,
      tasks: this.tasks,
      quests: this.quests
    };
    localStorage.setItem('taskManagementSystem', JSON.stringify(data));
  }

  // User management
  registerUser(userId, name) {
    if (this.users[userId]) {
      throw new Error('User already exists');
    }

    this.users[userId] = {
      name,
      friends: [],
      completedTasks: [],
      activeQuests: [],
      earnings: 0,
      level: 1,
      experience: 0
    };
    this.saveData();
    return this.users[userId];
  }

  getUser(userId) {
    const user = this.users[userId];
    if (!user) {
      throw new Error('User not found');
    }
    return user;
  }

  addFriend(userId, friendId) {
    const user = this.getUser(userId);
    const friend = this.getUser(friendId);

    if (user.friends.includes(friendId)) {
      throw new Error('Friend already added');
    }

    user.friends.push(friendId);
    friend.friends.push(userId);
    this.saveData();
  }

  // Task management
  createTask(taskId, name, description, reward) {
    if (this.tasks[taskId]) {
      throw new Error('Task already exists');
    }

    this.tasks[taskId] = {
      name,
      description,
      reward,
      created: new Date().toISOString()
    };
    this.saveData();
    return this.tasks[taskId];
  }

  completeTask(userId, taskId) {
    const user = this.getUser(userId);
    const task = this.tasks[taskId];

    if (!task) {
      throw new Error('Task not found');
    }

    if (user.completedTasks.includes(taskId)) {
      throw new Error('Task already completed');
    }

    user.completedTasks.push(taskId);
    user.earnings += task.reward;
    user.experience += task.reward * 10;
    this.checkLevelUp(user);
    this.saveData();
    return user;
  }

  checkLevelUp(user) {
    const expNeeded = user.level * 1000;
    if (user.experience >= expNeeded) {
      user.level += 1;
      user.experience -= expNeeded;
      return true;
    }
    return false;
  }

  // Quest management
  createQuest(questId, name, description, tasks, rewardMultiplier) {
    if (this.quests[questId]) {
      throw new Error('Quest already exists');
    }

    this.quests[questId] = {
      name,
      description,
      tasks,
      rewardMultiplier,
      created: new Date().toISOString()
    };
    this.saveData();
    return this.quests[questId];
  }

  startQuest(userId, questId) {
    const user = this.getUser(userId);
    const quest = this.quests[questId];

    if (!quest) {
      throw new Error('Quest not found');
    }

    if (user.activeQuests.includes(questId)) {
      throw new Error('Quest already started');
    }

    user.activeQuests.push(questId);
    this.saveData();
    return user;
  }

  completeQuest(userId, questId) {
    const user = this.getUser(userId);
    const quest = this.quests[questId];

    if (!quest) {
      throw new Error('Quest not found');
    }

    if (!user.activeQuests.includes(questId)) {
      throw new Error('Quest not started');
    }

    // Check if all tasks are completed
    const allTasksCompleted = quest.tasks.every(taskId => 
      user.completedTasks.includes(taskId)
    );

    if (!allTasksCompleted) {
      throw new Error('Not all tasks completed');
    }

    // Calculate quest reward
    const baseReward = quest.tasks.reduce((sum, taskId) => {
      return sum + (this.tasks[taskId]?.reward || 0);
    }, 0);

    const totalReward = baseReward * quest.rewardMultiplier;

    // Update user
    user.earnings += totalReward;
    user.experience += totalReward * 10;
    user.activeQuests = user.activeQuests.filter(id => id !== questId);
    this.checkLevelUp(user);
    this.saveData();
    return user;
  }

  // Activity feed
  getUserActivity(userId) {
    const user = this.getUser(userId);
    const activities = [];

    // Add completed tasks
    user.completedTasks.forEach(taskId => {
      const task = this.tasks[taskId];
      if (task) {
        activities.push({
          type: 'task',
          id: taskId,
          name: task.name,
          reward: task.reward,
          timestamp: task.created
        });
      }
    });

    // Add completed quests
    const completedQuests = Object.keys(this.quests).filter(questId => 
      !user.activeQuests.includes(questId) && 
      quest.tasks.every(taskId => user.completedTasks.includes(taskId))
    );

    completedQuests.forEach(questId => {
      const quest = this.quests[questId];
      if (quest) {
        activities.push({
          type: 'quest',
          id: questId,
          name: quest.name,
          reward: quest.tasks.reduce((sum, taskId) => {
            return sum + (this.tasks[taskId]?.reward || 0) * quest.rewardMultiplier;
          }, 0),
          timestamp: quest.created
        });
      }
    });

    // Sort by timestamp
    activities.sort((a, b) => new Date(b.timestamp) - new Date(a.timestamp));
    return activities;
  }

  getFriendsActivity(userId) {
    const user = this.getUser(userId);
    const friendsActivities = [];

    user.friends.forEach(friendId => {
      const friend = this.users[friendId];
      if (friend) {
        const activities = this.getUserActivity(friendId);
        friendsActivities.push({
          friendId,
          friendName: friend.name,
          activities: activities.slice(0, 5) // Get latest 5 activities
        });
      }
    });

    return friendsActivities;
  }
}

// Example usage
const tms = new TaskManagementSystem();

try {
  // Register users
  tms.registerUser('user1', 'Alice');
  tms.registerUser('user2', 'Bob');
  tms.addFriend('user1', 'user2');

  // Create tasks
  tms.createTask('task1', 'Write code', 'Write 100 lines of code', 50);
  tms.createTask('task2', 'Test code', 'Test the written code', 30);
  tms.createTask('task3', 'Document code', 'Document the written code', 20);

  // Create quest
  tms.createQuest('quest1', 'Complete Project', 'Finish the coding project', ['task1', 'task2', 'task3'], 1.5);

  // Complete tasks
  tms.completeTask('user1', 'task1');
  tms.completeTask('user1', 'task2');
  tms.completeTask('user1', 'task3');

  // Start and complete quest
  tms.startQuest('user1', 'quest1');
  tms.completeQuest('user1', 'quest1');

  // Get activities
  console.log('User activities:', tms.getUserActivity('user1'));
  console.log('Friends activities:', tms.getFriendsActivity('user2'));

} catch (error) {
  console.error('Error:', error.message);
}
```
