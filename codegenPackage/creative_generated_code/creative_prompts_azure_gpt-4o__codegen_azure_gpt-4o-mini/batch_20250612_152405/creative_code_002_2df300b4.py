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
// StudyPlanner.js

class Task {
    constructor(title, description, dueDate, reminderTime) {
        this.title = title; // Title of the task
        this.description = description; // Description of the task
        this.dueDate = new Date(dueDate); // Due date of the task
        this.reminderTime = new Date(reminderTime); // Reminder time for the task
        this.completed = false; // Task completion status
    }

    markCompleted() {
        this.completed = true; // Mark the task as completed
    }
}

class StudyPlanner {
    constructor() {
        this.tasks = []; // Array to hold tasks
    }

    addTask(title, description, dueDate, reminderTime) {
        try {
            const task = new Task(title, description, dueDate, reminderTime);
            this.tasks.push(task); // Add the new task to the tasks array
            console.log(`Task "${title}" added successfully.`);
        } catch (error) {
            console.error("Error adding task:", error.message);
        }
    }

    removeTask(title) {
        try {
            const index = this.tasks.findIndex(task => task.title === title);
            if (index === -1) {
                throw new Error("Task not found");
            }
            this.tasks.splice(index, 1); // Remove the task from the tasks array
            console.log(`Task "${title}" removed successfully.`);
        } catch (error) {
            console.error("Error removing task:", error.message);
        }
    }

    listTasks() {
        if (this.tasks.length === 0) {
            console.log("No tasks available.");
            return;
        }
        console.log("Current Tasks:");
        this.tasks.forEach((task, index) => {
            console.log(`${index + 1}. ${task.title} (Due: ${task.dueDate.toLocaleString()}) - ${task.completed ? 'Completed' : 'Pending'}`);
        });
    }

    setReminders() {
        this.tasks.forEach(task => {
            if (!task.completed && task.reminderTime > new Date()) {
                const timeUntilReminder = task.reminderTime - new Date();
                setTimeout(() => {
                    console.log(`Reminder: It's time to work on "${task.title}".`); // Notify user
                }, timeUntilReminder);
            }
        });
    }
}

// Example usage
const myStudyPlanner = new StudyPlanner();
myStudyPlanner.addTask("Math Homework", "Complete chapter 5 exercises", "2023-10-15T09:00:00", "2023-10-14T09:00:00");
myStudyPlanner.addTask("Science Project", "Work on group presentation", "2023-10-20T15:00:00", "2023-10-19T15:00:00");
myStudyPlanner.listTasks();
myStudyPlanner.setReminders();

// Export StudyPlanner class for potential use in other modules
export default StudyPlanner;
```

Make sure to integrate this file into a larger application structure and invoke methods appropriately to suit your needs.
