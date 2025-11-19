"""
Generated Code Metadata:
========================
Original URL: https://dogeai.eu
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message similar to "This app doesn't work properly without JavaScript enabled. Please enable it to continue," as seen on the DogeAI website.
Generated: DETERMINISTIC_fe1512dc2030ed56
Batch ID: 20250612_154312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// noscript.js

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // Create a hidden element to store a value
    const jsEnabledElement = document.createElement('noscript');
    jsEnabledElement.textContent = 'JavaScript is disabled';

    // Append the element to the body
    document.body.appendChild(jsEnabledElement);

    // Check if the element's text content has changed
    // If JavaScript is enabled, this will be executed and the text content will be different
    if (jsEnabledElement.textContent === 'JavaScript is disabled') {
        return false;
    } else {
        return true;
    }
}

// Function to display a message when JavaScript is disabled
function displayMessage() {
    // Create a message element
    const messageElement = document.createElement('div');
    messageElement.id = 'js-disabled-message';
    messageElement.textContent = 'This app doesn\'t work properly without JavaScript enabled. Please enable it to continue.';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#f44336';
    messageElement.style.color = '#ffffff';
    messageElement.style.padding = '1em';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '1000';

    // Append the message element to the body
    document.body.appendChild(messageElement);
}

// Check if JavaScript is enabled
if (!isJavaScriptEnabled()) {
    displayMessage();
} else {
    // If JavaScript is enabled, remove any existing message
    const messageElement = document.getElementById('js-disabled-message');
    if (messageElement) {
        messageElement.remove();
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
