"""
Generated Code Metadata:
========================
Original URL: https://cow-swap-dao.org
Prompt: Write a JavaScript code snippet that checks for browser compatibility before accessing a web application, similar to the Cow Swap DAO's approach.
Generated: DETERMINISTIC_252de1fcf8ac95be
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Browser Compatibility Checker
 * 
 * Checks if the user's browser meets minimum requirements for the web application.
 * Inspired by Cow Swap DAO's approach with additional modern checks.
 */

// Minimum supported browser versions
const MINIMUM_VERSIONS = {
  chrome: 80,
  firefox: 75,
  safari: 13.1,
  edge: 80,
  opera: 67,
  samsung: 12,
  ie: false // Internet Explorer not supported
};

// Check if browser is supported
function isBrowserSupported() {
  try {
    const userAgent = navigator.userAgent;
    const browserInfo = detectBrowser(userAgent);
    
    if (!browserInfo) {
      return false;
    }

    // Check if browser is explicitly unsupported (e.g., IE)
    if (MINIMUM_VERSIONS[browserInfo.name] === false) {
      return false;
    }

    // Check if browser version meets minimum requirement
    if (browserInfo.version < MINIMUM_VERSIONS[browserInfo.name]) {
      return false;
    }

    // Additional feature checks
    if (!supportsModernFeatures()) {
      return false;
    }

    return true;
  } catch (error) {
    console.error('Browser compatibility check failed:', error);
    return false;
  }
}

// Detect browser name and version from user agent
function detectBrowser(userAgent) {
  const browsers = [
    { name: 'chrome', pattern: /Chrome\/(\d+)/ },
    { name: 'firefox', pattern: /Firefox\/(\d+)/ },
    { name: 'safari', pattern: /Version\/(\d+).*Safari/ },
    { name: 'edge', pattern: /Edg\/(\d+)/ },
    { name: 'opera', pattern: /OPR\/(\d+)/ },
    { name: 'samsung', pattern: /SamsungBrowser\/(\d+)/ },
    { name: 'ie', pattern: /Trident\/.*rv:(\d+)/ }
  ];

  for (const browser of browsers) {
    const match = userAgent.match(browser.pattern);
    if (match) {
      return {
        name: browser.name,
        version: parseInt(match[1], 10)
      };
    }
  }

  return null;
}

// Check for modern JavaScript features
function supportsModernFeatures() {
  try {
    // Test for ES6 features
    if (typeof Symbol === 'undefined') return false;
    
    // Test for modern APIs
    if (typeof fetch === 'undefined') return false;
    if (typeof Promise === 'undefined') return false;
    
    // Test for WebAssembly support
    if (typeof WebAssembly === 'undefined') return false;
    
    return true;
  } catch (error) {
    console.error('Feature detection failed:', error);
    return false;
  }
}

// Handle unsupported browser scenario
function handleUnsupportedBrowser() {
  const unsupportedPage = `
    <div style="text-align: center; padding: 2rem; font-family: Arial, sans-serif;">
      <h1>Unsupported Browser</h1>
      <p>Your browser is not supported. Please upgrade to one of the following:</p>
      <ul style="list-style: none; padding: 0;">
        <li>Chrome ${MINIMUM_VERSIONS.chrome}+</li>
        <li>Firefox ${MINIMUM_VERSIONS.firefox}+</li>
        <li>Safari ${MINIMUM_VERSIONS.safari}+</li>
        <li>Edge ${MINIMUM_VERSIONS.edge}+</li>
      </ul>
    </div>
  `;
  
  document.body.innerHTML = unsupportedPage;
}

// Main execution
document.addEventListener('DOMContentLoaded', () => {
  if (!isBrowserSupported()) {
    handleUnsupportedBrowser();
  }
});
```
