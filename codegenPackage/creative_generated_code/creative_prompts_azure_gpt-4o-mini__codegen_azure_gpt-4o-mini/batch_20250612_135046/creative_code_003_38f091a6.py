"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.xyz
Prompt: Generate an example of using Phosphor to manage user notifications effectively in a JavaScript application.
Generated: DETERMINISTIC_38f091a6897e75c9
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Importing the necessary Phosphor packages for notifications
import { Widget } from '@phosphor/widgets';
import { MessageBox } from '@phosphor/widgets';
import { signal } from '@phosphor/signaling';

// Class definition for NotificationManager
class NotificationManager {
    constructor() {
        // Create a container widget to hold notifications
        this.container = new Widget();
        this.container.addClass('notification-container');
        document.body.appendChild(this.container.node);
    }

    // Method to show a notification
    showNotification(message, title = 'Notification', timeout = 5000) {
        try {
            // Create a notification widget
            const notification = new MessageBox({
                title: title,
                body: message,
                buttons: ['OK']
            });

            // Attach the notification to the container
            this.container.add(notification);

            // Automatically close the notification after a timeout
            setTimeout(() => {
                this.container.remove(notification);
                notification.dispose();
            }, timeout);
        } catch (error) {
            console.error('Error showing notification:', error);
        }
    }

    // Method to clear all notifications
    clearNotifications() {
        try {
            // Dispose of all child widgets (notifications) in the container
            this.container.children.forEach(child => {
                this.container.remove(child);
                child.dispose();
            });
        } catch (error) {
            console.error('Error clearing notifications:', error);
        }
    }
}

// Example usage of NotificationManager
const notificationManager = new NotificationManager();

// Show a notification
notificationManager.showNotification('This is a test notification!', 'Test Notification');

// Clear notifications after a certain action (for demonstration)
setTimeout(() => {
    notificationManager.clearNotifications();
}, 10000);
```

### CSS for Notification Styling (Optional)
```css
.notification-container {
    position: fixed;
    top: 10px;
    right: 10px;
    z-index: 9999;
}

.notification-container .message-box {
    margin-bottom: 10px;
    padding: 10px;
    background-color: #f0f0f0;
    border: 1px solid #ccc;
    border-radius: 5px;
}
```
