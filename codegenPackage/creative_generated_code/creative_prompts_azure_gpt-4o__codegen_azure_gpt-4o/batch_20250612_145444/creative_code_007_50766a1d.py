"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho-frontend.pages.dev
Prompt: Develop a JavaScript snippet to display a warning message if JavaScript is disabled in a Morpho-based app.
Generated: DETERMINISTIC_50766a1d11192944
Batch ID: 20250612_145444
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script ensures a warning message is displayed when JavaScript is disabled.
 * It is designed for a Morpho-based app but can be used in any web application.
 *
 * @file warning-message.js
 * @author [Your Name]
 * @date [Today's Date]
 */

// IIFE (Immediately Invoked Function Expression) to encapsulate the code
(function () {
  'use strict';

  // Create a warning message element
  const warningMessage = document.createElement('noscript');
  warningMessage.style.cssText = `
    display: block;
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ffcc00;
    color: #000;
    text-align: center;
    padding: 10px;
    font-size: 16px;
    font-weight: bold;
    z-index: 9999;
  `;
  warningMessage.innerText = 'Warning: JavaScript is disabled. Please enable it for a better experience in this app.';

  // Append the warning message to the body
  document.body.appendChild(warningMessage);

  // Optional: Log a message to the console for debugging purposes
  console.info('Warning for disabled JavaScript injected into the DOM.');
})();
```
