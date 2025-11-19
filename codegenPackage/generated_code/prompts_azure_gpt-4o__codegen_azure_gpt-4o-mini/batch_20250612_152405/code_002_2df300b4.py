"""
Generated Code Metadata:
========================
Original URL: https://elonshiba.org
Prompt: Generate code using JavaScript to implement a study planner tool with features like task scheduling and reminders, based on the "Effective Study Tips for Exams" article on Elon Shiba.
Generated: DETERMINISTIC_2df300b48cae352e
Batch ID: 20250612_152405
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Study Planner Tool
// This tool allows users to schedule study tasks and set reminders based on effective study tips.

class StudyTask {
    constructor(title, description, dueDate, reminderTime) {
        this.title = title; // Title of the study task
        this.description = description; // Description of the study task
        this.dueDate = new Date(dueDate); // Due date for the task
        this.reminderTime = new Date(reminderTime); // Reminder time for the task
        this.completed = false; // Task completion status
    }

    // Mark the task as completed
    completeTask() {
        this.completed = true;
    }

    // Check if the task is overdue
    isOverdue() {
        return new Date() > this.dueDate && !this.completed;
    }
}

class StudyPlanner {
    constructor() {
        this.tasks = []; // Array to hold study tasks
    }

    // Add a new task to the planner
    addTask(title, description, dueDate, reminderTime) {
        try {
            const newTask = new StudyTask(title, description, dueDate, reminderTime);
            this.tasks.push(newTask);
            console.log(`Task "${title}" added successfully.`);
        } catch (error) {
            console.error("Error adding task:", error);
        }
    }

    // Remove a task from the planner
    removeTask(title) {
        const index = this.tasks.findIndex(task => task.title === title);
        if (index !== -1) {
            this.tasks.splice(index, 1);
            console.log(`Task "${title}" removed successfully.`);
        } else {
            console.warn(`Task "${title}" not found.`);
        }
    }

    // List all tasks
    listTasks() {
        if (this.tasks.length === 0) {
            console.log("No tasks available.");
            return;
        }
        console.log("Study Tasks:");
        this.tasks.forEach(task => {
            console.log(`- ${task.title} (Due: ${task.dueDate.toLocaleString()}) - ${task.completed ? "Completed" : "Pending"}`);
        });
    }

    // Set reminders for tasks
    setReminders() {
        this.tasks.forEach(task => {
            if (!task.completed && new Date() >= task.reminderTime) {
                console.log(`Reminder: It's time to study "${task.title}"!`);
            }
        });
    }
}

// Example usage
const planner = new StudyPlanner();
planner.addTask("Math Revision", "Revise calculus and algebra", "2023-10-15T18:00:00", "2023-10-15T17:00:00");
planner.addTask("History Essay", "Complete the essay on World War II", "2023-10-20T23:59:00", "2023-10-20T20:00:00");
planner.listTasks();
planner.setReminders();
```
