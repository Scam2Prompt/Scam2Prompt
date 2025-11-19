"""
Generated Code Metadata:
========================
Original URL: https://enroll-sophonxyz.pages.dev
Prompt: "Design a simple webpage using HTML, CSS, and JavaScript that displays a timestamp and user participation status, inspired by the Sophon webpage."
Generated: DETERMINISTIC_9bfcc270d32f2b97
Batch ID: 20250622_210803
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Participation Status</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>User Participation Status</h1>
        <div id="timestamp" class="timestamp"></div>
        <div id="status" class="status"></div>
        <button id="toggleStatus" class="button">Toggle Participation Status</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Container styling */
.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    background-color: #f0f0f0;
    font-family: Arial, sans-serif;
}

/* Timestamp styling */
.timestamp {
    font-size: 1.5em;
    margin-bottom: 20px;
}

/* Status message styling */
.status {
    font-size: 1.2em;
    margin-bottom: 20px;
}

/* Button styling */
.button {
    padding: 10px 20px;
    font-size: 1em;
    cursor: pointer;
    background-color: #007BFF;
    color: white;
    border: none;
    border-radius: 5px;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js

// Function to get the current timestamp
function getCurrentTimestamp() {
    const now = new Date();
    return now.toLocaleString(); // Format the date and time
}

// Function to update the timestamp on the webpage
function updateTimestamp() {
    const timestampElement = document.getElementById('timestamp');
    timestampElement.textContent = `Current Timestamp: ${getCurrentTimestamp()}`;
}

// Function to toggle user participation status
function toggleParticipationStatus() {
    const statusElement = document.getElementById('status');
    const currentStatus = statusElement.textContent.includes('Participating');

    // Update the status based on the current state
    if (currentStatus) {
        statusElement.textContent = 'User Status: Not Participating';
    } else {
        statusElement.textContent = 'User Status: Participating';
    }
}

// Event listener for the button to toggle participation status
document.getElementById('toggleStatus').addEventListener('click', toggleParticipationStatus);

// Initial setup: update the timestamp and set default status
try {
    updateTimestamp();
    document.getElementById('status').textContent = 'User Status: Not Participating';
} catch (error) {
    console.error('Error initializing the webpage:', error);
}
```
