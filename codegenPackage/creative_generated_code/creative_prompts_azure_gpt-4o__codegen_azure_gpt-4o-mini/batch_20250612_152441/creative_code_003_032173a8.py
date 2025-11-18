"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://testnet-ten.pages.dev
Prompt: Generate code to detect the user's internet connection status and display a "You seem to be offline" message, as described on the Ten Gateway Testnet page.
Generated: DETERMINISTIC_032173a854e89837
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check the user's internet connection status
function checkConnection() {
    // Check if the browser supports the navigator.onLine property
    if (typeof navigator.onLine === 'undefined') {
        console.error("The browser does not support online/offline detection.");
        return;
    }

    // Function to update the connection status message
    function updateConnectionStatus() {
        const statusElement = document.getElementById('connection-status');
        
        if (!navigator.onLine) {
            // If offline, display the offline message
            statusElement.textContent = "You seem to be offline.";
            statusElement.style.color = "red"; // Change text color to red for visibility
        } else {
            // If online, clear the message
            statusElement.textContent = "";
        }
    }

    // Add event listeners for online and offline events
    window.addEventListener('online', updateConnectionStatus);
    window.addEventListener('offline', updateConnectionStatus);

    // Initial check to set the proper status on page load
    updateConnectionStatus();
}

// Run the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', (event) => {
    checkConnection();
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Connection Status</title>
    <style>
        #connection-status {
            font-size: 18px;
            margin: 20px;
        }
    </style>
</head>
<body>
    <div id="connection-status"></div>
    <script src="connection-check.js"></script> <!-- Ensure to link to the JavaScript file -->
</body>
</html>
```
