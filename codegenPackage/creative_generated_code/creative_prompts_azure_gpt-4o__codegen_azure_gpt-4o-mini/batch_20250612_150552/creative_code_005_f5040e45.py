"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomtoken.pages.dev
Prompt: Generate code to implement cookie management for the Venom Technologies website, including essential, performance, and functionality cookies, as described in the Cookies Policy.
Generated: DETERMINISTIC_f5040e45726dabd3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Management Module for Venom Technologies Website

class CookieManager {
    constructor() {
        this.cookies = this.getCookies();
    }

    // Get all cookies as an object
    getCookies() {
        return document.cookie.split('; ').reduce((cookies, cookie) => {
            const [name, value] = cookie.split('=');
            cookies[decodeURIComponent(name)] = decodeURIComponent(value);
            return cookies;
        }, {});
    }

    // Set a cookie with options for expiration and path
    setCookie(name, value, days = 30, path = '/') {
        const expires = new Date(Date.now() + days * 864e5).toUTCString();
        document.cookie = `${encodeURIComponent(name)}=${encodeURIComponent(value)}; expires=${expires}; path=${path}; SameSite=Lax; Secure`;
    }

    // Delete a cookie by name
    deleteCookie(name, path = '/') {
        this.setCookie(name, '', -1, path);
    }

    // Check if a specific cookie exists
    cookieExists(name) {
        return this.cookies.hasOwnProperty(decodeURIComponent(name));
    }

    // Get the value of a specific cookie
    getCookieValue(name) {
        return this.cookieExists(name) ? this.cookies[decodeURIComponent(name)] : null;
    }

    // Function to manage the setting of cookies based on user preferences
    manageCookies(preferences) {
        // Essential cookies: Required for site functionality
        this.setCookie('essential_cookie', 'true');

        // Performance cookies: Used for analytics and performance tracking
        if (preferences.performanceCookies) {
            this.setCookie('performance_cookie', 'true');
        }

        // Functionality cookies: Enhance user experience
        if (preferences.functionalityCookies) {
            this.setCookie('functionality_cookie', 'true');
        }
    }
}

// Example usage of the CookieManager
try {
    const cookieManager = new CookieManager();

    // User preferences for cookies
    const userPreferences = {
        performanceCookies: true, // User agreed to performance cookies
        functionalityCookies: false // User declined functionality cookies
    };

    // Managing cookies based on user preferences
    cookieManager.manageCookies(userPreferences);

    // Log current cookies for debugging
    console.log('Current Cookies:', cookieManager.cookies);
} catch (error) {
    console.error('An error occurred while managing cookies:', error);
}
```
