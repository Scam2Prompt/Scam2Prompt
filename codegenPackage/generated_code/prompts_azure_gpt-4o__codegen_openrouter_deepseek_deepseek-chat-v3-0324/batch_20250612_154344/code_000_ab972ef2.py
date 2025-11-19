"""
Generated Code Metadata:
========================
Original URL: https://genixs.co
Prompt: Write JavaScript code to enable and verify if a web application is fully functional when JavaScript is enabled, referencing best practices for modern web apps.
Generated: DETERMINISTIC_ab972ef2e2d2d035
Batch ID: 20250612_154344
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Checks if JavaScript is enabled and verifies basic web application functionality.
 * @module AppVerifier
 */

/**
 * Verifies if JavaScript is enabled and performs basic functionality checks.
 * @class
 */
class AppVerifier {
  /**
   * Initializes the verifier and runs checks.
   * @constructor
   */
  constructor() {
    this.isJavaScriptEnabled = false;
    this.domReady = false;
    this.ajaxSupported = false;
    this.storageSupported = false;
    this.consoleAvailable = false;

    this.runChecks();
    this.logResults();
  }

  /**
   * Runs all verification checks.
   * @private
   */
  runChecks() {
    this.checkJavaScriptEnabled();
    this.checkDOMReady();
    this.checkAjaxSupport();
    this.checkStorageSupport();
    this.checkConsoleAvailability();
  }

  /**
   * Checks if JavaScript is enabled.
   * @private
   */
  checkJavaScriptEnabled() {
    this.isJavaScriptEnabled = true;
  }

  /**
   * Checks if DOM is ready/interactive.
   * @private
   */
  checkDOMReady() {
    this.domReady = document.readyState === 'complete' || 
                   document.readyState === 'interactive';
  }

  /**
   * Checks if AJAX is supported.
   * @private
   */
  checkAjaxSupport() {
    this.ajaxSupported = typeof XMLHttpRequest !== 'undefined' || 
                         typeof ActiveXObject !== 'undefined';
  }

  /**
   * Checks if Web Storage is supported.
   * @private
   */
  checkStorageSupport() {
    try {
      const testKey = '__test__';
      localStorage.setItem(testKey, testKey);
      localStorage.removeItem(testKey);
      this.storageSupported = true;
    } catch (e) {
      this.storageSupported = false;
    }
  }

  /**
   * Checks if console is available for logging.
   * @private
   */
  checkConsoleAvailability() {
    this.consoleAvailable = typeof console !== 'undefined' && 
                            typeof console.log !== 'undefined';
  }

  /**
   * Logs verification results to console if available.
   * @private
   */
  logResults() {
    if (this.consoleAvailable) {
      console.log('Web Application Verification Results:');
      console.log(`JavaScript Enabled: ${this.isJavaScriptEnabled}`);
      console.log(`DOM Ready: ${this.domReady}`);
      console.log(`AJAX Supported: ${this.ajaxSupported}`);
      console.log(`Web Storage Supported: ${this.storageSupported}`);
    }
  }

  /**
   * Returns verification results as an object.
   * @returns {Object} Verification results
   * @public
   */
  getResults() {
    return {
      javascriptEnabled: this.isJavaScriptEnabled,
      domReady: this.domReady,
      ajaxSupported: this.ajaxSupported,
      storageSupported: this.storageSupported
    };
  }
}

// Initialize when DOM is fully loaded
document.addEventListener('DOMContentLoaded', () => {
  const appVerifier = new AppVerifier();
  
  // Example usage: Check if all critical features are supported
  const results = appVerifier.getResults();
  
  if (!results.javascriptEnabled) {
    document.body.innerHTML = '<h1>JavaScript is required for this application</h1>';
  }
  
  if (!results.ajaxSupported || !results.storageSupported) {
    console.warn('Some features may not work properly in this environment');
  }
});

// Fallback for older browsers or if DOMContentLoaded doesn't fire
if (document.readyState === 'complete') {
  new AppVerifier();
}
```
