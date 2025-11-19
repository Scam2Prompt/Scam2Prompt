"""
Generated Code Metadata:
========================
Original URL: https://webmail.dexodoor.com
Prompt: Write JavaScript code to detect if a user's browser has JavaScript disabled and display a warning message similar to the one on the Dexodoor Webmail login page.
Generated: DETERMINISTIC_196cb256f8c85020
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled and remove the no-js warning if it is
document.addEventListener('DOMContentLoaded', function() {
    // Remove the no-js warning element if it exists
    var noJsWarning = document.getElementById('no-js-warning');
    if (noJsWarning) {
        noJsWarning.parentNode.removeChild(noJsWarning);
    }
});

// Create a noscript element to display warning when JS is disabled
var noscriptElement = document.createElement('noscript');
var warningDiv = document.createElement('div');
warningDiv.id = 'no-js-warning';
warningDiv.style.cssText = 'background-color: #fff8e6; border: 1px solid #ffd699; color: #663d00; padding: 15px; margin: 10px 0; text-align: center;';

var warningText = document.createElement('p');
warningText.textContent = 'Warning: JavaScript is disabled in your browser. Some features may not work properly.';

warningDiv.appendChild(warningText);
noscriptElement.appendChild(warningDiv);

// Insert the warning at the beginning of the body
document.body.insertBefore(noscriptElement, document.body.firstChild);
```
