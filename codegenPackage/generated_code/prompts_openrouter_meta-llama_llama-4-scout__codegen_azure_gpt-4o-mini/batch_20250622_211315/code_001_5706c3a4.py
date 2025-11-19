"""
Generated Code Metadata:
========================
Original URL: https://digitalconsultinggroup.my
Prompt: Generate a JavaScript code snippet that checks if JavaScript is enabled for a given website, similar to the functionality on https://digitalconsultinggroup.my.
Generated: DETERMINISTIC_5706c3a4c70a151a
Batch ID: 20250622_211315
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a div element to test JavaScript functionality
    const testDiv = document.createElement('div');
    
    // Set a property that will be modified by JavaScript
    testDiv.innerHTML = 'JavaScript is enabled';
    
    // Append the test div to the body
    document.body.appendChild(testDiv);
    
    // Check if the innerHTML was set correctly
    if (testDiv.innerHTML === 'JavaScript is enabled') {
        // JavaScript is enabled, remove the test div
        document.body.removeChild(testDiv);
        return true;
    } else {
        // JavaScript is not enabled, remove the test div
        document.body.removeChild(testDiv);
        return false;
    }
}

// Function to display a message based on JavaScript status
function displayJavaScriptStatus() {
    // Check if JavaScript is enabled
    const isEnabled = checkJavaScriptEnabled();
    
    // Create a message element
    const messageDiv = document.createElement('div');
    
    // Set the message based on the JavaScript status
    if (isEnabled) {
        messageDiv.innerHTML = 'JavaScript is enabled on this website.';
    } else {
        messageDiv.innerHTML = 'JavaScript is not enabled on this website. Please enable it for the best experience.';
    }
    
    // Append the message to the body
    document.body.appendChild(messageDiv);
}

// Execute the function to display the JavaScript status
try {
    displayJavaScriptStatus();
} catch (error) {
    console.error('An error occurred while checking JavaScript status:', error);
}
```
