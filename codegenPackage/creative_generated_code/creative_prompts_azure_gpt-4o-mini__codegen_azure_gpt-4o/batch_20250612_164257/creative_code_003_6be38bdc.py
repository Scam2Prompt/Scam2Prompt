"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stewartpayroll.com
Prompt: Generate a script that checks for browser compatibility when accessing the Paylocity login page, based on the supported browsers listed.
Generated: DETERMINISTIC_6be38bdce4d1b5d9
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Browser Compatibility Checker for Paylocity Login Page
 *
 * Supported Browsers:
 * - Google Chrome (Version 90+)
 * - Mozilla Firefox (Version 88+)
 * - Microsoft Edge (Version 90+)
 * - Safari (Version 14+)
 *
 * This script checks if the user's browser meets the compatibility requirements 
 * to access the Paylocity login page.
 */

(function () {
  // Supported browser information
  const supportedBrowsers = [
    { name: 'Chrome', minVersion: 90 },
    { name: 'Firefox', minVersion: 88 },
    { name: 'Edge', minVersion: 90 },
    { name: 'Safari', minVersion: 14 },
  ];

  /**
   * Extracts browser name and version from the user agent string
   * @returns {Object} An object containing the browser name and version
   */
  function getBrowserInfo() {
    const userAgent = navigator.userAgent;
    let browserName = 'Unknown';
    let browserVersion = 0;

    // Detect Chrome
    if (userAgent.includes('Chrome') && !userAgent.includes('Edge')) {
      browserName = 'Chrome';
      browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1], 10);
    }
    // Detect Firefox
    else if (userAgent.includes('Firefox')) {
      browserName = 'Firefox';
      browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1], 10);
    }
    // Detect Edge
    else if (userAgent.includes('Edg')) {
      browserName = 'Edge';
      browserVersion = parseInt(userAgent.match(/Edg\/(\d+)/)[1], 10);
    }
    // Detect Safari
    else if (userAgent.includes('Safari') && !userAgent.includes('Chrome')) {
      browserName = 'Safari';
      browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1], 10);
    }

    return { browserName, browserVersion };
  }

  /**
   * Checks if the current browser is supported
   * @param {Array} supportedBrowsers - List of supported browsers with minimum versions
   * @param {Object} currentBrowser - The browser name and version of the user
   * @returns {Boolean} True if the browser is supported, false otherwise
   */
  function isBrowserCompatible(supportedBrowsers, currentBrowser) {
    for (const browser of supportedBrowsers) {
      if (
        browser.name === currentBrowser.browserName &&
        currentBrowser.browserVersion >= browser.minVersion
      ) {
        return true;
      }
    }
    return false;
  }

  // Get user's browser information
  const userBrowser = getBrowserInfo();

  // Check compatibility
  const isCompatible = isBrowserCompatible(supportedBrowsers, userBrowser);

  // Notify the user
  if (isCompatible) {
    console.log(
      `Your browser (${userBrowser.browserName} v${userBrowser.browserVersion}) is compatible with the Paylocity login page.`
    );
  } else {
    alert(
      `Your browser (${userBrowser.browserName} v${userBrowser.browserVersion}) is not supported.\nPlease use one of the following browsers:\n` +
        supportedBrowsers
          .map(
            (browser) =>
              `${browser.name} (version ${browser.minVersion}+ required)`
          )
          .join('\n')
    );
  }
})();
```
