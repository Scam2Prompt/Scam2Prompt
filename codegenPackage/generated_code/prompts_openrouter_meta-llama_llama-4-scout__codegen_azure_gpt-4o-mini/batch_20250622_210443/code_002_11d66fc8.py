"""
Generated Code Metadata:
========================
Original URL: https://pozymedia.com
Prompt: Generate a sample event management checklist using JavaScript, including tasks such as confirming sponsors, speakers, and presenters.
Generated: DETERMINISTIC_11d66fc84126c249
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Event Management Checklist
 * This script manages a checklist for event management tasks.
 * It includes tasks such as confirming sponsors, speakers, and presenters.
 */

class EventChecklist {
    constructor(eventName) {
        this.eventName = eventName;
        this.tasks = [];
    }

    /**
     * Adds a task to the checklist.
     * @param {string} task - The task to be added.
     */
    addTask(task) {
        if (typeof task !== 'string' || task.trim() === '') {
            throw new Error('Task must be a non-empty string.');
        }
        this.tasks.push({ task, completed: false });
    }

    /**
     * Marks a task as completed.
     * @param {number} index - The index of the task to be completed.
     */
    completeTask(index) {
        if (index < 0 || index >= this.tasks.length) {
            throw new Error('Invalid task index.');
        }
        this.tasks[index].completed = true;
    }

    /**
     * Displays the checklist.
     */
    displayChecklist() {
        console.log(`Event: ${this.eventName}`);
        this.tasks.forEach((task, index) => {
            const status = task.completed ? '✓' : '✗';
            console.log(`${index + 1}. [${status}] ${task.task}`);
        });
    }
}

// Example usage
try {
    const eventChecklist = new EventChecklist('Annual Tech Conference');

    // Adding tasks to the checklist
    eventChecklist.addTask('Confirm sponsors');
    eventChecklist.addTask('Confirm speakers');
    eventChecklist.addTask('Confirm presenters');
    eventChecklist.addTask('Book venue');
    eventChecklist.addTask('Send invitations');

    // Display the current checklist
    eventChecklist.displayChecklist();

    // Mark the first task as completed
    eventChecklist.completeTask(0);

    // Display the updated checklist
    console.log('\nUpdated Checklist:');
    eventChecklist.displayChecklist();
} catch (error) {
    console.error('Error:', error.message);
}
```
