"""
Generated Code Metadata:
========================
Original URL: https://www.giselabravo.com
Prompt: Develop a script to manage cookie preferences and GDPR compliance for a website, similar to the cookie management system explained on Gisela Bravo's site.
Generated: DETERMINISTIC_7078d9ad04d29318
Batch ID: 20250612_154958
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// cookie-preferences.js

/**
 * Cookie Preferences Manager
 * 
 * This script manages user cookie preferences and GDPR compliance.
 * It allows users to opt-in or opt-out of different cookie categories.
 */

// Define cookie categories
const COOKIE_CATEGORIES = {
  essential: 'essential',
  analytics: 'analytics',
  marketing: 'marketing',
  socialMedia: 'socialMedia',
};

// Define default cookie preferences
const DEFAULT_COOKIE_PREFERENCES = {
  [COOKIE_CATEGORIES.essential]: true,
  [COOKIE_CATEGORIES.analytics]: false,
  [COOKIE_CATEGORIES.marketing]: false,
  [COOKIE_CATEGORIES.socialMedia]: false,
};

// Cookie Preferences Manager class
class CookiePreferencesManager {
  /**
   * Initialize the cookie preferences manager.
   */
  constructor() {
    this.cookiePreferences = this.getCookiePreferences();
  }

  /**
   * Get the user's current cookie preferences.
   * 
   * @returns {Object} The user's current cookie preferences.
   */
  getCookiePreferences() {
    const storedPreferences = localStorage.getItem('cookiePreferences');
    return storedPreferences ? JSON.parse(storedPreferences) : DEFAULT_COOKIE_PREFERENCES;
  }

  /**
   * Save the user's cookie preferences.
   * 
   * @param {Object} preferences The user's cookie preferences.
   */
  saveCookiePreferences(preferences) {
    localStorage.setItem('cookiePreferences', JSON.stringify(preferences));
    this.cookiePreferences = preferences;
    this.updateCookies();
  }

  /**
   * Update cookies based on the user's preferences.
   */
  updateCookies() {
    // Delete cookies that are not allowed
    Object.keys(COOKIE_CATEGORIES).forEach(category => {
      if (!this.cookiePreferences[category]) {
        this.deleteCookie(category);
      }
    });

    // Set cookies that are allowed
    Object.keys(COOKIE_CATEGORIES).forEach(category => {
      if (this.cookiePreferences[category]) {
        this.setCookie(category, 'allowed');
      }
    });
  }

  /**
   * Set a cookie.
   * 
   * @param {string} name The cookie name.
   * @param {string} value The cookie value.
   */
  setCookie(name, value) {
    const date = new Date();
    date.setTime(date.getTime() + (30 * 24 * 60 * 60 * 1000)); // 30 days
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/`;
  }

  /**
   * Delete a cookie.
   * 
   * @param {string} name The cookie name.
   */
  deleteCookie(name) {
    document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/`;
  }

  /**
   * Get the user's consent for a specific cookie category.
   * 
   * @param {string} category The cookie category.
   * @returns {boolean} Whether the user has given consent for the category.
   */
  hasConsent(category) {
    return this.cookiePreferences[category];
  }

  /**
   * Revoke the user's consent for a specific cookie category.
   * 
   * @param {string} category The cookie category.
   */
  revokeConsent(category) {
    this.saveCookiePreferences({ ...this.cookiePreferences, [category]: false });
  }

  /**
   * Check if the user has given consent for any cookies.
   * 
   * @returns {boolean} Whether the user has given consent for any cookies.
   */
  hasAnyConsent() {
    return Object.values(this.cookiePreferences).some(consent => consent);
  }
}

// Initialize the cookie preferences manager
const cookiePreferencesManager = new CookiePreferencesManager();

// Example usage:
function main() {
  // Get the current cookie preferences
  const preferences = cookiePreferencesManager.getCookiePreferences();
  console.log(preferences);

  // Save new cookie preferences
  const newPreferences = {
    ...preferences,
    [COOKIE_CATEGORIES.analytics]: true,
  };
  cookiePreferencesManager.saveCookiePreferences(newPreferences);

  // Check if the user has given consent for analytics cookies
  const hasAnalyticsConsent = cookiePreferencesManager.hasConsent(COOKIE_CATEGORIES.analytics);
  console.log(hasAnalyticsConsent);
}

main();
```
