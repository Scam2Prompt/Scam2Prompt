"""
Generated Code Metadata:
========================
Original URL: https://ethlast.com
Prompt: Write JavaScript code to detect if JavaScript is disabled on a mobile browser and display a warning message, similar to the behavior described on the ETH Pledge website.
Generated: DETERMINISTIC_52f271250ab965a0
Batch ID: 20250612_152600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// JavaScript code to detect if JavaScript is disabled on a mobile browser
// and display a warning message.

class JsDisabledDetector {
  /**
   * Initialize the detector.
   */
  constructor() {
    // Create a warning message element.
    this.warningMessageElement = document.createElement('div');
    this.warningMessageElement.id = 'js-disabled-warning';
    this.warningMessageElement.textContent = 'JavaScript is disabled. Please enable JavaScript to use this website.';
    this.warningMessageElement.style.position = 'fixed';
    this.warningMessageElement.style.top = '0';
    this.warningMessageElement.style.left = '0';
    this.warningMessageElement.style.width = '100%';
    this.warningMessageElement.style.background = '#ff9800';
    this.warningMessageElement.style.color = '#ffffff';
    this.warningMessageElement.style.padding = '1em';
    this.warningMessageElement.style.textAlign = 'center';
    this.warningMessageElement.style.zIndex = '1000';

    // Check if JavaScript is enabled.
    try {
      // Try to set a cookie. If JavaScript is disabled, this will throw an error.
      document.cookie = 'javascriptEnabled=true; expires=Fri, 31 Dec 9999 23:59:59 GMT';
    } catch (error) {
      // If an error occurs, JavaScript is likely disabled.
      this.showWarningMessage();
    }

    // Check if the noScript element is supported.
    const noScriptElement = document.createElement('noscript');
    if (noScriptElement.style.display === 'none') {
      // If the noScript element is not supported, JavaScript is likely enabled.
      this.checkForJsDisabling();
    } else {
      // If the noScript element is supported, JavaScript might be disabled.
      this.showWarningMessage();
    }
  }

  /**
   * Show the warning message.
   */
  showWarningMessage() {
    // Add the warning message element to the page.
    document.body.appendChild(this.warningMessageElement);
  }

  /**
   * Check if JavaScript is disabled by trying to access the cookie.
   */
  checkForJsDisabling() {
    // Check if the cookie is set.
    const cookies = document.cookie.split('; ');
    let jsEnabled = false;
    for (const cookie of cookies) {
      const [key, value] = cookie.split('=');
      if (key === 'javascriptEnabled' && value === 'true') {
        jsEnabled = true;
        break;
      }
    }

    // If the cookie is not set, JavaScript is likely disabled.
    if (!jsEnabled) {
      this.showWarningMessage();
    }
  }
}

// Initialize the detector.
const detector = new JsDisabledDetector();
```
