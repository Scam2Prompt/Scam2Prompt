"""
Generated Code Metadata:
========================
Original URL: https://alghanim-capital.com
Prompt: Write code to implement a consent management system for tracking user preferences, similar to the cookie management system described on Alghanim Capital's website.
Generated: DETERMINISTIC_e5ad3482851edf1f
Batch ID: 20250612_153854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// ConsentManager.js - A consent management system for tracking user preferences

class ConsentManager {
  constructor(options = {}) {
    // Default configuration
    this.defaultConfig = {
      cookieName: 'user_consent_preferences',
      cookieExpiryDays: 365,
      cookieDomain: window.location.hostname,
      cookiePath: '/',
      cookieSecure: false,
      categories: {
        necessary: {
          title: 'Necessary',
          description: 'These cookies are essential for the website to function properly.',
          required: true,
          enabled: true
        },
        analytics: {
          title: 'Analytics',
          description: 'These cookies help us understand how visitors interact with our website.',
          required: false,
          enabled: false
        },
        marketing: {
          title: 'Marketing',
          description: 'These cookies are used to track visitors across websites.',
          required: false,
          enabled: false
        },
        preferences: {
          title: 'Preferences',
          description: 'These cookies allow the website to remember choices you make.',
          required: false,
          enabled: false
        }
      }
    };

    // Merge user options with defaults
    this.config = { ...this.defaultConfig, ...options };

    // Initialize consent preferences
    this.consentPreferences = this.loadPreferences();
  }

  /**
   * Load user consent preferences from cookie
   * @returns {Object} User consent preferences
   */
  loadPreferences() {
    try {
      const cookieValue = this.getCookie(this.config.cookieName);
      if (cookieValue) {
        return JSON.parse(cookieValue);
      }
      return this.getDefaultPreferences();
    } catch (error) {
      console.error('Error loading consent preferences:', error);
      return this.getDefaultPreferences();
    }
  }

  /**
   * Get default consent preferences based on configuration
   * @returns {Object} Default consent preferences
   */
  getDefaultPreferences() {
    const defaultPrefs = {};
    Object.keys(this.config.categories).forEach(category => {
      defaultPrefs[category] = this.config.categories[category].enabled;
    });
    return defaultPrefs;
  }

  /**
   * Save user consent preferences to cookie
   * @param {Object} preferences - User consent preferences to save
   */
  savePreferences(preferences) {
    try {
      const expiryDate = new Date();
      expiryDate.setDate(expiryDate.getDate() + this.config.cookieExpiryDays);

      const cookieValue = JSON.stringify(preferences);
      let cookieString = `${this.config.cookieName}=${encodeURIComponent(cookieValue)};`;
      cookieString += `expires=${expiryDate.toUTCString()};`;
      cookieString += `path=${this.config.cookiePath};`;
      cookieString += `domain=${this.config.cookieDomain};`;
      if (this.config.cookieSecure) {
        cookieString += 'secure;';
      }

      document.cookie = cookieString;
      this.consentPreferences = preferences;
    } catch (error) {
      console.error('Error saving consent preferences:', error);
    }
  }

  /**
   * Get cookie value by name
   * @param {string} name - Cookie name
   * @returns {string|null} Cookie value or null if not found
   */
  getCookie(name) {
    const cookies = document.cookie.split(';');
    for (const cookie of cookies) {
      const [cookieName, cookieValue] = cookie.trim().split('=');
      if (cookieName === name) {
        return decodeURIComponent(cookieValue);
      }
    }
    return null;
  }

  /**
   * Check if a consent category is enabled
   * @param {string} category - Consent category to check
   * @returns {boolean} Whether the category is enabled
   */
  isCategoryEnabled(category) {
    if (!this.config.categories[category]) {
      console.warn(`Consent category '${category}' does not exist`);
      return false;
    }
    return this.consentPreferences[category] || false;
  }

  /**
   * Set consent for a specific category
   * @param {string} category - Consent category to update
   * @param {boolean} enabled - Whether to enable or disable the category
   */
  setCategory(category, enabled) {
    if (!this.config.categories[category]) {
      console.warn(`Cannot set consent for unknown category '${category}'`);
      return;
    }

    if (this.config.categories[category].required) {
      console.warn(`Cannot modify required category '${category}'`);
      return;
    }

    const newPreferences = { ...this.consentPreferences };
    newPreferences[category] = enabled;
    this.savePreferences(newPreferences);
  }

  /**
   * Set consent for all categories at once
   * @param {Object} preferences - Object with category preferences
   */
  setAllCategories(preferences) {
    const newPreferences = { ...this.consentPreferences };

    Object.keys(preferences).forEach(category => {
      if (this.config.categories[category] && !this.config.categories[category].required) {
        newPreferences[category] = preferences[category];
      }
    });

    this.savePreferences(newPreferences);
  }

  /**
   * Reset all consent preferences to default values
   */
  resetPreferences() {
    this.savePreferences(this.getDefaultPreferences());
  }

  /**
   * Get current consent preferences
   * @returns {Object} Current consent preferences
   */
  getPreferences() {
    return { ...this.consentPreferences };
  }

  /**
   * Get configuration for all consent categories
   * @returns {Object} Consent categories configuration
   */
  getCategories() {
    return { ...this.config.categories };
  }
}

// Example usage:
// const consentManager = new ConsentManager();
// consentManager.setCategory('analytics', true);
// console.log(consentManager.isCategoryEnabled('analytics'));
```
