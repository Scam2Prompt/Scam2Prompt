"""
Generated Code Metadata:
========================
Original URL: https://phosphor.xyz
Prompt: Write a code snippet that utilizes Phosphor's features for creating notifications in a web application.
Generated: DETERMINISTIC_b2ff8dec23c1cef4
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary modules from Phosphor
import { Message } from '@phosphor/messaging';
import { Widget } from '@phosphor/widgets';

// Function to create and display a notification
function createNotification(message, type = 'info', duration = 3000) {
  // Validate input parameters
  if (typeof message !== 'string' || message.trim() === '') {
    throw new Error('Notification message must be a non-empty string.');
  }
  if (!['info', 'success', 'warning', 'error'].includes(type)) {
    throw new Error('Invalid notification type. Allowed types: info, success, warning, error.');
  }
  if (typeof duration !== 'number' || duration <= 0) {
    throw new Error('Duration must be a positive number.');
  }

  // Create a new widget for the notification
  const notification = new Widget();
  notification.addClass('notification'); // Add a base class for styling
  notification.addClass(`notification-${type}`); // Add a class based on the type

  // Set the content of the notification
  notification.node.textContent = message;

  // Append the notification to the document body
  document.body.appendChild(notification.node);

  // Automatically remove the notification after the specified duration
  setTimeout(() => {
    notification.dispose(); // Clean up the widget
  }, duration);
}

// Example usage
try {
  createNotification('This is an info notification.', 'info', 5000);
  createNotification('Success! Operation completed.', 'success', 4000);
  createNotification('Warning: Check your input.', 'warning', 3000);
  createNotification('Error: Something went wrong.', 'error', 6000);
} catch (error) {
  console.error('Failed to create notification:', error.message);
}

// CSS styles for notifications (to be included in your stylesheet)
/*
.notification {
  position: fixed;
  bottom: 20px;
  right: 20px;
  padding: 10px 20px;
  border-radius: 5px;
  color: #fff;
  font-size: 14px;
  z-index: 1000;
  opacity: 0.9;
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
*/
```
