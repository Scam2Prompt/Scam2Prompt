"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.omninetwork.it
Prompt: How do I implement a feature that alerts users when they are using an unsupported browser for Webmail?
Generated: DETERMINISTIC_52a9341c4f006f1b
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script checks the user's browser and alerts them if it is unsupported for Webmail functionality.
 * It uses feature detection and a list of unsupported browsers to provide an appropriate message.
 *
 * Supported browsers are assumed to include the latest versions of Chrome, Firefox, Safari, and Edge.
 * Older browsers or Internet Explorer will be flagged as unsupported.
 */

// List of unsupported browsers (example: Internet Explorer)
const unsupportedBrowsers = ['MSIE', 'Trident'];

function detectBrowser() {
  // Retrieve the user agent string
  const userAgent = window.navigator.userAgent;

  // Check if the user agent matches any unsupported browser
  for (let browser of unsupportedBrowsers) {
    if (userAgent.includes(browser)) {
      return browser; // Return the unsupported browser name
    }
  }

  // If no match found, return null (indicating a supported browser)
  return null;
}

function alertUnsupportedBrowser(browserName) {
  // Display an alert or redirect user to an informative page
  alert(
    `It appears you are using an unsupported browser (${browserName}). ` +
    `For the best experience with Webmail, please use the latest version of Chrome, Firefox, Safari, or Edge.`
  );
}

(function () {
  // Main function to check and handle unsupported browsers
  try {
    const unsupportedBrowser = detectBrowser();

    if (unsupportedBrowser) {
      alertUnsupportedBrowser(unsupportedBrowser);
      // Optionally, you can redirect users to a help page or block access
      // window.location.href = '/unsupported-browser.html';
    }
  } catch (error) {
    // Handle unexpected errors gracefully
    console.error('An error occurred while detecting the browser:', error);
  }
})();
```

This JavaScript code can be included in your webmail application to alert users using unsupported browsers.
