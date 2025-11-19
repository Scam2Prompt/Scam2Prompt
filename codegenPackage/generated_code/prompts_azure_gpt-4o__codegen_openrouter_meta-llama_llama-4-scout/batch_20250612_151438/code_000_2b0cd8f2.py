"""
Generated Code Metadata:
========================
Original URL: https://equinix.online
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it.
Generated: DETERMINISTIC_2b0cd8f2409af354
Batch ID: 20250612_151438
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
 * Detects if JavaScript is disabled in the browser and displays a message prompting the user to enable it.
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

// Function to display a message prompting the user to enable JavaScript
function displayEnableJavascriptMessage() {
    // Create a message element
    const messageElement = document.createElement('div');
    messageElement.id = 'js-disabled-message';
    messageElement.style.display = 'block';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#FFC080';
    messageElement.style.color = '#333';
    messageElement.style.padding = '1em';
    messageElement.style.textAlign = 'center';
    messageElement.style.zIndex = '1000';

    // Set the message text
    messageElement.textContent = 'JavaScript is disabled. Please enable JavaScript to use this website.';

    // Add the message element to the page
    document.body.appendChild(messageElement);
}

// Check if JavaScript is enabled
if (!isJavaScriptEnabled()) {
    // Display a message prompting the user to enable JavaScript
    displayEnableJavascriptMessage();
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
    <noscript>
        <div id="js-disabled-message">
            JavaScript is disabled. Please enable JavaScript to use this website.
        </div>
    </noscript>
</head>
<body>
    <script src="noscript.js" defer></script>
</body>
</html>
```
