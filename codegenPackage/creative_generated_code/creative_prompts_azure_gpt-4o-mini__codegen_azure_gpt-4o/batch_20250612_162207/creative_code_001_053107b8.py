"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claims-masafinance.pages.dev
Prompt: Write a JavaScript function to customize cookie consent preferences based on user interactions, inspired by the Masa Finance cookie policy.
Generated: DETERMINISTIC_053107b8d974a997
Batch ID: 20250612_162207
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to manage cookie consent preferences based on user interactions.
 * Inspired by Masa Finance cookie policy.
 * 
 * This function allows users to customize their cookie preferences
 * and dynamically updates the cookie settings accordingly.
 */

// Enum for cookie categories
const COOKIE_CATEGORIES = {
  ESSENTIAL: 'essential',
  PERFORMANCE: 'performance',
  FUNCTIONAL: 'functional',
  TARGETING: 'targeting',
};

// Default cookie preferences (essential cookies are always enabled)
const defaultPreferences = {
  [COOKIE_CATEGORIES.ESSENTIAL]: true,
  [COOKIE_CATEGORIES.PERFORMANCE]: false,
  [COOKIE_CATEGORIES.FUNCTIONAL]: false,
  [COOKIE_CATEGORIES.TARGETING]: false,
};

/**
 * Updates the user's cookie preferences and stores them.
 * @param {Object} preferences - User's updated cookie preferences.
 */
function updateCookiePreferences(preferences) {
  try {
    // Validate input preferences
    if (typeof preferences !== 'object') {
      throw new Error('Invalid preferences format. Expected an object.');
    }

    // Merge preferences with default settings
    const updatedPreferences = { ...defaultPreferences, ...preferences };

    // Store preferences in a cookie (valid for 1 year)
    const cookieValue = encodeURIComponent(JSON.stringify(updatedPreferences));
    const expiryDate = new Date();
    expiryDate.setFullYear(expiryDate.getFullYear() + 1); // 1-year expiration
    document.cookie = `cookiePreferences=${cookieValue}; expires=${expiryDate.toUTCString()}; path=/`;

    console.log('Cookie preferences updated:', updatedPreferences);
  } catch (error) {
    console.error('Error updating cookie preferences:', error.message);
  }
}

/**
 * Gets the current cookie preferences stored in the browser.
 * @returns {Object} - Current cookie preferences or default preferences if none are set.
 */
function getCookiePreferences() {
  try {
    // Retrieve the cookie
    const cookies = document.cookie.split('; ').reduce((acc, cookie) => {
      const [name, value] = cookie.split('=');
      acc[name] = decodeURIComponent(value);
      return acc;
    }, {});

    // Parse the cookie preferences
    const preferences = cookies.cookiePreferences
      ? JSON.parse(cookies.cookiePreferences)
      : defaultPreferences;

    return preferences;
  } catch (error) {
    console.error('Error retrieving cookie preferences:', error.message);
    return defaultPreferences;
  }
}

/**
 * Displays a cookie consent banner to collect user preferences.
 * @param {Function} onSave - Callback function to handle saving preferences.
 */
function showCookieConsentBanner(onSave) {
  // Create banner elements
  const banner = document.createElement('div');
  banner.id = 'cookie-consent-banner';
  banner.style.cssText = 'position: fixed; bottom: 0; left: 0; right: 0; background: #333; color: #fff; padding: 10px; text-align: center; z-index: 1000;';
  banner.innerHTML = `
    <p>We use cookies to improve your experience. Customize your preferences:</p>
    <label><input type="checkbox" id="performance"> Performance Cookies</label>
    <label><input type="checkbox" id="functional"> Functional Cookies</label>
    <label><input type="checkbox" id="targeting"> Targeting Cookies</label>
    <button id="savePreferences" style="margin-left: 10px;">Save Preferences</button>
  `;

  // Append banner to the page
  document.body.appendChild(banner);

  // Attach event listener to save button
  document.getElementById('savePreferences').addEventListener('click', () => {
    const preferences = {
      [COOKIE_CATEGORIES.PERFORMANCE]: document.getElementById('performance').checked,
      [COOKIE_CATEGORIES.FUNCTIONAL]: document.getElementById('functional').checked,
      [COOKIE_CATEGORIES.TARGETING]: document.getElementById('targeting').checked,
    };
    onSave(preferences);

    // Remove banner after saving preferences
    document.body.removeChild(banner);
  });
}

// Example usage
document.addEventListener('DOMContentLoaded', () => {
  const currentPreferences = getCookiePreferences();

  console.log('Current cookie preferences:', currentPreferences);

  showCookieConsentBanner((preferences) => {
    updateCookiePreferences(preferences);
  });
});
```
