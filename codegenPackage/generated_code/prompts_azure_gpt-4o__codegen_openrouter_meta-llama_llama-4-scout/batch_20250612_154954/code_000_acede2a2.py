"""
Generated Code Metadata:
========================
Original URL: https://d952.com
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message like "mining-h5 doesn't work properly without JavaScript enabled."
Generated: DETERMINISTIC_acede2a23bea3833
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled in a browser

// Create a noscript element to display a message when JavaScript is disabled
const noscriptElement = document.createElement('noscript');

// Set the text content of the noscript element
noscriptElement.textContent = "mining-h5 doesn't work properly without JavaScript enabled.";

// Append the noscript element to the body of the HTML document
document.body.appendChild(noscriptElement);

// Alternatively, you can use a more modern approach with the <script> tag's 'nomodule' attribute
// However, this method has limited browser support

// Check if JavaScript is enabled by trying to execute a simple script
try {
    // If this script runs, JavaScript is enabled
    const jsEnabled = true;

    // Remove the noscript element if JavaScript is enabled
    const existingNoscript = document.querySelector('noscript');
    if (existingNoscript) {
        existingNoscript.remove();
    }
} catch (error) {
    // If an error occurs, JavaScript is disabled (but this won't happen here)
    console.error("Error checking JavaScript status:", error);
}

// To make sure it works properly, let's add an event listener to the document
document.addEventListener('DOMContentLoaded', function () {
    // Check if the noscript element still exists
    const existingNoscript = document.querySelector('noscript');
    if (existingNoscript) {
        // If it does, JavaScript was disabled and then re-enabled (unlikely, but possible)
        existingNoscript.remove();
    }
});
```
