"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://status.ttec.smartteam.chat
Prompt: Develop a JavaScript function that dynamically adjusts cookie settings on the TTEC STC Cluster Status website based on user preferences, ensuring compliance with essential and functional cookie requirements.
Generated: DETERMINISTIC_910fb5753c2542a1
Batch ID: 20250612_154742
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Dynamically adjusts cookie settings on the TTEC STC Cluster Status website 
 * based on user preferences, ensuring compliance with essential 
 * and functional cookie requirements.
 */

/**
 * Adjusts cookies based on user preferences.
 * @param {Object} userPreferences - Object containing user cookie preferences.
 * @property {boolean} userPreferences.acceptEssential - Whether to accept essential cookies.
 * @property {boolean} userPreferences.acceptFunctional - Whether to accept functional cookies.
 */
function adjustCookieSettings(userPreferences) {
  try {
    // Validate user preferences object
    if (!userPreferences || typeof userPreferences !== 'object') {
      throw new Error('Invalid user preferences object');
    }

    const { acceptEssential, acceptFunctional } = userPreferences;

    // Ensure essential cookies are always enabled (mandatory for compliance)
    if (acceptEssential === false) {
      console.warn('Essential cookies cannot be disabled as they are required for site functionality.');
    }

    // Configure essential cookies
    setCookie('essential_cookies', 'enabled', 365); // Mandatory, enabled for 365 days

    // Configure functional cookies based on user preference
    if (acceptFunctional) {
      setCookie('functional_cookies', 'enabled', 365); // Enabled for 365 days
    } else {
      deleteCookie('functional_cookies'); // Disable functional cookies
    }

    console.log('Cookie settings successfully updated based on user preferences.');
  } catch (error) {
    console.error('An error occurred while adjusting cookie settings:', error.message);
  }
}

/**
 * Sets a cookie with the specified name, value, and expiration days.
 * @param {string} name - Name of the cookie.
 * @param {string} value - Value of the cookie.
 * @param {number} days - Expiration time in days.
 */
function setCookie(name, value, days) {
  try {
    const date = new Date();
    date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${value}; ${expires}; path=/`;
  } catch (error) {
    console.error('An error occurred while setting the cookie:', error.message);
  }
}

/**
 * Deletes a cookie by name.
 * @param {string} name - Name of the cookie to delete.
 */
function deleteCookie(name) {
  try {
    document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/`;
  } catch (error) {
    console.error('An error occurred while deleting the cookie:', error.message);
  }
}

// Example usage:
// User preferences object
const userPreferences = {
  acceptEssential: true,  // Mandatory, always true
  acceptFunctional: false // User decision
};

// Adjust cookie settings based on user preferences
adjustCookieSettings(userPreferences);
```
