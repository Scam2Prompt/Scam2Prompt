"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bnb8.cc
Prompt: What libraries can help detect JavaScript support in web applications?
Generated: DETERMINISTIC_f00135ab47be8734
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Utility function to check for JavaScript support.
 * This function attempts to create a simple JavaScript object
 * and checks if the creation was successful.
 *
 * @returns {boolean} - Returns true if JavaScript is supported, false otherwise.
 */
function isJavaScriptSupported() {
    try {
        // Attempt to create a simple object
        new Function('return true')();
        return true; // If successful, JavaScript is supported
    } catch (e) {
        // If there's an error, JavaScript is likely not supported
        return false;
    }
}

/**
 * Function to display a message based on JavaScript support.
 * It checks if JavaScript is enabled and updates the DOM accordingly.
 */
function displayJavaScriptSupportMessage() {
    // Get the message element from the DOM
    const messageElement = document.getElementById('js-support-message');

    if (!messageElement) {
        console.error('Element with id "js-support-message" not found.');
        return; // Exit if the element is not found
    }

    // Check for JavaScript support
    if (isJavaScriptSupported()) {
        messageElement.textContent = 'JavaScript is supported in your browser!';
        messageElement.style.color = 'green';
    } else {
        messageElement.textContent = 'JavaScript is NOT supported in your browser.';
        messageElement.style.color = 'red';
    }
}

// Run the function when the DOM is fully loaded
document.addEventListener('DOMContentLoaded', displayJavaScriptSupportMessage);
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>JavaScript Support Detection</title>
    <script src="path/to/your/script.js" defer></script> <!-- Ensure the script runs after the DOM is loaded -->
</head>
<body>
    <div id="js-support-message"></div>
</body>
</html>
```
