"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Write a code snippet that uses cookies to track user consent preferences, inspired by the cookie management features on the Masa website.
Generated: DETERMINISTIC_a14e9a3963db075b
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// CookieManager.js

/**
 * Manages user consent preferences using cookies.
 */
class CookieManager {
  /**
   * Cookie name for storing user consent preferences.
   */
  static COOKIE_NAME = 'userConsent';

  /**
   * Expiration time for the cookie in days.
   */
  static COOKIE_EXPIRATION_DAYS = 365;

  /**
   * Checks if the user has given consent for a specific cookie category.
   * 
   * @param {string} category - The category of the cookie (e.g., 'analytics', 'marketing').
   * @returns {boolean} True if the user has given consent, false otherwise.
   */
  static hasConsent(category) {
    const cookie = CookieManager.getCookie();
    if (!cookie) return false;
    return cookie[category] === true;
  }

  /**
   * Sets the user's consent preference for a specific cookie category.
   * 
   * @param {string} category - The category of the cookie (e.g., 'analytics', 'marketing').
   * @param {boolean} consent - True if the user gives consent, false otherwise.
   */
  static setConsent(category, consent) {
    const cookie = CookieManager.getCookie() || {};
    cookie[category] = consent;
    CookieManager.setCookie(cookie);
  }

  /**
   * Gets the user's consent preferences from the cookie.
   * 
   * @returns {object} An object containing the user's consent preferences.
   */
  static getCookie() {
    const cookieValue = document.cookie.match(new RegExp(`(^| )${CookieManager.COOKIE_NAME}=([^;]+)`));
    if (!cookieValue) return null;
    try {
      return JSON.parse(decodeURIComponent(cookieValue[2]));
    } catch {
      return null;
    }
  }

  /**
   * Sets the cookie with the user's consent preferences.
   * 
   * @param {object} cookie - An object containing the user's consent preferences.
   */
  static setCookie(cookie) {
    const expires = new Date(Date.now() + CookieManager.COOKIE_EXPIRATION_DAYS * 86400 * 1000).toUTCString();
    document.cookie = `${CookieManager.COOKIE_NAME}=${encodeURIComponent(JSON.stringify(cookie))}; expires=${expires}; path=/`;
  }

  /**
   * Revokes the user's consent for all cookie categories.
   */
  static revokeConsent() {
    CookieManager.setCookie({});
  }
}

// Example usage:
function main() {
  try {
    // Check if the user has given consent for analytics cookies
    const hasAnalyticsConsent = CookieManager.hasConsent('analytics');
    console.log(`User has given analytics consent: ${hasAnalyticsConsent}`);

    // Set the user's consent preference for marketing cookies
    CookieManager.setConsent('marketing', true);

    // Get the user's consent preferences
    const cookie = CookieManager.getCookie();
    console.log(`User's consent preferences: ${JSON.stringify(cookie)}`);

    // Revoke the user's consent for all cookie categories
    CookieManager.revokeConsent();
  } catch (error) {
    console.error('Error managing cookies:', error);
  }
}

main();
```
