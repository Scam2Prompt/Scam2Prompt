"""
Generated Code Metadata:
========================
Original URL: https://whitelist-bonkboxes.web.app
Prompt: Develop a JavaScript snippet to check if JavaScript is enabled in the browser and display a custom message for the BONKBOXES Whitelist application.
Generated: DETERMINISTIC_db3f379131332a6f
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled in the browser
function isJavaScriptEnabled() {
    // If JavaScript is disabled, this element will not be hidden
    const jsEnabledElement = document.getElementById('js-enabled');
    
    // If the element exists, JavaScript is enabled
    return jsEnabledElement !== null;
}

// Display a custom message for the BONKBOXES Whitelist application
function displayMessage() {
    try {
        // Get the container element to display the message
        const messageContainer = document.getElementById('message-container');
        
        if (messageContainer) {
            // Check if JavaScript is enabled
            if (isJavaScriptEnabled()) {
                // Display a success message
                messageContainer.innerHTML = `
                    <div class="alert alert-success">
                        <strong>JavaScript is enabled!</strong> You can proceed with the BONKBOXES Whitelist application.
                    </div>
                `;
            } else {
                // Display an error message if JavaScript is disabled
                messageContainer.innerHTML = `
                    <div class="alert alert-error">
                        <strong>JavaScript is disabled!</strong> Please enable JavaScript to use the BONKBOXES Whitelist application.
                    </div>
                `;
            }
        } else {
            throw new Error('Message container element not found');
        }
    } catch (error) {
        console.error('Error displaying message:', error);
    }
}

// Initialize the application
document.addEventListener('DOMContentLoaded', () => {
    // Hide the noscript element
    const noscriptElement = document.getElementById('noscript');
    if (noscriptElement) {
        noscriptElement.style.display = 'none';
    }
    
    // Display the message
    displayMessage();
});
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <titleBONKBOXES Whitelist</title>
    <style>
        /* Add some basic styling */
        .alert {
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .alert-success {
            background-color: #cff6cf;
            border: 1px solid #3e8e41;
            color: #3e8e41;
        }
        .alert-error {
            background-color: #fbe3e3;
            border: 1px solid #a94442;
            color: #a94442;
        }
    </style>
</head>
<body>
    <noscript id="noscript">
        <div class="alert alert-error">
            <strong>JavaScript is disabled!</strong> Please enable JavaScript to use the BONKBOXES Whitelist application.
        </div>
    </noscript>
    <div id="js-enabled" style="display: none;">JavaScript is enabled!</div>
    <div id="message-container"></div>
    <script src="script.js"></script>
</body>
</html>
```
