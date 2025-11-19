"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Create a simple JavaScript code snippet that checks browser compatibility and displays a message if JavaScript is disabled.
Generated: DETERMINISTIC_335f3a4d65ab6bad
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Check if JavaScript is enabled
function checkJavaScriptEnabled() {
    // Create a noscript element
    const noscriptElement = document.createElement('noscript');
    
    // Create a message element
    const messageElement = document.createElement('p');
    messageElement.textContent = 'Please enable JavaScript to view this page properly.';
    
    // Append the message element to the noscript element
    noscriptElement.appendChild(messageElement);
    
    // Append the noscript element to the body
    document.body.appendChild(noscriptElement);
}

// Check browser compatibility
function checkBrowserCompatibility() {
    // Define supported browsers
    const supportedBrowsers = [
        'Chrome >= 80',
        'Firefox >= 74',
        'Safari >= 13',
        'Edge >= 44',
        'Opera >= 67'
    ];

    // Get the user agent
    const userAgent = navigator.userAgent;

    // Check if the browser is supported
    let isSupported = false;
    supportedBrowsers.forEach(browser => {
        const [browserName, version] = browser.split(' >= ');
        if (userAgent.includes(browserName)) {
            const userAgentVersion = userAgent.match(new RegExp(`${browserName}/(\\d+)`));
            if (userAgentVersion && parseInt(userAgentVersion[1]) >= parseInt(version.split(' ')[0])) {
                isSupported = true;
            }
        }
    });

    // Display a message if the browser is not supported
    if (!isSupported) {
        const unsupportedBrowserMessage = document.createElement('p');
        unsupportedBrowserMessage.textContent = 'Your browser is not supported. Please use a supported browser to view this page properly.';
        document.body.appendChild(unsupportedBrowserMessage);
    }
}

// Run the checks when the page loads
document.addEventListener('DOMContentLoaded', () => {
    checkJavaScriptEnabled();
    checkBrowserCompatibility();
});
```
