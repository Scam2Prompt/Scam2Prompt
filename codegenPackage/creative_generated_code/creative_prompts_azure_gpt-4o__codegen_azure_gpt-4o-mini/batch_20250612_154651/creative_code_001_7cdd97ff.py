"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: Create a script to check if a user is accessing a webpage using Internet Explorer 11 and display a message recommending an alternative browser, as mentioned in the cPanel Webmail login system.
Generated: DETERMINISTIC_7cdd97ff5bf0e7a8
Batch ID: 20250612_154651
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to check if the user is using Internet Explorer 11
function isInternetExplorer11() {
    // Check the user agent string for 'Trident' which indicates IE
    return navigator.userAgent.indexOf('Trident/') > -1 && navigator.userAgent.indexOf('rv:11') > -1;
}

// Function to display a warning message if IE 11 is detected
function displayBrowserWarning() {
    // Create a warning message element
    const warningMessage = document.createElement('div');

    // Set the message content and styles for visibility
    warningMessage.innerText = "You are using Internet Explorer 11. For a better experience, please switch to a modern browser such as Chrome, Firefox, or Edge.";
    warningMessage.style.position = 'fixed';
    warningMessage.style.top = '0';
    warningMessage.style.left = '0';
    warningMessage.style.width = '100%';
    warningMessage.style.backgroundColor = '#ffcc00';
    warningMessage.style.color = '#000';
    warningMessage.style.textAlign = 'center';
    warningMessage.style.padding = '10px';
    warningMessage.style.zIndex = '1000'; // Ensure it appears on top

    // Append the warning message to the body
    document.body.appendChild(warningMessage);
}

// Main script execution
try {
    // Check for IE 11 and display warning if true
    if (isInternetExplorer11()) {
        displayBrowserWarning();
    }
} catch (error) {
    // Log any errors to the console for debugging
    console.error("An error occurred while checking the browser type:", error);
}
```
