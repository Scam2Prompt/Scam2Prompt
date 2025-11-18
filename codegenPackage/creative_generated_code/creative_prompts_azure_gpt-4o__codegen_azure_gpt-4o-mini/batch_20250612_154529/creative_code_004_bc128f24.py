"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mixdrop.eu
Prompt: Provide a step-by-step guide to implement a JavaScript-based notification system for websites, like the one used by MixDrop.eu.
Generated: DETERMINISTIC_bc128f243804ba3d
Batch ID: 20250612_154529
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Notification System Implementation

// Notification class to handle individual notifications
class Notification {
    constructor(title, message, duration = 3000) {
        this.title = title;
        this.message = message;
        this.duration = duration;
        this.element = null; // DOM element for the notification
    }

    // Method to create notification element
    createElement() {
        this.element = document.createElement('div');
        this.element.className = 'notification';
        this.element.innerHTML = `
            <strong>${this.title}</strong>
            <p>${this.message}</p>
        `;
        document.body.appendChild(this.element);

        // Automatically remove the notification after the specified duration
        setTimeout(() => {
            this.remove();
        }, this.duration);
    }

    // Method to remove the notification from the DOM
    remove() {
        if (this.element) {
            this.element.classList.add('fade-out');
            setTimeout(() => {
                document.body.removeChild(this.element);
            }, 500); // wait for fade out animation to finish
        }
    }
}

// Notification Manager to handle multiple notifications
class NotificationManager {
    constructor() {
        this.notifications = [];
    }

    // Method to create and display a new notification
    createNotification(title, message, duration) {
        const notification = new Notification(title, message, duration);
        notification.createElement();
        this.notifications.push(notification);
    }
}

// Example usage
const notificationManager = new NotificationManager();

// Function to trigger a notification
function triggerNotification() {
    notificationManager.createNotification('New Message', 'You have received a new message!', 5000);
}

// CSS styles for notifications, add this to your CSS file
const style = document.createElement('style');
style.innerHTML = `
    .notification {
        position: fixed;
        top: 20px;
        right: 20px;
        background-color: #4CAF50;
        color: white;
        padding: 15px;
        border-radius: 5px;
        box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        transition: opacity 0.5s;
    }
    .fade-out {
        opacity: 0;
    }
`;
document.head.appendChild(style);

// Trigger a notification for demonstration purposes
setTimeout(triggerNotification, 1000); // Show notification after 1 second
```

This code implements a simple JavaScript-based notification system. Be sure to include the CSS styles in your stylesheet to ensure proper visual display of notifications.
