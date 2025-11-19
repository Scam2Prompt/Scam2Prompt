"""
Generated Code Metadata:
========================
Original URL: https://eth-usdc.xyz
Prompt: Generate HTML and JavaScript code to create a simple webpage that checks if JavaScript is enabled and displays a custom message if it is not.
Generated: DETERMINISTIC_9b05a08ec63bdaf5
Batch ID: 20250622_211812
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Enabled Check</title>
    <style>
        #js-enabled-message {
            display: none;
        }
        
        #js-disabled-message {
            display: block;
        }
    </style>
</head>
<body>
    <div id="js-disabled-message">
        <h1>JavaScript is disabled</h1>
        <p>Please enable JavaScript to view this page.</p>
    </div>
    <div id="js-enabled-message">
        <h1>JavaScript is enabled</h1>
        <p>Welcome to our webpage!</p>
    </div>

    <script src="script.js" defer></script>
</body>
</html>
```

**script.js**
```javascript
// Get the message elements
const jsEnabledMessage = document.getElementById('js-enabled-message');
const jsDisabledMessage = document.getElementById('js-disabled-message');

// Check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', () => {
    // If JavaScript is enabled, hide the disabled message and show the enabled message
    jsDisabledMessage.style.display = 'none';
    jsEnabledMessage.style.display = 'block';
});

// Fallback for older browsers that don't support the 'defer' attribute
window.onload = () => {
    const jsEnabled = document.getElementById('js-enabled-message');
    if (jsEnabled) {
        jsEnabled.style.display = 'block';
    }
};

// Error handling: Check if the elements exist before trying to access them
try {
    if (!jsEnabledMessage || !jsDisabledMessage) {
        throw new Error('Message elements not found');
    }
} catch (error) {
    console.error('Error:', error.message);
}
```
