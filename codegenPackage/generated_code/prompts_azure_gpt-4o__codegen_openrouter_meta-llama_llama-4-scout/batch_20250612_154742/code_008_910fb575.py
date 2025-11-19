"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Develop a JavaScript function that dynamically adjusts cookie settings on the TTEC STC Cluster Status website based on user preferences, ensuring compliance with essential and functional cookie requirements.
Generated: DETERMINISTIC_910fb5753c2542a1
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Adjusts cookie settings on the TTEC STC Cluster Status website based on user preferences.
 * Ensures compliance with essential and functional cookie requirements.
 */

// Define the CookieManager class
class CookieManager {
  /**
   * Essential cookies required for the website to function.
   * @type {string[]}
   */
  static ESSENTIAL_COOKIES = ['session_id', 'authentication_token'];

  /**
   * Functional cookies that can be opted out.
   * @type {string[]}
   */
  static FUNCTIONAL_COOKIES = ['analytics_tracking', 'personalization'];

  /**
   * Updates cookie settings based on user preferences.
   * @param {Object} userPreferences - User preferences object.
   * @param {boolean} userPreferences.essential - Whether to allow essential cookies.
   * @param {boolean} userPreferences.functional - Whether to allow functional cookies.
   */
  static updateCookieSettings(userPreferences) {
    try {
      // Check if user preferences are provided
      if (!userPreferences) {
        throw new Error('User preferences are required');
      }

      // Ensure essential cookies are always allowed
      CookieManager.allowEssentialCookies();

      // Update functional cookies based on user preference
      if (userPreferences.functional) {
        CookieManager.allowFunctionalCookies();
      } else {
        CookieManager.denyFunctionalCookies();
      }
    } catch (error) {
      console.error('Error updating cookie settings:', error);
    }
  }

  /**
   * Allows essential cookies.
   */
  static allowEssentialCookies() {
    CookieManager.ESSENTIAL_COOKIES.forEach((cookie) => {
      CookieManager.setCookie(cookie, true);
    });
  }

  /**
   * Allows functional cookies.
   */
  static allowFunctionalCookies() {
    CookieManager.FUNCTIONAL_COOKIES.forEach((cookie) => {
      CookieManager.setCookie(cookie, true);
    });
  }

  /**
   * Denies functional cookies.
   */
  static denyFunctionalCookies() {
    CookieManager.FUNCTIONAL_COOKIES.forEach((cookie) => {
      CookieManager.setCookie(cookie, false);
    });
  }

  /**
   * Sets a cookie.
   * @param {string} cookieName - Name of the cookie.
   * @param {boolean} allowed - Whether the cookie is allowed.
   */
  static setCookie(cookieName, allowed) {
    const date = new Date();
    date.setTime(date.getTime() + (allowed ? 30 : -30) * 24 * 60 * 60 * 1000);
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${cookieName}=${allowed ? 'true' : 'false'};${expires};path=/`;
  }
}

// Example usage:
const userPreferences = {
  essential: true,
  functional: false,
};

CookieManager.updateCookieSettings(userPreferences);
```
