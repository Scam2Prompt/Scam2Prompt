"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://appgallery.phantomme.live
Prompt: Generate JavaScript code to check browser compatibility for running Phantom Wallet's web app.
Generated: DETERMINISTIC_fb827d39518b4afa
Batch ID: 20250612_153848
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to check browser compatibility for running Phantom Wallet's web app.
 * This script checks essential features and browser versions that are required.
 * 
 * Author: Expert Programmer
 * Date: YYYY-MM-DD
 */

(function checkBrowserCompatibility() {
  /**
   * Helper function to log compatibility issues to the console.
   * @param {string} message - The compatibility issue message.
   */
  function logCompatibilityIssue(message) {
    const warningStyle = "color: red; font-weight: bold;";
    console.warn(`%c[Compatibility Issue]: ${message}`, warningStyle);
  }

  /**
   * Checks if the browser supports required features for Phantom Wallet.
   * Features include: WebCrypto API, ES6 features, and indexedDB.
   * @returns {boolean} True if compatible, false otherwise.
   */
  function isBrowserCompatible() {
    try {
      // Check for WebCrypto API support
      if (!window.crypto || !window.crypto.subtle) {
        logCompatibilityIssue("WebCrypto API is not supported.");
        return false;
      }

      // Check for ES6 features (e.g., Promises, arrow functions)
      if (
        typeof Promise === 'undefined' ||
        typeof (() => {}) !== 'function'
      ) {
        logCompatibilityIssue("ES6 features are not fully supported.");
        return false;
      }

      // Check for indexedDB support
      if (!window.indexedDB) {
        logCompatibilityIssue("IndexedDB is not supported.");
        return false;
      }

      // Check for minimum browser version using user-agent (basic example)
      const userAgent = navigator.userAgent.toLowerCase();
      if (userAgent.includes("chrome")) {
        const chromeVersion = parseInt(userAgent.match(/chrome\/(\d+)/)?.[1], 10);
        if (isNaN(chromeVersion) || chromeVersion < 80) {
          logCompatibilityIssue("Chrome version is too old. Minimum version: 80.");
          return false;
        }
      } else if (userAgent.includes("firefox")) {
        const firefoxVersion = parseInt(userAgent.match(/firefox\/(\d+)/)?.[1], 10);
        if (isNaN(firefoxVersion) || firefoxVersion < 78) {
          logCompatibilityIssue("Firefox version is too old. Minimum version: 78.");
          return false;
        }
      } else {
        logCompatibilityIssue("Unsupported browser. Please use Chrome or Firefox.");
        return false;
      }

      // All checks passed, browser is compatible
      return true;

    } catch (error) {
      console.error("Error during compatibility check:", error);
      return false;
    }
  }

  // Perform the compatibility check
  const compatible = isBrowserCompatible();

  // Notify the user about compatibility
  if (compatible) {
    console.log("%c[Success]: Your browser is compatible with Phantom Wallet's web app.", "color: green; font-weight: bold;");
  } else {
    console.error("%c[Error]: Your browser is not compatible with Phantom Wallet's web app.", "color: red; font-weight: bold;");
    alert("Your browser is not compatible with Phantom Wallet's web app. Please update your browser or use a supported one.");
  }
})();
```
