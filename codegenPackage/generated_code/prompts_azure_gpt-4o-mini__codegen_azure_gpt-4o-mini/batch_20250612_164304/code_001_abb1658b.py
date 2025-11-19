"""
Generated Code Metadata:
========================
Original URL: https://harvesters-app.pages.dev
Prompt: What are the key features of the Harvest App that require JavaScript for functionality?
Generated: DETERMINISTIC_abb1658ba089b8e7
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Harvest App Key Features
 * This module outlines the key features of the Harvest App that require JavaScript for functionality.
 * Each feature is represented as a function that simulates its behavior.
 */

// Simulated data for demonstration purposes
const tasks = [
    { id: 1, name: 'Design', hours: 5 },
    { id: 2, name: 'Development', hours: 10 },
    { id: 3, name: 'Testing', hours: 3 },
];

/**
 * Function to calculate total hours worked on tasks
 * @returns {number} Total hours
 */
function calculateTotalHours() {
    try {
        return tasks.reduce((total, task) => total + task.hours, 0);
    } catch (error) {
        console.error('Error calculating total hours:', error);
        return 0;
    }
}

/**
 * Function to add a new task
 * @param {string} taskName - The name of the task
 * @param {number} hours - The number of hours for the task
 * @returns {object} The newly created task
 */
function addTask(taskName, hours) {
    if (!taskName || typeof hours !== 'number' || hours < 0) {
        throw new Error('Invalid task name or hours');
    }

    const newTask = {
        id: tasks.length + 1,
        name: taskName,
        hours: hours,
    };

    tasks.push(newTask);
    return newTask;
}

/**
 * Function to remove a task by ID
 * @param {number} taskId - The ID of the task to remove
 * @returns {boolean} True if the task was removed, false otherwise
 */
function removeTask(taskId) {
    const initialLength = tasks.length;
    tasks = tasks.filter(task => task.id !== taskId);
    return tasks.length < initialLength;
}

/**
 * Function to list all tasks
 * @returns {Array} Array of tasks
 */
function listTasks() {
    return tasks;
}

// Example usage
try {
    console.log('Total Hours:', calculateTotalHours());
    console.log('Adding Task:', addTask('Deployment', 4));
    console.log('Current Tasks:', listTasks());
    console.log('Removing Task:', removeTask(2));
    console.log('Current Tasks After Removal:', listTasks());
} catch (error) {
    console.error('An error occurred:', error);
}
```
