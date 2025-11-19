"""
Generated Code Metadata:
========================
Original URL: https://stewartpayroll.com
Prompt: Generate a script that checks for browser compatibility when accessing the Paylocity login page, based on the supported browsers listed.
Generated: DETERMINISTIC_6be38bdce4d1b5d9
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Browser Compatibility Checker for Paylocity Login Page
 * Supported Browsers: Google Chrome (latest 3 versions), Mozilla Firefox (latest 3 versions),
 * Microsoft Edge (latest 3 versions), Safari (latest 3 versions).
 */

// Function to detect browser and version
function getBrowserInfo() {
    const userAgent = navigator.userAgent;
    let browserName = "Unknown";
    let browserVersion = "Unknown";

    if (userAgent.includes("Chrome") && !userAgent.includes("Edg")) {
        browserName = "Chrome";
        browserVersion = userAgent.match(/Chrome\/(\d+)/)[1];
    } else if (userAgent.includes("Firefox")) {
        browserName = "Firefox";
        browserVersion = userAgent.match(/Firefox\/(\d+)/)[1];
    } else if (userAgent.includes("Edg")) {
        browserName = "Edge";
        browserVersion = userAgent.match(/Edg\/(\d+)/)[1];
    } else if (userAgent.includes("Safari") && !userAgent.includes("Chrome")) {
        browserName = "Safari";
        browserVersion = userAgent.match(/Version\/(\d+)/)[1];
    }

    return { browserName, browserVersion: parseInt(browserVersion, 10) };
}

// Function to check compatibility
function isBrowserCompatible(browserInfo) {
    const supportedBrowsers = {
        Chrome: 3, // Latest 3 versions
        Firefox: 3, // Latest 3 versions
        Edge: 3, // Latest 3 versions
        Safari: 3, // Latest 3 versions
    };

    const { browserName, browserVersion } = browserInfo;

    if (supportedBrowsers[browserName]) {
        const latestVersion = getLatestBrowserVersion(browserName);
        return browserVersion >= latestVersion - supportedBrowsers[browserName] + 1;
    }

    return false; // Unsupported browser
}

// Mock function to get the latest browser version (in production, use an API or database)
function getLatestBrowserVersion(browserName) {
    const latestVersions = {
        Chrome: 117, // Example latest version
        Firefox: 118, // Example latest version
        Edge: 116, // Example latest version
        Safari: 16, // Example latest version
    };

    return latestVersions[browserName] || 0;
}

// Main function to check browser compatibility and display a message
function checkBrowserCompatibility() {
    const browserInfo = getBrowserInfo();
    const compatible = isBrowserCompatible(browserInfo);

    if (compatible) {
        alert(`Your browser (${browserInfo.browserName} v${browserInfo.browserVersion}) is compatible.`);
    } else {
        alert(
            `Your browser (${browserInfo.browserName} v${browserInfo.browserVersion}) is not compatible. ` +
            `Please use one of the latest 3 versions of Chrome, Firefox, Edge, or Safari.`
        );
    }
}

// Run the compatibility check when the page loads
window.onload = checkBrowserCompatibility;
```
