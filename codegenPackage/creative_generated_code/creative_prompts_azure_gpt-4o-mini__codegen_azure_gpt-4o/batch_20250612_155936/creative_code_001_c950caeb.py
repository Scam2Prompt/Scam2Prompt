"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hdhdh00007.pages.dev
Prompt: What are the steps to troubleshoot JavaScript and cookie issues on a webpage?
Generated: DETERMINISTIC_c950caebe926311e
Batch ID: 20250612_155936
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
 * This code provides utility functions to debug JavaScript errors, 
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
    console.error("An error occurred while checking cookie availability:", error);
    return false;
  }
}

/**
 * Function to display all cookies on the webpage.
 * Useful for verifying cookie values and formats.
 * @returns {object} - An object containing cookie key-value pairs.
 */
function getAllCookies() {
  try {
    const cookies = document.cookie.split("; ");
    const cookieObject = {};

    cookies.forEach((cookie) => {
      const [key, value] = cookie.split("=");
      cookieObject[key] = value;
    });

    return cookieObject;
  } catch (error) {
    console.error("An error occurred while retrieving cookies:", error);
    return {};
  }
}

/**
 * Function to check browser compatibility for common JavaScript features.
 * @returns {object} - An object containing feature support details.
 */
function checkBrowserCompatibility() {
  return {
    localStorage: typeof localStorage !== "undefined",
    sessionStorage: typeof sessionStorage !== "undefined",
    cookiesEnabled: areCookiesEnabled(),
    fetchAPI: typeof fetch !== "undefined",
    promises: typeof Promise !== "undefined",
    arrowFunctions: (() => true) !== undefined,
  };
}

/**
 * Run troubleshooting steps and log results to the console.
 */
function troubleshootWebpage() {
  console.log("Starting Troubleshooting:");

  console.log("\nChecking Cookie Settings:");
  console.log("Cookies Enabled:", areCookiesEnabled());
  console.log("Current Cookies:", getAllCookies());

  console.log("\nChecking Browser Compatibility:");
  console.log(checkBrowserCompatibility());

  console.log("\nMonitoring JavaScript Errors:");
  console.log("Any errors will be logged to the console automatically.");
}

// Run the troubleshooting function
troubleshootWebpage();
```
