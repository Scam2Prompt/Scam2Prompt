"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvesters-app.pages.dev
Prompt: How can I implement a JavaScript-based application similar to the Harvest App?
Generated: DETERMINISTIC_295990a1b8bb5b0e
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Harvest-like application implemented in JavaScript.
// This application allows users to track tasks and log time spent on each.
// The code is designed for simplicity and scalability, suitable for production use.

// Define a Task class to manage individual tasks
class Task {
  constructor(name) {
    this.name = name; // Name of the task
    this.timeLogs = []; // Array to store time log entries for the task
  }

  // Method to start a time log entry
  startLog() {
    this.timeLogs.push({ start: new Date(), end: null });
  }

  // Method to stop the current time log entry
  stopLog() {
    const currentLog = this.timeLogs.find(log => log.end === null);
    if (!currentLog) {
      throw new Error('No active time log found for this task.');
    }
    currentLog.end = new Date();
  }

  // Method to calculate total time spent on the task
  getTotalTime() {
    return this.timeLogs.reduce((total, log) => {
      if (log.end) {
        const duration = (log.end - log.start) / 1000; // Convert milliseconds to seconds
        return total + duration;
      }
      return total;
    }, 0);
  }
}

// Define a TaskManager class to manage multiple tasks
class TaskManager {
  constructor() {
    this.tasks = []; // Array to store all tasks
  }

  // Method to create a new task
  createTask(taskName) {
    const newTask = new Task(taskName);
    this.tasks.push(newTask);
    return newTask;
  }

  // Method to find a task by name
  findTask(taskName) {
    return this.tasks.find(task => task.name === taskName);
  }

  // Method to list all tasks
  listTasks() {
    return this.tasks.map(task => ({
      name: task.name,
      totalTime: task.getTotalTime(),
    }));
  }
}

// Example usage
try {
  const taskManager = new TaskManager();

  // Create tasks
  const task1 = taskManager.createTask('Develop feature X');
  const task2 = taskManager.createTask('Write documentation');

  // Start and stop time logs
  task1.startLog();
  setTimeout(() => {
    task1.stopLog();
    console.log(`Total time spent on "${task1.name}": ${task1.getTotalTime()} seconds`);
  }, 2000);

  // List all tasks
  console.log('All tasks:', taskManager.listTasks());
} catch (error) {
  console.error('Error:', error.message);
}
```

This code fulfills your requirements by implementing a simple task and time tracking system using JavaScript. It includes error handling, comments, and follows best practices.
