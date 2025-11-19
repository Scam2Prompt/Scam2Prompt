"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomchromeextension.flazio.com
Prompt: How can I use the Phantom Chrome Extension to enhance my productivity while browsing?
Generated: DETERMINISTIC_795d0ad5aa8c0af5
Batch ID: 20250612_160319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Phantom Chrome Extension Script
// This script enhances productivity by providing a simple UI for managing tasks and notes while browsing.

const TASKS_KEY = 'tasks'; // Key for storing tasks in local storage

// Function to initialize the extension
function init() {
    // Load existing tasks from local storage
    const tasks = loadTasks();
    renderTasks(tasks);
}

// Function to load tasks from local storage
function loadTasks() {
    try {
        const tasks = JSON.parse(localStorage.getItem(TASKS_KEY)) || [];
        return tasks;
    } catch (error) {
        console.error("Error loading tasks:", error);
        return [];
    }
}

// Function to save tasks to local storage
function saveTasks(tasks) {
    try {
        localStorage.setItem(TASKS_KEY, JSON.stringify(tasks));
    } catch (error) {
        console.error("Error saving tasks:", error);
    }
}

// Function to render tasks in the UI
function renderTasks(tasks) {
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Clear existing tasks

    tasks.forEach((task, index) => {
        const taskItem = document.createElement('li');
        taskItem.textContent = task;
        taskItem.dataset.index = index; // Store index for later use
        
        // Add a remove button
        const removeBtn = document.createElement('button');
        removeBtn.textContent = 'Remove';
        removeBtn.onclick = () => removeTask(index);
        taskItem.appendChild(removeBtn);
        
        taskList.appendChild(taskItem);
    });
}

// Function to add a new task
function addTask() {
    const taskInput = document.getElementById('task-input');
    const task = taskInput.value.trim();
    
    if (task) {
        const tasks = loadTasks();
        tasks.push(task);
        saveTasks(tasks);
        renderTasks(tasks);
        taskInput.value = ''; // Clear input after adding
    } else {
        alert('Please enter a task.');
    }
}

// Function to remove a task
function removeTask(index) {
    const tasks = loadTasks();
    tasks.splice(index, 1); // Remove task at specified index
    saveTasks(tasks);
    renderTasks(tasks);
}

// Event listeners for DOMContentLoaded
document.addEventListener('DOMContentLoaded', () => {
    init();
    document.getElementById('add-task-btn').onclick = addTask; // Button to add a task
});

// HTML structure for the extension
const extensionHTML = `
    <div>
        <h1>Productivity Task Manager</h1>
        <input id="task-input" type="text" placeholder="Enter your task here" />
        <button id="add-task-btn">Add Task</button>
        <ul id="task-list"></ul>
    </div>
`;

// Inject HTML into the extension's popup
document.body.innerHTML = extensionHTML;
```

Make sure to include the required permissions and manifest file to enable this extension to run correctly in Chrome. This code provides a basic task management feature to enhance your productivity while browsing.
