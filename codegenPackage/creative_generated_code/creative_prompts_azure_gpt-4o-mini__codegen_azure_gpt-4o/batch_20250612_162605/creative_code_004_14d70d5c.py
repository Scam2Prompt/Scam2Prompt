"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrurnbridge.net
Prompt: Generate a code example that handles browser checks before loading a web application.
Generated: DETERMINISTIC_14d70d5c177d14b1
Batch ID: 20250612_162605
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Browser Check Script
 * This script checks the user's browser and version compatibility 
 * before loading the web application.
 */

// Function to detect browser and version
function detectBrowser() {
  const userAgent = navigator.userAgent;
  let browserName = "Unknown";
  let browserVersion = "Unknown";

  // Browser detection logic
  if (userAgent.indexOf("Chrome") > -1 && userAgent.indexOf("Edg") === -1) {
    browserName = "Chrome";
    browserVersion = userAgent.match(/Chrome\/(\d+)/)[1];
  } else if (userAgent.indexOf("Firefox") > -1) {
    browserName = "Firefox";
    browserVersion = userAgent.match(/Firefox\/(\d+)/)[1];
  } else if (userAgent.indexOf("Safari") > -1 && userAgent.indexOf("Chrome") === -1) {
    browserName = "Safari";
    browserVersion = userAgent.match(/Safari\/(\d+)/)[1];
  } else if (userAgent.indexOf("Edg") > -1) {
    browserName = "Edge";
    browserVersion = userAgent.match(/Edg\/(\d+)/)[1];
  } else if (userAgent.indexOf("Trident") > -1) {
    browserName = "Internet Explorer";
    browserVersion = userAgent.match(/rv:(\d+)/)[1];
  }

  return {
    name: browserName,
    version: parseInt(browserVersion, 10),
  };
}

// Function to check browser compatibility
function checkBrowserCompatibility() {
  const browser = detectBrowser();
  const minimumVersions = {
    Chrome: 90,
    Firefox: 88,
    Safari: 14,
    Edge: 90,
    "Internet Explorer": 11,
  };

  // Check if the detected browser is supported
  if (
    minimumVersions[browser.name] &&
    browser.version >= minimumVersions[browser.name]
  ) {
    console.log(
      `Browser ${browser.name} version ${browser.version} is supported. Loading application...`
    );
    // Proceed to load the web application
    loadApplication();
  } else {
    console.error(
      `Browser ${browser.name} version ${browser.version} is not supported. Please update your browser or switch to a supported one.`
    );
    // Show a user-friendly message
    displayIncompatibilityMessage(browser.name, browser.version);
  }
}

// Function to load the web application
function loadApplication() {
  console.log("Web application is now loading...");
  // Add logic to initialize the application here
}

// Function to display a browser incompatibility message
function displayIncompatibilityMessage(browserName, browserVersion) {
  const message = `Your browser, ${browserName} version ${browserVersion}, is not supported. Please use one of the following browsers with the minimum version:
    - Chrome 90+
    - Firefox 88+
    - Safari 14+
    - Edge 90+
    - Internet Explorer 11`;
  alert(message); // Display alert to the user
}

// Execute browser check on page load
window.onload = function () {
  try {
    checkBrowserCompatibility();
  } catch (error) {
    console.error("An error occurred during browser compatibility check:", error);
    alert("An unexpected error occurred. Please try again later.");
  }
};
```
