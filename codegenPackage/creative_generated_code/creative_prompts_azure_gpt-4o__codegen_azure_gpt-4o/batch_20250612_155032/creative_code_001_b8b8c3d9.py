"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://m.coinbasenft.eu
Prompt: Create a JavaScript snippet that checks if a webpage's core functionality depends on JavaScript and provides an alert if JavaScript is disabled.
Generated: DETERMINISTIC_b8b8c3d998ce6dd5
Batch ID: 20250612_155032
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script checks if JavaScript is required for the core functionality of a webpage.
 * If JavaScript is disabled, it provides a visual alert to the user.
 */

(function () {
  'use strict';

  // Create a message container element for users without JavaScript enabled
  const noJsMessage = document.createElement('div');
  noJsMessage.id = 'no-js-warning';
  noJsMessage.style.position = 'fixed';
  noJsMessage.style.top = '0';
  noJsMessage.style.left = '0';
  noJsMessage.style.width = '100%';
  noJsMessage.style.backgroundColor = '#ffcc00'; // Yellow background for visibility
  noJsMessage.style.color = '#000'; // Black text
  noJsMessage.style.textAlign = 'center';
  noJsMessage.style.padding = '10px 0';
  noJsMessage.style.fontFamily = 'Arial, sans-serif';
  noJsMessage.style.fontSize = '14px';
  noJsMessage.style.zIndex = '9999';
  noJsMessage.textContent =
    'This webpage requires JavaScript for core functionality. Please enable JavaScript in your browser settings.';

  // Add the message to the page if JavaScript is disabled (via <noscript> fallback)
  const noscriptFallback = document.createElement('noscript');
  noscriptFallback.appendChild(noJsMessage);
  document.body.appendChild(noscriptFallback);

  // Remove the warning if JavaScript is enabled and working
  document.addEventListener('DOMContentLoaded', () => {
    try {
      const existingWarning = document.getElementById('no-js-warning');
      if (existingWarning) {
        existingWarning.remove(); // Remove the warning if JavaScript is enabled
      }
    } catch (error) {
      console.error('Error while removing the no-JS warning:', error);
    }
  });
})();
```
