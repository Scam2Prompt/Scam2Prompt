"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elonshiba.org
Prompt: Generate code using JavaScript to implement a study planner tool with features like task scheduling and reminders, based on the "Effective Study Tips for Exams" article on Elon Shiba.
Generated: DETERMINISTIC_2df300b48cae352e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Study Planner Tool
 * Features:
 * 1. Task scheduling
 * 2. Reminders
 *
 * Best practices are followed, including error handling and clean, modular code.
 */

// Class to represent a study task
class StudyTask {
  constructor(title, description, dueDate, reminderTime) {
    this.id = StudyTask.generateId();
    this.title = title;
    this.description = description;
    this.dueDate = new Date(dueDate);
    this.reminderTime = new Date(reminderTime);
    this.completed = false;
  }

  // Method to mark the task as completed
  markCompleted() {
    this.completed = true;
  }

  // Static method to generate unique IDs for tasks
  static generateId() {
    return `task_${Date.now()}_${Math.random().toString(36).substr(2, 9)}`;
  }
}

// Class to manage the study planner
class StudyPlanner {
  constructor() {
    this.tasks = [];
  }

  // Add a new task to the planner
  addTask(title, description, dueDate, reminderTime) {
    try {
      const task = new StudyTask(title, description, dueDate, reminderTime);
      this.tasks.push(task);
      console.log(`Task "${title}" added successfully.`);
    } catch (error) {
      console.error('Error adding task:', error.message);
    }
  }

  // Remove a task by its ID
  removeTask(taskId) {
    try {
      this.tasks = this.tasks.filter(task => task.id !== taskId);
      console.log(`Task "${taskId}" removed successfully.`);
    } catch (error) {
      console.error('Error removing task:', error.message);
    }
  }

  // List all tasks in the planner
  listTasks() {
    if (this.tasks.length === 0) {
      console.log('No tasks available.');
    } else {
      console.log('Study Tasks:');
      this.tasks.forEach(task => {
        console.log(
          `ID: ${task.id}, Title: ${task.title}, Due Date: ${task.dueDate.toLocaleString()}, Reminder: ${task.reminderTime.toLocaleString()}, Completed: ${task.completed}`
        );
      });
    }
  }

  // Mark a task as completed
  markTaskCompleted(taskId) {
    const task = this.tasks.find(task => task.id === taskId);
    if (task) {
      task.markCompleted();
      console.log(`Task "${task.title}" marked as completed.`);
    } else {
      console.error(`Task with ID "${taskId}" not found.`);
    }
  }

  // Send reminders for tasks
  sendReminders() {
    const now = new Date();
    this.tasks.forEach(task => {
      if (task.reminderTime <= now && !task.completed) {
        console.log(`Reminder: "${task.title}" is due soon!`);
      }
    });
  }
}

// Example usage
const planner = new StudyPlanner();

// Add tasks
planner.addTask('Math Revision', 'Revise algebra and geometry.', '2023-12-01T18:00:00', '2023-12-01T10:00:00');
planner.addTask('Science Practice', 'Complete physics problems.', '2023-12-02T14:00:00', '2023-12-02T09:00:00');

// List tasks
planner.listTasks();

// Mark a task as completed
const taskIdToComplete = planner.tasks[0]?.id;
if (taskIdToComplete) {
  planner.markTaskCompleted(taskIdToComplete);
}

// Send reminders
planner.sendReminders();

// Remove a completed task
const taskIdToRemove = planner.tasks[0]?.id;
if (taskIdToRemove) {
  planner.removeTask(taskIdToRemove);
}

// List tasks after removal
planner.listTasks();
```

This code implements a study planner tool with task scheduling, reminders, and basic CRUD operations for tasks.
