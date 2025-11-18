"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cxconnect1-dss.coinbase.co.za
Prompt: Write a script using JavaScript to display a custom error message when a web application fails to load due to JavaScript being disabled, as seen on the Coinbase domain details page.
Generated: DETERMINISTIC_9cc94cdc420e6054
Batch ID: 20250612_150211
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Ensure DOM is fully loaded before executing the script
document.addEventListener('DOMContentLoaded', function () {
  // Check if JavaScript is enabled by attempting to set a flag in the DOM
  const jsEnabledFlag = document.getElementById('js-enabled-flag');

  // If the flag exists, JavaScript is enabled, and no further action is needed
  if (jsEnabledFlag) return;

  // Create a container for the error message
  const errorMessage = document.createElement('div');
  errorMessage.setAttribute('id', 'javascript-error');
  errorMessage.style.position = 'fixed';
  errorMessage.style.top = '0';
  errorMessage.style.left = '0';
  errorMessage.style.width = '100%';
  errorMessage.style.padding = '20px';
  errorMessage.style.backgroundColor = '#ff4d4f'; // Error color (red)
  errorMessage.style.color = '#ffffff'; // Text color (white)
  errorMessage.style.fontSize = '18px';
  errorMessage.style.textAlign = 'center';
  errorMessage.style.zIndex = '9999';

  // Add the error message text
  errorMessage.textContent =
    'Error: JavaScript is disabled in your browser. Please enable JavaScript to use this application.';

  // Append the error message to the body
  document.body.appendChild(errorMessage);
});

/* 
HTML code to include in the web application for proper functionality:
Add the following element inside the <body> tag to detect JavaScript status:

<div id="js-enabled-flag" style="display:none;"></div>

This invisible flag is used to confirm that JavaScript is running. 
If JavaScript is disabled, the flag will not be added to the DOM, triggering the error message.
*/
```
