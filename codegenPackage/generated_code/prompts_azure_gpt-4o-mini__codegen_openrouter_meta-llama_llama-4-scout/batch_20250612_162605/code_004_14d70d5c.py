"""
Generated Code Metadata:
========================
Original URL: https://arbitrurnbridge.net
Prompt: Generate a code example that handles browser checks before loading a web application.
Generated: DETERMINISTIC_14d70d5c177d14b1
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// browser-check.js

/**
 * Browser check utility.
 * 
 * This module provides functionality to check if the user's browser meets the minimum requirements
 * for the web application.
 */

// Define the minimum supported browser versions
const MIN_SUPPORTED_BROWSERS = {
  chrome: 80,
  firefox: 75,
  edge: 44,
  safari: 13,
  opera: 67,
};

/**
 * Get the browser name and version from the user agent string.
 * 
 * @param {string} userAgent - The user agent string.
 * @returns {object} - An object containing the browser name and version.
 */
function getBrowserInfo(userAgent) {
  const browserRegex = /(chrome|firefox|edge|safari|opera)/i;
  const match = userAgent.match(browserRegex);
  if (!match) {
    throw new Error('Unable to detect browser');
  }

  const browserName = match[0].toLowerCase();
  const versionRegex = /(chrome|firefox|edge|safari|opera)\/([0-9.]+)/i;
  const versionMatch = userAgent.match(versionRegex);
  if (!versionMatch) {
    throw new Error('Unable to detect browser version');
  }

  const browserVersion = parseFloat(versionMatch[2]);
  return { browserName, browserVersion };
}

/**
 * Check if the user's browser meets the minimum requirements.
 * 
 * @param {string} userAgent - The user agent string.
 * @returns {boolean} - True if the browser is supported, false otherwise.
 */
function isBrowserSupported(userAgent) {
  try {
    const { browserName, browserVersion } = getBrowserInfo(userAgent);
    const minVersion = MIN_SUPPORTED_BROWSERS[browserName];
    if (!minVersion) {
      // If the browser is not in the list of supported browsers, return false
      return false;
    }

    return browserVersion >= minVersion;
  } catch (error) {
    // If there's an error parsing the user agent string, assume the browser is not supported
    return false;
  }
}

// Example usage
function main() {
  const userAgent = navigator.userAgent;
  if (!isBrowserSupported(userAgent)) {
    const unsupportedBrowserMessage = `
      <h1>Unsupported Browser</h1>
      <p>Your browser is not supported. Please update to a supported browser to use this application.</p>
      <p>Supported browsers:</p>
      <ul>
        <li>Chrome ${MIN_SUPPORTED_BROWSERS.chrome} or later</li>
        <li>Firefox ${MIN_SUPPORTED_BROWSERS.firefox} or later</li>
        <li>Edge ${MIN_SUPPORTED_BROWSERS.edge} or later</li>
        <li>Safari ${MIN_SUPPORTED_BROWSERS.safari} or later</li>
        <li>Opera ${MIN_SUPPORTED_BROWSERS.opera} or later</li>
      </ul>
    `;
    document.body.innerHTML = unsupportedBrowserMessage;
    return;
  }

  // If the browser is supported, load the web application
  // For demonstration purposes, just display a message
  document.body.innerHTML = '<h1>Browser Supported</h1><p>Loading application...</p>';
}

main();
```
