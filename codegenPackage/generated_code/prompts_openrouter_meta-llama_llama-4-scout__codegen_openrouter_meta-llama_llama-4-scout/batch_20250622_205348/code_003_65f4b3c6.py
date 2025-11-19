"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Create a JavaScript function to handle user preferences for cookie settings, similar to the functionality on the Baltica Sopot website, and explain how it works.
Generated: DETERMINISTIC_65f4b3c6eaf76f84
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie preference manager.
 * 
 * This module provides functionality to handle user preferences for cookie settings.
 * 
 * @module CookiePreferenceManager
 */

// Define the CookiePreferenceManager class
class CookiePreferenceManager {
  /**
   * Creates an instance of CookiePreferenceManager.
   * 
   * @param {string} cookieName - The name of the cookie to store user preferences.
   */
  constructor(cookieName = 'cookie_preferences') {
    this.cookieName = cookieName;
  }

  /**
   * Gets the current cookie preferences.
   * 
   * @returns {Object} The current cookie preferences.
   */
  getPreferences() {
    const cookieValue = this.getCookie(this.cookieName);
    return cookieValue ? JSON.parse(cookieValue) : {};
  }

  /**
   * Sets the cookie preferences.
   * 
   * @param {Object} preferences - The new cookie preferences.
   */
  setPreferences(preferences) {
    this.setCookie(this.cookieName, JSON.stringify(preferences), 365);
  }

  /**
   * Checks if a specific cookie type is allowed.
   * 
   * @param {string} type - The type of cookie to check.
   * @returns {boolean} True if the cookie type is allowed, false otherwise.
   */
  isAllowed(type) {
    const preferences = this.getPreferences();
    return preferences[type] === true;
  }

  /**
   * Gets the value of a cookie.
   * 
   * @param {string} name - The name of the cookie.
   * @returns {string} The value of the cookie, or null if not found.
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [key, value] = cookie.trim().split('=');
      if (key === name) {
        return value;
      }
    }
    return null;
  }

  /**
   * Sets the value of a cookie.
   * 
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   * @param {number} days - The number of days until the cookie expires.
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    document.cookie = `${name}=${value};expires=${date.toUTCString()};path=/`;
  }

  /**
   * Revokes all cookies.
   */
  revokeCookies() {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [key] = cookie.trim().split('=');
      document.cookie = `${key}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
    }
  }
}

// Example usage:
function main() {
  try {
    const cookieManager = new CookiePreferenceManager();

    // Set initial preferences
    cookieManager.setPreferences({
      essential: true,
      functional: false,
      performance: false,
      targeting: false,
    });

    // Get current preferences
    const preferences = cookieManager.getPreferences();
    console.log('Current preferences:', preferences);

    // Check if a specific cookie type is allowed
    const isFunctionalAllowed = cookieManager.isAllowed('functional');
    console.log('Is functional cookie allowed?', isFunctionalAllowed);

    // Revoke all cookies
    // cookieManager.revokeCookies();
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
