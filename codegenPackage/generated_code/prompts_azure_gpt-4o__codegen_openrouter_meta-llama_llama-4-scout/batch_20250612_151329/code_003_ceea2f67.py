"""
Generated Code Metadata:
========================
Original URL: https://mdex-4ld.pages.dev
Prompt: Write code to check if JavaScript is enabled in a browser and display an error message if it is disabled, as seen on https://mdex-4ld.pages.dev.
Generated: DETERMINISTIC_ceea2f678726d8be
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the browser
function checkJavaScriptEnabled() {
    // Create a hidden element to store a value if JavaScript is enabled
    const jsEnabledElement = document.createElement('div');
    jsEnabledElement.style.display = 'none';
    jsEnabledElement.id = 'js-enabled-check';

    // Add the element to the page
    document.body.appendChild(jsEnabledElement);

    // Set a value on the element if JavaScript is enabled
    jsEnabledElement.textContent = 'JavaScript is enabled';

    // Check if the element has the value after 100ms
    setTimeout(() => {
        if (document.getElementById('js-enabled-check').textContent === '') {
            // Display an error message if JavaScript is disabled
            displayErrorMessage();
        }
    }, 100);
}

// Display an error message if JavaScript is disabled
function displayErrorMessage() {
    // Create a container for the error message
    const errorContainer = document.createElement('div');
    errorContainer.style.position = 'fixed';
    errorContainer.style.top = '0';
    errorContainer.style.left = '0';
    errorContainer.style.width = '100%';
    errorContainer.style.backgroundColor = '#FF0000';
    errorContainer.style.color = '#FFFFFF';
    errorContainer.style.padding = '1em';
    errorContainer.style.textAlign = 'center';
    errorContainer.style.zIndex = '1000';

    // Create the error message element
    const errorMessage = document.createElement('p');
    errorMessage.textContent = 'Error: JavaScript is disabled. Please enable JavaScript to use this website.';

    // Add the error message to the container
    errorContainer.appendChild(errorMessage);

    // Add the container to the page
    document.body.appendChild(errorContainer);
}

// Run the check when the page loads
document.addEventListener('DOMContentLoaded', checkJavaScriptEnabled);
```
