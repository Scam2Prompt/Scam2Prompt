"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds.pages.dev
Prompt: What are the steps to troubleshoot JavaScript and cookie issues on a webpage?
Generated: DETERMINISTIC_c950caebe926311e
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Troubleshooting JavaScript and cookie issues on a webpage.
 * This script provides utility functions to debug JavaScript errors, 
 * check cookie settings, and verify browser compatibility.
 */

/**
 * Function to log JavaScript errors globally.
 * Captures and logs runtime errors occurring on the webpage.
 */
window.onerror = function (message, source, lineno, colno, error) {
  console.error("JavaScript Error Caught!");
  console.error(`Message: ${message}`);
  console.error(`Source: ${source}`);
  console.error(`Line: ${lineno}, Column: ${colno}`);
  console.error(`Error Object:`, error);
};

/**
 * Function to check if cookies are enabled in the browser.
 * Returns true if cookies are enabled, false otherwise.
 */
function areCookiesEnabled() {
  try {
    // Attempt to set and retrieve a test cookie
    document.cookie = "test_cookie=1; path=/";
    const cookies = document.cookie;
    return cookies.includes("test_cookie=1");
  } catch (error) {
    console.error("Error while checking cookies:", error);
    return false;
  }
}

/**
 * Function to list all cookies available for the webpage.
 * Returns an array of cookies in key-value format.
 */
function listCookies() {
  try {
    const cookies = document.cookie.split("; ");
    return cookies.map(cookie => {
      const [key, value] = cookie.split("=");
      return { key: key.trim(), value: value.trim() };
    });
  } catch (error) {
    console.error("Error while listing cookies:", error);
    return [];
  }
}

/**
 * Function to verify browser compatibility.
 * Checks if necessary JavaScript features are supported.
 */
function checkBrowserCompatibility() {
  try {
    const features = {
      localStorage: typeof localStorage !== "undefined",
      sessionStorage: typeof sessionStorage !== "undefined",
      cookiesEnabled: areCookiesEnabled(),
    };

    console.log("Browser Compatibility Check:");
    console.log(`Local Storage Supported: ${features.localStorage}`);
    console.log(`Session Storage Supported: ${features.sessionStorage}`);
    console.log(`Cookies Enabled: ${features.cookiesEnabled}`);

    return features;
  } catch (error) {
    console.error("Error during browser compatibility check:", error);
    return null;
  }
}

/**
 * Utility to clear all cookies (use with caution!).
 * Deletes every cookie available on the current domain.
 */
function clearAllCookies() {
  try {
    const cookies = document.cookie.split("; ");
    cookies.forEach(cookie => {
      const [key] = cookie.split("=");
      document.cookie = `${key}=; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC`;
    });
    console.log("All cookies cleared.");
  } catch (error) {
    console.error("Error while clearing cookies:", error);
  }
}

/**
 * Entry point to troubleshoot JavaScript and cookie issues.
 */
function troubleshoot() {
  console.log("Starting Troubleshooting Process...");
  
  // Log browser compatibility diagnostics
  const compatibility = checkBrowserCompatibility();
  if (!compatibility) {
    console.warn("Browser compatibility check failed.");
  }

  // List current cookies
  const cookies = listCookies();
  console.log("Cookies Found:", cookies);

  // Warn if cookies are disabled
  if (!compatibility.cookiesEnabled) {
    console.warn("Cookies are disabled in the browser. Please enable cookies for full functionality.");
  }

  console.log("Troubleshooting Process Completed.");
}

// Start troubleshooting when DOM is fully loaded.
document.addEventListener("DOMContentLoaded", troubleshoot);
```
