"""
Generated Code Metadata:
========================
Original URL: https://dcqey.com
Prompt: Given that dcqey.com seems to require JavaScript, can you write a basic example of how JavaScript can be used to create an interactive element on a webpage?
Generated: DETERMINISTIC_c71590944c3de86b
Batch ID: 20250622_211317
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates an interactive toggle button that changes color and text when clicked.
 * This demonstrates basic DOM manipulation and event handling in JavaScript.
 */

// Wait for the DOM to be fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function() {
    // Get references to DOM elements
    const toggleButton = document.getElementById('toggleButton');
    const statusText = document.getElementById('statusText');

    // Check if elements exist to prevent errors
    if (!toggleButton || !statusText) {
        console.error('Required elements not found in the DOM');
        return;
    }

    // Initial state
    let isActive = false;

    /**
     * Updates the button's appearance and status text based on current state
     */
    function updateUI() {
        if (isActive) {
            toggleButton.textContent = 'Deactivate';
            toggleButton.style.backgroundColor = '#dc3545'; // Red color
            statusText.textContent = 'Status: Active';
            statusText.style.color = '#28a745'; // Green color
        } else {
            toggleButton.textContent = 'Activate';
            toggleButton.style.backgroundColor = '#28a745'; // Green color
            statusText.textContent = 'Status: Inactive';
            statusText.style.color = '#dc3545'; // Red color
        }
    }

    /**
     * Handles the button click event
     */
    function handleClick() {
        // Toggle the state
        isActive = !isActive;
        
        // Update the UI
        updateUI();
        
        // Optional: Log the action
        console.log(`Button clicked. New state: ${isActive ? 'Active' : 'Inactive'}`);
    }

    // Add event listener to the button
    toggleButton.addEventListener('click', handleClick);

    // Initialize the UI
    updateUI();
});
```

HTML to accompany this JavaScript:
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Button Example</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        #statusText {
            margin-top: 20px;
            font-size: 18px;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <button id="toggleButton">Activate</button>
    <div id="statusText">Status: Inactive</div>

    <script src="script.js"></script>
</body>
</html>
```
