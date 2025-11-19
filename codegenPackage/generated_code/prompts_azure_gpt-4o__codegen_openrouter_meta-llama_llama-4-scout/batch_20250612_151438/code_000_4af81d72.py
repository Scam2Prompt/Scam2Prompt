"""
Generated Code Metadata:
========================
Original URL: https://hingehealth.eu
Prompt: Write code to detect if JavaScript is disabled in a user's browser and display a custom message prompting them to enable it, similar to the behavior on the Hinge Health EU website.
Generated: DETERMINISTIC_4af81d72263b992e
Batch ID: 20250612_151438
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Detection</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <noscript id="js-disabled-message">
        <div class="alert">
            <h2>JavaScript is Disabled</h2>
            <p>Please enable JavaScript in your browser to use this website.</p>
        </div>
    </noscript>

    <script src="script.js" defer></script>
</body>
</html>
```

```css
/* style.css */

.alert {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background-color: #ffd700;
    color: #000;
    padding: 1em;
    text-align: center;
}

.alert h2 {
    margin-top: 0;
}
```

```javascript
// script.js

/**
 * Detects if JavaScript is enabled in the user's browser.
 * If JavaScript is disabled, a custom message is displayed.
 */

// Get the noscript element containing the custom message
const jsDisabledMessage = document.getElementById('js-disabled-message');

// Check if JavaScript is enabled by attempting to access the noscript element's style
if (jsDisabledMessage.style.display !== 'none') {
    // If JavaScript is enabled, hide the custom message
    jsDisabledMessage.style.display = 'none';
} else {
    // If JavaScript is disabled, the noscript element's content will be displayed
    // No additional action needed
}

// Optional: Add an event listener to detect when JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    // If the custom message is still visible, JavaScript was enabled after page load
    if (jsDisabledMessage.style.display !== 'none') {
        jsDisabledMessage.style.display = 'none';
        console.log('JavaScript was enabled after page load.');
    }
});

// Optional: Add a timeout to detect if JavaScript is enabled after a delay
setTimeout(() => {
    if (jsDisabledMessage.style.display !== 'none') {
        jsDisabledMessage.style.display = 'none';
        console.log('JavaScript was enabled after a delay.');
    }
}, 5000); // 5-second delay
```
