"""
Generated Code Metadata:
========================
Original URL: https://webmail.omninetwork.it
Prompt: How do I implement a feature that alerts users when they are using an unsupported browser for Webmail?
Generated: DETERMINISTIC_52a9341c4f006f1b
Batch ID: 20250612_155752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// This script checks the user's browser and alerts them if they are using an unsupported browser for Webmail.

// List of supported browsers
const supportedBrowsers = [
  { name: "Chrome", minVersion: 90 },
  { name: "Firefox", minVersion: 88 },
  { name: "Edge", minVersion: 90 },
  { name: "Safari", minVersion: 14 },
];

// Function to parse the browser's user agent string
function getBrowserInfo() {
  const userAgent = navigator.userAgent;
  let browserName = "Unknown";
  let browserVersion = "Unknown";

  if (userAgent.includes("Chrome") && !userAgent.includes("Edg")) {
    browserName = "Chrome";
    browserVersion = parseInt(userAgent.match(/Chrome\/(\d+)/)[1], 10);
  } else if (userAgent.includes("Firefox")) {
    browserName = "Firefox";
    browserVersion = parseInt(userAgent.match(/Firefox\/(\d+)/)[1], 10);
  } else if (userAgent.includes("Edg")) {
    browserName = "Edge";
    browserVersion = parseInt(userAgent.match(/Edg\/(\d+)/)[1], 10);
  } else if (userAgent.includes("Safari") && !userAgent.includes("Chrome")) {
    browserName = "Safari";
    browserVersion = parseInt(userAgent.match(/Version\/(\d+)/)[1], 10);
  }

  return { browserName, browserVersion };
}

// Function to check if the browser is supported
function isBrowserSupported(browserInfo) {
  const { browserName, browserVersion } = browserInfo;

  for (const supportedBrowser of supportedBrowsers) {
    if (
      browserName === supportedBrowser.name &&
      browserVersion >= supportedBrowser.minVersion
    ) {
      return true;
    }
  }

  return false;
}

// Main function to alert the user if the browser is unsupported
function checkBrowserSupport() {
  try {
    const browserInfo = getBrowserInfo();
    const supported = isBrowserSupported(browserInfo);

    if (!supported) {
      alert(
        `Your browser (${browserInfo.browserName} version ${browserInfo.browserVersion}) is not supported for Webmail. Please use one of the following browsers:\n` +
          supportedBrowsers
            .map(
              (browser) =>
                `${browser.name} (version ${browser.minVersion} or higher)`
            )
            .join("\n")
      );
    }
  } catch (error) {
    console.error("An error occurred while checking browser support:", error);
    alert(
      "An error occurred while checking your browser compatibility. Please ensure you are using a modern browser."
    );
  }
}

// Run the browser check when the page loads
window.onload = checkBrowserSupport;
```
