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
 * Handles user preferences for cookie settings.
 * This function allows users to set, update, and retrieve their cookie preferences.
 * It uses localStorage to persist preferences and provides error handling for unsupported browsers.
 */

// Define the cookie preferences handler
const CookiePreferences = (() => {
  const STORAGE_KEY = 'userCookiePreferences';

  /**
   * Saves user preferences to localStorage.
   * @param {Object} preferences - An object containing cookie preferences (e.g., { analytics: true, marketing: false }).
   */
  const savePreferences = (preferences) => {
    try {
      if (typeof preferences !== 'object') {
        throw new Error('Preferences must be an object.');
      }
      localStorage.setItem(STORAGE_KEY, JSON.stringify(preferences));
    } catch (error) {
      console.error('Failed to save cookie preferences:', error.message);
    }
  };

  /**
   * Retrieves user preferences from localStorage.
   * @returns {Object|null} - The stored preferences object, or null if not set.
   */
  const getPreferences = () => {
    try {
      const preferences = localStorage.getItem(STORAGE_KEY);
      return preferences ? JSON.parse(preferences) : null;
    } catch (error) {
      console.error('Failed to retrieve cookie preferences:', error.message);
      return null;
    }
  };

  /**
   * Updates a specific preference in the stored preferences.
   * @param {string} key - The preference key to update (e.g., 'analytics').
   * @param {boolean} value - The new value for the preference.
   */
  const updatePreference = (key, value) => {
    try {
      const preferences = getPreferences() || {};
      preferences[key] = value;
      savePreferences(preferences);
    } catch (error) {
      console.error('Failed to update cookie preference:', error.message);
    }
  };

  /**
   * Clears all stored preferences.
   */
  const clearPreferences = () => {
    try {
      localStorage.removeItem(STORAGE_KEY);
    } catch (error) {
      console.error('Failed to clear cookie preferences:', error.message);
    }
  };

  // Public API
  return {
    savePreferences,
    getPreferences,
    updatePreference,
    clearPreferences,
  };
})();

// Example usage:
// Save preferences
CookiePreferences.savePreferences({ analytics: true, marketing: false });

// Get preferences
const userPreferences = CookiePreferences.getPreferences();
console.log('User Preferences:', userPreferences);

// Update a specific preference
CookiePreferences.updatePreference('analytics', false);

// Clear all preferences
CookiePreferences.clearPreferences();
```
