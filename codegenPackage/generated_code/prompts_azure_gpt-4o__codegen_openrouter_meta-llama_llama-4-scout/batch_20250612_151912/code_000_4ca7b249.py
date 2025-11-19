"""
Generated Code Metadata:
========================
Original URL: https://raiden.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a custom message instructing them to enable it, similar to the functionality described on the Raiden Online domain details page.
Generated: DETERMINISTIC_4ca7b2495ee4ca9e
Batch ID: 20250612_151912
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript.js

/**
 * Detects if JavaScript is disabled in the user's browser and displays a custom message.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden element to store a JavaScript-generated value
    const jsEnabledElement = document.createElement('div');
    jsEnabledElement.style.display = 'none';
    jsEnabledElement.id = 'js-enabled';

    // Set a JavaScript-generated value
    jsEnabledElement.textContent = 'javascript-enabled';

    // Add the element to the page
    document.body.appendChild(jsEnabledElement);

    // Check if the JavaScript-generated value is still present
    const isEnabled = document.getElementById('js-enabled').textContent === 'javascript-enabled';

    // Remove the element
    document.body.removeChild(jsEnabledElement);

    return isEnabled;
}

// Function to display a custom message if JavaScript is disabled
function displayMessageIfJavaScriptDisabled() {
    // Check if JavaScript is enabled
    if (!isJavaScriptEnabled()) {
        // Create a container for the custom message
        const messageContainer = document.createElement('div');
        messageContainer.id = 'javascript-disabled-message';

        // Set the custom message
        const message = document.createElement('p');
        message.textContent = 'JavaScript is disabled in your browser. Please enable it to use this site properly.';

        // Add the message to the container
        messageContainer.appendChild(message);

        // Add the container to the page
        document.body.appendChild(messageContainer);

        // Style the message container
        messageContainer.style.position = 'fixed';
        messageContainer.style.top = '0';
        messageContainer.style.left = '0';
        messageContainer.style.width = '100%';
        messageContainer.style.background = '#FFC080';
        messageContainer.style.color = '#333';
        messageContainer.style.padding = '1em';
        messageContainer.style.textAlign = 'center';
        messageContainer.style.zIndex = '1000';
    }
}

// Run the function on page load
document.addEventListener('DOMContentLoaded', displayMessageIfJavaScriptDisabled);
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <noscript>
        <div id="javascript-disabled-message">
            <p>JavaScript is disabled in your browser. Please enable it to use this site properly.</p>
        </div>
    </noscript>
</head>
<body>
    <script src="noscript.js" defer></script>
</body>
</html>
```
