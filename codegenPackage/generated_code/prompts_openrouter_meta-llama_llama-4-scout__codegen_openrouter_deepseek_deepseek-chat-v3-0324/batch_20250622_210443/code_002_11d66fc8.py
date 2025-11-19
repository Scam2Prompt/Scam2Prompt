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
 * A sample implementation for managing event tasks like confirming sponsors, speakers, and presenters.
 */

class EventChecklist {
  constructor(eventName) {
    this.eventName = eventName;
    this.tasks = [];
    this.completedTasks = [];
  }

  /**
   * Add a new task to the checklist
   * @param {string} taskName - Name of the task
   * @param {string} category - Category of the task (e.g., 'sponsor', 'speaker')
   * @param {Date} deadline - Deadline for the task
   * @param {string} assignedTo - Person responsible for the task
   */
  addTask(taskName, category, deadline, assignedTo) {
    if (!taskName || !category || !deadline || !assignedTo) {
      throw new Error('All task parameters must be provided');
    }

    if (!(deadline instanceof Date)) {
      throw new Error('Deadline must be a valid Date object');
    }

    const task = {
      id: Date.now().toString(),
      name: taskName,
      category,
      deadline,
      assignedTo,
      isCompleted: false,
      createdAt: new Date()
    };

    this.tasks.push(task);
    return task;
  }

  /**
   * Mark a task as completed
   * @param {string} taskId - ID of the task to complete
   */
  completeTask(taskId) {
    const taskIndex = this.tasks.findIndex(task => task.id === taskId);
    
    if (taskIndex === -1) {
      throw new Error('Task not found');
    }

    const completedTask = this.tasks[taskIndex];
    completedTask.isCompleted = true;
    completedTask.completedAt = new Date();

    this.completedTasks.push(completedTask);
    this.tasks.splice(taskIndex, 1);

    return completedTask;
  }

  /**
   * Get all tasks by category
   * @param {string} category - Category to filter by
   * @returns {Array} - Array of tasks in the specified category
   */
  getTasksByCategory(category) {
    return this.tasks.filter(task => task.category === category);
  }

  /**
   * Get all pending tasks
   * @returns {Array} - Array of incomplete tasks
   */
  getPendingTasks() {
    return this.tasks.filter(task => !task.isCompleted);
  }

  /**
   * Get all completed tasks
   * @returns {Array} - Array of completed tasks
   */
  getCompletedTasks() {
    return this.completedTasks;
  }

  /**
   * Get tasks that are past their deadline
   * @returns {Array} - Array of overdue tasks
   */
  getOverdueTasks() {
    const now = new Date();
    return this.tasks.filter(task => task.deadline < now && !task.isCompleted);
  }
}

// Sample usage
const techConference = new EventChecklist('Annual Tech Conference');

// Add sample tasks
techConference.addTask(
  'Confirm keynote speaker',
  'speaker',
  new Date('2023-12-15'),
  'Jane Smith'
);

techConference.addTask(
  'Finalize sponsorship with Acme Inc',
  'sponsor',
  new Date('2023-11-30'),
  'John Doe'
);

techConference.addTask(
  'Book venue for main event',
  'venue',
  new Date('2023-10-31'),
  'Alex Johnson'
);

// Complete a task
const firstTaskId = techConference.tasks[0].id;
techConference.completeTask(firstTaskId);

// Get tasks by category
const sponsorTasks = techConference.getTasksByCategory('sponsor');
const pendingTasks = techConference.getPendingTasks();
const completedTasks = techConference.getCompletedTasks();
const overdueTasks = techConference.getOverdueTasks();
```
