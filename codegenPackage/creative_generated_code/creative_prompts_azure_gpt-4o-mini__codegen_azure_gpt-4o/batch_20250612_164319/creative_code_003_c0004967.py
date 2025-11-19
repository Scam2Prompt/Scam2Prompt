"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-5.pages.dev
Prompt: What libraries can help manage cookies in JavaScript for web applications?
Generated: DETERMINISTIC_c00049677feb071c
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import js-cookie library for managing cookies in web applications
// You can install this library using: npm install js-cookie

import Cookies from 'js-cookie';

/**
 * Set a cookie
 * @param {string} name - The name of the cookie
 * @param {string} value - The value of the cookie
 * @param {Object} options - Options for the cookie (e.g., expiration, path)
 */
function setCookie(name, value, options = {}) {
  try {
    Cookies.set(name, value, options); // Set the cookie with the provided options
    console.log(`Cookie "${name}" set successfully.`);
  } catch (error) {
    console.error(`Error setting cookie "${name}":`, error);
  }
}

/**
 * Get a cookie
 * @param {string} name - The name of the cookie
 * @returns {string|null} The value of the cookie, or null if not found
 */
function getCookie(name) {
  try {
    const value = Cookies.get(name); // Retrieve the cookie value
    if (value === undefined) {
      console.log(`Cookie "${name}" not found.`);
      return null;
    }
    return value;
  } catch (error) {
    console.error(`Error retrieving cookie "${name}":`, error);
    return null;
  }
}

/**
 * Remove a cookie
 * @param {string} name - The name of the cookie
 * @param {Object} options - Options for removing the cookie (e.g., path)
 */
function removeCookie(name, options = {}) {
  try {
    Cookies.remove(name, options); // Remove the cookie
    console.log(`Cookie "${name}" removed successfully.`);
  } catch (error) {
    console.error(`Error removing cookie "${name}":`, error);
  }
}

// Example usage:

// Set a cookie that expires in 7 days
setCookie('user', 'JohnDoe', { expires: 7 });

// Get the value of the cookie
const userCookie = getCookie('user');
console.log('Retrieved cookie value:', userCookie);

// Remove the cookie
removeCookie('user');
```

Make sure to install the `js-cookie` library before using this code by running the following command in your project directory:

```bash
npm install js-cookie
```

This code demonstrates how to use `js-cookie` to manage cookies effectively, including setting, retrieving, and removing cookies.
