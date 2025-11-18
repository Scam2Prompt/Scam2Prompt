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
 * CookieManager handles the dynamic adjustment of cookie settings
 * based on user preferences while ensuring compliance with essential
 * and functional cookie requirements.
 */
class CookieManager {
    constructor() {
        this.cookies = {};
        this.defaultSettings = {
            essential: true,
            functional: false,
            analytics: false,
        };
    }

    /**
     * Initializes the cookie settings based on user preferences.
     */
    init() {
        this.loadPreferences();
        this.applyCookies();
    }

    /**
     * Loads user preferences from local storage or defaults.
     */
    loadPreferences() {
        try {
            const preferences = JSON.parse(localStorage.getItem('cookiePreferences'));
            this.cookies = preferences ? { ...this.defaultSettings, ...preferences } : this.defaultSettings;
        } catch (error) {
            console.error('Error loading cookie preferences:', error);
            this.cookies = this.defaultSettings; // Fallback to default settings
        }
    }

    /**
     * Applies cookies based on the loaded preferences.
     */
    applyCookies() {
        try {
            if (this.cookies.essential) {
                this.setCookie('essentialCookie', 'true', 365);
            }

            if (this.cookies.functional) {
                this.setCookie('functionalCookie', 'true', 365);
            }

            if (this.cookies.analytics) {
                this.setCookie('analyticsCookie', 'true', 365);
            }
        } catch (error) {
            console.error('Error applying cookies:', error);
        }
    }

    /**
     * Sets a cookie with the specified name, value, and expiration in days.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until the cookie expires.
     */
    setCookie(name, value, days) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (days * 24 * 60 * 60 * 1000));
        const expiresString = `expires=${expires.toUTCString()}`;
        document.cookie = `${name}=${value};${expiresString};path=/;`;
    }

    /**
     * Updates the cookie preferences based on user input.
     * @param {Object} preferences - An object containing the updated user preferences.
     */
    updatePreferences(preferences) {
        try {
            this.cookies = { ...this.cookies, ...preferences };
            localStorage.setItem('cookiePreferences', JSON.stringify(this.cookies));
            this.applyCookies();
        } catch (error) {
            console.error('Error updating cookie preferences:', error);
        }
    }
}

// Example usage:
// Create an instance of CookieManager
const cookieManager = new CookieManager();
// Initialize cookies on page load
cookieManager.init();

// Example of updating preferences (should be triggered by user actions)
document.getElementById('acceptFunctionalCookies').addEventListener('change', (event) => {
    cookieManager.updatePreferences({ functional: event.target.checked });
});

document.getElementById('acceptAnalyticsCookies').addEventListener('change', (event) => {
    cookieManager.updatePreferences({ analytics: event.target.checked });
});
```
