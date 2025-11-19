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
 * CookieManager class to handle cookie settings based on user preferences.
 */
class CookieManager {
    constructor() {
        this.cookies = {
            essential: true,
            functional: false,
        };
    }

    /**
     * Initializes the cookie settings based on user preferences.
     * @param {Object} userPreferences - User's cookie preferences.
     */
    init(userPreferences) {
        try {
            this.setCookies(userPreferences);
            this.applyCookies();
        } catch (error) {
            console.error("Error initializing cookie settings:", error);
        }
    }

    /**
     * Sets the cookie preferences based on user input.
     * @param {Object} userPreferences - User's cookie preferences.
     */
    setCookies(userPreferences) {
        if (userPreferences) {
            this.cookies.essential = userPreferences.essential !== undefined ? userPreferences.essential : this.cookies.essential;
            this.cookies.functional = userPreferences.functional !== undefined ? userPreferences.functional : this.cookies.functional;
        }
    }

    /**
     * Applies the cookie settings to the website.
     */
    applyCookies() {
        try {
            if (this.cookies.essential) {
                this.setCookie('essential', 'true', 365);
            }
            if (this.cookies.functional) {
                this.setCookie('functional', 'true', 365);
            }
        } catch (error) {
            console.error("Error applying cookie settings:", error);
        }
    }

    /**
     * Sets a cookie in the browser.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until the cookie expires.
     */
    setCookie(name, value, days) {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = `${name}=${encodeURIComponent(value)}; expires=${expires}; path=/`;
    }

    /**
     * Retrieves the value of a specified cookie.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The value of the cookie or null if not found.
     */
    getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return decodeURIComponent(parts.pop().split(';').shift());
        return null;
    }
}

// Example usage:
const userPreferences = {
    essential: true,
    functional: true,
};

const cookieManager = new CookieManager();
cookieManager.init(userPreferences);
```
