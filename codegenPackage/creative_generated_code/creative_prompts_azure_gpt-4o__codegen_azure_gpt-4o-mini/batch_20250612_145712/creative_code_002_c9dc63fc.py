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
// Task Management System

class Task {
    constructor(title, description) {
        this.title = title;
        this.description = description;
        this.completed = false;
        this.earnings = 0;
    }

    // Mark task as completed
    complete() {
        if (!this.completed) {
            this.completed = true;
            this.earnings = this.calculateEarnings();
            return this.earnings;
        }
        throw new Error("Task is already completed.");
    }

    // Calculate earnings based on task type
    calculateEarnings() {
        return Math.floor(Math.random() * 100) + 1; // Random earnings between 1 and 100
    }
}

class User {
    constructor(name) {
        this.name = name;
        this.completedTasks = [];
        this.totalEarnings = 0;
    }

    // Complete a task and track progress
    completeTask(task) {
        try {
            const earnings = task.complete();
            this.completedTasks.push(task);
            this.totalEarnings += earnings;
            console.log(`Task '${task.title}' completed! Earnings: ${earnings}. Total Earnings: ${this.totalEarnings}`);
        } catch (error) {
            console.error(error.message);
        }
    }

    // Get a summary of completed tasks
    getTaskSummary() {
        return this.completedTasks.map(task => ({
            title: task.title,
            description: task.description,
            completed: task.completed,
            earnings: task.earnings
        }));
    }
}

class TaskManager {
    constructor() {
        this.tasks = [];
        this.users = [];
    }

    // Add a new task
    addTask(title, description) {
        const task = new Task(title, description);
        this.tasks.push(task);
    }

    // Register a new user
    registerUser(name) {
        const user = new User(name);
        this.users.push(user);
    }

    // Get all users' activities
    getAllUsersActivities() {
        return this.users.map(user => ({
            user: user.name,
            completedTasks: user.getTaskSummary(),
            totalEarnings: user.totalEarnings
        }));
    }
}

// Example usage:
const taskManager = new TaskManager();

// Register users
taskManager.registerUser("Alice");
taskManager.registerUser("Bob");

// Add tasks
taskManager.addTask("Fetch a book", "Go to the library and fetch a book.");
taskManager.addTask("Clean room", "Clean your room thoroughly.");

// Users completing tasks
const alice = taskManager.users[0];
const bob = taskManager.users[1];

alice.completeTask(taskManager.tasks[0]); // Alice completes the first task
bob.completeTask(taskManager.tasks[1]);    // Bob completes the second task

// Display all users' activities
console.log(taskManager.getAllUsersActivities());
```
