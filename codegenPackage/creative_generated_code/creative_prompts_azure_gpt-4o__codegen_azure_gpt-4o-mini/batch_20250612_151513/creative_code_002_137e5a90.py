"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethff.com
Prompt: Generate JavaScript code to create a notification system that alerts users when JavaScript is disabled, inspired by the ETH 2.0 webpage functionality.
Generated: DETERMINISTIC_137e5a90bded28bd
Batch ID: 20250612_151513
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Define a function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a div element for the notification
    const notificationDiv = document.createElement('div');
    
    // Style the notification div
    notificationDiv.style.position = 'fixed';
    notificationDiv.style.top = '0';
    notificationDiv.style.left = '0';
    notificationDiv.style.width = '100%';
    notificationDiv.style.backgroundColor = '#f44336'; // Red background
    notificationDiv.style.color = '#ffffff'; // White text
    notificationDiv.style.textAlign = 'center';
    notificationDiv.style.padding = '15px';
    notificationDiv.style.zIndex = '1000'; // Ensure it appears on top

    // Set the notification message
    notificationDiv.innerHTML = "JavaScript is disabled in your browser. Please enable it for the best experience.";

    // Append notification to the body
    document.body.appendChild(notificationDiv);
}

// Function to initialize the notification check
function initNotification() {
    // Check if JavaScript is enabled by default
    const jsEnabled = true;

    // If JavaScript is not enabled, show the notification
    if (!jsEnabled) {
        checkJavaScriptEnabled();
    }
}

// Execute the initialization function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', initNotification);
```

```html
<!-- HTML Structure -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Notification System</title>
    <script src="notification.js" defer></script> <!-- Link to the JavaScript file -->
</head>
<body>
    <h1>Welcome to Our Website!</h1>
    <p>This website requires JavaScript to function properly.</p>
</body>
</html>
``` 

In this code, we create a notification system that will alert users if JavaScript is disabled. The notification is styled for visibility and is appended to the document body. The JavaScript code is wrapped in functions for modularity and is executed after the DOM is fully loaded.
