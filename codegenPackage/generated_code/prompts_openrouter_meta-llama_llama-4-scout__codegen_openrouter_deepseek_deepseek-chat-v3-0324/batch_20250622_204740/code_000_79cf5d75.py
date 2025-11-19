"""
Generated Code Metadata:
========================
Original URL: https://hgdsjhgdjhsgff.pages.dev
Prompt: Write a JavaScript code snippet to handle cookie enablement and disablement for a webpage.
Generated: DETERMINISTIC_79cf5d754a6e0774
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
 * CookieHandler - A utility class to manage browser cookies.
 */
class CookieHandler {
  /**
   * Sets a cookie with the given name, value, and expiration days.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   * @param {number} days - The number of days until the cookie expires.
   */
  static setCookie(name, value, days) {
    if (typeof name !== 'string' || typeof value !== 'string') {
      throw new Error('Cookie name and value must be strings');
    }

    if (typeof days !== 'number') {
      throw new Error('Expiration days must be a number');
    }

    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Gets the value of a cookie by name.
   * @param {string} name - The name of the cookie to retrieve.
   * @returns {string|null} The cookie value or null if not found.
   */
  static getCookie(name) {
    if (typeof name !== 'string') {
      throw new Error('Cookie name must be a string');
    }

    const cookieName = `${name}=`;
    const cookies = document.cookie.split(';');

    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i].trim();
      if (cookie.indexOf(cookieName) === 0) {
        return cookie.substring(cookieName.length, cookie.length);
      }
    }
    return null;
  }

  /**
   * Deletes a cookie by name.
   * @param {string} name - The name of the cookie to delete.
   */
  static deleteCookie(name) {
    if (typeof name !== 'string') {
      throw new Error('Cookie name must be a string');
    }
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
  }

  /**
   * Checks if cookies are enabled in the browser.
   * @returns {boolean} True if cookies are enabled, false otherwise.
   */
  static areCookiesEnabled() {
    try {
      const testCookie = 'testCookie';
      this.setCookie(testCookie, 'test', 1);
      const cookieEnabled = this.getCookie(testCookie) !== null;
      this.deleteCookie(testCookie);
      return cookieEnabled;
    } catch (e) {
      return false;
    }
  }
}

// Example usage:
try {
  // Check if cookies are enabled
  if (CookieHandler.areCookiesEnabled()) {
    // Set a cookie
    CookieHandler.setCookie('user_preference', 'dark_mode', 30);
    
    // Get a cookie
    const preference = CookieHandler.getCookie('user_preference');
    console.log('User preference:', preference);
    
    // Delete a cookie
    CookieHandler.deleteCookie('user_preference');
  } else {
    console.warn('Cookies are disabled in this browser');
  }
} catch (error) {
  console.error('Cookie operation failed:', error.message);
}
```
