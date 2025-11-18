"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.everclear.pk
Prompt: Create a script that checks if a user is accessing a webpage using Internet Explorer 11 and displays a message recommending an alternative browser, as mentioned in the Webmail login page of https://webmail.everclear.pk.
Generated: DETERMINISTIC_af0b81a18d306a11
Batch ID: 20250612_153447
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to detect if the user is using Internet Explorer 11
function isInternetExplorer() {
    // Check the user agent string for 'MSIE' or 'Trident'
    return /MSIE|Trident/.test(window.navigator.userAgent);
}

// Function to display a message recommending an alternative browser
function showBrowserRecommendation() {
    // Create a div element for the message
    const messageDiv = document.createElement('div');
    // Set the message content and style
    messageDiv.textContent = 'You are using Internet Explorer 11. For a better experience, please consider using a modern browser like Chrome, Firefox, or Edge.';
    messageDiv.style.position = 'fixed';
    messageDiv.style.top = '10px';
    messageDiv.style.right = '10px';
    messageDiv.style.backgroundColor = '#ffcc00';
    messageDiv.style.padding = '15px';
    messageDiv.style.border = '1px solid #ddaa00';
    messageDiv.style.zIndex = '1000';
    messageDiv.style.borderRadius = '5px';
    
    // Append the message to the body
    document.body.appendChild(messageDiv);
}

// Check if the user is using Internet Explorer and display a recommendation if true
try {
    if (isInternetExplorer()) {
        showBrowserRecommendation();
    }
} catch (error) {
    console.error('Error checking browser type:', error);
}
```
