"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://booking-lk.com
Prompt: How can I enable JavaScript in my browser to use the features on booking-lk.com?
Generated: DETERMINISTIC_213d6786a84278ea
Batch ID: 20250612_163030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// This script checks if JavaScript is enabled in the browser.
// If JavaScript is disabled, it will provide instructions to enable it.

// Function to display a message if JavaScript is disabled
function displayMessage() {
    const messageContainer = document.createElement('div');
    messageContainer.style.position = 'fixed';
    messageContainer.style.top = '0';
    messageContainer.style.left = '0';
    messageContainer.style.width = '100%';
    messageContainer.style.backgroundColor = '#ffcc00';
    messageContainer.style.color = '#000';
    messageContainer.style.padding = '10px';
    messageContainer.style.textAlign = 'center';
    messageContainer.style.zIndex = '1000';

    messageContainer.innerHTML = `
        <strong>JavaScript is disabled in your browser.</strong>
        <p>Please enable JavaScript to use all features of booking-lk.com.</p>
        <p>Here's how to enable JavaScript:</p>
        <ul>
            <li><strong>Chrome:</strong> Go to Settings > Privacy and security > Site settings > JavaScript, then turn it on.</li>
            <li><strong>Firefox:</strong> Type about:config in the address bar, search for 'javascript.enabled', and toggle it to true.</li>
            <li><strong>Safari:</strong> Go to Preferences > Security, then check the Enable JavaScript option.</li>
            <li><strong>Edge:</strong> Go to Settings > Cookies and site permissions > JavaScript, then turn it on.</li>
        </ul>
    `;

    document.body.prepend(messageContainer);
}

// Check if JavaScript is enabled
if (typeof window === 'undefined' || !window.document) {
    // If JavaScript is not enabled, call the displayMessage function
    displayMessage();
} else {
    // JavaScript is enabled; you can initialize your application here
    console.log('JavaScript is enabled. You can now use the features of booking-lk.com.');
}
```
