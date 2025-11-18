"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wt.menara-capital.net
Prompt: Generate JavaScript code to detect browser compatibility for a trading application and prompt the user to enable JavaScript if it is disabled.
Generated: DETERMINISTIC_88b17fbb0634625d
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * @fileoverview Browser Compatibility Script for Trading Application
 * This script checks browser compatibility and ensures JavaScript is enabled.
 * If JavaScript is disabled, it prompts the user to enable it.
 */

/**
 * Detects browser compatibility and JavaScript status.
 * Alerts the user if requirements are not met.
 */
(function () {
    "use strict";

    // Define minimal browser requirements
    const MIN_BROWSER_REQUIREMENTS = {
        chrome: 80,
        firefox: 75,
        edge: 80,
        safari: 13
    };

    /**
     * Gets browser information using userAgent string.
     * @returns {object} Browser name and version.
     */
    function getBrowserInfo() {
        const userAgent = navigator.userAgent;
        let browserName = "unknown";
        let browserVersion = "unknown";

        if (userAgent.includes("Chrome") && !userAgent.includes("Edg")) {
            browserName = "chrome";
            browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1], 10);
        } else if (userAgent.includes("Firefox")) {
            browserName = "firefox";
            browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1], 10);
        } else if (userAgent.includes("Edg")) {
            browserName = "edge";
            browserVersion = parseInt(userAgent.match(/Edg\/(\d+)/)[1], 10);
        } else if (userAgent.includes("Safari") && !userAgent.includes("Chrome")) {
            browserName = "safari";
            browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1], 10);
        }

        return { browserName, browserVersion };
    }

    /**
     * Checks if the browser meets minimum requirements.
     * @param {object} browserInfo - Browser name and version.
     * @returns {boolean} True if compatible, false otherwise.
     */
    function isBrowserCompatible(browserInfo) {
        const { browserName, browserVersion } = browserInfo;

        if (
            MIN_BROWSER_REQUIREMENTS[browserName] &&
            browserVersion >= MIN_BROWSER_REQUIREMENTS[browserName]
        ) {
            return true;
        }
        return false;
    }

    /**
     * Handles the case where JavaScript is disabled.
     * This function is primarily for fallback in static HTML content.
     */
    function handleJavaScriptDisabled() {
        const noJsElement = document.getElementById("no-js-warning");
        if (noJsElement) {
            noJsElement.style.display = "block"; // Show warning if applicable
        }
    }

    // Main script execution
    document.addEventListener("DOMContentLoaded", function () {
        try {
            // Check JS status (if this script runs, JS is enabled)
            handleJavaScriptDisabled();

            // Get browser info
            const browserInfo = getBrowserInfo();

            // Check compatibility
            if (!isBrowserCompatible(browserInfo)) {
                alert(
                    "Your browser is not compatible with this trading application. " +
                        "Please update to the latest version of Chrome, Firefox, Edge, or Safari."
                );
            }
        } catch (error) {
            console.error("An error occurred while checking browser compatibility:", error);
        }
    });
})();

/*
 * Note: Include the following fallback HTML in your page for users with JavaScript disabled:
 * <noscript>
 *   <div id="no-js-warning" style="display: none; color: red;">
 *     JavaScript is disabled in your browser. Please enable JavaScript to use the trading application.
 *   </div>
 * </noscript>
 */
```
