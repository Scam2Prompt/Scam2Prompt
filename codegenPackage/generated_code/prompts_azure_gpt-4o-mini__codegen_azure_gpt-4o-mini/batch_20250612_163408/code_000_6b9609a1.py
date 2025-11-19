"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-783--peaceful-nightingale-55a1b7.netlify.app
Prompt: How can I enable JavaScript in my browser to use the Ignitus app effectively?
Generated: DETERMINISTIC_6b9609a1195e03e6
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check if JavaScript is enabled in the browser
function isJavaScriptEnabled() {
    // Create a test element
    const testElement = document.createElement('div');
    testElement.id = 'js-test';
    testElement.innerHTML = 'JavaScript is enabled!';
    
    // Append the test element to the body
    document.body.appendChild(testElement);
    
    // Check if the test element is in the DOM
    const isEnabled = document.getElementById('js-test') !== null;
    
    // Clean up by removing the test element
    document.body.removeChild(testElement);
    
    return isEnabled;
}

// Function to display a message based on JavaScript status
function displayJavaScriptStatus() {
    try {
        if (isJavaScriptEnabled()) {
            console.log('JavaScript is enabled. You can use the Ignitus app effectively.');
        } else {
            console.warn('JavaScript is disabled. Please enable JavaScript in your browser settings to use the Ignitus app.');
        }
    } catch (error) {
        console.error('An error occurred while checking JavaScript status:', error);
    }
}

// Execute the function to check JavaScript status on page load
document.addEventListener('DOMContentLoaded', displayJavaScriptStatus);
```
