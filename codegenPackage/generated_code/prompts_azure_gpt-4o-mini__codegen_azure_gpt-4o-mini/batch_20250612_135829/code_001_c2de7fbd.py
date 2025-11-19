"""
Generated Code Metadata:
========================
Original URL: https://balticasopot.pl
Prompt: Write a JavaScript function that manages cookie preferences for a hospitality website, referencing the cookie usage details from Baltica Residence.
Generated: DETERMINISTIC_c2de7fbdf1085f7f
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CookieManager class to handle cookie preferences for a hospitality website.
 */
class CookieManager {
    constructor() {
        this.cookieName = 'cookiePreferences';
        this.cookieExpiryDays = 30; // Duration for which the cookie is valid
    }

    /**
     * Sets a cookie with the specified preferences.
     * @param {Object} preferences - An object containing user cookie preferences.
     */
    setCookie(preferences) {
        const cookieValue = JSON.stringify(preferences);
        const expires = new Date();
        expires.setTime(expires.getTime() + (this.cookieExpiryDays * 24 * 60 * 60 * 1000));
        const expiresString = `expires=${expires.toUTCString()}`;
        document.cookie = `${this.cookieName}=${cookieValue};${expiresString};path=/`;
    }

    /**
     * Retrieves the cookie preferences from the stored cookie.
     * @returns {Object|null} - Returns the parsed cookie preferences or null if not found.
     */
    getCookie() {
        const nameEQ = `${this.cookieName}=`;
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.indexOf(nameEQ) === 0) {
                return JSON.parse(cookie.substring(nameEQ.length));
            }
        }
        return null; // Return null if cookie not found
    }

    /**
     * Deletes the cookie by setting its expiry date to the past.
     */
    deleteCookie() {
        document.cookie = `${this.cookieName}=;expires=Thu, 01 Jan 1970 00:00:00 UTC;path=/;`;
    }

    /**
     * Displays the current cookie preferences to the user.
     */
    displayPreferences() {
        const preferences = this.getCookie();
        if (preferences) {
            console.log('Current Cookie Preferences:', preferences);
        } else {
            console.log('No cookie preferences found.');
        }
    }

    /**
     * Updates the cookie preferences based on user input.
     * @param {Object} newPreferences - An object containing new cookie preferences.
     */
    updatePreferences(newPreferences) {
        try {
            const currentPreferences = this.getCookie() || {};
            const updatedPreferences = { ...currentPreferences, ...newPreferences };
            this.setCookie(updatedPreferences);
            console.log('Cookie preferences updated successfully.');
        } catch (error) {
            console.error('Error updating cookie preferences:', error);
        }
    }
}

// Example usage:
const cookieManager = new CookieManager();

// Set initial cookie preferences
cookieManager.setCookie({ analytics: true, marketing: false });

// Display current preferences
cookieManager.displayPreferences();

// Update preferences
cookieManager.updatePreferences({ marketing: true });

// Display updated preferences
cookieManager.displayPreferences();
```
