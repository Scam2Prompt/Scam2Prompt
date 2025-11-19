"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoz999.pages.dev
Prompt: How do I troubleshoot issues related to JavaScript and cookie settings on a web page?
Generated: DETERMINISTIC_fbfdb10b1f9f9563
Batch ID: 20250612_155905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A JavaScript utility to troubleshoot issues related to cookie settings on a web page.
 * This script includes functions to check, read, write, delete, and debug cookies.
 * It follows best practices and includes proper error handling.
 */

// Utility to check if cookies are enabled in the browser
function areCookiesEnabled() {
  try {
    document.cookie = "test_cookie=1";
    const isEnabled = document.cookie.indexOf("test_cookie=1") !== -1;
    document.cookie = "test_cookie=1; expires=Thu, 01 Jan 1970 00:00:00 UTC"; // Clean up test cookie
    return isEnabled;
  } catch (error) {
    console.error("Error checking cookie availability:", error);
    return false;
  }
}

// Function to write a cookie
function setCookie(name, value, days = 7) {
  try {
    const expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + days);
    const expires = expirationDate.toUTCString();
    document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(
      value
    )}; expires=${expires}; path=/`;
    console.log(`Cookie '${name}' successfully set.`);
  } catch (error) {
    console.error(`Error setting cookie '${name}':`, error);
  }
}

// Function to read a cookie
function getCookie(name) {
  try {
    const cookies = document.cookie.split("; ");
    for (const cookie of cookies) {
      const [key, value] = cookie.split("=");
      if (decodeURIComponent(key) === name) {
        return decodeURIComponent(value);
      }
    }
    console.warn(`Cookie '${name}' not found.`);
    return null;
  } catch (error) {
    console.error(`Error reading cookie '${name}':`, error);
    return null;
  }
}

// Function to delete a cookie
function deleteCookie(name) {
  try {
    document.cookie = `${encodeURIComponent(name)}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
    console.log(`Cookie '${name}' successfully deleted.`);
  } catch (error) {
    console.error(`Error deleting cookie '${name}':`, error);
  }
}

// Debugging cookies: Logs all cookies and their values
function debugCookies() {
  try {
    const cookies = document.cookie.split("; ");
    if (cookies.length === 1 && cookies[0] === "") {
      console.warn("No cookies found.");
    } else {
      console.log("Cookies:");
      cookies.forEach((cookie) => {
        const [key, value] = cookie.split("=");
        console.log(`- ${decodeURIComponent(key)}: ${decodeURIComponent(value)}`);
      });
    }
  } catch (error) {
    console.error("Error debugging cookies:", error);
  }
}

// Example Usage:
// Check if cookies are enabled
if (areCookiesEnabled()) {
  console.log("Cookies are enabled.");
} else {
  console.warn("Cookies are disabled in this browser.");
}

// Set a cookie
setCookie("test_cookie", "test_value", 7);

// Get a cookie
const testValue = getCookie("test_cookie");
console.log("Retrieved value for 'test_cookie':", testValue);

// Delete a cookie
deleteCookie("test_cookie");

// Debug all cookies
debugCookies();
```
