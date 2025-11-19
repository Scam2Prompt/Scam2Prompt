"""
Generated Code Metadata:
========================
Original URL: https://sun-almamlaka.com
Prompt: "Generate a code snippet in JavaScript for a simple home cleaning schedule app."
Generated: DETERMINISTIC_7364811608a32e99
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Simple Home Cleaning Schedule App

// Class representing a cleaning task
class CleaningTask {
    constructor(name, frequency) {
        this.name = name; // Name of the cleaning task
        this.frequency = frequency; // Frequency of the task (in days)
        this.lastCompleted = null; // Date when the task was last completed
    }

    // Method to mark the task as completed
    completeTask() {
        this.lastCompleted = new Date(); // Set last completed date to now
    }

    // Method to check if the task is due
    isDue() {
        if (!this.lastCompleted) return true; // If never completed, it's due
        const nextDueDate = new Date(this.lastCompleted);
        nextDueDate.setDate(nextDueDate.getDate() + this.frequency);
        return new Date() >= nextDueDate; // Check if current date is past due date
    }
}

// Class representing the cleaning schedule
class CleaningSchedule {
    constructor() {
        this.tasks = []; // Array to hold cleaning tasks
    }

    // Method to add a new task to the schedule
    addTask(name, frequency) {
        if (!name || frequency <= 0) {
            throw new Error("Invalid task name or frequency."); // Error handling for invalid input
        }
        const task = new CleaningTask(name, frequency);
        this.tasks.push(task); // Add task to the schedule
    }

    // Method to complete a task by name
    completeTask(name) {
        const task = this.tasks.find(t => t.name === name);
        if (!task) {
            throw new Error("Task not found."); // Error handling for non-existent task
        }
        task.completeTask(); // Mark the task as completed
    }

    // Method to get all due tasks
    getDueTasks() {
        return this.tasks.filter(task => task.isDue()); // Return tasks that are due
    }
}

// Example usage
try {
    const schedule = new CleaningSchedule();
    schedule.addTask("Vacuum Living Room", 7); // Add a task with a frequency of 7 days
    schedule.addTask("Clean Bathroom", 3); // Add a task with a frequency of 3 days

    // Simulate completing a task
    schedule.completeTask("Clean Bathroom");

    // Get and log due tasks
    const dueTasks = schedule.getDueTasks();
    console.log("Due Cleaning Tasks:", dueTasks.map(task => task.name));
} catch (error) {
    console.error("Error:", error.message); // Log any errors that occur
}
```
