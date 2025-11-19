"""
Generated Code Metadata:
========================
Original URL: https://claim-satoshi.app
Prompt: Generate a code snippet in JavaScript to display a warning message to users visiting a suspected phishing site.
Generated: DETERMINISTIC_fc0321e424456339
Batch ID: 20250622_211126
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// phishing-warning.js

/**
 * Displays a warning message to users visiting a suspected phishing site.
 */

// Define the warning message
const WARNING_MESSAGE = `
  <h1>Warning: Suspected Phishing Site</h1>
  <p>This website has been reported as a suspected phishing site.</p>
  <p>Please do not enter any sensitive information on this site.</p>
  <p>If you have already entered information, please monitor your accounts for suspicious activity.</p>
`;

/**
 * Displays the warning message to the user.
 */
function displayWarning() {
  try {
    // Create a warning container element
    const warningContainer = document.createElement('div');
    warningContainer.id = 'phishing-warning';
    warningContainer.innerHTML = WARNING_MESSAGE;

    // Style the warning container
    warningContainer.style.position = 'fixed';
    warningContainer.style.top = '0';
    warningContainer.style.left = '0';
    warningContainer.style.width = '100%';
    warningContainer.style.background = '#FFC080';
    warningContainer.style.color = '#000';
    warningContainer.style.padding = '1em';
    warningContainer.style.textAlign = 'center';
    warningContainer.style.zIndex = '1000';

    // Add the warning container to the page
    document.body.insertBefore(warningContainer, document.body.firstChild);
  } catch (error) {
    console.error('Error displaying phishing warning:', error);
  }
}

// Display the warning message on page load
document.addEventListener('DOMContentLoaded', displayWarning);
```
