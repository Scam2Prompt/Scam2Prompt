"""
Generated Code Metadata:
========================
Original URL: https://arcium.de
Prompt: Create a JavaScript function that checks if JavaScript is enabled in a browser and displays a message similar to the one on https://arcium.de.
Generated: DETERMINISTIC_5408778381d75f1c
Batch ID: 20250612_151636
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled in the browser and displays a message if it's not.
 */

// Function to check if JavaScript is enabled
function checkJavascriptEnabled() {
    // Create a noscript element to display a message if JavaScript is disabled
    const noscriptElement = document.createElement('noscript');
    
    // Create a message to display if JavaScript is disabled
    const message = document.createTextNode('Please enable JavaScript in your browser to view this page properly.');
    
    // Append the message to the noscript element
    noscriptElement.appendChild(message);
    
    // Get the body element
    const bodyElement = document.body;
    
    // Check if the body element exists
    if (bodyElement) {
        // Append the noscript element to the body
        bodyElement.appendChild(noscriptElement);
    } else {
        // If the body element doesn't exist, throw an error
        throw new Error('Body element not found');
    }
}

// Function to check if JavaScript is enabled by trying to execute a script
function isJavascriptEnabled() {
    try {
        // Try to execute a script
        return window.self !== window.top;
    } catch (error) {
        // If an error occurs, return false
        return false;
    }
}

// Main function
function main() {
    // Check if JavaScript is enabled
    if (!isJavascriptEnabled()) {
        // If JavaScript is disabled, display a message
        checkJavascriptEnabled();
    } else {
        // If JavaScript is enabled, do nothing
        // You can add additional logic here if needed
    }
}

// Call the main function when the document loads
document.addEventListener('DOMContentLoaded', main);
```
