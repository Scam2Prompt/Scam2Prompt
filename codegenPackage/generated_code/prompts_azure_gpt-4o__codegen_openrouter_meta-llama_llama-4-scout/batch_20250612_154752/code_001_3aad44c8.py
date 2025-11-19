"""
Generated Code Metadata:
========================
Original URL: https://rarecrew-app.com
Prompt: Create a script that ensures a web application's core functionality, such as a shopping feature, works only when JavaScript is enabled, similar to the requirements on the Rarecrew app's "Shop" page.
Generated: DETERMINISTIC_3aad44c8ed504ce5
Batch ID: 20250612_154752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript.js
// This script checks if JavaScript is enabled in the browser.
// If JavaScript is disabled, it displays a notification to the user.

class NoscriptDetector {
  /**
   * Initialize the NoscriptDetector.
   * @param {string} notificationMessage - The message to display when JavaScript is disabled.
   * @param {string} notificationElementId - The ID of the HTML element to display the notification in.
   */
  constructor(notificationMessage, notificationElementId) {
    this.notificationMessage = notificationMessage;
    this.notificationElementId = notificationElementId;
  }

  /**
   * Check if JavaScript is enabled by trying to access the document object.
   * @returns {boolean} True if JavaScript is enabled, false otherwise.
   */
  isJavascriptEnabled() {
    try {
      return typeof document !== 'undefined' && document instanceof Object;
    } catch (error) {
      return false;
    }
  }

  /**
   * Display a notification to the user if JavaScript is disabled.
   */
  displayNotification() {
    if (!this.isJavascriptEnabled()) {
      const notificationElement = document.getElementById(this.notificationElementId);
      if (notificationElement) {
        notificationElement.innerText = this.notificationMessage;
        notificationElement.style.display = 'block';
      } else {
        console.error(`Element with ID ${this.notificationElementId} not found.`);
      }
    }
  }

  /**
   * Initialize the script and check for JavaScript support.
   */
  init() {
    document.addEventListener('DOMContentLoaded', () => {
      this.displayNotification();
    });
  }
}

// Usage
const noscriptDetector = new NoscriptDetector(
  'Please enable JavaScript to use the shopping feature.',
  'noscript-notification'
);

// Initialize the script
noscriptDetector.init();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Noscript Detector</title>
  <style>
    #noscript-notification {
      display: none;
      background-color: #ff0;
      color: #666;
      padding: 1em;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>Shopping Feature</h1>
  <div id="noscript-notification"></div>
  <script src="noscript.js"></script>
</body>
</html>
```

```javascript
// noscript.js ( alternate approach using HTML )
// Alternatively, you can use a simple HTML noscript tag
// <script>
//   // If JavaScript is enabled, remove the noscript block
//   document.addEventListener('DOMContentLoaded', function() {
//     const noscriptBlock = document.getElementById('noscript-block');
//     if (noscriptBlock) {
//       noscriptBlock.style.display = 'none';
//     }
//   });
// </script>

<!-- index.html (alternate) -->
<!-- <noscript id="noscript-block">
  <div style="background-color: #ff0; color: #666; padding: 1em; text-align: center;">
    Please enable JavaScript to use the shopping feature.
  </div>
</noscript> -->
```
