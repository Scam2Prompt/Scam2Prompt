"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imtaoekecn.com
Prompt: Write a script to check browser compatibility for Ethereum-related web applications, ensuring JavaScript is enabled as required by the ETH Pledge website.
Generated: DETERMINISTIC_4eb4ef3371da5efc
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Checks for browser compatibility for Ethereum-related web applications.
 * Specifically, it verifies if JavaScript is enabled.
 * If JavaScript is disabled, it provides a notification to the user.
 */

// Function to check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a dummy HTML element to test JavaScript functionality
    const jsTestElement = document.createElement('div');
    jsTestElement.id = 'js-test';
    jsTestElement.innerHTML = 'JavaScript is working!';
    document.body.appendChild(jsTestElement);

    // Check if the dummy element was successfully created and modified
    const isJavaScriptEnabled = jsTestElement.innerHTML === 'JavaScript is working!';
    
    // Remove the test element from the DOM
    document.body.removeChild(jsTestElement);
    
    return isJavaScriptEnabled;
}

// Function to display a notification if JavaScript is disabled
function displayNotification() {
    const notification = document.createElement('div');
    notification.style.position = 'fixed';
    notification.style.bottom = '20px';
    notification.style.left = '20px';
    notification.style.padding = '10px';
    notification.style.backgroundColor = '#f44336'; // Red
    notification.style.color = '#ffffff'; // White
    notification.style.zIndex = '1000';
    notification.style.borderRadius = '5px';
    notification.innerHTML = 'JavaScript is disabled. Please enable JavaScript for the best experience on our site.';
    
    document.body.appendChild(notification);
}

// Main function to run the compatibility check
function runCompatibilityCheck() {
    try {
        if (!checkJavaScriptEnabled()) {
            displayNotification();
        }
    } catch (error) {
        console.error('Error occurred during browser compatibility check:', error);
    }
}

// Execute the compatibility check on page load
document.addEventListener('DOMContentLoaded', runCompatibilityCheck);
```
