"""
Generated Code Metadata:
========================
Original URL: https://status.ttec.smartteam.chat
Prompt: Develop a JavaScript function that dynamically adjusts cookie settings on the TTEC STC Cluster Status website based on user preferences, ensuring compliance with essential and functional cookie requirements.
Generated: DETERMINISTIC_910fb5753c2542a1
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Manager for TTEC STC Cluster Status Website
 * Handles dynamic adjustment of cookie settings based on user preferences
 * Ensures compliance with essential and functional cookie requirements
 */

class CookieManager {
  /**
   * Initialize CookieManager with default settings
   * @param {Object} options - Configuration options
   * @param {string} options.prefix - Cookie name prefix
   * @param {number} options.expiryDays - Default cookie expiry in days
   * @param {Object} options.cookieTypes - Cookie categories and their defaults
   */
  constructor(options = {}) {
    this.prefix = options.prefix || 'ttc_stc_';
    this.expiryDays = options.expiryDays || 365;
    this.cookieTypes = options.cookieTypes || {
      essential: {
        enabled: true,
        required: true,
        description: 'Essential cookies required for website functionality'
      },
      functional: {
        enabled: false,
        required: false,
        description: 'Functional cookies for enhanced user experience'
      }
    };
    
    this.init();
  }

  /**
   * Initialize cookie settings from stored preferences or defaults
   */
  init() {
    if (!this.getCookie(`${this.prefix}consent`)) {
      this.setDefaultPreferences();
    } else {
      this.loadPreferences();
    }
  }

  /**
   * Set default cookie preferences
   */
  setDefaultPreferences() {
    Object.keys(this.cookieTypes).forEach(type => {
      this.setCookiePreference(type, this.cookieTypes[type].enabled);
    });
    this.setCookie(`${this.prefix}consent`, 'false', this.expiryDays);
  }

  /**
   * Load saved cookie preferences
   */
  loadPreferences() {
    Object.keys(this.cookieTypes).forEach(type => {
      const value = this.getCookie(`${this.prefix}${type}`);
      if (value !== null) {
        this.cookieTypes[type].enabled = value === 'true';
      }
    });
  }

  /**
   * Set cookie preference for a specific type
   * @param {string} type - Cookie type (essential, functional, etc.)
   * @param {boolean} enabled - Whether the cookie type is enabled
   */
  setCookiePreference(type, enabled) {
    if (!this.cookieTypes[type]) {
      console.error(`Invalid cookie type: ${type}`);
      return;
    }
    
    if (this.cookieTypes[type].required) {
      enabled = true;
    }
    
    this.cookieTypes[type].enabled = enabled;
    this.setCookie(`${this.prefix}${type}`, enabled.toString(), this.expiryDays);
    
    if (type === 'essential') {
      this.setCookie(`${this.prefix}consent`, 'true', this.expiryDays);
    }
  }

  /**
   * Set a cookie
   * @param {string} name - Cookie name
   * @param {string} value - Cookie value
   * @param {number} days - Expiry in days
   */
  setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
  }

  /**
   * Get a cookie value by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const nameEQ = `${name}=`;
    const cookies = document.cookie.split(';');
    
    for (let i = 0; i < cookies.length; i++) {
      let cookie = cookies[i];
      while (cookie.charAt(0) === ' ') {
        cookie = cookie.substring(1);
      }
      if (cookie.indexOf(nameEQ) === 0) {
        return cookie.substring(nameEQ.length);
      }
    }
    return null;
  }

  /**
   * Delete a cookie
   * @param {string} name - Cookie name
   */
  deleteCookie(name) {
    this.setCookie(name, '', -1);
  }

  /**
   * Check if a cookie type is enabled
   * @param {string} type - Cookie type
   * @returns {boolean} Whether the cookie type is enabled
   */
  isEnabled(type) {
    if (!this.cookieTypes[type]) {
      console.error(`Invalid cookie type: ${type}`);
      return false;
    }
    return this.cookieTypes[type].enabled;
  }

  /**
   * Save all current preferences
   */
  savePreferences() {
    Object.keys(this.cookieTypes).forEach(type => {
      this.setCookiePreference(type, this.cookieTypes[type].enabled);
    });
    this.setCookie(`${this.prefix}consent`, 'true', this.expiryDays);
  }

  /**
   * Reset all preferences to defaults
   */
  resetPreferences() {
    Object.keys(this.cookieTypes).forEach(type => {
      this.setCookiePreference(type, this.cookieTypes[type].required);
    });
    this.setCookie(`${this.prefix}consent`, 'false', this.expiryDays);
  }

  /**
   * Get current cookie settings
   * @returns {Object} Current cookie preferences
   */
  getPreferences() {
    return JSON.parse(JSON.stringify(this.cookieTypes));
  }
}

// Example usage:
// const cookieManager = new CookieManager();
// cookieManager.setCookiePreference('functional', true);
// cookieManager.savePreferences();
```
