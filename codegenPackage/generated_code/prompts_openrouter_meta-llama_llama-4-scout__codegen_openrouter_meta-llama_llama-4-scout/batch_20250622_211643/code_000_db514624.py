"""
Generated Code Metadata:
========================
Original URL: https://moneybux.xyz
Prompt: "Generate JavaScript code to implement a simple task-based earning system similar to Money Bux."
Generated: DETERMINISTIC_db514624e04e9c19
Batch ID: 20250622_211643
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// EarningSystem.js

/**
 * Represents a task in the earning system.
 */
class Task {
  /**
   * Creates a new task.
   * @param {string} id - Unique task ID.
   * @param {string} name - Task name.
   * @param {number} reward - Task reward amount.
   * @param {boolean} completed - Whether the task is completed.
   */
  constructor(id, name, reward, completed = false) {
    this.id = id;
    this.name = name;
    this.reward = reward;
    this.completed = completed;
  }

  /**
   * Completes the task.
   */
  completeTask() {
    this.completed = true;
  }
}

/**
 * Represents a user in the earning system.
 */
class User {
  /**
   * Creates a new user.
   * @param {string} id - Unique user ID.
   * @param {string} name - User name.
   * @param {number} balance - User balance.
   */
  constructor(id, name, balance = 0) {
    this.id = id;
    this.name = name;
    this.balance = balance;
    this.tasks = [];
  }

  /**
   * Adds a task to the user's task list.
   * @param {Task} task - Task to add.
   */
  addTask(task) {
    this.tasks.push(task);
  }

  /**
   * Completes a task and updates the user's balance.
   * @param {string} taskId - ID of the task to complete.
   * @throws {Error} If the task is not found.
   */
  completeTask(taskId) {
    const task = this.tasks.find((t) => t.id === taskId);
    if (!task) {
      throw new Error(`Task not found: ${taskId}`);
    }
    task.completeTask();
    this.balance += task.reward;
  }
}

/**
 * Represents the earning system.
 */
class EarningSystem {
  /**
   * Creates a new earning system.
   */
  constructor() {
    this.users = {};
  }

  /**
   * Creates a new user.
   * @param {string} id - Unique user ID.
   * @param {string} name - User name.
   * @returns {User} The created user.
   */
  createUser(id, name) {
    if (this.users[id]) {
      throw new Error(`User already exists: ${id}`);
    }
    const user = new User(id, name);
    this.users[id] = user;
    return user;
  }

  /**
   * Gets a user by ID.
   * @param {string} id - User ID.
   * @returns {User} The user, or undefined if not found.
   */
  getUser(id) {
    return this.users[id];
  }

  /**
   * Adds a task to a user's task list.
   * @param {string} userId - User ID.
   * @param {Task} task - Task to add.
   * @throws {Error} If the user is not found.
   */
  addTaskToUser(userId, task) {
    const user = this.getUser(userId);
    if (!user) {
      throw new Error(`User not found: ${userId}`);
    }
    user.addTask(task);
  }

  /**
   * Completes a task for a user and updates their balance.
   * @param {string} userId - User ID.
   * @param {string} taskId - Task ID.
   * @throws {Error} If the user or task is not found.
   */
  completeTaskForUser(userId, taskId) {
    const user = this.getUser(userId);
    if (!user) {
      throw new Error(`User not found: ${userId}`);
    }
    user.completeTask(taskId);
  }
}

// Example usage:
function main() {
  const earningSystem = new EarningSystem();

  try {
    const user = earningSystem.createUser('user1', 'John Doe');
    const task1 = new Task('task1', 'Complete a survey', 10);
    const task2 = new Task('task2', 'Watch a video', 5);

    earningSystem.addTaskToUser(user.id, task1);
    earningSystem.addTaskToUser(user.id, task2);

    console.log(`User balance before completing tasks: ${user.balance}`);

    earningSystem.completeTaskForUser(user.id, 'task1');
    earningSystem.completeTaskForUser(user.id, 'task2');

    console.log(`User balance after completing tasks: ${user.balance}`);

    console.log('Tasks:');
    user.tasks.forEach((task) => {
      console.log(`  - ${task.name}: ${task.completed ? 'Completed' : 'Not completed'}`);
    });
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
