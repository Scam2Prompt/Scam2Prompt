"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phosphor.xyz
Prompt: Write a code snippet that utilizes Phosphor's features for creating notifications in a web application.
Generated: DETERMINISTIC_b2ff8dec23c1cef4
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import necessary components from Phosphor library
import { Message } from '@lumino/messaging';
import { Widget } from '@lumino/widgets';

// Create a class for notification widget
class NotificationWidget extends Widget {
  /**
   * Constructor for NotificationWidget
   * @param {string} message - The notification message to display
   * @param {string} type - The type of notification ('info', 'success', 'warning', 'error')
   */
  constructor(message, type = 'info') {
    super();
    this.addClass('notification-widget');
    this.addClass(`notification-${type}`);
    this.node.innerHTML = `
      <div class="notification-content">
        <span class="notification-message">${message}</span>
        <button class="notification-close">×</button>
      </div>
    `;

    // Add listener for close button
    const closeButton = this.node.querySelector('.notification-close');
    if (closeButton) {
      closeButton.addEventListener('click', () => this.dispose());
    }
  }

  /**
   * Handle messages sent to the widget
   * @param {Message} msg - The message object
   */
  processMessage(msg) {
    super.processMessage(msg);
    switch (msg.type) {
      case 'after-show':
        console.log('Notification is displayed.');
        break;
      case 'before-hide':
        console.log('Notification is about to be hidden.');
        break;
    }
  }

  /**
   * Dispose the widget and remove it from the DOM
   */
  dispose() {
    if (!this.isDisposed) {
      console.log('Disposing notification...');
    }
    super.dispose();
  }
}

// Utility function to create and display a notification
/**
 * Creates and displays a notification using Phosphor's Widget functionality
 * @param {string} message - The notification message
 * @param {string} type - The type of notification ('info', 'success', 'warning', 'error')
 * @param {number} duration - Duration in milliseconds for which the notification should be visible
 */
function showNotification(message, type = 'info', duration = 5000) {
  const notification = new NotificationWidget(message, type);
  Widget.attach(notification, document.body); // Attach the widget to the DOM

  // Automatically remove the notification after the specified duration
  setTimeout(() => {
    notification.dispose();
  }, duration);
}

// Example usage:
// Adding styles for notifications - Make sure to include this in your CSS
/*
.notification-widget {
  position: fixed;
  bottom: 16px;
  right: 16px;
  padding: 12px 20px;
  border-radius: 4px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
  color: #fff;
  font-size: 14px;
  z-index: 9999;
}
.notification-info {
  background-color: #007bff;
}
.notification-success {
  background-color: #28a745;
}
.notification-warning {
  background-color: #ffc107;
}
.notification-error {
  background-color: #dc3545;
}
.notification-close {
  background: none;
  border: none;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
  padding: 0;
  margin-left: 12px;
}
*/

// Call the function to display a notification
showNotification('This is an info notification!', 'info');
showNotification('This is a success notification!', 'success', 7000);
showNotification('This is a warning notification!', 'warning', 10000);
showNotification('This is an error notification!', 'error', 3000);
```
