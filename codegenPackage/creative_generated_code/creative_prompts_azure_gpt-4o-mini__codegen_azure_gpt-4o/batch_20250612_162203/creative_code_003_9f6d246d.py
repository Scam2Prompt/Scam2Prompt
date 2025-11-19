"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Create a JavaScript function to manage necessary and functional cookies, reflecting the cookie categories used by Masa.
Generated: DETERMINISTIC_9f6d246d5012da6f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage cookies based on their categories.
 * The categories are 'necessary' and 'functional'.
 * This function allows setting, getting, and deleting cookies
 * while adhering to best practices for privacy compliance.
 */

// Enum to define cookie categories
const CookieCategory = {
  NECESSARY: 'necessary',
  FUNCTIONAL: 'functional',
};

/**
 * Set a cookie with a specified name, value, expiration days, and category.
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {number} days - The number of days the cookie should persist.
 * @param {string} category - The category of the cookie ('necessary' or 'functional').
 */
function setCookie(name, value, days, category) {
  if (!Object.values(CookieCategory).includes(category)) {
    throw new Error('Invalid cookie category. Must be "necessary" or "functional".');
  }

  const date = new Date();
  date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
  const expires = `expires=${date.toUTCString()}`;
  document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;

  console.log(`Cookie "${name}" set under "${category}" category.`);
}

/**
 * Get the value of a cookie by its name.
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
  const cookies = document.cookie.split(';');
  for (const cookie of cookies) {
    const [key, value] = cookie.trim().split('=');
    if (key === name) {
      return decodeURIComponent(value);
    }
  }
  return null;
}

/**
 * Delete a cookie by its name.
 * @param {string} name - The name of the cookie to delete.
 */
function deleteCookie(name) {
  document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;SameSite=Lax`;
  console.log(`Cookie "${name}" deleted.`);
}

/**
 * Manage cookies by category.
 * @param {string} category - The category of cookie management ('necessary' or 'functional').
 * @param {string} action - The action to perform ('set', 'get', 'delete').
 * @param {string} name - The name of the cookie (required for 'set' and 'delete').
 * @param {string} value - The value of the cookie (required for 'set').
 * @param {number} days - The expiration days (required for 'set').
 * @returns {string|null} - The cookie value for the 'get' action, or null.
 */
function manageCookies(category, action, name = '', value = '', days = 0) {
  try {
    switch (action) {
      case 'set':
        if (!name || !value || !days) {
          throw new Error('Missing parameters for setting a cookie.');
        }
        setCookie(name, value, days, category);
        break;
      case 'get':
        if (!name) {
          throw new Error('Missing cookie name for getting a cookie.');
        }
        return getCookie(name);
      case 'delete':
        if (!name) {
          throw new Error('Missing cookie name for deleting a cookie.');
        }
        deleteCookie(name);
        break;
      default:
        throw new Error('Invalid action. Must be "set", "get", or "delete".');
    }
  } catch (error) {
    console.error(`Error managing cookies: ${error.message}`);
  }
}

// Example usage:
// manageCookies(CookieCategory.NECESSARY, 'set', 'userSession', 'abc123', 7);
// console.log(manageCookies(CookieCategory.NECESSARY, 'get', 'userSession'));
// manageCookies(CookieCategory.FUNCTIONAL, 'delete', 'userSession');
```
