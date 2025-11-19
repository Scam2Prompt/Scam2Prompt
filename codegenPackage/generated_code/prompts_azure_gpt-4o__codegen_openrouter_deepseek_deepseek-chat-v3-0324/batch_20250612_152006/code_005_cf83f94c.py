"""
Generated Code Metadata:
========================
Original URL: https://governance-sym.biotic.fi
Prompt: Develop a JavaScript-based notification system to inform users when certain app features are unavailable due to disabled JavaScript, inspired by the functionality on "sym.biotic.fi."
Generated: DETERMINISTIC_cf83f94cee2ecf5d
Batch ID: 20250612_152006
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Notification System for JavaScript-Dependent Features
 * 
 * This script checks if JavaScript is enabled and displays notifications
 * for features that require JavaScript to function properly.
 */

class NotificationSystem {
  constructor(options = {}) {
    // Default configuration
    this.config = {
      notificationContainerId: 'js-notification-container',
      notificationClass: 'js-notification',
      closeButtonClass: 'js-notification-close',
      featureSelectors: [], // Array of CSS selectors for JS-dependent features
      ...options
    };

    // Initialize the notification system
    this.init();
  }

  /**
   * Initialize the notification system
   */
  init() {
    // Create notification container if it doesn't exist
    if (!document.getElementById(this.config.notificationContainerId)) {
      const container = document.createElement('div');
      container.id = this.config.notificationContainerId;
      container.style.position = 'fixed';
      container.style.bottom = '20px';
      container.style.right = '20px';
      container.style.zIndex = '1000';
      document.body.appendChild(container);
    }

    // Check for JS-dependent features
    this.checkFeatures();
  }

  /**
   * Check for JavaScript-dependent features and show notifications
   */
  checkFeatures() {
    if (this.config.featureSelectors.length === 0) return;

    this.config.featureSelectors.forEach(selector => {
      const elements = document.querySelectorAll(selector);
      if (elements.length > 0) {
        this.showNotification(
          `Some features of ${selector} may not work properly without JavaScript enabled.`
        );
      }
    });
  }

  /**
   * Show a notification message
   * @param {string} message - The notification message to display
   */
  showNotification(message) {
    const container = document.getElementById(this.config.notificationContainerId);
    if (!container) return;

    const notification = document.createElement('div');
    notification.className = this.config.notificationClass;
    notification.style.padding = '15px';
    notification.style.marginBottom = '10px';
    notification.style.backgroundColor = '#f8d7da';
    notification.style.color = '#721c24';
    notification.style.borderRadius = '4px';
    notification.style.boxShadow = '0 2px 10px rgba(0,0,0,0.1)';
    notification.style.maxWidth = '300px';
    notification.style.position = 'relative';

    const closeButton = document.createElement('button');
    closeButton.className = this.config.closeButtonClass;
    closeButton.innerHTML = '&times;';
    closeButton.style.position = 'absolute';
    closeButton.style.top = '5px';
    closeButton.style.right = '5px';
    closeButton.style.background = 'none';
    closeButton.style.border = 'none';
    closeButton.style.cursor = 'pointer';
    closeButton.style.fontSize = '16px';
    closeButton.addEventListener('click', () => {
      notification.style.display = 'none';
    });

    const messageElement = document.createElement('p');
    messageElement.textContent = message;
    messageElement.style.margin = '0';
    messageElement.style.paddingRight = '15px';

    notification.appendChild(messageElement);
    notification.appendChild(closeButton);
    container.appendChild(notification);
  }

  /**
   * Add a new feature selector to check
   * @param {string} selector - CSS selector for the JS-dependent feature
   */
  addFeatureSelector(selector) {
    if (!this.config.featureSelectors.includes(selector)) {
      this.config.featureSelectors.push(selector);
      this.checkFeatures();
    }
  }
}

// Example usage:
// document.addEventListener('DOMContentLoaded', () => {
//   const notificationSystem = new NotificationSystem({
//     featureSelectors: [
//       '.js-dependent-feature',
//       '[data-requires-js]'
//     ]
//   });
// });
```
