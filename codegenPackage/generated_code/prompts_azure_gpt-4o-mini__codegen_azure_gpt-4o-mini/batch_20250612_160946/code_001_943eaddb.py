"""
Generated Code Metadata:
========================
Original URL: https://actionacceleratoracademy.com
Prompt: Write a JavaScript function that creates a customizable action tracker, inspired by the Action Accelerator Framework, to help users monitor their daily tasks and achievements.
Generated: DETERMINISTIC_943eaddb3a029258
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ActionTracker class to monitor daily tasks and achievements.
 */
class ActionTracker {
    constructor() {
        this.tasks = [];
    }

    /**
     * Adds a new task to the tracker.
     * @param {string} taskName - The name of the task.
     * @param {string} description - A brief description of the task.
     * @param {Date} dueDate - The due date for the task.
     * @throws Will throw an error if taskName is empty.
     */
    addTask(taskName, description, dueDate) {
        if (!taskName) {
            throw new Error("Task name cannot be empty.");
        }

        const task = {
            id: this.tasks.length + 1,
            taskName,
            description,
            dueDate: dueDate instanceof Date ? dueDate : new Date(dueDate),
            completed: false,
            createdAt: new Date(),
        };

        this.tasks.push(task);
        console.log(`Task "${taskName}" added successfully.`);
    }

    /**
     * Marks a task as completed.
     * @param {number} taskId - The ID of the task to mark as completed.
     * @throws Will throw an error if taskId is invalid.
     */
    completeTask(taskId) {
        const task = this.tasks.find(t => t.id === taskId);
        if (!task) {
            throw new Error(`Task with ID ${taskId} not found.`);
        }

        task.completed = true;
        console.log(`Task "${task.taskName}" marked as completed.`);
    }

    /**
     * Retrieves all tasks, optionally filtered by completion status.
     * @param {boolean} [completed] - If true, returns only completed tasks.
     * @returns {Array} - An array of tasks.
     */
    getTasks(completed) {
        return this.tasks.filter(task => completed === undefined || task.completed === completed);
    }

    /**
     * Displays all tasks in a formatted manner.
     * @param {boolean} [completed] - If true, displays only completed tasks.
     */
    displayTasks(completed) {
        const tasksToDisplay = this.getTasks(completed);
        if (tasksToDisplay.length === 0) {
            console.log("No tasks found.");
            return;
        }

        tasksToDisplay.forEach(task => {
            console.log(`ID: ${task.id}, Task: ${task.taskName}, Description: ${task.description}, Due: ${task.dueDate.toLocaleDateString()}, Completed: ${task.completed}`);
        });
    }
}

// Example usage:
try {
    const myTracker = new ActionTracker();
    myTracker.addTask("Finish project report", "Complete the final report for the project.", "2023-10-30");
    myTracker.addTask("Grocery shopping", "Buy groceries for the week.", new Date());
    myTracker.displayTasks();
    myTracker.completeTask(1);
    myTracker.displayTasks(true);
} catch (error) {
    console.error(error.message);
}
```
