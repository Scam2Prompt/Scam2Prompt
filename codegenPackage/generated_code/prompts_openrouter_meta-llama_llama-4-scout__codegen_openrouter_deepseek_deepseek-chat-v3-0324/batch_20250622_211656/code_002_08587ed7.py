"""
Generated Code Metadata:
========================
Original URL: https://peipeitest.pages.dev
Prompt: Generate code to handle JavaScript and cookie settings for a user-facing application.
Generated: DETERMINISTIC_08587ed715efbaad
Batch ID: 20250622_211656
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CookieHandler - A utility class to manage cookies in a user-facing application.
 * Provides methods to set, get, delete, and check cookies with proper error handling.
 */
class CookieHandler {
  /**
   * Sets a cookie with the given name, value, and options.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   * @param {Object} [options] - Optional settings for the cookie.
   * @param {number} [options.days] - Number of days until the cookie expires.
   * @param {string} [options.path] - Path for the cookie (default: '/').
   * @param {string} [options.domain] - Domain for the cookie.
   * @param {boolean} [options.secure] - If true, the cookie is sent only over HTTPS.
   * @param {string} [options.sameSite] - SameSite attribute ('Strict', 'Lax', or 'None').
   * @throws {Error} If name or value is not provided.
   */
  static setCookie(name, value, options = {}) {
    if (!name || !value) {
      throw new Error('Cookie name and value are required.');
    }

    let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

    if (options.days) {
      const date = new Date();
      date.setTime(date.getTime() + (options.days * 24 * 60 * 60 * 1000));
      cookieString += `; expires=${date.toUTCString()}`;
    }

    if (options.path) {
      cookieString += `; path=${options.path}`;
    } else {
      cookieString += '; path=/';
    }

    if (options.domain) {
      cookieString += `; domain=${options.domain}`;
    }

    if (options.secure) {
      cookieString += '; secure';
    }

    if (options.sameSite) {
      cookieString += `; SameSite=${options.sameSite}`;
    }

    document.cookie = cookieString;
  }

  /**
   * Retrieves the value of a cookie by name.
   * @param {string} name - The name of the cookie to retrieve.
   * @returns {string|null} The cookie value, or null if not found.
   */
  static getCookie(name) {
    if (!name) {
      return null;
    }

    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=');
      if (decodeURIComponent(cookieName) === name) {
        return decodeURIComponent(cookieValue);
      }
    }
    return null;
  }

  /**
   * Deletes a cookie by name.
   * @param {string} name - The name of the cookie to delete.
   * @param {string} [path] - The path of the cookie (default: '/').
   * @param {string} [domain] - The domain of the cookie.
   */
  static deleteCookie(name, path = '/', domain) {
    if (!name) {
      return;
    }

    document.cookie = `${encodeURIComponent(name)}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=${path}` +
      (domain ? `; domain=${domain}` : '');
  }

  /**
   * Checks if cookies are enabled in the browser.
   * @returns {boolean} True if cookies are enabled, false otherwise.
   */
  static areCookiesEnabled() {
    try {
      const testCookie = 'testCookie';
      this.setCookie(testCookie, 'testValue', { days: 1 });
      const cookieExists = this.getCookie(testCookie) !== null;
      this.deleteCookie(testCookie);
      return cookieExists;
    } catch (e) {
      return false;
    }
  }
}

/**
 * UserSettings - Handles user preferences and settings using cookies.
 */
class UserSettings {
  /**
   * Saves a user preference to a cookie.
   * @param {string} key - The preference key.
   * @param {string} value - The preference value.
   * @param {Object} [options] - Cookie options (see CookieHandler.setCookie).
   */
  static savePreference(key, value, options) {
    try {
      CookieHandler.setCookie(`user_pref_${key}`, value, options);
    } catch (e) {
      console.error(`Failed to save preference: ${e.message}`);
    }
  }

  /**
   * Retrieves a user preference from a cookie.
   * @param {string} key - The preference key.
   * @returns {string|null} The preference value, or null if not found.
   */
  static getPreference(key) {
    return CookieHandler.getCookie(`user_pref_${key}`);
  }

  /**
   * Deletes a user preference cookie.
   * @param {string} key - The preference key.
   */
  static deletePreference(key) {
    CookieHandler.deleteCookie(`user_pref_${key}`);
  }
}

// Example usage:
// CookieHandler.setCookie('theme', 'dark', { days: 30, path: '/', sameSite: 'Lax' });
// const theme = CookieHandler.getCookie('theme');
// CookieHandler.deleteCookie('theme');

// UserSettings.savePreference('language', 'en', { days: 365 });
// const language = UserSettings.getPreference('language');
// UserSettings.deletePreference('language');
```
