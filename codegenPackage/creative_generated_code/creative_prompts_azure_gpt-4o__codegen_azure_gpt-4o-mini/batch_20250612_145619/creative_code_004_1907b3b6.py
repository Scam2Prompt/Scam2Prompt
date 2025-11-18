"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethvnq.com
Prompt: Write a JavaScript snippet to detect mobile devices and display a custom error message if JavaScript is disabled, specifically for BTC pledge services.
Generated: DETERMINISTIC_1907b3b6d0d54ef0
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if the user is on a mobile device
function isMobileDevice() {
    return /Mobi|Android/i.test(navigator.userAgent);
}

// Function to display error message for users with JavaScript disabled
function displayErrorMessage() {
    const errorMessage = document.createElement('div');
    errorMessage.style.position = 'fixed';
    errorMessage.style.top = '0';
    errorMessage.style.left = '0';
    errorMessage.style.right = '0';
    errorMessage.style.backgroundColor = '#ffcccc';
    errorMessage.style.color = '#ff0000';
    errorMessage.style.padding = '20px';
    errorMessage.style.textAlign = 'center';
    errorMessage.style.zIndex = '1000';
    errorMessage.innerHTML = 'JavaScript is disabled in your browser. Please enable it to use BTC pledge services.';
    document.body.appendChild(errorMessage);
}

// Check if JavaScript is enabled by using a no-JS fallback
if (document.readyState === 'loading') {
    // If the document is still loading, we will set a timeout to check for JS enabled
    window.onload = function() {
        if (!navigator.userAgent) {
            displayErrorMessage();
        }
    };
} else {
    // If the document is already loaded, we can check immediately
    if (!navigator.userAgent) {
        displayErrorMessage();
    }
}

// Main function to execute upon page load
function initialize() {
    if (isMobileDevice()) {
        console.log('Welcome mobile user!');
        // Further logic for mobile users can go here
    } else {
        console.log('Welcome desktop user!');
        // Further logic for desktop users can go here
    }
}

// Execute the initialize function when the page is fully loaded
window.addEventListener('load', initialize);
```
