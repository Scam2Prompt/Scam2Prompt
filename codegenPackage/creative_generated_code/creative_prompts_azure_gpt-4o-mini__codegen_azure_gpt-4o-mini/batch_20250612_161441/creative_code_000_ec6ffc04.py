"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://linea-five.vercel.app
Prompt: How can I enable JavaScript in my browser to run the Linea app?
Generated: DETERMINISTIC_ec6ffc04fc5cb234
Batch ID: 20250612_161441
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
    // Create a script element
    const script = document.createElement('script');
    script.textContent = 'window.jsEnabled = true;'; // Set a global variable to indicate JavaScript is enabled
    document.head.appendChild(script); // Append the script to the document

    // Check if the variable is set
    if (window.jsEnabled) {
        return true; // JavaScript is enabled
    } else {
        return false; // JavaScript is not enabled
    }
}

// Function to notify user about enabling JavaScript
function notifyUser() {
    // Create a notification element
    const notification = document.createElement('div');
    notification.style.position = 'fixed';
    notification.style.top = '10px';
    notification.style.right = '10px';
    notification.style.backgroundColor = '#ffcc00';
    notification.style.padding = '10px';
    notification.style.border = '1px solid #ff9900';
    notification.style.zIndex = '1000';
    notification.innerText = 'JavaScript is disabled. Please enable it to run the Linea app.';

    // Append the notification to the body
    document.body.appendChild(notification);
}

// Main function to run the check and notify
function main() {
    try {
        // Check if JavaScript is enabled
        if (!isJavaScriptEnabled()) {
            notifyUser(); // Notify user if JavaScript is not enabled
        } else {
            console.log('JavaScript is enabled. You can run the Linea app.'); // Success message
        }
    } catch (error) {
        console.error('An error occurred while checking JavaScript status:', error);
    }
}

// Run the main function on page load
window.onload = main;
```
