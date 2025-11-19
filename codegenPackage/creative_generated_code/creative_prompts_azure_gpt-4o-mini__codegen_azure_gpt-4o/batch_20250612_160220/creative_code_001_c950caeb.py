"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-sol.pages.dev
Prompt: What are the steps to troubleshoot JavaScript and cookie issues on a webpage?
Generated: DETERMINISTIC_c950caebe926311e
Batch ID: 20250612_160220
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
 * This helps capture runtime errors on the webpage.
 */
window.onerror = function (message, source, lineno, colno, error) {
  console.error("JavaScript Error Detected:");
  console.error("Message:", message);
  console.error("Source:", source);
  console.error("Line:", lineno);
  console.error("Column:", colno);
  console.error("Error Object:", error);
};

/**
 * Function to check if cookies are enabled in the browser.
 * @returns {boolean} - True if cookies are enabled, false otherwise.
 */
function areCookiesEnabled() {
  try {
    // Attempt to set and retrieve a test cookie
    document.cookie = "test_cookie=1; path=/";
    const cookiesEnabled = document.cookie.indexOf("test_cookie=1") !== -1;

    // Clean up test cookie
    document.cookie = "test_cookie=1; path=/; expires=Thu, 01 Jan 1970 00:00:00 UTC";

    return cookiesEnabled;
  } catch (error) {
    console.error("Error checking cookie settings:", error);
    return false;
  }
}

/**
 * Function to list all cookies for the current domain.
 * @returns {Object} - An object containing all cookies as key-value pairs.
 */
function listCookies() {
  try {
    const cookies = document.cookie.split("; ");
    const cookieObj = {};

    cookies.forEach(cookie => {
      const [key, value] = cookie.split("=");
      cookieObj[key] = decodeURIComponent(value || "");
    });

    return cookieObj;
  } catch (error) {
    console.error("Error retrieving cookies:", error);
    return {};
  }
}

/**
 * Function to check browser compatibility for JavaScript and cookies.
 * @returns {Object} - Summary of browser compatibility checks.
 */
function checkBrowserCompatibility() {
  return {
    javascriptEnabled: typeof window === "object" && typeof document === "object",
    cookiesEnabled: areCookiesEnabled(),
  };
}

/**
 * Function to troubleshoot JavaScript and cookie issues.
 * Logs compatibility and cookie details to the console for debugging.
 */
function troubleshootIssues() {
  console.log("Checking browser compatibility...");
  const compatibility = checkBrowserCompatibility();

  if (!compatibility.javascriptEnabled) {
    console.warn("JavaScript is not enabled in this browser.");
  } else {
    console.log("JavaScript is enabled.");
  }

  if (!compatibility.cookiesEnabled) {
    console.warn("Cookies are not enabled in this browser.");
  } else {
    console.log("Cookies are enabled.");
    console.log("Cookies:", listCookies());
  }

  console.log("JavaScript and cookie troubleshooting complete.");
}

// Run the troubleshooting function on page load
window.onload = function () {
  troubleshootIssues();
};
```
