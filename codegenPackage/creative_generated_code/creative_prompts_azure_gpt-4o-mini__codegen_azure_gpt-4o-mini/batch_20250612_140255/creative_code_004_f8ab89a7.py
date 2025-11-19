"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://basedswap.xyz
Prompt: How do I enable JavaScript in my browser to access the BasedSwap app effectively?
Generated: DETERMINISTIC_f8ab89a7e1d5c57c
Batch ID: 20250612_140255
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if JavaScript is enabled in the browser
function isJavaScriptEnabled() {
    // Create a test element
    const testElement = document.createElement('div');
    
    // Attempt to set a property to the test element
    try {
        testElement.setAttribute('data-js-enabled', 'true');
        return testElement.getAttribute('data-js-enabled') === 'true';
    } catch (error) {
        console.error('Error checking if JavaScript is enabled:', error);
        return false;
    }
}

// Function to display a message based on JavaScript status
function displayStatusMessage() {
    const messageElement = document.createElement('p');
    
    if (isJavaScriptEnabled()) {
        messageElement.textContent = 'JavaScript is enabled. You can access the BasedSwap app effectively!';
    } else {
        messageElement.textContent = 'JavaScript is disabled. Please enable JavaScript in your browser settings to use BasedSwap.';
    }
    
    // Append the message to the body of the document
    document.body.appendChild(messageElement);
}

// Call the function to display the status message
displayStatusMessage();
```

This code snippet will check if JavaScript is enabled in the browser and display an appropriate message to the user. Make sure to include this script in your HTML file within the `<script>` tags or as an external JavaScript file.
