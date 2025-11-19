"""
Generated Code Metadata:
========================
Original URL: https://bitsoft360.de
Prompt: Write code to implement a JavaScript-based notification system for users when JavaScript is disabled on their browser.
Generated: DETERMINISTIC_36f3ec56502306aa
Batch ID: 20250612_151934
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// notification.js

/**
 * Notification system for users when JavaScript is disabled on their browser.
 */

// Define a class for the notification system
class NotificationSystem {
  /**
   * Constructor for the notification system.
   * @param {string} message - The message to display to the user.
   * @param {string} containerId - The ID of the container element.
   */
  constructor(message, containerId) {
    this.message = message;
    this.containerId = containerId;
  }

  /**
   * Check if JavaScript is enabled by checking for a specific cookie.
   * If the cookie is not present, display the notification.
   */
  checkJavaScriptEnabled() {
    // Check for a specific cookie that is set when JavaScript is enabled
    const jsEnabledCookie = this.getCookie('javascriptEnabled');

    // If the cookie is not present, display the notification
    if (!jsEnabledCookie) {
      this.displayNotification();
    }
  }

  /**
   * Display the notification to the user.
   */
  displayNotification() {
    // Create a notification element
    const notificationElement = document.createElement('div');
    notificationElement.textContent = this.message;
    notificationElement.classList.add('notification');

    // Get the container element
    const containerElement = document.getElementById(this.containerId);

    // Check if the container element exists
    if (containerElement) {
      // Append the notification element to the container
      containerElement.appendChild(notificationElement);
    } else {
      // Log an error if the container element is not found
      console.error(`Container element with ID ${this.containerId} not found.`);
    }
  }

  /**
   * Get a cookie by name.
   * @param {string} name - The name of the cookie.
   * @returns {string|null} The value of the cookie or null if not found.
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) {
        return value;
      }
    }
    return null;
  }

  /**
   * Set a cookie with a specific value.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   */
  setCookie(name, value) {
    document.cookie = `${name}=${value}; expires=Fri, 31 Dec 9999 23:59:59 GMT`;
  }
}

// Usage example
document.addEventListener('DOMContentLoaded', () => {
  // Create a new notification system instance
  const notificationSystem = new NotificationSystem(
    'Please enable JavaScript to use this website.',
    'notification-container'
  );

  // Check if JavaScript is enabled and display a notification if not
  notificationSystem.checkJavaScriptEnabled();

  // Set a cookie to indicate that JavaScript is enabled
  notificationSystem.setCookie('javascriptEnabled', 'true');
});
```

```css
/* styles.css */

.notification {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: #ff9800;
  color: #fff;
  padding: 1em;
  text-align: center;
  z-index: 1000;
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Notification System</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="notification-container"></div>
  <script src="notification.js"></script>
</body>
</html>
```
