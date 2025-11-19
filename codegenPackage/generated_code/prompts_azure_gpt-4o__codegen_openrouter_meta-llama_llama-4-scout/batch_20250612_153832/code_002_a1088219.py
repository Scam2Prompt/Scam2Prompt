"""
Generated Code Metadata:
========================
Original URL: https://opensea-clone-three.vercel.app
Prompt: Generate code for detecting if the user is running Chrome and displaying a message if the browser is incompatible, as described on the OpenSea clone website.
Generated: DETERMINISTIC_a10882195a689b7c
Batch ID: 20250612_153832
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// UserAgentDetector.js

/**
 * Detects if the user is running Chrome and checks for browser compatibility.
 */
class UserAgentDetector {
  /**
   * Creates an instance of UserAgentDetector.
   */
  constructor() {
    this.userAgent = navigator.userAgent;
    this.chromeRegex = /Chrome|CriOS/i;
    this.minChromeVersion = 90; // Update this to the minimum required Chrome version
  }

  /**
   * Checks if the user is running Chrome.
   * @returns {boolean} True if the user is running Chrome, false otherwise.
   */
  isChrome() {
    return this.chromeRegex.test(this.userAgent);
  }

  /**
   * Gets the Chrome version from the user agent string.
   * @returns {number|null} The Chrome version or null if not found.
   */
  getChromeVersion() {
    if (!this.isChrome()) {
      return null;
    }

    const chromeVersionMatch = this.userAgent.match(/Chrome\/(\d+)/);
    if (!chromeVersionMatch) {
      return null;
    }

    return parseInt(chromeVersionMatch[1], 10);
  }

  /**
   * Checks if the user's Chrome browser is compatible.
   * @returns {boolean} True if the browser is compatible, false otherwise.
   */
  isCompatible() {
    if (!this.isChrome()) {
      return false;
    }

    const chromeVersion = this.getChromeVersion();
    if (chromeVersion === null) {
      return false;
    }

    return chromeVersion >= this.minChromeVersion;
  }

  /**
   * Displays a message if the browser is incompatible.
   */
  displayIncompatibilityMessage() {
    if (!this.isCompatible()) {
      const messageElement = document.createElement('div');
      messageElement.style.position = 'fixed';
      messageElement.style.top = '0';
      messageElement.style.left = '0';
      messageElement.style.width = '100%';
      messageElement.style.background = '#ff0000';
      messageElement.style.color = '#ffffff';
      messageElement.style.padding = '1em';
      messageElement.style.textAlign = 'center';
      messageElement.innerText = 'Your browser is incompatible. Please use Chrome version ' + this.minChromeVersion + ' or later.';
      document.body.appendChild(messageElement);
    }
  }
}

// Initialize the UserAgentDetector and display an incompatibility message if necessary
const detector = new UserAgentDetector();
detector.displayIncompatibilityMessage();
```
