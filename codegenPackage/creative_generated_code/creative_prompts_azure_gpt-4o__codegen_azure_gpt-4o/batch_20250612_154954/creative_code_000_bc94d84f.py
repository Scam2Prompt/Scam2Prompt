"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elbdataplanescope.zhy.coinbasenft.de
Prompt: Write JavaScript code to check if JavaScript is enabled in a browser and display a message prompting the user to enable it, as seen on the domain details page at elbdataplanescope.zhy.coinbasenft.de.
Generated: DETERMINISTIC_bc94d84ffbf8e898
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script checks if JavaScript is enabled in a browser.
 * If JavaScript is disabled, a message will be displayed prompting the user to enable it.
 */

// Wrap code in an Immediately Invoked Function Expression (IIFE) to avoid polluting the global scope
(function () {
  'use strict';

  // Check if JavaScript is enabled by executing code
  document.addEventListener('DOMContentLoaded', function () {
    try {
      // Create a DOM element to display the message
      const messageContainer = document.createElement('div');
      messageContainer.id = 'js-enabled-message';
      messageContainer.style.cssText = `
        position: fixed;
        top: 20px;
        left: 50%;
        transform: translateX(-50%);
        background-color: #f8e71c;
        color: #333;
        padding: 10px 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
        font-size: 14px;
        font-family: Arial, sans-serif;
        z-index: 1000;
      `;

      // Set the message text
      messageContainer.textContent = 'JavaScript is enabled.';

      // Append the message to the body
      document.body.appendChild(messageContainer);

      // Optional: Remove the message after a few seconds
      setTimeout(() => {
        if (messageContainer) {
          document.body.removeChild(messageContainer);
        }
      }, 5000); // Message disappears after 5 seconds
    } catch (error) {
      console.error('An error occurred while displaying the JavaScript enabled message:', error);
    }
  });
})();
```

Note: This script assumes that JavaScript is enabled since the code itself cannot run if JavaScript is disabled. In scenarios where JavaScript is disabled, you could use the `<noscript>` HTML element to display the appropriate message. Example:

```html
<noscript>
  <div style="color: red; font-weight: bold;">
    JavaScript is disabled. Please enable JavaScript in your browser to view this page properly.
  </div>
</noscript>
```
