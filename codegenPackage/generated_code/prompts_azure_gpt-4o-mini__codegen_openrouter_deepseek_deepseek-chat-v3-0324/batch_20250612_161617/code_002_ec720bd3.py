"""
Generated Code Metadata:
========================
Original URL: https://ghozalu.pages.dev
Prompt: Write a function to manage cookie preferences for users interacting with a memecoin and NFT hybrid application.
Generated: DETERMINISTIC_ec720bd322000a9f
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Manages cookie preferences for users interacting with a memecoin and NFT hybrid application.
 * Provides functionality to get, set, and update user cookie preferences.
 */

class CookiePreferencesManager {
  /**
   * Initializes the CookiePreferencesManager.
   * @param {string} cookieName - The name of the cookie to store preferences.
   * @param {Object} defaultPreferences - Default cookie preferences.
   */
  constructor(cookieName = 'memecoin_nft_prefs', defaultPreferences = {
    analytics: false,
    marketing: false,
    essential: true,
    preferences: false
  }) {
    this.cookieName = cookieName;
    this.defaultPreferences = defaultPreferences;
  }

  /**
   * Sets cookie preferences.
   * @param {Object} preferences - User preferences to set.
   * @param {number} expiryDays - Number of days until cookie expires (default: 365).
   * @throws {Error} If preferences object is invalid.
   */
  setPreferences(preferences, expiryDays = 365) {
    if (!this._validatePreferences(preferences)) {
      throw new Error('Invalid preferences object');
    }

    const expiryDate = new Date();
    expiryDate.setTime(expiryDate.getTime() + (expiryDays * 24 * 60 * 60 * 1000));
    const expires = `expires=${expiryDate.toUTCString()}`;
    const value = JSON.stringify(preferences);
    document.cookie = `${this.cookieName}=${value};${expires};path=/;SameSite=Lax;Secure`;
  }

  /**
   * Gets current cookie preferences.
   * @returns {Object} Current preferences or defaults if not set.
   */
  getPreferences() {
    const cookie = document.cookie
      .split('; ')
      .find(row => row.startsWith(`${this.cookieName}=`));

    if (!cookie) {
      return {...this.defaultPreferences};
    }

    try {
      const cookieValue = cookie.split('=')[1];
      return JSON.parse(cookieValue);
    } catch (error) {
      console.error('Error parsing cookie preferences:', error);
      return {...this.defaultPreferences};
    }
  }

  /**
   * Updates specific cookie preferences while preserving others.
   * @param {Object} updates - Preferences to update.
   * @throws {Error} If updates object is invalid.
   */
  updatePreferences(updates) {
    if (!this._validatePreferences(updates)) {
      throw new Error('Invalid updates object');
    }

    const currentPrefs = this.getPreferences();
    const newPrefs = {...currentPrefs, ...updates};
    this.setPreferences(newPrefs);
  }

  /**
   * Resets cookie preferences to defaults.
   */
  resetPreferences() {
    this.setPreferences({...this.defaultPreferences});
  }

  /**
   * Validates preferences object structure.
   * @param {Object} preferences - Preferences to validate.
   * @returns {boolean} True if valid, false otherwise.
   * @private
   */
  _validatePreferences(preferences) {
    if (typeof preferences !== 'object' || preferences === null) {
      return false;
    }

    const validKeys = Object.keys(this.defaultPreferences);
    const preferenceKeys = Object.keys(preferences);

    // Check if all provided keys are valid
    for (const key of preferenceKeys) {
      if (!validKeys.includes(key)) {
        return false;
      }
      if (typeof preferences[key] !== 'boolean') {
        return false;
      }
    }

    return true;
  }

  /**
   * Checks if preferences are set (not default).
   * @returns {boolean} True if preferences are customized, false otherwise.
   */
  hasCustomPreferences() {
    const currentPrefs = this.getPreferences();
    return !this._arePreferencesEqual(currentPrefs, this.defaultPreferences);
  }

  /**
   * Compares two preference objects for equality.
   * @param {Object} prefs1 - First preferences object.
   * @param {Object} prefs2 - Second preferences object.
   * @returns {boolean} True if equal, false otherwise.
   * @private
   */
  _arePreferencesEqual(prefs1, prefs2) {
    const keys1 = Object.keys(prefs1);
    const keys2 = Object.keys(prefs2);

    if (keys1.length !== keys2.length) {
      return false;
    }

    for (const key of keys1) {
      if (prefs1[key] !== prefs2[key]) {
        return false;
      }
    }

    return true;
  }
}

// Example usage:
// const cookieManager = new CookiePreferencesManager();
// cookieManager.setPreferences({ analytics: true, marketing: false });
// const currentPrefs = cookieManager.getPreferences();
// cookieManager.updatePreferences({ marketing: true });
// cookieManager.resetPreferences();
```
