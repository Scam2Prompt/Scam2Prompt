"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: How can I implement cookie management in a JavaScript application to enhance user experience, based on the cookie categories mentioned on the Masa site?
Generated: DETERMINISTIC_cb4395f12dd0e5fd
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
 * Cookie Management Utility for JavaScript applications
 * This script provides methods to manage cookies based on categories
 * commonly seen on cookie consent banners (e.g., Masa site).
 * Categories: Necessary, Functional, Analytics, Marketing
 */

// Utility functions for managing cookies
const CookieManager = {
  /**
   * Sets a cookie with a specified name, value, and expiration days.
   * @param {string} name - The name of the cookie.
   * @param {string} value - The value of the cookie.
   * @param {number} days - The number of days before the cookie expires.
   */
  setCookie(name, value, days) {
    try {
      const date = new Date();
      date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
      const expires = "expires=" + date.toUTCString();
      document.cookie = `${name}=${value};${expires};path=/;secure;SameSite=Strict`;
    } catch (error) {
      console.error("Error setting cookie:", error);
    }
  },

  /**
   * Gets the value of a cookie by name.
   * @param {string} name - The name of the cookie.
   * @returns {string|null} - The value of the cookie, or null if not found.
   */
  getCookie(name) {
    try {
      const nameEQ = name + "=";
      const cookies = document.cookie.split("; ");
      for (let cookie of cookies) {
        if (cookie.indexOf(nameEQ) === 0) {
          return cookie.substring(nameEQ.length);
        }
      }
      return null;
    } catch (error) {
      console.error("Error retrieving cookie:", error);
      return null;
    }
  },

  /**
   * Deletes a cookie by name.
   * @param {string} name - The name of the cookie.
   */
  deleteCookie(name) {
    try {
      this.setCookie(name, "", -1); // Set expiration to the past to delete the cookie
    } catch (error) {
      console.error("Error deleting cookie:", error);
    }
  },

  /**
   * Checks if a specific cookie category is accepted.
   * Categories: Necessary, Functional, Analytics, Marketing.
   * @param {string} category - The cookie category to check.
   * @returns {boolean} - True if the category is accepted, false otherwise.
   */
  isCategoryAccepted(category) {
    try {
      const consentCookie = this.getCookie("cookieConsent");
      if (!consentCookie) return false;

      const consent = JSON.parse(consentCookie);
      return consent[category] === true;
    } catch (error) {
      console.error("Error checking cookie category consent:", error);
      return false;
    }
  },

  /**
   * Stores user cookie consent preferences.
   * @param {Object} preferences - An object containing user preferences for cookie categories.
   * Example: { Necessary: true, Functional: false, Analytics: true, Marketing: false }
   */
  setCookieConsent(preferences) {
    try {
      const jsonPreferences = JSON.stringify(preferences);
      this.setCookie("cookieConsent", jsonPreferences, 365); // Store consent for 1 year
    } catch (error) {
      console.error("Error saving cookie consent preferences:", error);
    }
  },
};

// Example usage:
// Setting cookie consent preferences (call when user submits consent form)
CookieManager.setCookieConsent({
  Necessary: true,
  Functional: false,
  Analytics: true,
  Marketing: false,
});

// Checking if a specific category (e.g., "Analytics") is accepted
if (CookieManager.isCategoryAccepted("Analytics")) {
  console.log("Analytics cookies are accepted. Proceed with tracking.");
} else {
  console.log("Analytics cookies are not accepted.");
}

// Setting a cookie only if the user has accepted 'Functional' cookies
if (CookieManager.isCategoryAccepted("Functional")) {
  CookieManager.setCookie("userLanguage", "en", 30); // Example: set user language preference
}

// Retrieving a cookie value
const userLanguage = CookieManager.getCookie("userLanguage");
console.log("User language preference:", userLanguage);

// Deleting a cookie (e.g., on user logout)
CookieManager.deleteCookie("userLanguage");
```

This script provides a reusable utility for cookie management in JavaScript applications, adhering to best practices and ensuring proper error handling.
