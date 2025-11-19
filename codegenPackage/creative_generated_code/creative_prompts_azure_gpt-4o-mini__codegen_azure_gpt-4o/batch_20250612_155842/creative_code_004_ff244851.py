"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7473441704.pages.dev
Prompt: What are common issues related to JavaScript and cookies that developers face when building web applications?
Generated: DETERMINISTIC_ff2448516f31d753
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Demonstrates common issues and solutions when working with cookies in JavaScript.
 * This code provides examples of setting, getting, deleting cookies, 
 * and handling potential problems (e.g., security, size limits, encoding, etc.).
 */

// Utility function to set a cookie
function setCookie(name, value, days = 7, path = "/", secure = false, sameSite = "Lax") {
  try {
    // Validate input
    if (!name || typeof name !== "string") {
      throw new Error("Cookie name must be a non-empty string.");
    }

    // Encode value to avoid special characters causing issues
    const encodedValue = encodeURIComponent(value);

    // Create cookie string
    let cookieString = `${name}=${encodedValue}; path=${path}; samesite=${sameSite}`;

    // Add expiration date
    const expirationDate = new Date();
    expirationDate.setDate(expirationDate.getDate() + days);
    cookieString += `; expires=${expirationDate.toUTCString()}`;

    // Add secure flag if specified
    if (secure) {
      cookieString += "; secure";
    }

    // Set the cookie
    document.cookie = cookieString;
  } catch (error) {
    console.error("Error setting cookie:", error.message);
  }
}

// Utility function to get a cookie value by name
function getCookie(name) {
  try {
    // Validate input
    if (!name || typeof name !== "string") {
      throw new Error("Cookie name must be a non-empty string.");
    }

    // Parse cookies
    const cookies = document.cookie.split("; ").reduce((acc, cookie) => {
      const [key, value] = cookie.split("=");
      acc[key] = decodeURIComponent(value);
      return acc;
    }, {});

    // Return requested cookie value
    return cookies[name] || null;
  } catch (error) {
    console.error("Error getting cookie:", error.message);
    return null;
  }
}

// Utility function to delete a cookie
function deleteCookie(name, path = "/") {
  try {
    // Validate input
    if (!name || typeof name !== "string") {
      throw new Error("Cookie name must be a non-empty string.");
    }

    // Set expiration date to a past date
    document.cookie = `${name}=; path=${path}; expires=Thu, 01 Jan 1970 00:00:00 UTC`;
  } catch (error) {
    console.error("Error deleting cookie:", error.message);
  }
}

// Example usage of the cookie utility functions
try {
  // Set a cookie
  setCookie("userToken", "12345", 7, "/", true, "Strict");

  // Retrieve the cookie
  const userToken = getCookie("userToken");
  console.log("Retrieved cookie value:", userToken);

  // Delete the cookie
  deleteCookie("userToken");
  console.log("Cookie deleted successfully.");
} catch (error) {
  console.error("General error:", error.message);
}

/**
 * Common issues related to cookies in JavaScript:
 * 1. Cookies exceeding size limits (usually 4KB per cookie).
 * 2. Missing secure flag for sensitive data (use the `secure` option).
 * 3. Special characters in cookie values causing encoding issues (use `encodeURIComponent`).
 * 4. Cookie scope not being properly set (use `path` and `samesite` appropriately).
 * 5. Cookies not being available in cross-origin requests (understand `SameSite` restrictions).
 */
```
