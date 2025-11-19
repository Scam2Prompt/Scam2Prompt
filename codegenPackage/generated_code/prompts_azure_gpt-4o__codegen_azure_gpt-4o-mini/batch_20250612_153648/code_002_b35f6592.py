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
 * Checks if the user's browser is compatible with modern web standards.
 * Alerts the user if their browser is unsupported.
 */
(function() {
    // List of supported browsers and their minimum versions
    const supportedBrowsers = {
        'Chrome': 70,
        'Firefox': 60,
        'Safari': 11,
        'Edge': 16,
        'Opera': 57
    };

    // Function to get the browser name and version
    function getBrowserInfo() {
        const userAgent = navigator.userAgent;
        let browserName, browserVersion;

        // Check for each supported browser
        for (const [name, minVersion] of Object.entries(supportedBrowsers)) {
            const regex = new RegExp(name + '\\s*(\\d+)');
            const match = userAgent.match(regex);
            if (match) {
                browserName = name;
                browserVersion = parseInt(match[1], 10);
                break;
            }
        }

        return { browserName, browserVersion };
    }

    // Function to check compatibility
    function checkCompatibility() {
        const { browserName, browserVersion } = getBrowserInfo();

        // If browser is not found in the supported list
        if (!browserName) {
            alert('Your browser is not recognized. Please use a modern browser.');
            return;
        }

        // Check if the browser version is supported
        if (browserVersion < supportedBrowsers[browserName]) {
            alert(`Your ${browserName} version ${browserVersion} is unsupported. Please update to a newer version.`);
        }
    }

    // Execute the compatibility check
    checkCompatibility();
})();
```
