"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Create a JavaScript function to handle user preferences for cookie settings, similar to the functionality on the Baltica Sopot website, and explain how it works.
Generated: DETERMINISTIC_65f4b3c6eaf76f84
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Preferences Manager
 * Handles user preferences for cookie settings similar to Baltica Sopot website
 * Provides functionality to set, get, and manage cookie consent preferences
 */

class CookiePreferences {
  /**
   * Initialize cookie preferences
   * @param {Object} options - Configuration options
   * @param {string} options.cookieName - Name of the cookie to store preferences
   * @param {number} options.expiryDays - Number of days until cookie expires
   * @param {Object} options.defaultPreferences - Default preferences if none set
   */
  constructor(options = {}) {
    this.cookieName = options.cookieName || 'cookie_preferences';
    this.expiryDays = options.expiryDays || 365;
    this.defaultPreferences = options.defaultPreferences || {
      necessary: true,
      preferences: false,
      statistics: false,
      marketing: false
    };
    
    this.preferences = this.getPreferences();
    this.initEventListeners();
  }

  /**
   * Get current preferences from cookie
   * @returns {Object} Current preferences object
   */
  getPreferences() {
    const cookieValue = this.getCookie(this.cookieName);
    
    if (cookieValue) {
      try {
        return JSON.parse(cookieValue);
      } catch (e) {
        console.error('Error parsing cookie preferences:', e);
        return {...this.defaultPreferences};
      }
    }
    
    return {...this.defaultPreferences};
  }

  /**
   * Save preferences to cookie
   * @param {Object} preferences - Preferences to save
   */
  savePreferences(preferences) {
    try {
      const serialized = JSON.stringify(preferences);
      this.setCookie(this.cookieName, serialized, this.expiryDays);
      this.preferences = {...preferences};
      this.dispatchEvent('preferencesUpdated', this.preferences);
    } catch (e) {
      console.error('Error saving preferences:', e);
    }
  }

  /**
   * Set a cookie with given name, value and expiration
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {number} days - Expiration in days
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Get cookie value by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (let cookie of cookies) {
      cookie = cookie.trim();
      if (cookie.startsWith(`${name}=`)) {
        return cookie.substring(name.length + 1);
      }
    }
    return null;
  }

  /**
   * Initialize event listeners for UI elements
   */
  initEventListeners() {
    // Listen for cookie banner accept all button
    document.addEventListener('click', (e) => {
      if (e.target.matches('.cookie-accept-all')) {
        this.savePreferences({
          necessary: true,
          preferences: true,
          statistics: true,
          marketing: true
        });
        this.hideBanner();
      }
    });

    // Listen for cookie banner save preferences button
    document.addEventListener('click', (e) => {
      if (e.target.matches('.cookie-save-preferences')) {
        const preferences = {
          necessary: true,
          preferences: document.getElementById('preferences-cookies').checked,
          statistics: document.getElementById('statistics-cookies').checked,
          marketing: document.getElementById('marketing-cookies').checked
        };
        this.savePreferences(preferences);
        this.hideBanner();
      }
    });

    // Listen for cookie banner reject all button
    document.addEventListener('click', (e) => {
      if (e.target.matches('.cookie-reject-all')) {
        this.savePreferences({
          necessary: true,
          preferences: false,
          statistics: false,
          marketing: false
        });
        this.hideBanner();
      }
    });
  }

  /**
   * Hide the cookie banner
   */
  hideBanner() {
    const banner = document.querySelector('.cookie-banner');
    if (banner) {
      banner.style.display = 'none';
    }
  }

  /**
   * Dispatch custom event
   * @param {string} eventName - Name of the event
   * @param {Object} detail - Event detail data
   */
  dispatchEvent(eventName, detail) {
    const event = new CustomEvent(eventName, { detail });
    document.dispatchEvent(event);
  }

  /**
   * Check if specific cookie category is enabled
   * @param {string} category - Category to check
   * @returns {boolean} Whether category is enabled
   */
  isEnabled(category) {
    return this.preferences[category] || false;
  }
}

// Example usage:
// const cookieManager = new CookiePreferences();
// if (!cookieManager.getCookie('cookie_preferences')) {
//   document.querySelector('.cookie-banner').style.display = 'block';
// }
```
