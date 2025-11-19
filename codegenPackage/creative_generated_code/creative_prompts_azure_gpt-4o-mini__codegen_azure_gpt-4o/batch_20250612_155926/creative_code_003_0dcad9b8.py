"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://duoiudf-dsdds.pages.dev
Prompt: What libraries can help manage cookies in a JavaScript application?
Generated: DETERMINISTIC_0dcad9b8f25a43e6
Batch ID: 20250612_155926
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Example JavaScript code demonstrating the use of cookie-management libraries.
 * This example uses the popular "js-cookie" library for handling cookies in a web application.
 *
 * To install the library, use: npm install js-cookie
 */

const Cookies = require('js-cookie');

/**
 * Function to set a cookie.
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {object} [options] - Optional settings for the cookie (e.g., expires, path, secure).
 */
function setCookie(name, value, options = {}) {
  try {
    Cookies.set(name, value, options);
    console.log(`Cookie "${name}" set successfully!`);
  } catch (error) {
    console.error(`Error setting cookie "${name}":`, error);
  }
}

/**
 * Function to get a cookie.
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
  try {
    const value = Cookies.get(name);
    console.log(`Cookie "${name}" retrieved:`, value);
    return value || null;
  } catch (error) {
    console.error(`Error retrieving cookie "${name}":`, error);
    return null;
  }
}

/**
 * Function to delete a cookie.
 * @param {string} name - The name of the cookie to delete.
 */
function deleteCookie(name) {
  try {
    Cookies.remove(name);
    console.log(`Cookie "${name}" deleted successfully!`);
  } catch (error) {
    console.error(`Error deleting cookie "${name}":`, error);
  }
}

// Example usage:

// Setting a cookie
setCookie('userToken', 'abc123', { expires: 7, path: '/', secure: true });

// Getting a cookie
const userToken = getCookie('userToken');

// Deleting a cookie
deleteCookie('userToken');
```

To run this code, make sure you install the `js-cookie` library using `npm install js-cookie`.
