"""
Generated Code Metadata:
========================
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: Develop a simple JavaScript application that checks if JavaScript is enabled and displays a message similar to "You need to enable JavaScript to run this app."
Generated: DETERMINISTIC_565ba245807f5efc
Batch ID: 20250612_153648
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
    <title>JavaScript Enabled Check</title>
    <style>
        /* Add some basic styling to make the message more readable */
        #js-enabled-message {
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 20vh;
        }
    </style>
</head>
<body>
    <div id="js-enabled-message"></div>
    <script src="script.js"></script>
</body>
</html>
```

```javascript
// script.js

/**
 * Checks if JavaScript is enabled in the browser and displays a message accordingly.
 */

// Get the message element
const messageElement = document.getElementById('js-enabled-message');

// Check if JavaScript is enabled
function checkJavaScriptEnabled() {
    try {
        // If JavaScript is enabled, this code will execute
        if (messageElement) {
            messageElement.textContent = 'JavaScript is enabled. You can now use the app.';
        } else {
            throw new Error('Could not find message element');
        }
    } catch (error) {
        // If JavaScript is disabled, this code will not execute, 
        // but we can use a noscript tag as a fallback
        console.error('Error checking JavaScript enabled:', error);
    }
}

// Fallback for users with JavaScript disabled
const noscriptElement = document.createElement('noscript');
noscriptElement.textContent = 'You need to enable JavaScript to run this app.';
document.body.appendChild(noscriptElement);

// Check JavaScript enabled after a short delay
setTimeout(checkJavaScriptEnabled, 100);
```
