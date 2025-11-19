"""
Generated Code Metadata:
========================
Original URL: https://airdrop.gti.finance
Prompt: Generate code to detect if JavaScript is enabled in a browser and display a message prompting users to enable it, as required by web apps like GTI Finance's airdrop service.
Generated: DETERMINISTIC_1ee9a96dc80d39dd
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript detection and enablement prompt

// Function to check if JavaScript is enabled
function isJavaScriptEnabled() {
    // If JavaScript is disabled, this variable will not be defined
    return typeof jsEnabledCheck !== 'undefined';
}

// Function to display a message prompting users to enable JavaScript
function displayEnableJSPrompt() {
    // Create a div element to display the message
    const jsDisabledMessage = document.createElement('div');
    jsDisabledMessage.id = 'js-disabled-message';
    jsDisabledMessage.style.position = 'fixed';
    jsDisabledMessage.style.top = '0';
    jsDisabledMessage.style.left = '0';
    jsDisabledMessage.style.width = '100%';
    jsDisabledMessage.style.background = '#FF0000';
    jsDisabledMessage.style.color = '#FFFFFF';
    jsDisabledMessage.style.padding = '1em';
    jsDisabledMessage.style.textAlign = 'center';
    jsDisabledMessage.style.zIndex = '1000';

    // Set the message text
    jsDisabledMessage.innerText = 'JavaScript is disabled. Please enable JavaScript to use this web application.';

    // Add the message element to the page
    document.body.appendChild(jsDisabledMessage);
}

// Check if JavaScript is enabled
if (!isJavaScriptEnabled()) {
    // If JavaScript is disabled, display a message prompting users to enable it
    document.addEventListener('DOMContentLoaded', displayEnableJSPrompt);
} else {
    // If JavaScript is enabled, remove any existing message
    const jsDisabledMessage = document.getElementById('js-disabled-message');
    if (jsDisabledMessage) {
        jsDisabledMessage.remove();
    }
}

// Set a flag to indicate that JavaScript is enabled
var jsEnabledCheck = true;
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
    <noscript>
        <!-- Fallback content for browsers with JavaScript disabled -->
        <div style="position: fixed; top: 0; left: 0; width: 100%; background: #FF0000; color: #FFFFFF; padding: 1em; text-align: center;">
            JavaScript is disabled. Please enable JavaScript to use this web application.
        </div>
    </noscript>
    <script src="script.js"></script>
</body>
</html>
```
