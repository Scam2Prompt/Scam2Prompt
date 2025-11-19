"""
Generated Code Metadata:
========================
Original URL: https://getbonus.eu
Prompt: Create a JavaScript snippet that checks for browser compatibility and ensures proper functionality of a web app, referencing the behavior of the GetBonus platform.
Generated: DETERMINISTIC_304c6e752ef82b2b
Batch ID: 20250612_154703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Browser Compatibility Checker
 * Ensures the web app functions properly across different browsers by checking for required features.
 * Inspired by the behavior of the GetBonus platform.
 */

// List of required features for the web app to function properly
const REQUIRED_FEATURES = {
    fetch: typeof window.fetch === 'function',
    promises: typeof Promise !== 'undefined',
    localStorage: typeof window.localStorage !== 'undefined',
    sessionStorage: typeof window.sessionStorage !== 'undefined',
    serviceWorker: 'serviceWorker' in navigator,
    webWorker: typeof Worker !== 'undefined',
    crypto: window.crypto && typeof window.crypto.subtle !== 'undefined'
};

// Minimum supported browser versions
const MIN_BROWSER_VERSIONS = {
    chrome: 60,
    firefox: 55,
    safari: 11,
    edge: 15,
    opera: 47,
    ie: false // Not supported
};

/**
 * Checks if the current browser is compatible with the web app
 * @returns {Object} { isCompatible: boolean, missingFeatures: string[], unsupportedBrowser: boolean }
 */
function checkBrowserCompatibility() {
    const missingFeatures = [];
    let unsupportedBrowser = false;

    // Check for missing features
    for (const [feature, isSupported] of Object.entries(REQUIRED_FEATURES)) {
        if (!isSupported) {
            missingFeatures.push(feature);
        }
    }

    // Detect browser and version
    const userAgent = navigator.userAgent;
    let browserName;
    let browserVersion;

    // Chrome, Edge, Opera
    if (userAgent.includes('Chrome') && !userAgent.includes('Edge')) {
        browserName = 'chrome';
        browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1], 10);
    } else if (userAgent.includes('Firefox')) {
        browserName = 'firefox';
        browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1], 10);
    } else if (userAgent.includes('Safari') && !userAgent.includes('Chrome')) {
        browserName = 'safari';
        browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1], 10);
    } else if (userAgent.includes('Edge')) {
        browserName = 'edge';
        browserVersion = parseInt(userAgent.match(/Edge\/(\d+)/)[1], 10);
    } else if (userAgent.includes('Opera') || userAgent.includes('OPR')) {
        browserName = 'opera';
        browserVersion = parseInt(userAgent.match(/(?:Opera|OPR)\/(\d+)/)[1], 10);
    } else if (userAgent.includes('Trident')) {
        browserName = 'ie';
        unsupportedBrowser = true;
    }

    // Check if browser version is supported
    if (browserName && MIN_BROWSER_VERSIONS[browserName] !== false) {
        if (browserVersion < MIN_BROWSER_VERSIONS[browserName]) {
            unsupportedBrowser = true;
        }
    }

    return {
        isCompatible: missingFeatures.length === 0 && !unsupportedBrowser,
        missingFeatures,
        unsupportedBrowser
    };
}

/**
 * Handles incompatible browsers by showing an error message or fallback
 * @param {Object} compatibilityResult - Result from checkBrowserCompatibility()
 */
function handleIncompatibleBrowser(compatibilityResult) {
    if (!compatibilityResult.isCompatible) {
        const errorContainer = document.createElement('div');
        errorContainer.style.position = 'fixed';
        errorContainer.style.top = '0';
        errorContainer.style.left = '0';
        errorContainer.style.width = '100%';
        errorContainer.style.padding = '20px';
        errorContainer.style.backgroundColor = '#ffebee';
        errorContainer.style.color = '#b71c1c';
        errorContainer.style.zIndex = '10000';
        errorContainer.style.textAlign = 'center';

        let errorMessage = 'Your browser is not fully compatible with this application. ';

        if (compatibilityResult.unsupportedBrowser) {
            errorMessage += 'Please update your browser or use a modern browser like Chrome, Firefox, or Edge.';
        } else if (compatibilityResult.missingFeatures.length > 0) {
            errorMessage += `Missing features: ${compatibilityResult.missingFeatures.join(', ')}. `;
            errorMessage += 'Please update your browser to the latest version.';
        }

        errorContainer.textContent = errorMessage;
        document.body.prepend(errorContainer);

        // Optionally, disable certain functionality
        if (!REQUIRED_FEATURES.serviceWorker) {
            console.warn('Service workers not available - offline functionality disabled');
        }
    }
}

// Initialize compatibility check when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    const compatibility = checkBrowserCompatibility();
    handleIncompatibleBrowser(compatibility);

    // Log compatibility status for debugging
    console.log('Browser Compatibility:', compatibility);
});

// Export for module systems if needed
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        checkBrowserCompatibility,
        handleIncompatibleBrowser
    };
}
```
