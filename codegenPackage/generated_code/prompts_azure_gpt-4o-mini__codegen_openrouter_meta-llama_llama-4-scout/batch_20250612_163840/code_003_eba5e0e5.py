"""
Generated Code Metadata:
========================
Original URL: https://ethjya.com
Prompt: Generate a JavaScript function that alerts users to enable JavaScript for better experience on ethjya.com.
Generated: DETERMINISTIC_eba5e0e533a544cc
Batch ID: 20250612_163840
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and alerts users to enable it for a better experience on ethjya.com.
 */

/**
 * Function to check if JavaScript is enabled and display a message if not.
 */
function checkJavascriptEnabled() {
    // Check if the browser supports JavaScript
    if (typeof window === 'undefined') {
        // If not, do nothing (Node.js environment)
        return;
    }

    // Check if JavaScript is enabled by checking for a specific property
    if ('alert' in window) {
        // If JavaScript is enabled, do nothing
        return;
    }

    // If JavaScript is disabled, display a message
    const messageElement = document.createElement('noscript');
    messageElement.textContent = 'Please enable JavaScript for a better experience on ethjya.com.';
    document.body.appendChild(messageElement);
}

/**
 * Function to display a warning message to users to enable JavaScript.
 */
function displayJavascriptWarning() {
    try {
        // Create a warning message element
        const warningElement = document.createElement('div');
        warningElement.style.position = 'fixed';
        warningElement.style.top = '0';
        warningElement.style.left = '0';
        warningElement.style.width = '100%';
        warningElement.style.background = '#FFC080';
        warningElement.style.color = '#333';
        warningElement.style.padding = '1em';
        warningElement.style.textAlign = 'center';
        warningElement.style.zIndex = '1000';

        // Set the warning message text
        warningElement.textContent = 'For a better experience on ethjya.com, please enable JavaScript in your browser.';

        // Add the warning message to the page
        document.body.appendChild(warningElement);
    } catch (error) {
        // Log any errors that occur
        console.error('Error displaying JavaScript warning:', error);
    }
}

// Call the functions
checkJavascriptEnabled();
displayJavascriptWarning();
```
