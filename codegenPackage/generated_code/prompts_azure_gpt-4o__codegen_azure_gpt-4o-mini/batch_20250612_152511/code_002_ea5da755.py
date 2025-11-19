"""
Generated Code Metadata:
========================
Original URL: https://ten-testnet.pages.dev
Prompt: Generate a script to detect the user's internet connection status and notify them if they are offline, similar to the functionality on the Ten Gateway Testnet page.
Generated: DETERMINISTIC_ea5da755b1cdd199
Batch ID: 20250612_152511
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// internetConnectionStatus.js

// Function to check internet connection status
function checkInternetConnection() {
    // Check if the browser is online
    return navigator.onLine;
}

// Function to notify the user about their internet connection status
function notifyUser(status) {
    const notificationElement = document.getElementById('connection-status');

    if (status) {
        notificationElement.textContent = 'You are online.';
        notificationElement.style.color = 'green';
    } else {
        notificationElement.textContent = 'You are offline. Please check your connection.';
        notificationElement.style.color = 'red';
    }
}

// Event listener for online and offline events
window.addEventListener('online', () => {
    notifyUser(true);
});

window.addEventListener('offline', () => {
    notifyUser(false);
});

// Initial check on page load
document.addEventListener('DOMContentLoaded', () => {
    try {
        const isOnline = checkInternetConnection();
        notifyUser(isOnline);
    } catch (error) {
        console.error('Error checking internet connection:', error);
    }
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internet Connection Status</title>
    <style>
        #connection-status {
            font-size: 20px;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="connection-status"></div>
    <script src="internetConnectionStatus.js"></script>
</body>
</html>
```
