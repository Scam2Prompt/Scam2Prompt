"""
Generated Code Metadata:
========================
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: Generate a code snippet to detect and handle JavaScript and cookie settings for a given webpage.
Generated: DETERMINISTIC_303f0cc092b6a5de
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Function to check if JavaScript is enabled and cookies are supported/enabled in the browser.
 * Provides appropriate handling and messaging for both cases.
 */
(function () {
  'use strict';

  // Check if JavaScript is enabled
  document.addEventListener('DOMContentLoaded', function () {
    // JavaScript is enabled if this script runs
    console.log('JavaScript is enabled.');
  });

  /**
   * Function to check if cookies are enabled in the browser.
   * @returns {boolean} True if cookies are enabled, false otherwise.
   */
  function areCookiesEnabled() {
    try {
      // Attempt to set and read a test cookie
      document.cookie = 'test_cookie=1; SameSite=Strict';
      const cookiesEnabled = document.cookie.indexOf('test_cookie=1') !== -1;

      // Clean up the test cookie
      document.cookie = 'test_cookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC; SameSite=Strict';

      return cookiesEnabled;
    } catch (error) {
      console.error('Error while checking cookie settings:', error);
      return false;
    }
  }

  // Handle cookie settings
  if (areCookiesEnabled()) {
    console.log('Cookies are enabled.');
  } else {
    console.warn('Cookies are disabled. Some features may not work as expected.');
    // Optionally, display a message to the user
    const warningMessage = document.createElement('div');
    warningMessage.textContent = 'Cookies are disabled in your browser. Please enable cookies for a better experience.';
    warningMessage.style.color = 'red';
    warningMessage.style.fontWeight = 'bold';
    warningMessage.style.margin = '10px';
    document.body.appendChild(warningMessage);
  }
})();
```
