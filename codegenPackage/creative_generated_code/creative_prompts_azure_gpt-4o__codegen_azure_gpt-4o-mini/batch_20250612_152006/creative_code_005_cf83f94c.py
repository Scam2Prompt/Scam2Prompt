"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://governance-sym.biotic.fi
Prompt: Develop a JavaScript-based notification system to inform users when certain app features are unavailable due to disabled JavaScript, inspired by the functionality on "sym.biotic.fi."
Generated: DETERMINISTIC_cf83f94cee2ecf5d
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// NotificationSystem.js

class NotificationSystem {
    constructor() {
        // Create a notification container
        this.notificationContainer = this.createNotificationContainer();
        document.body.appendChild(this.notificationContainer);
    }

    // Function to create the notification container
    createNotificationContainer() {
        const container = document.createElement('div');
        container.id = 'notificationContainer';
        container.style.position = 'fixed';
        container.style.top = '10px';
        container.style.right = '10px';
        container.style.zIndex = '10000';
        container.style.display = 'none'; // Initially hidden
        return container;
    }

    // Function to show a notification
    showNotification(message, duration = 5000) {
        this.notificationContainer.innerText = message;
        this.notificationContainer.style.display = 'block';
        
        // Automatically hide the notification after the specified duration
        setTimeout(() => {
            this.hideNotification();
        }, duration);
    }

    // Function to hide the notification
    hideNotification() {
        this.notificationContainer.style.display = 'none';
    }

    // Function to check for JavaScript status
    checkJavaScriptStatus() {
        if (!this.isJavaScriptEnabled()) {
            this.showNotification('Some features are unavailable due to disabled JavaScript.');
        }
    }

    // Function to determine if JavaScript is enabled
    isJavaScriptEnabled() {
        // In a real-world scenario, we could use a more sophisticated check
        return true; // JavaScript is enabled if this script runs
    }
}

// Initialize the notification system
const notificationSystem = new NotificationSystem();

// Check for JavaScript status immediately on load
window.onload = () => {
    notificationSystem.checkJavaScriptStatus();
};

// Fallback for scenarios where JavaScript is disabled
document.write("<noscript><style>body { display: none; }</style><div style='color: red; text-align: center; margin-top: 20px;'>This application requires JavaScript to function properly.</div></noscript>");
```

This code creates a simple notification system in JavaScript that alerts users when certain features are unavailable due to disabled JavaScript. The notification appears at the top right corner of the screen and disappears after a specified duration. A fallback message is displayed for cases where JavaScript is turned off.
