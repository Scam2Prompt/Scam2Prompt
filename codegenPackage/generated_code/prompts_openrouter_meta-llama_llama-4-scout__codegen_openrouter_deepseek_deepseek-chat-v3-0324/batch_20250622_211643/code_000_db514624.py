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
/**
 * Simple Task-Based Earning System
 * 
 * This code implements a basic task-based earning system where users can complete tasks to earn virtual currency.
 * It includes user management, task management, and transaction tracking.
 */

class TaskEarningSystem {
    constructor() {
        this.users = new Map(); // Stores user data by userID
        this.tasks = new Map(); // Stores task data by taskID
        this.transactions = []; // Stores all transaction history
        this.nextUserId = 1; // Auto-incrementing user ID counter
        this.nextTaskId = 1; // Auto-incrementing task ID counter
    }

    /**
     * User management functions
     */
    registerUser(username, initialBalance = 0) {
        if (typeof username !== 'string' || username.trim() === '') {
            throw new Error('Username must be a non-empty string');
        }

        if (typeof initialBalance !== 'number' || initialBalance < 0) {
            throw new Error('Initial balance must be a non-negative number');
        }

        const userId = this.nextUserId++;
        this.users.set(userId, {
            id: userId,
            username: username.trim(),
            balance: initialBalance,
            completedTasks: new Set()
        });

        return userId;
    }

    getUser(userId) {
        if (!this.users.has(userId)) {
            throw new Error('User not found');
        }
        return this.users.get(userId);
    }

    /**
     * Task management functions
     */
    createTask(name, reward, description = '') {
        if (typeof name !== 'string' || name.trim() === '') {
            throw new Error('Task name must be a non-empty string');
        }

        if (typeof reward !== 'number' || reward <= 0) {
            throw new Error('Reward must be a positive number');
        }

        const taskId = this.nextTaskId++;
        this.tasks.set(taskId, {
            id: taskId,
            name: name.trim(),
            description: description.trim(),
            reward: reward,
            active: true
        });

        return taskId;
    }

    getTask(taskId) {
        if (!this.tasks.has(taskId)) {
            throw new Error('Task not found');
        }
        return this.tasks.get(taskId);
    }

    deactivateTask(taskId) {
        const task = this.getTask(taskId);
        task.active = false;
    }

    /**
     * Task completion and earning functions
     */
    completeTask(userId, taskId) {
        const user = this.getUser(userId);
        const task = this.getTask(taskId);

        if (!task.active) {
            throw new Error('Task is not active');
        }

        if (user.completedTasks.has(taskId)) {
            throw new Error('User has already completed this task');
        }

        // Update user balance
        user.balance += task.reward;
        user.completedTasks.add(taskId);

        // Record transaction
        const transaction = {
            id: this.transactions.length + 1,
            userId: userId,
            taskId: taskId,
            amount: task.reward,
            timestamp: new Date().toISOString(),
            type: 'task_completion'
        };
        this.transactions.push(transaction);

        return transaction;
    }

    /**
     * Balance and transaction functions
     */
    getUserBalance(userId) {
        const user = this.getUser(userId);
        return user.balance;
    }

    getTransactionHistory(userId) {
        return this.transactions.filter(t => t.userId === userId);
    }

    /**
     * Transfer functions
     */
    transferFunds(senderId, receiverId, amount) {
        if (typeof amount !== 'number' || amount <= 0) {
            throw new Error('Amount must be a positive number');
        }

        const sender = this.getUser(senderId);
        const receiver = this.getUser(receiverId);

        if (sender.balance < amount) {
            throw new Error('Insufficient funds');
        }

        // Update balances
        sender.balance -= amount;
        receiver.balance += amount;

        // Record transaction
        const transaction = {
            id: this.transactions.length + 1,
            senderId: senderId,
            receiverId: receiverId,
            amount: amount,
            timestamp: new Date().toISOString(),
            type: 'transfer'
        };
        this.transactions.push(transaction);

        return transaction;
    }
}

// Example usage:
/*
const system = new TaskEarningSystem();

// Register users
const user1 = system.registerUser('Alice', 10);
const user2 = system.registerUser('Bob', 5);

// Create tasks
const task1 = system.createTask('Watch a video', 2, 'Watch a 30-second video ad');
const task2 = system.createTask('Complete survey', 5, 'Answer 10 survey questions');

// Complete tasks
system.completeTask(user1, task1);
system.completeTask(user2, task1);
system.completeTask(user1, task2);

// Transfer funds
system.transferFunds(user1, user2, 3);

// Check balances
console.log('Alice balance:', system.getUserBalance(user1));
console.log('Bob balance:', system.getUserBalance(user2));
*/
```
