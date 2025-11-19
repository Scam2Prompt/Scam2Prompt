"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Write JavaScript code to detect if a user's browser supports JavaScript and display a custom message if it does not, similar to the functionality described on the website https://getin.co.il.
Generated: DETERMINISTIC_8756a4e8b5aa1fb9
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled
function checkJavascriptSupport() {
    // Create a noscript element to display a message if JavaScript is disabled
    const noscriptElement = document.createElement('noscript');
    
    // Create a div element to display the custom message
    const messageElement = document.createElement('div');
    messageElement.textContent = 'Please enable JavaScript to view this site properly.';
    messageElement.style.position = 'fixed';
    messageElement.style.top = '0';
    messageElement.style.left = '0';
    messageElement.style.width = '100%';
    messageElement.style.background = '#FF0000';
    messageElement.style.color = '#FFFFFF';
    messageElement.style.textAlign = 'center';
    messageElement.style.padding = '10px';
    messageElement.style.zIndex = '1000';

    // Append the message element to the noscript element
    noscriptElement.appendChild(messageElement);

    // Append the noscript element to the body
    document.body.appendChild(noscriptElement);
}

// Check if JavaScript is supported
function isJavascriptSupported() {
    // If the user has disabled JavaScript, this function will not be executed
    // However, we can use a simple trick to detect if JavaScript is enabled
    // If the script is executed, it means JavaScript is enabled
    return true;
}

// Main function
function main() {
    try {
        // Check if JavaScript is supported
        if (isJavascriptSupported()) {
            // If JavaScript is supported, remove the noscript element (if it exists)
            const noscriptElement = document.querySelector('noscript');
            if (noscriptElement) {
                noscriptElement.remove();
            }
        } else {
            // If JavaScript is not supported, display the custom message
            checkJavascriptSupport();
        }
    } catch (error) {
        console.error('Error checking JavaScript support:', error);
    }
}

// Execute the main function
main();
```
