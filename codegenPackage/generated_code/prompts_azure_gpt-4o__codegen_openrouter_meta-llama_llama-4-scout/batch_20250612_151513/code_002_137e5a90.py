"""
Generated Code Metadata:
========================
Original URL: https://ethff.com
Prompt: Generate JavaScript code to create a notification system that alerts users when JavaScript is disabled, inspired by the ETH 2.0 webpage functionality.
Generated: DETERMINISTIC_137e5a90bded28bd
Batch ID: 20250612_151513
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
 * Notification system to alert users when JavaScript is disabled.
 */

// Define the Notification class
class Notification {
  /**
   * Constructor for the Notification class.
   * @param {string} message - The notification message to display.
   * @param {string} type - The type of notification (e.g., error, warning, info).
   */
  constructor(message, type) {
    this.message = message;
    this.type = type;
  }

  /**
   * Render the notification HTML.
   * @returns {string} The notification HTML.
   */
  render() {
    return `
      <div class="notification ${this.type}">
        <span>${this.message}</span>
      </div>
    `;
  }
}

// Define the NoScriptDetector class
class NoScriptDetector {
  /**
   * Constructor for the NoScriptDetector class.
   * @param {HTMLElement} container - The container element to render the notification.
   */
  constructor(container) {
    this.container = container;
  }

  /**
   * Check if JavaScript is enabled.
   * @returns {boolean} True if JavaScript is enabled, false otherwise.
   */
  isJavaScriptEnabled() {
    return (
      typeof window !== "undefined" &&
      window.document &&
      window.document.createElement
    );
  }

  /**
   * Render the no-script notification.
   */
  renderNoScriptNotification() {
    if (!this.isJavaScriptEnabled()) {
      const notification = new Notification(
        "Please enable JavaScript to use this website.",
        "error"
      );
      this.container.innerHTML = notification.render();
    }
  }
}

// Initialize the no-script detector
document.addEventListener("DOMContentLoaded", () => {
  const container = document.getElementById("no-script-notification");
  if (container) {
    const noScriptDetector = new NoScriptDetector(container);
    noScriptDetector.renderNoScriptNotification();
  }
});

// Fallback for older browsers
try {
  // Check if the browser supports modern JavaScript features
  if (!("serviceWorker" in navigator)) {
    throw new Error("Unsupported browser");
  }
} catch (error) {
  const notification = new Notification(
    "Your browser is not supported. Please update your browser.",
    "error"
  );
  document.body.innerHTML = notification.render();
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
  <style>
    .notification {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      padding: 1rem;
      text-align: center;
      font-weight: bold;
    }
    .notification.error {
      background-color: #ffcccc;
      border: 1px solid #ff0000;
    }
  </style>
</head>
<body>
  <div id="no-script-notification"></div>
  <script src="notification.js"></script>
</body>
</html>
```
