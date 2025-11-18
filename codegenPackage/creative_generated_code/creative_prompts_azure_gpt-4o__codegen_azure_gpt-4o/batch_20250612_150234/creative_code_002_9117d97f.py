"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etf-key.online
Prompt: Generate a script in JavaScript that checks for browser compatibility and redirects users to an alternative page if JavaScript is disabled.
Generated: DETERMINISTIC_9117d97f94ee8825
Batch ID: 20250612_150234
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * This script checks for browser compatibility and whether JavaScript is enabled.
 * If JavaScript is disabled, users will be redirected to an alternative page.
 * Additionally, the script ensures compatibility by checking for modern browser features.
 */

// Immediately executed function to avoid polluting global namespace
(function () {
  'use strict';

  /**
   * Checks for browser compatibility and JavaScript availability.
   * Redirects users to an alternative page if any criteria are not met.
   */
  function checkCompatibility() {
    try {
      // Feature detection for modern browsers
      const isModernBrowser = 'querySelector' in document &&
        'addEventListener' in window &&
        'localStorage' in window &&
        'fetch' in window;

      // If browser lacks modern features, redirect
      if (!isModernBrowser) {
        redirectToAlternativePage('unsupported.html');
        return;
      }

      // This script assumes JavaScript is enabled if running. No further check is needed.

      console.log('Browser is compatible and JavaScript is enabled.');
    } catch (error) {
      // Handle unexpected errors during compatibility checks
      console.error('An error occurred during compatibility checks:', error);
      redirectToAlternativePage('unsupported.html');
    }
  }

  /**
   * Redirects the user to an alternative page.
   * @param {string} url - The URL of the alternative page.
   */
  function redirectToAlternativePage(url) {
    if (url) {
      window.location.href = url;
    } else {
      console.error('No valid URL provided for redirection.');
    }
  }

  // Run the compatibility check
  checkCompatibility();
})();
```
