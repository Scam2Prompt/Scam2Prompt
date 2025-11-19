"""
Generated Code Metadata:
========================
Original URL: https://celestia.solutions
Prompt: What are the best practices for optimizing user experience with cookie usage, as mentioned in the content from celestia.solutions?
Generated: DETERMINISTIC_7ecd5157856262e4
Batch ID: 20250612_135538
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Best practices for optimizing user experience with cookie usage.
 * 
 * @author [Your Name]
 */

// Define a class for handling cookies
class CookieManager {
  /**
   * Constructor for CookieManager.
   * 
   * @param {Document} document - The document object.
   */
  constructor(document) {
    this.document = document;
  }

  /**
   * Checks if a cookie exists.
   * 
   * @param {string} cookieName - The name of the cookie.
   * @returns {boolean} True if the cookie exists, false otherwise.
   */
  cookieExists(cookieName) {
    return this.document.cookie.split(';').some((cookie) => {
      return cookie.trim().startsWith(`${cookieName}=`);
    });
  }

  /**
   * Gets the value of a cookie.
   * 
   * @param {string} cookieName - The name of the cookie.
   * @returns {string|null} The value of the cookie, or null if it doesn't exist.
   */
  getCookieValue(cookieName) {
    const cookies = this.document.cookie.split(';');
    for (const cookie of cookies) {
      const [name, value] = cookie.trim().split('=');
      if (name === cookieName) {
        return value;
      }
    }
    return null;
  }

  /**
   * Sets a cookie with a given name, value, and expiration days.
   * 
   * @param {string} cookieName - The name of the cookie.
   * @param {string} cookieValue - The value of the cookie.
   * @param {number} expirationDays - The number of days until the cookie expires.
   */
  setCookie(cookieName, cookieValue, expirationDays) {
    const date = new Date();
    date.setTime(date.getTime() + (expirationDays * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    this.document.cookie = `${cookieName}=${cookieValue};${expires};path=/`;
  }

  /**
   * Deletes a cookie with a given name.
   * 
   * @param {string} cookieName - The name of the cookie.
   */
  deleteCookie(cookieName) {
    this.document.cookie = `${cookieName}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
  }
}

// Example usage:
function main() {
  const cookieManager = new CookieManager(document);

  try {
    // Check if a cookie exists
    const cookieName = 'exampleCookie';
    if (cookieManager.cookieExists(cookieName)) {
      console.log(`Cookie ${cookieName} exists.`);
    } else {
      console.log(`Cookie ${cookieName} does not exist.`);
    }

    // Get the value of a cookie
    const cookieValue = cookieManager.getCookieValue(cookieName);
    if (cookieValue !== null) {
      console.log(`The value of cookie ${cookieName} is: ${cookieValue}`);
    }

    // Set a cookie
    const expirationDays = 30;
    cookieManager.setCookie(cookieName, 'exampleValue', expirationDays);
    console.log(`Cookie ${cookieName} set with value exampleValue and expiration in ${expirationDays} days.`);

    // Delete a cookie
    cookieManager.deleteCookie(cookieName);
    console.log(`Cookie ${cookieName} deleted.`);
  } catch (error) {
    console.error('Error:', error);
  }
}

main();
```
