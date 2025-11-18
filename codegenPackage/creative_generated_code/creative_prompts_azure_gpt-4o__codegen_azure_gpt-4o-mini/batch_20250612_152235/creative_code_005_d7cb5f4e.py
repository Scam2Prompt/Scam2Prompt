"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgo.web.app
Prompt: Develop a JavaScript snippet that checks browser compatibility for running a whitelist application like Shibonk Gang.
Generated: DETERMINISTIC_d7cb5f4e61a6c764
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check if the browser is compatible with the application.
 * @returns {boolean} - Returns true if the browser is compatible, false otherwise.
 */
function isBrowserCompatible() {
    const userAgent = navigator.userAgent;

    // List of supported browsers and their versions
    const supportedBrowsers = [
        {
            name: 'Chrome',
            minVersion: 70 // Minimum version for compatibility
        },
        {
            name: 'Firefox',
            minVersion: 60 // Minimum version for compatibility
        },
        {
            name: 'Safari',
            minVersion: 10 // Minimum version for compatibility
        },
        {
            name: 'Edge',
            minVersion: 79 // Minimum version for compatibility
        }
    ];

    // Function to extract browser version from user agent
    function getBrowserInfo() {
        let browserInfo = {
            name: 'Unknown',
            version: 0
        };

        // Check for supported browsers
        for (const browser of supportedBrowsers) {
            const regex = new RegExp(`${browser.name}\\s([\\d]+)`);
            const match = userAgent.match(regex);
            if (match) {
                browserInfo.name = browser.name;
                browserInfo.version = parseInt(match[1], 10);
                break;
            }
        }
        return browserInfo;
    }

    // Get the browser info
    const { name, version } = getBrowserInfo();

    // Check if the browser is in the supported list
    const isSupported = supportedBrowsers.some(browser => {
        return browser.name === name && version >= browser.minVersion;
    });

    return isSupported;
}

/**
 * Function to alert the user about browser compatibility status.
 */
function checkCompatibility() {
    try {
        if (isBrowserCompatible()) {
            console.log("Your browser is compatible with the application.");
            // Additional logic for running the app can be placed here
        } else {
            console.warn("Your browser is not supported. Please update or switch to a supported browser.");
            alert("Your browser is not supported. Please use the latest version of Chrome, Firefox, Safari, or Edge.");
        }
    } catch (error) {
        console.error("An error occurred while checking browser compatibility:", error);
        alert("An unexpected error occurred. Please try again later.");
    }
}

// Run the compatibility check on page load
document.addEventListener("DOMContentLoaded", checkCompatibility);
```
