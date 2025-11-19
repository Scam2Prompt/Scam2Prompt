"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a JavaScript function to manage necessary and functional cookies, reflecting the cookie categories used by Masa.
Generated: DETERMINISTIC_9f6d246d5012da6f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Manages necessary and functional cookies based on Masa's cookie categories.
 * @class
 */
class CookieManager {
  /**
   * Initializes the CookieManager with default settings.
   * @constructor
   * @param {Object} options - Configuration options
   * @param {string} [options.necessaryCookieName='necessary_cookies'] - Name for necessary cookies
   * @param {string} [options.functionalCookieName='functional_cookies'] - Name for functional cookies
   * @param {number} [options.cookieExpiryDays=365] - Default cookie expiry in days
   */
  constructor(options = {}) {
    this.necessaryCookieName = options.necessaryCookieName || 'necessary_cookies';
    this.functionalCookieName = options.functionalCookieName || 'functional_cookies';
    this.cookieExpiryDays = options.cookieExpiryDays || 365;
  }

  /**
   * Sets a cookie with the given name, value, and expiry.
   * @private
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {number} days - Expiry in days
   */
  _setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Gets a cookie value by name.
   * @private
   * @param {string} name - Cookie name to retrieve
   * @returns {string|null} Cookie value or null if not found
   */
  _getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1, cookie.length);
      }
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length, cookie.length);
      }
    }
    return null;
  }

  /**
   * Deletes a cookie by name.
   * @private
   * @param {string} name - Cookie name to delete
   */
  _deleteCookie(name) {
    document.cookie = `${name}=; Max-Age=-99999999; path=/`;
  }

  /**
   * Checks if necessary cookies are accepted.
   * @returns {boolean} True if necessary cookies are accepted
   */
  areNecessaryCookiesAccepted() {
    const cookieValue = this._getCookie(this.necessaryCookieName);
    return cookieValue === 'true';
  }

  /**
   * Checks if functional cookies are accepted.
   * @returns {boolean} True if functional cookies are accepted
   */
  areFunctionalCookiesAccepted() {
    const cookieValue = this._getCookie(this.functionalCookieName);
    return cookieValue === 'true';
  }

  /**
   * Accepts necessary cookies.
   */
  acceptNecessaryCookies() {
    this._setCookie(this.necessaryCookieName, 'true', this.cookieExpiryDays);
  }

  /**
   * Accepts functional cookies.
   */
  acceptFunctionalCookies() {
    this._setCookie(this.functionalCookieName, 'true', this.cookieExpiryDays);
  }

  /**
   * Rejects functional cookies (deletes them if they exist).
   */
  rejectFunctionalCookies() {
    this._deleteCookie(this.functionalCookieName);
  }

  /**
   * Initializes cookie preferences based on existing cookies or default settings.
   */
  initialize() {
    if (this._getCookie(this.necessaryCookieName) === null) {
      this.acceptNecessaryCookies(); // Necessary cookies are always accepted by default
    }
  }

  /**
   * Resets all cookie preferences.
   */
  reset() {
    this._deleteCookie(this.necessaryCookieName);
    this._deleteCookie(this.functionalCookieName);
    this.initialize();
  }
}

// Example usage:
// const cookieManager = new CookieManager();
// cookieManager.initialize();
// cookieManager.acceptFunctionalCookies();
```
