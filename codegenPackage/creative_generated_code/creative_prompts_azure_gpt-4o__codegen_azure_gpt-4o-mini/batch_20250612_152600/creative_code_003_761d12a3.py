"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethlast.com
Prompt: Write code to implement a JavaScript-based notification system that informs users of the ETH Pledge website if their browser settings are incompatible.
Generated: DETERMINISTIC_761d12a3fffc13b9
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Notification System for ETH Pledge website
// This script checks browser settings and informs users if they are incompatible

// Function to detect compatibility
function checkBrowserCompatibility() {
    // Check if localStorage is available
    const localStorageSupported = typeof Storage !== "undefined";
    
    // Check for cookie support
    const cookiesEnabled = navigator.cookieEnabled;

    // Check for JavaScript enabled
    const jsEnabled = (function() { return true; })();

    // Prepare an array to hold incompatible features
    const incompatibilities = [];

    // Check each compatibility feature
    if (!localStorageSupported) {
        incompatibilities.push("Local Storage is not supported.");
    }
    if (!cookiesEnabled) {
        incompatibilities.push("Cookies are disabled.");
    }
    if (!jsEnabled) {
        incompatibilities.push("JavaScript is disabled.");
    }

    return incompatibilities;
}

// Function to create and display notification
function displayNotification(message) {
    // Create a notification div element
    const notification = document.createElement("div");
    notification.className = "notification";
    notification.style.position = "fixed";
    notification.style.top = "10px";
    notification.style.right = "10px";
    notification.style.backgroundColor = "#f44336"; // Red background
    notification.style.color = "#fff"; // White text
    notification.style.padding = "15px";
    notification.style.borderRadius = "5px";
    notification.style.zIndex = "1000";
    notification.innerHTML = message;

    // Append notification to the body
    document.body.appendChild(notification);

    // Automatically remove notification after 5 seconds
    setTimeout(() => {
        notification.remove();
    }, 5000);
}

// Function to initialize the notification system
function initNotificationSystem() {
    // Check for browser compatibility
    const incompatibilities = checkBrowserCompatibility();

    // If there are incompatibilities, display the notification
    if (incompatibilities.length > 0) {
        const message = "Incompatible Browser Settings: " + incompatibilities.join(" ");
        displayNotification(message);
    }
}

// Initialize the notification system once the DOM is fully loaded
document.addEventListener("DOMContentLoaded", initNotificationSystem);
```

```css
/* CSS for notification styling */
.notification {
    font-family: Arial, sans-serif;
    font-size: 14px;
    line-height: 1.5;
}
```

Make sure to include the CSS within a `<style>` tag in your HTML or in a separate CSS file for proper styling of the notification.
