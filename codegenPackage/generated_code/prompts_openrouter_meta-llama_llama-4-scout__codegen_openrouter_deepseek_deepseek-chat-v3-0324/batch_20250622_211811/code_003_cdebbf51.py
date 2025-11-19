"""
Generated Code Metadata:
========================
Original URL: https://claims-stether.org
Prompt: Create a basic example of how to use the `document.cookie` API to save and retrieve user preferences regarding cookie usage on a website, inspired by Amazon.es's user interface.
Generated: DETERMINISTIC_cdebbf5169dce3ec
Batch ID: 20250622_211811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Utility Module
 * Provides functions to manage user preferences via cookies.
 * Inspired by Amazon.es's cookie preferences interface.
 */

/**
 * Sets a cookie with the given name, value, and expiration days.
 * @param {string} name - Cookie name
 * @param {string} value - Cookie value
 * @param {number} days - Days until cookie expires
 */
function setCookie(name, value, days) {
    try {
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = `expires=${date.toUTCString()}`;
        document.cookie = `${name}=${value};${expires};path=/;SameSite=Lax`;
    } catch (error) {
        console.error('Error setting cookie:', error);
    }
}

/**
 * Gets the value of a cookie by name.
 * @param {string} name - Cookie name to retrieve
 * @returns {string|null} Cookie value or null if not found
 */
function getCookie(name) {
    try {
        const cookieName = `${name}=`;
        const cookies = document.cookie.split(';');
        
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.indexOf(cookieName) === 0) {
                return cookie.substring(cookieName.length, cookie.length);
            }
        }
        return null;
    } catch (error) {
        console.error('Error getting cookie:', error);
        return null;
    }
}

/**
 * Deletes a cookie by name.
 * @param {string} name - Cookie name to delete
 */
function deleteCookie(name) {
    try {
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;`;
    } catch (error) {
        console.error('Error deleting cookie:', error);
    }
}

/**
 * Saves user preferences for cookie usage.
 * @param {Object} preferences - User preferences object
 * @param {boolean} preferences.necessary - Necessary cookies preference
 * @param {boolean} preferences.preferences - Preferences cookies preference
 * @param {boolean} preferences.statistics - Statistics cookies preference
 * @param {boolean} preferences.marketing - Marketing cookies preference
 */
function saveCookiePreferences(preferences) {
    try {
        const preferencesString = JSON.stringify(preferences);
        setCookie('cookie_preferences', preferencesString, 365);
    } catch (error) {
        console.error('Error saving cookie preferences:', error);
    }
}

/**
 * Retrieves user cookie preferences.
 * @returns {Object|null} User preferences object or null if not found
 */
function getCookiePreferences() {
    try {
        const preferencesString = getCookie('cookie_preferences');
        return preferencesString ? JSON.parse(preferencesString) : null;
    } catch (error) {
        console.error('Error retrieving cookie preferences:', error);
        return null;
    }
}

/**
 * Example usage:
 * 
 * // Save preferences
 * saveCookiePreferences({
 *     necessary: true,
 *     preferences: true,
 *     statistics: false,
 *     marketing: false
 * });
 * 
 * // Retrieve preferences
 * const preferences = getCookiePreferences();
 * console.log('User preferences:', preferences);
 * 
 * // Delete preferences
 * deleteCookie('cookie_preferences');
 */
```
