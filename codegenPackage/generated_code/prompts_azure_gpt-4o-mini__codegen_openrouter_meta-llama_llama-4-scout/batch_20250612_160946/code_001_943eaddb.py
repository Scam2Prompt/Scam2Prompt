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
  /**
   * Constructor to initialize the action tracker.
   * @param {Object} options - Configuration options for the tracker.
   * @param {String} options.name - Name of the tracker.
   * @param {Array} options.tasks - Initial list of tasks.
   */
  constructor(options) {
    if (!options || typeof options !== 'object') {
      throw new Error('Invalid options');
    }

    this.name = options.name || 'Default Tracker';
    this.tasks = options.tasks || [];
    this.achievements = {};
  }

  /**
   * Add a new task to the tracker.
   * @param {String} taskName - Name of the task.
   * @param {Boolean} completed - Initial completion status.
   */
  addTask(taskName, completed = false) {
    if (typeof taskName !== 'string' || taskName.trim() === '') {
      throw new Error('Invalid task name');
    }

    const existingTask = this.tasks.find(task => task.name === taskName);
    if (existingTask) {
      throw new Error(`Task '${taskName}' already exists`);
    }

    this.tasks.push({ name: taskName, completed });
  }

  /**
   * Remove a task from the tracker.
   * @param {String} taskName - Name of the task to remove.
   */
  removeTask(taskName) {
    if (typeof taskName !== 'string' || taskName.trim() === '') {
      throw new Error('Invalid task name');
    }

    this.tasks = this.tasks.filter(task => task.name !== taskName);
  }

  /**
   * Mark a task as completed.
   * @param {String} taskName - Name of the task to complete.
   */
  completeTask(taskName) {
    if (typeof taskName !== 'string' || taskName.trim() === '') {
      throw new Error('Invalid task name');
    }

    const task = this.tasks.find(task => task.name === taskName);
    if (!task) {
      throw new Error(`Task '${taskName}' not found`);
    }

    task.completed = true;
    this.checkAchievement(taskName);
  }

  /**
   * Check if an achievement is unlocked.
   * @param {String} taskName - Name of the task to check.
   */
  checkAchievement(taskName) {
    if (!this.achievements[taskName]) {
      this.achievements[taskName] = true;
      console.log(`Achievement unlocked: ${taskName}`);
    }
  }

  /**
   * Get the current tasks and achievements.
   * @returns {Object} Current state of the tracker.
   */
  getStatus() {
    return {
      name: this.name,
      tasks: this.tasks,
      achievements: this.achievements,
    };
  }
}

// Example usage:
function main() {
  try {
    const tracker = new ActionTracker({
      name: 'Daily Tasks',
      tasks: ['Task 1', 'Task 2', 'Task 3'],
    });

    console.log(tracker.getStatus());

    tracker.completeTask('Task 1');
    tracker.addTask('Task 4');
    tracker.removeTask('Task 2');

    console.log(tracker.getStatus());
  } catch (error) {
    console.error(error.message);
  }
}

main();
```
