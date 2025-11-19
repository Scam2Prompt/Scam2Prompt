"""
Generated Code Metadata:
========================
Original URL: https://phosphor.xyz
Prompt: Generate an example of using Phosphor to manage user notifications effectively in a JavaScript application.
Generated: DETERMINISTIC_38f091a6897e75c9
Batch ID: 20250612_135046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Import necessary Phosphor icons for notification UI
import { Bell, X, CheckCircle, WarningCircle } from '@phosphor-icons/react';

// Notification types
const NOTIFICATION_TYPES = {
  SUCCESS: 'success',
  ERROR: 'error',
  INFO: 'info',
  WARNING: 'warning'
};

// Notification component
class Notification {
  constructor(message, type = NOTIFICATION_TYPES.INFO, duration = 5000) {
    this.id = Date.now().toString();
    this.message = message;
    this.type = type;
    this.duration = duration;
    this.isDismissed = false;
  }

  dismiss() {
    this.isDismissed = true;
  }
}

// Notification manager
class NotificationManager {
  constructor() {
    this.notifications = [];
    this.container = null;
    this.setupContainer();
  }

  setupContainer() {
    this.container = document.createElement('div');
    this.container.className = 'notification-container';
    document.body.appendChild(this.container);
  }

  addNotification(message, type, duration) {
    const notification = new Notification(message, type, duration);
    this.notifications.push(notification);
    this.renderNotification(notification);
    this.autoDismiss(notification);
    return notification;
  }

  renderNotification(notification) {
    const notificationElement = document.createElement('div');
    notificationElement.className = `notification ${notification.type}`;
    notificationElement.id = `notification-${notification.id}`;

    // Determine icon based on notification type
    let icon;
    switch (notification.type) {
      case NOTIFICATION_TYPES.SUCCESS:
        icon = <CheckCircle size={24} weight="fill" />;
        break;
      case NOTIFICATION_TYPES.ERROR:
        icon = <WarningCircle size={24} weight="fill" />;
        break;
      case NOTIFICATION_TYPES.WARNING:
        icon = <WarningCircle size={24} weight="fill" />;
        break;
      default:
        icon = <Bell size={24} weight="fill" />;
    }

    // Create close button
    const closeButton = document.createElement('button');
    closeButton.className = 'notification-close';
    closeButton.innerHTML = <X size={16} />;
    closeButton.addEventListener('click', () => this.removeNotification(notification.id));

    // Build notification content
    notificationElement.innerHTML = `
      <div class="notification-icon">${icon}</div>
      <div class="notification-content">${notification.message}</div>
    `;
    notificationElement.appendChild(closeButton);

    this.container.appendChild(notificationElement);
  }

  removeNotification(id) {
    const notification = this.notifications.find(n => n.id === id);
    if (notification) {
      notification.dismiss();
      const element = document.getElementById(`notification-${id}`);
      if (element) {
        element.classList.add('fade-out');
        setTimeout(() => {
          element.remove();
          this.notifications = this.notifications.filter(n => n.id !== id);
        }, 300);
      }
    }
  }

  autoDismiss(notification) {
    if (notification.duration > 0) {
      setTimeout(() => {
        if (!notification.isDismissed) {
          this.removeNotification(notification.id);
        }
      }, notification.duration);
    }
  }

  clearAll() {
    this.notifications.forEach(notification => {
      this.removeNotification(notification.id);
    });
  }
}

// Styles for notifications
const style = document.createElement('style');
style.textContent = `
  .notification-container {
    position: fixed;
    top: 20px;
    right: 20px;
    z-index: 1000;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .notification {
    position: relative;
    padding: 15px 20px;
    border-radius: 8px;
    color: white;
    display: flex;
    align-items: center;
    gap: 12px;
    max-width: 350px;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    transform: translateX(0);
    transition: all 0.3s ease;
  }

  .notification.success {
    background-color: #4CAF50;
  }

  .notification.error {
    background-color: #F44336;
  }

  .notification.warning {
    background-color: #FF9800;
  }

  .notification.info {
    background-color: #2196F3;
  }

  .notification-icon {
    display: flex;
    align-items: center;
  }

  .notification-content {
    flex: 1;
  }

  .notification-close {
    background: none;
    border: none;
    color: white;
    cursor: pointer;
    padding: 0;
    margin-left: 10px;
    display: flex;
    align-items: center;
  }

  .fade-out {
    opacity: 0;
    transform: translateX(100%);
  }
`;
document.head.appendChild(style);

// Export notification manager instance
const notificationManager = new NotificationManager();

// Example usage:
// notificationManager.addNotification('Operation successful!', NOTIFICATION_TYPES.SUCCESS);
// notificationManager.addNotification('Something went wrong', NOTIFICATION_TYPES.ERROR);
// notificationManager.addNotification('Please check your input', NOTIFICATION_TYPES.WARNING);
// notificationManager.addNotification('New message received', NOTIFICATION_TYPES.INFO);
```
