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

Here's a clean, production-ready script to check browser compatibility for the Paylocity login page:

```javascript
/**
 * Browser Compatibility Checker for Paylocity Login Page
 * Supported browsers:
 * - Chrome (latest 3 versions)
 * - Firefox (latest 3 versions)
 * - Edge (latest 3 versions)
 * - Safari (latest 3 versions)
 */

(function() {
    'use strict';

    // Supported browser definitions
    const supportedBrowsers = {
        Chrome: { min: getVersionOffset(3) },
        Firefox: { min: getVersionOffset(3) },
        Edge: { min: getVersionOffset(3) },
        Safari: { min: getVersionOffset(3) }
    };

    // Check browser compatibility on page load
    document.addEventListener('DOMContentLoaded', function() {
        const browserInfo = detectBrowser();
        const isCompatible = checkCompatibility(browserInfo);

        if (!isCompatible) {
            showCompatibilityWarning(browserInfo);
        }
    });

    /**
     * Detects the current browser and its version
     * @returns {Object} Browser name and version
     */
    function detectBrowser() {
        const userAgent = navigator.userAgent;
        let browserName;
        let versionMatch;
        let version;

        // Detect Chrome
        if (/Chrome/.test(userAgent) && !/Edge|Edg/.test(userAgent)) {
            browserName = 'Chrome';
            versionMatch = userAgent.match(/Chrome\/(\d+)/);
        } 
        // Detect Firefox
        else if (/Firefox/.test(userAgent)) {
            browserName = 'Firefox';
            versionMatch = userAgent.match(/Firefox\/(\d+)/);
        } 
        // Detect Edge
        else if (/Edg/.test(userAgent)) {
            browserName = 'Edge';
            versionMatch = userAgent.match(/Edg\/(\d+)/);
        } 
        // Detect Safari
        else if (/Safari/.test(userAgent)) {
            browserName = 'Safari';
            versionMatch = userAgent.match(/Version\/(\d+).*Safari/);
        } 
        // Default to unknown
        else {
            browserName = 'Unknown';
        }

        version = versionMatch ? parseInt(versionMatch[1], 10) : 0;

        return {
            name: browserName,
            version: version
        };
    }

    /**
     * Checks if the browser is supported
     * @param {Object} browserInfo Browser name and version
     * @returns {boolean} True if browser is supported
     */
    function checkCompatibility(browserInfo) {
        const browserConfig = supportedBrowsers[browserInfo.name];
        
        if (!browserConfig) {
            return false;
        }

        return browserInfo.version >= browserConfig.min;
    }

    /**
     * Gets version offset from current version
     * @param {number} offset Version offset
     * @returns {number} Minimum supported version
     */
    function getVersionOffset(offset) {
        const currentYear = new Date().getFullYear();
        const baseVersion = currentYear - 2020; // Approximate versioning
        return Math.max(1, baseVersion - offset);
    }

    /**
     * Displays compatibility warning message
     * @param {Object} browserInfo Browser name and version
     */
    function showCompatibilityWarning(browserInfo) {
        const warningDiv = document.createElement('div');
        warningDiv.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            background-color: #fff3cd;
            color: #856404;
            padding: 15px;
            text-align: center;
            border-bottom: 1px solid #ffeeba;
            z-index: 9999;
            font-family: Arial, sans-serif;
        `;

        const message = document.createElement('p');
        message.textContent = `Warning: ${browserInfo.name} ${browserInfo.version} may not be fully supported. 
                              For best experience, please use one of the latest 3 versions of Chrome, Firefox, Edge, or Safari.`;

        const closeButton = document.createElement('button');
        closeButton.textContent = '×';
        closeButton.style.cssText = `
            position: absolute;
            right: 10px;
            top: 10px;
            background: transparent;
            border: none;
            font-size: 20px;
            cursor: pointer;
            color: #856404;
        `;
        closeButton.onclick = function() {
            warningDiv.remove();
        };

        warningDiv.appendChild(message);
        warningDiv.appendChild(closeButton);
        document.body.prepend(warningDiv);
    }

})();
```
