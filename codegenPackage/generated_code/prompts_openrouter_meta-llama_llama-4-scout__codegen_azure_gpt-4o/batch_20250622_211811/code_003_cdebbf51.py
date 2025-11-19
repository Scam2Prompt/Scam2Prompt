"""
Generated Code Metadata:
========================
Original URL: https://claims-stether.org
Prompt: Create a basic example of how to use the `document.cookie` API to save and retrieve user preferences regarding cookie usage on a website, inspired by Amazon.es's user interface.
Generated: DETERMINISTIC_cdebbf5169dce3ec
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * A basic example of using the `document.cookie` API to save and retrieve
 * user preferences regarding cookie usage on a website.
 * Inspired by Amazon.es's user interface.
 */

/**
 * Sets a cookie with the given name, value, and expiration days.
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {number} days - The number of days until the cookie expires.
 */
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000); // Convert days to milliseconds
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${encodeURIComponent(value)};${expires};path=/`;
  } catch (error) {
    console.error("Error setting cookie:", error);
  }
}

/**
 * Retrieves the value of a cookie by its name.
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
  try {
    const cookies = document.cookie.split("; ");
    for (const cookie of cookies) {
      const [key, value] = cookie.split("=");
      if (key === name) {
        return decodeURIComponent(value);
      }
    }
    return null; // Return null if the cookie is not found
  } catch (error) {
    console.error("Error retrieving cookie:", error);
    return null;
  }
}

/**
 * Deletes a cookie by its name.
 * @param {string} name - The name of the cookie to delete.
 */
function deleteCookie(name) {
  try {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
  } catch (error) {
    console.error("Error deleting cookie:", error);
  }
}

/**
 * Example usage: Save and retrieve user preferences for cookie usage.
 */
function handleCookiePreferences() {
  const cookieName = "userCookiePreferences";
  const userPreference = getCookie(cookieName);

  if (userPreference) {
    console.log("User preference retrieved:", userPreference);
  } else {
    const userConsent = confirm("Do you accept cookies for a better experience?");
    if (userConsent) {
      setCookie(cookieName, "accepted", 365); // Save preference for 1 year
      console.log("User preference saved: accepted");
    } else {
      setCookie(cookieName, "declined", 365); // Save preference for 1 year
      console.log("User preference saved: declined");
    }
  }
}

// Run the example
handleCookiePreferences();
```
