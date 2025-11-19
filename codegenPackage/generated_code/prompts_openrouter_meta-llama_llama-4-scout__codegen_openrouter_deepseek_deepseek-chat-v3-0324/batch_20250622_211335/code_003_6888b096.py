"""
Generated Code Metadata:
========================
Original URL: https://thedefiant.de
Prompt: How can I use JavaScript to detect and handle different error messages on a webpage, like the one provided?
Generated: DETERMINISTIC_6888b0964f0ce7ee
Batch ID: 20250622_211335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * ErrorHandler class to detect and handle different error messages on a webpage.
 * This class provides methods to monitor the DOM for error messages and execute
 * custom handlers when errors are detected.
 */
class ErrorHandler {
  /**
   * Initializes the ErrorHandler with a configuration object.
   * @param {Object} config - Configuration options.
   * @param {Array} config.errorSelectors - Array of CSS selectors for error elements.
   * @param {Function} config.onError - Callback function to execute when an error is detected.
   * @param {number} config.pollInterval - Interval (in ms) to check for errors (default: 1000).
   */
  constructor(config) {
    this.errorSelectors = config.errorSelectors || [];
    this.onError = config.onError || (() => {});
    this.pollInterval = config.pollInterval || 1000;
    this.observer = null;
    this.intervalId = null;
    this.init();
  }

  /**
   * Initializes the error detection mechanism.
   * Uses MutationObserver if supported, otherwise falls back to polling.
   */
  init() {
    if (typeof MutationObserver !== 'undefined') {
      this.setupMutationObserver();
    } else {
      this.setupPolling();
    }
  }

  /**
   * Sets up a MutationObserver to watch for DOM changes and detect errors.
   */
  setupMutationObserver() {
    this.observer = new MutationObserver((mutations) => {
      mutations.forEach((mutation) => {
        this.checkForErrors();
      });
    });

    this.observer.observe(document.body, {
      childList: true,
      subtree: true,
      attributes: false,
      characterData: false
    });
  }

  /**
   * Sets up polling to periodically check for errors.
   */
  setupPolling() {
    this.intervalId = setInterval(() => {
      this.checkForErrors();
    }, this.pollInterval);
  }

  /**
   * Checks the DOM for error elements matching the configured selectors.
   * Executes the onError callback if errors are found.
   */
  checkForErrors() {
    try {
      const errors = this.errorSelectors.flatMap(selector => {
        const elements = Array.from(document.querySelectorAll(selector));
        return elements.map(el => ({
          element: el,
          message: el.textContent.trim(),
          selector
        }));
      });

      if (errors.length > 0) {
        this.onError(errors);
      }
    } catch (error) {
      console.error('Error while checking for errors:', error);
    }
  }

  /**
   * Cleans up resources (observer or interval) when no longer needed.
   */
  destroy() {
    if (this.observer) {
      this.observer.disconnect();
    }
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }
}

// Example usage:
/*
const handler = new ErrorHandler({
  errorSelectors: [
    '.error-message',
    '.alert-danger',
    '[role="alert"]'
  ],
  onError: (errors) => {
    errors.forEach(error => {
      console.log(`Error detected (${error.selector}): ${error.message}`);
      // Add custom error handling logic here
    });
  },
  pollInterval: 2000
});

// To clean up when done:
// handler.destroy();
*/
```
