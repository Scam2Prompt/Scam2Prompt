"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://finance-masa.pages.dev
Prompt: How can I implement cookie management in a JavaScript application to enhance user experience, based on the cookie categories mentioned on the Masa site?
Generated: DETERMINISTIC_cb4395f12dd0e5fd
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Management Module
class CookieManager {
    constructor() {
        // Initialize empty cookie categories
        this.cookies = {
            essential: [],
            analytics: [],
            marketing: []
        };
    }

    /**
     * Set a cookie
     * @param {string} name - The name of the cookie
     * @param {string} value - The value of the cookie
     * @param {number} days - Number of days until the cookie expires
     * @param {string} category - The category of the cookie
     */
    setCookie(name, value, days, category) {
        if (!this.cookies[category]) {
            console.error(`Category ${category} does not exist.`);
            return;
        }

        const expires = new Date(Date.now() + days * 24 * 60 * 60 * 1000).toUTCString();
        document.cookie = `${name}=${value}; expires=${expires}; path=/`;

        // Store in internal cookie management
        this.cookies[category].push({ name, value, expires });
    }

    /**
     * Get a cookie value by name
     * @param {string} name - The name of the cookie
     * @returns {string|null} - The cookie value or null if not found
     */
    getCookie(name) {
        const cookieArray = document.cookie.split('; ');
        for (let cookie of cookieArray) {
            const [cookieName, cookieValue] = cookie.split('=');
            if (cookieName === name) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null;
    }

    /**
     * Delete a cookie by name
     * @param {string} name - The name of the cookie
     * @param {string} category - The category of the cookie
     */
    deleteCookie(name, category) {
        if (!this.cookies[category]) {
            console.error(`Category ${category} does not exist.`);
            return;
        }

        this.setCookie(name, '', -1, category); // Set expiration in the past to delete
        this.cookies[category] = this.cookies[category].filter(cookie => cookie.name !== name);
    }

    /**
     * Check if the user has given consent for a specific cookie category
     * @param {string} category - The category to check
     * @returns {boolean} - True if consent is given, false otherwise
     */
    hasConsent(category) {
        // This function can be expanded based on the consent management logic
        // For demonstration, returning true for essential cookies
        return category === 'essential';
    }

    /**
     * Initialize cookies based on user consent
     */
    initCookies() {
        // Logic to obtain user consent can be implemented here
        // For the purpose of this example, we assume consent is given
        if (this.hasConsent('analytics')) {
            this.setCookie('analytics_enabled', 'true', 30, 'analytics');
        }
        if (this.hasConsent('marketing')) {
            this.setCookie('marketing_enabled', 'true', 30, 'marketing');
        }
    }
}

// Usage example:
const cookieManager = new CookieManager();
cookieManager.initCookies();

// Setting a cookie
cookieManager.setCookie('user_session', 'abc123', 7, 'essential');

// Getting a cookie
const userSession = cookieManager.getCookie('user_session');
console.log(`User session: ${userSession}`);

// Deleting a cookie
cookieManager.deleteCookie('user_session', 'essential');
```
