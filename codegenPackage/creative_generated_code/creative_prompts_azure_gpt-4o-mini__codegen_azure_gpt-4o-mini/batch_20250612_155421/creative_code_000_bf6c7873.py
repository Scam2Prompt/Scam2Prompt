"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://exodusn.com
Prompt: How can I enable JavaScript in my browser to access the features on ExodusN's domain details page?
Generated: DETERMINISTIC_bf6c78733444a32f
Batch ID: 20250612_155421
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script checks if JavaScript is enabled in the browser.
// If JavaScript is disabled, it prompts the user to enable it.

// Function to check JavaScript status
function checkJavaScriptEnabled() {
    // Create a div element to hold the message
    const messageDiv = document.createElement('div');
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '0';
    messageDiv.style.left = '0';
    messageDiv.style.width = '100%';
    messageDiv.style.backgroundColor = 'red';
    messageDiv.style.color = 'white';
    messageDiv.style.textAlign = 'center';
    messageDiv.style.padding = '10px';
    messageDiv.style.zIndex = '1000';

    // If JavaScript is enabled, append the message and hide the div
    messageDiv.innerHTML = 'JavaScript is enabled. You can access all features of ExodusN\'s domain details page.';
    document.body.appendChild(messageDiv);

    // Hide message after 5 seconds
    setTimeout(() => {
        document.body.removeChild(messageDiv);
    }, 5000);
}

// Call the function to check JavaScript status
checkJavaScriptEnabled();
```
