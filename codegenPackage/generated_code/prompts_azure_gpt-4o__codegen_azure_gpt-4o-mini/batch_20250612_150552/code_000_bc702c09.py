"""
Generated Code Metadata:
========================
Original URL: https://collect-6tp.pages.dev
Prompt: Write code to detect if a user's device is running iOS 17.1 and display a message prompting them to update to iOS 17.2 or later for push notification compatibility, as described on friend.tech.
Generated: DETERMINISTIC_bc702c0957daf995
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check the iOS version of the user's device
function checkIOSVersion() {
    // Get the user agent string
    const userAgent = window.navigator.userAgent;

    // Regular expression to match iOS version
    const iosVersionMatch = /OS (\d+)_(\d+)_?(\d+)?/i.exec(userAgent);

    // Check if the user agent matches the iOS version format
    if (iosVersionMatch) {
        // Extract major and minor version numbers
        const majorVersion = parseInt(iosVersionMatch[1], 10);
        const minorVersion = parseInt(iosVersionMatch[2], 10);

        // Check if the version is 17.1
        if (majorVersion === 17 && minorVersion === 1) {
            // Display update message to the user
            displayUpdateMessage();
        }
    } else {
        console.warn("Unable to detect iOS version.");
    }
}

// Function to display the update message
function displayUpdateMessage() {
    // Create a message element
    const messageElement = document.createElement('div');
    messageElement.style.position = 'fixed';
    messageElement.style.bottom = '20px';
    messageElement.style.left = '50%';
    messageElement.style.transform = 'translateX(-50%)';
    messageElement.style.backgroundColor = '#ffcc00';
    messageElement.style.padding = '10px';
    messageElement.style.borderRadius = '5px';
    messageElement.style.zIndex = '1000';
    messageElement.innerText = "You are running iOS 17.1. Please update to iOS 17.2 or later for push notification compatibility.";

    // Append the message to the body
    document.body.appendChild(messageElement);

    // Automatically remove the message after 10 seconds
    setTimeout(() => {
        messageElement.remove();
    }, 10000);
}

// Execute the version check on page load
window.onload = () => {
    try {
        checkIOSVersion();
    } catch (error) {
        console.error("An error occurred while checking iOS version:", error);
    }
};
```
