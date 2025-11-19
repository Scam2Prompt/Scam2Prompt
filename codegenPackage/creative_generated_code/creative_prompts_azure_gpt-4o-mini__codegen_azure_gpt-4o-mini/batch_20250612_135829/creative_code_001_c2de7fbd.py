"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://balticasopot.pl
Prompt: Write a JavaScript function that manages cookie preferences for a hospitality website, referencing the cookie usage details from Baltica Residence.
Generated: DETERMINISTIC_c2de7fbdf1085f7f
Batch ID: 20250612_135829
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieManager class for managing cookie preferences on a hospitality website.
 * This class allows users to accept, reject, or review cookie usage.
 */
class CookieManager {
    constructor() {
        this.cookies = {
            necessary: true,
            preferences: false,
            statistics: false,
            marketing: false,
        };
    }

    /**
     * Initializes the cookie preferences based on saved settings.
     * If no settings are saved, defaults are used.
     */
    init() {
        const savedCookies = this.getCookies();
        if (savedCookies) {
            this.cookies = savedCookies;
        } else {
            this.saveCookies(this.cookies);
        }
    }

    /**
     * Accepts all cookie categories.
     */
    acceptAll() {
        this.cookies = {
            necessary: true,
            preferences: true,
            statistics: true,
            marketing: true,
        };
        this.saveCookies(this.cookies);
        this.showConfirmation('All cookies accepted.');
    }

    /**
     * Rejects all non-necessary cookies.
     */
    rejectAll() {
        this.cookies = {
            necessary: true,
            preferences: false,
            statistics: false,
            marketing: false,
        };
        this.saveCookies(this.cookies);
        this.showConfirmation('Non-necessary cookies rejected.');
    }

    /**
     * Updates the preference for a specific cookie category.
     * @param {string} category - The cookie category to update.
     * @param {boolean} value - The user's preference (true to accept, false to reject).
     */
    updatePreference(category, value) {
        if (this.cookies.hasOwnProperty(category)) {
            this.cookies[category] = value;
            this.saveCookies(this.cookies);
            this.showConfirmation(`${category} cookies updated to ${value}.`);
        } else {
            console.error(`Error: Invalid cookie category "${category}".`);
        }
    }

    /**
     * Saves the current cookie preferences in localStorage.
     * @param {object} cookies - The cookie preferences to save.
     */
    saveCookies(cookies) {
        try {
            localStorage.setItem('cookiePreferences', JSON.stringify(cookies));
        } catch (error) {
            console.error('Error saving cookie preferences:', error);
        }
    }

    /**
     * Retrieves the cookie preferences from localStorage.
     * @returns {object|null} - The saved cookie preferences or null if not found.
     */
    getCookies() {
        try {
            const cookies = localStorage.getItem('cookiePreferences');
            return cookies ? JSON.parse(cookies) : null;
        } catch (error) {
            console.error('Error retrieving cookie preferences:', error);
            return null;
        }
    }

    /**
     * Displays a confirmation message to the user.
     * @param {string} message - The message to display.
     */
    showConfirmation(message) {
        console.log(message); // Replace with actual UI confirmation logic.
    }
}

// Usage example:
const cookieManager = new CookieManager();
cookieManager.init();

// Accept all cookies
// cookieManager.acceptAll();

// Reject all non-necessary cookies
// cookieManager.rejectAll();

// Update specific cookie preference
// cookieManager.updatePreference('statistics', true);
```
