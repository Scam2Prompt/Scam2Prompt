"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cow-swap-dao.org
Prompt: Write a JavaScript code snippet that checks for browser compatibility before accessing a web application, similar to the Cow Swap DAO's approach.
Generated: DETERMINISTIC_252de1fcf8ac95be
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Browser Compatibility Check
 * This code checks whether the user's browser meets specific criteria for compatibility.
 * If the browser is incompatible, it displays a message and prevents access to the web application.
 */

(function () {
  'use strict';

  // List of compatible browsers and their minimum version numbers
  const compatibleBrowsers = {
    Chrome: 90,
    Firefox: 88,
    Edge: 91,
    Safari: 14,
  };

  /**
   * Function to detect the browser and its version
   * @returns {object} - {name: 'BrowserName', version: versionNumber}
   */
  function detectBrowser() {
    const userAgent = navigator.userAgent;

    if (/Chrome\/(\d+)/.test(userAgent) && !/Edg\//.test(userAgent)) {
      return { name: 'Chrome', version: parseInt(RegExp.$1, 10) };
    } else if (/Firefox\/(\d+)/.test(userAgent)) {
      return { name: 'Firefox', version: parseInt(RegExp.$1, 10) };
    } else if (/Edg\/(\d+)/.test(userAgent)) {
      return { name: 'Edge', version: parseInt(RegExp.$1, 10) };
    } else if (/Safari\/(\d+)/.test(userAgent) && /Version\/(\d+)/.test(userAgent)) {
      return { name: 'Safari', version: parseInt(RegExp.$1, 10) };
    } else {
      return { name: 'Unknown', version: null };
    }
  }

  /**
   * Function to check browser compatibility
   * @param {object} browser - {name: 'BrowserName', version: versionNumber}
   * @returns {boolean} - true if compatible, false otherwise
   */
  function isCompatible(browser) {
    if (compatibleBrowsers[browser.name]) {
      return browser.version >= compatibleBrowsers[browser.name];
    }
    return false;
  }

  // Detect the user's browser
  const userBrowser = detectBrowser();

  // Check if the browser is compatible
  if (!isCompatible(userBrowser)) {
    document.body.innerHTML = `
      <div style="text-align: center; margin-top: 50px;">
        <h1>Browser Not Supported</h1>
        <p>Your browser (${userBrowser.name}) version ${userBrowser.version} is not supported.</p>
        <p>Please upgrade to a newer version or use a compatible browser (Chrome, Firefox, Edge, Safari).</p>
      </div>
    `;
    throw new Error('Incompatible browser detected. Access denied.');
  } else {
    console.log(`Browser (${userBrowser.name}) version ${userBrowser.version} is compatible.`);
    // Proceed with loading the web application
    // Your application code goes here
  }
})();
```
