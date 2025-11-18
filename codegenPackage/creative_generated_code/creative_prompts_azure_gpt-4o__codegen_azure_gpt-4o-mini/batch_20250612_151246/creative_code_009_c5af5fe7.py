"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://getgrass-claim.pages.dev
Prompt: Write a JavaScript function to monitor and manage the background activity of a Grass-like web extension, ensuring it doesn't interfere with the user's internet experience.
Generated: DETERMINISTIC_c5af5fe740525181
Batch ID: 20250612_151246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * BackgroundActivityManager is a class to monitor and manage background activities
 * of a Grass-like web extension, ensuring it does not interfere with the user's 
 * internet experience.
 */
class BackgroundActivityManager {
    constructor() {
        // Track active background tasks
        this.activeTasks = new Set();
        
        // Maximum allowed background tasks
        this.maxTasks = 5;

        // Monitor the performance of active tasks
        this.monitorInterval = 1000; // in milliseconds
        this.startMonitoring();
    }

    /**
     * Start monitoring background tasks at regular intervals.
     */
    startMonitoring() {
        this.monitoringTimer = setInterval(() => {
            this.checkActiveTasks();
        }, this.monitorInterval);
    }

    /**
     * Check the current number of active tasks and manage them based on user experience.
     */
    checkActiveTasks() {
        if (this.activeTasks.size > this.maxTasks) {
            console.warn(`Too many active tasks: ${this.activeTasks.size}. Reducing to max limit.`);
            this.reduceActiveTasks();
        }
    }

    /**
     * Reduces the number of active tasks to the maximum allowed limit.
     */
    reduceActiveTasks() {
        const tasksToRemove = this.activeTasks.size - this.maxTasks;
        const tasksArray = Array.from(this.activeTasks);
        
        for (let i = 0; i < tasksToRemove; i++) {
            this.stopTask(tasksArray[i]);
        }
    }

    /**
     * Add a new background task and manage its lifecycle.
     * @param {Function} task - The function representing a background task.
     * @returns {string} - A unique identifier for the task.
     */
    addTask(task) {
        if (this.activeTasks.size >= this.maxTasks) {
            console.error(`Cannot add task: Maximum number of active tasks reached (${this.maxTasks}).`);
            return null;
        }
        
        const taskId = this.generateTaskId();
        this.activeTasks.add({ id: taskId, task });
        console.log(`Task added: ${taskId}`);
        
        // Execute the task
        try {
            task(); // Assuming task is a callable function
        } catch (error) {
            console.error(`Error executing task ${taskId}:`, error);
            this.stopTask(taskId);
        }
        
        return taskId;
    }

    /**
     * Stop a background task by its identifier.
     * @param {string} taskId - The unique identifier of the task to stop.
     */
    stopTask(taskId) {
        this.activeTasks.forEach((activeTask) => {
            if (activeTask.id === taskId) {
                this.activeTasks.delete(activeTask);
                console.log(`Task stopped: ${taskId}`);
            }
        });
    }

    /**
     * Generate a unique identifier for a new task.
     * @returns {string} - A unique task identifier.
     */
    generateTaskId() {
        return `task-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`;
    }

    /**
     * Stop monitoring and clear active tasks.
     */
    stopMonitoring() {
        clearInterval(this.monitoringTimer);
        this.activeTasks.clear();
        console.log('Monitoring stopped and all tasks cleared.');
    }
}

// Example usage
const manager = new BackgroundActivityManager();
const myTask = () => {
    // Simulate background activity
    console.log('Background task is running...');
};

const taskId = manager.addTask(myTask);

// To stop monitoring after a while (for demonstration purposes)
setTimeout(() => {
    manager.stopMonitoring();
}, 10000); // Stop after 10 seconds
```
