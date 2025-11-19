"""
Generated Code Metadata:
========================
Original URL: https://cow-swap-dao.org
Prompt: Write a JavaScript code snippet that checks for browser compatibility before accessing a web application, similar to the Cow Swap DAO's approach.
Generated: DETERMINISTIC_252de1fcf8ac95be
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// browserCompatibility.js

/**
 * Checks if the user's browser is compatible with the web application.
 * 
 * @param {object} supportedBrowsers - An object containing the supported browsers and their minimum versions.
 * @returns {boolean} True if the browser is compatible, false otherwise.
 */
function isBrowserCompatible(supportedBrowsers) {
    try {
        // Get the user's browser information
        const userAgent = navigator.userAgent;
        const browser = getBrowser(userAgent);
        const version = getBrowserVersion(userAgent);

        // Check if the browser is supported
        if (!supportedBrowsers[browser]) {
            console.error(`Browser ${browser} is not supported`);
            return false;
        }

        // Check if the browser version is supported
        if (compareVersions(version, supportedBrowsers[browser]) < 0) {
            console.error(`Browser ${browser} version ${version} is not supported. Minimum version ${supportedBrowsers[browser]} required`);
            return false;
        }

        return true;
    } catch (error) {
        console.error('Error checking browser compatibility:', error);
        return false;
    }
}

/**
 * Extracts the browser type from the user agent string.
 * 
 * @param {string} userAgent - The user agent string.
 * @returns {string} The browser type (e.g. Chrome, Firefox, Safari, etc.).
 */
function getBrowser(userAgent) {
    const browserRegex = {
        Chrome: /Chrome/i,
        Firefox: /Firefox/i,
        Safari: /Safari/i,
        Edge: /Edge/i,
        IE: /MSIE|Trident/i,
    };

    for (const browser in browserRegex) {
        if (browserRegex[browser].test(userAgent)) {
            return browser;
        }
    }

    return null;
}

/**
 * Extracts the browser version from the user agent string.
 * 
 * @param {string} userAgent - The user agent string.
 * @returns {string} The browser version.
 */
function getBrowserVersion(userAgent) {
    const versionRegex = {
        Chrome: /Chrome\/(\d+\.\d+\.\d+)/i,
        Firefox: /Firefox\/(\d+\.\d+)/i,
        Safari: /Version\/(\d+\.\d+)/i,
        Edge: /Edge\/(\d+\.\d+)/i,
        IE: /MSIE (\d+\.\d+)/i,
    };

    for (const browser in versionRegex) {
        const match = userAgent.match(versionRegex[browser]);
        if (match) {
            return match[1];
        }
    }

    return null;
}

/**
 * Compares two version strings.
 * 
 * @param {string} version1 - The first version string.
 * @param {string} version2 - The second version string.
 * @returns {number} A negative number if version1 is less than version2, a positive number if version1 is greater than version2, and 0 if they are equal.
 */
function compareVersions(version1, version2) {
    const version1Parts = version1.split('.').map(Number);
    const version2Parts = version2.split('.').map(Number);

    for (let i = 0; i < Math.max(version1Parts.length, version2Parts.length); i++) {
        const part1 = version1Parts[i] || 0;
        const part2 = version2Parts[i] || 0;

        if (part1 < part2) {
            return -1;
        } else if (part1 > part2) {
            return 1;
        }
    }

    return 0;
}

// Example usage:
const supportedBrowsers = {
    Chrome: '90.0.4430.212',
    Firefox: '88.0',
    Safari: '14.2',
    Edge: '90.0.818.66',
};

if (!isBrowserCompatible(supportedBrowsers)) {
    alert('Your browser is not compatible with this web application.');
}
```
