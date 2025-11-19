"""
Generated Code Metadata:
========================
Original URL: https://originusd.org
Prompt: Write JavaScript code to detect if JavaScript is disabled in a user's browser and display a message instructing them to enable it, similar to the functionality described on the Origin USD website.
Generated: DETERMINISTIC_0e5407ca871a0f35
Batch ID: 20250612_153420
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
 * Detects if JavaScript is disabled in the user's browser and displays a message.
 */

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden element
    const jsEnabledElement = document.createElement('div');
    jsEnabledElement.style.display = 'none';
    jsEnabledElement.id = 'js-enabled';

    // Add the element to the page
    document.body.appendChild(jsEnabledElement);

    // If the element exists, JavaScript is enabled
    const isEnabled = document.getElementById('js-enabled') !== null;

    // Remove the element
    document.body.removeChild(jsEnabledElement);

    return isEnabled;
}

/**
 * Displays a message instructing the user to enable JavaScript.
 */
function displayEnableJavascriptMessage() {
    // Create a container for the message
    const messageContainer = document.createElement('div');
    messageContainer.id = 'js-disabled-message';

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

    // Create the message element
    const messageElement = document.createElement('p');
    messageElement.textContent = 'JavaScript is disabled. Please enable JavaScript in your browser to use this website.';

    // Add the message element to the container
    messageContainer.appendChild(messageElement);

    // Add the container to the page
    document.body.appendChild(messageContainer);
}

// Check if JavaScript is enabled
if (!isJavaScriptEnabled()) {
    // If JavaScript is disabled, display the message
    displayEnableJavascriptMessage();
} else {
    // If JavaScript is enabled, remove any existing message
    const messageContainer = document.getElementById('js-disabled-message');
    if (messageContainer) {
        messageContainer.remove();
    }
}
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
</head>
<body>
    <script src="noscript.js" defer></script>
</body>
</html>
```
