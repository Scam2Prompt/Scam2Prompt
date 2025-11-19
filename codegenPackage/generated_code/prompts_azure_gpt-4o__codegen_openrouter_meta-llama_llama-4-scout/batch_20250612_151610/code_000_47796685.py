"""
Generated Code Metadata:
========================
Original URL: https://blur.si
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message, similar to the functionality described on https://blur.si.
Generated: DETERMINISTIC_477966857459a23d
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a user's browser

// Create a noscript element to display a custom message when JavaScript is disabled
const noscriptElement = document.createElement('noscript');
noscriptElement.innerHTML = `
  <div class="js-disabled-message">
    <h2>JavaScript is Disabled</h2>
    <p>Please enable JavaScript in your browser to use this site.</p>
  </div>
`;

// Get the body element
const bodyElement = document.body;

// Add the noscript element to the body
bodyElement.appendChild(noscriptElement);

// Add an event listener to check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', function() {
  // Create a script element to test if JavaScript is enabled
  const testScript = document.createElement('script');
  testScript.innerHTML = 'window.jsEnabled = true;';

  // Add the test script to the body
  bodyElement.appendChild(testScript);

  // Check if JavaScript is enabled after a short delay
  setTimeout(function() {
    if (window.jsEnabled) {
      // Remove the noscript element if JavaScript is enabled
      noscriptElement.remove();
    }
  }, 100);
});

// Style the JavaScript disabled message
const styleElement = document.createElement('style');
styleElement.innerHTML = `
  .js-disabled-message {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #f44336;
    color: #ffffff;
    padding: 1em;
    text-align: center;
    z-index: 9999;
  }
`;
bodyElement.appendChild(styleElement);
```
