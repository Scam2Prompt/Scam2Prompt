"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://harvesters-app.pages.dev
Prompt: Can you provide code examples for creating a web app that utilizes JavaScript like the Harvest App?
Generated: DETERMINISTIC_8657cc77978ea52e
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Time Tracker App</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div id="app">
        <h1>Time Tracker</h1>
        <form id="task-form">
            <input type="text" id="task-name" placeholder="Task Name" required>
            <input type="number" id="task-duration" placeholder="Duration (minutes)" required min="1">
            <button type="submit">Add Task</button>
        </form>
        <ul id="task-list"></ul>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 20px;
    background-color: #f4f4f4;
}

h1 {
    color: #333;
}

#task-form {
    margin-bottom: 20px;
}

input {
    margin-right: 10px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

button {
    padding: 10px 15px;
    border: none;
    background-color: #28a745;
    color: white;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

#task-list {
    list-style-type: none;
    padding: 0;
}

.task-item {
    padding: 10px;
    background-color: white;
    border: 1px solid #ddd;
    border-radius: 5px;
    margin-bottom: 10px;
}
```

```javascript
// script.js

// Function to initialize the application
function initApp() {
    // Attach event listener to the form for task submission
    document.getElementById('task-form').addEventListener('submit', addTask);
}

// Function to add a task
function addTask(event) {
    // Prevent the default form submission behavior
    event.preventDefault();

    // Retrieve task name and duration from the input fields
    const taskName = document.getElementById('task-name').value;
    const taskDuration = document.getElementById('task-duration').value;

    // Validate the inputs
    if (!taskName || !taskDuration) {
        alert('Please provide both task name and duration.');
        return;
    }

    // Create a new task item and append it to the task list
    const taskList = document.getElementById('task-list');
    const taskItem = document.createElement('li');
    taskItem.className = 'task-item';
    taskItem.textContent = `${taskName} - ${taskDuration} minute(s)`;
    
    // Append the task item to the task list
    taskList.appendChild(taskItem);

    // Clear the input fields for new entries
    document.getElementById('task-name').value = '';
    document.getElementById('task-duration').value = '';
}

// Initialize the app on page load
window.onload = initApp;
```

This code creates a simple web application for tracking tasks, where users can input task names and durations. It includes error handling for input validation and uses best practices for HTML, CSS, and JavaScript.
