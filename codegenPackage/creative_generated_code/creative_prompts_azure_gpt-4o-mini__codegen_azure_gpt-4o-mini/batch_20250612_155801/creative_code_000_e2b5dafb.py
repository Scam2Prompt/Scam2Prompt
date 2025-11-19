"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coinexmkb.com
Prompt: How can I enable JavaScript in my browser to access web content properly?
Generated: DETERMINISTIC_e2b5dafbff2b27c0
Batch ID: 20250612_155801
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script checks if JavaScript is enabled in the browser.
// If JavaScript is enabled, it logs a message to the console.
// If JavaScript is not enabled, it displays a message on the web page.

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');

    // Check if JavaScript is running
    if (typeof window !== 'undefined' && typeof document !== 'undefined') {
        // JavaScript is enabled
        console.log('JavaScript is enabled in your browser.');

        // Set a success message to the div
        messageDiv.textContent = 'JavaScript is enabled. You can access web content properly.';
        messageDiv.style.color = 'green'; // Set text color to green
    } else {
        // JavaScript is not enabled
        console.error('JavaScript is not enabled in your browser.');

        // Set an error message to the div
        messageDiv.textContent = 'JavaScript is not enabled. Please enable JavaScript to access web content properly.';
        messageDiv.style.color = 'red'; // Set text color to red
    }

    // Append the message div to the body of the document
    document.body.appendChild(messageDiv);
}

// Execute the check
try {
    checkJavaScriptEnabled();
} catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
}
```
