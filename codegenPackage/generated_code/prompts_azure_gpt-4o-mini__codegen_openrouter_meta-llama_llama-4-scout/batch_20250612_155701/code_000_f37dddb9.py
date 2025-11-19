"""
Generated Code Metadata:
========================
Original URL: https://flowstudio.app
Prompt: How can I use Flow Studio to manage my workflow effectively with JavaScript enabled?
Generated: DETERMINISTIC_f37dddb9215e0179
Batch ID: 20250612_155701
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// workflow.js

/**
 * Represents a workflow task.
 */
class Task {
  /**
   * Creates a new task.
   * @param {string} id - Unique task identifier.
   * @param {string} name - Task name.
   * @param {string} status - Task status (e.g., "pending", "in_progress", "completed").
   */
  constructor(id, name, status = "pending") {
    this.id = id;
    this.name = name;
    this.status = status;
  }

  /**
   * Updates the task status.
   * @param {string} status - New task status.
   */
  updateStatus(status) {
    this.status = status;
  }
}

/**
 * Represents a workflow.
 */
class Workflow {
  /**
   * Creates a new workflow.
   * @param {string} id - Unique workflow identifier.
   * @param {string} name - Workflow name.
   */
  constructor(id, name) {
    this.id = id;
    this.name = name;
    this.tasks = [];
  }

  /**
   * Adds a task to the workflow.
   * @param {Task} task - Task to add.
   */
  addTask(task) {
    this.tasks.push(task);
  }

  /**
   * Removes a task from the workflow.
   * @param {string} taskId - ID of the task to remove.
   */
  removeTask(taskId) {
    this.tasks = this.tasks.filter((task) => task.id !== taskId);
  }

  /**
   * Gets a task by ID.
   * @param {string} taskId - ID of the task to retrieve.
   * @returns {Task|null} The task, or null if not found.
   */
  getTask(taskId) {
    return this.tasks.find((task) => task.id === taskId) || null;
  }
}

// Example usage:
function main() {
  try {
    // Create a workflow
    const workflow = new Workflow("wf-1", "My Workflow");

    // Create tasks
    const task1 = new Task("task-1", "Task 1");
    const task2 = new Task("task-2", "Task 2");

    // Add tasks to the workflow
    workflow.addTask(task1);
    workflow.addTask(task2);

    // Update task status
    task1.updateStatus("in_progress");

    // Log workflow tasks
    console.log(`Workflow: ${workflow.name}`);
    workflow.tasks.forEach((task) => {
      console.log(`Task ${task.id}: ${task.name} (${task.status})`);
    });

    // Remove a task
    workflow.removeTask("task-2");

    // Log updated workflow tasks
    console.log("\nUpdated Workflow Tasks:");
    workflow.tasks.forEach((task) => {
      console.log(`Task ${task.id}: ${task.name} (${task.status})`);
    });
  } catch (error) {
    console.error("Error:", error.message);
  }
}

main();
```
