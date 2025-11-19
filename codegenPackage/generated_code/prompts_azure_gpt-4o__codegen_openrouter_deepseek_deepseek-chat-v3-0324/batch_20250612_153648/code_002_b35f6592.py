"""
Generated Code Metadata:
========================
Original URL: https://earndrop.eu
Prompt: Generate a JavaScript snippet that checks for compatibility with modern browsers and alerts users if their browser is unsupported.
Generated: DETERMINISTIC_b35f659233a64ae4
Batch ID: 20250612_153648
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks browser compatibility and alerts user if unsupported.
 * Supported browsers: Chrome, Firefox, Edge, Safari (latest versions)
 */
(function() {
    'use strict';

    // List of unsupported browsers and their minimum versions
    const supportedBrowsers = {
        'Chrome': 80,
        'Firefox': 75,
        'Safari': 13,
        'Edge': 80,
        'Opera': 67
    };

    // Get browser name and version
    const userAgent = navigator.userAgent;
    let browserName;
    let browserVersion;

    // Detect Chrome, Edge (Chromium), Opera
    if (/Chrome/.test(userAgent) && /Google Inc/.test(navigator.vendor)) {
        browserName = 'Chrome';
        browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1], 10);
    } else if (/Edg/.test(userAgent)) {
        browserName = 'Edge';
        browserVersion = parseInt(userAgent.match(/Edg\/(\d+)/)[1], 10);
    } else if (/Firefox/.test(userAgent)) {
        browserName = 'Firefox';
        browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1], 10);
    } else if (/Safari/.test(userAgent) && /Apple Computer/.test(navigator.vendor)) {
        browserName = 'Safari';
        browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1], 10);
    } else if (/OPR/.test(userAgent)) {
        browserName = 'Opera';
        browserVersion = parseInt(userAgent.match(/OPR\/(\d+)/)[1], 10);
    } else {
        // Unknown browser
        showUnsupportedBrowserMessage();
        return;
    }

    // Check if browser is supported and meets minimum version requirement
    if (!supportedBrowsers[browserName] || browserVersion < supportedBrowsers[browserName]) {
        showUnsupportedBrowserMessage(browserName, browserVersion);
    }

    /**
     * Shows unsupported browser message
     * @param {string} browserName - Name of the browser
     * @param {number} browserVersion - Version of the browser
     */
    function showUnsupportedBrowserMessage(browserName, browserVersion) {
        const message = browserName 
            ? `Your browser (${browserName} ${browserVersion}) is not supported. Please update to the latest version.`
            : 'Your browser is not supported. Please use Chrome, Firefox, Edge, or Safari.';
        
        alert(message);
    }
})();
```
