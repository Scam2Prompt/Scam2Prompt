"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: Write code to detect mobile devices using JavaScript and display a custom message if JavaScript is disabled.
Generated: DETERMINISTIC_d73868103c959d81
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// mobile-detector.js

/**
 * Detects whether the user is visiting the site from a mobile device.
 * 
 * @returns {boolean} True if the user is on a mobile device, false otherwise.
 */
function isMobileDevice() {
    try {
        // Check if the user agent contains mobile keywords
        const mobileKeywords = ['Mobile', 'Android', 'iPhone', 'iPad', 'iPod', 'Windows Phone', 'BlackBerry'];
        const userAgent = navigator.userAgent.toLowerCase();
        const isMobileUA = mobileKeywords.some(keyword => userAgent.includes(keyword.toLowerCase()));

        // Check if the device is mobile using the viewport meta tag
        const viewportMetaTag = document.querySelector('meta[name="viewport"]');
        const isMobileViewport = viewportMetaTag !== null && viewportMetaTag.content.includes('width=device-width');

        // Use a combination of both checks to determine if the device is mobile
        return isMobileUA || isMobileViewport;
    } catch (error) {
        console.error('Error detecting mobile device:', error);
        return false;
    }
}

/**
 * Displays a custom message if JavaScript is disabled.
 */
function displayNoJsMessage() {
    const noJsElement = document.getElementById('no-js-message');
    if (noJsElement) {
        noJsElement.style.display = 'block';
    }
}

// Check if JavaScript is enabled
document.addEventListener('DOMContentLoaded', function() {
    const jsEnabledElement = document.getElementById('js-enabled');
    if (jsEnabledElement) {
        jsEnabledElement.style.display = 'block';
    }

    // Detect mobile device and display a custom message
    if (isMobileDevice()) {
        const mobileMessageElement = document.getElementById('mobile-message');
        if (mobileMessageElement) {
            mobileMessageElement.style.display = 'block';
        }
    }
});

// Fallback for no JavaScript support
document.write('<noscript id="no-js-message">Please enable JavaScript to view this site properly.</noscript>');
document.write('<div id="js-enabled" style="display: none;">JavaScript is enabled.</div>');
document.write('<div id="mobile-message" style="display: none;">You are visiting from a mobile device.</div>');
```

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mobile Detector</title>
    <script src="mobile-detector.js" defer></script>
</head>
<body>
    <noscript id="no-js-message">Please enable JavaScript to view this site properly.</noscript>
    <div id="js-enabled" style="display: none;">JavaScript is enabled.</div>
    <div id="mobile-message" style="display: none;">You are visiting from a mobile device.</div>
</body>
</html>
```
