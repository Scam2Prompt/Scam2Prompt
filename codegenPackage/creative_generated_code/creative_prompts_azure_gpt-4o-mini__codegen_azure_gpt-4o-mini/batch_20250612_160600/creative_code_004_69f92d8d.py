"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://abubit.com
Prompt: What are best practices for optimizing website experience through cookie usage as hinted at on abubit.com?
Generated: DETERMINISTIC_69f92d8df8ea7662
Batch ID: 20250612_160600
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieManager.js - A module to handle cookies efficiently for optimizing website experience

class CookieManager {
    constructor() {
        // Initializes the cookie manager
    }

    /**
     * Sets a cookie with the specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - An object containing cookie options (expires, path, domain, secure, sameSite).
     */
    setCookie(name, value, options = {}) {
        try {
            let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

            // Add expiration date if provided
            if (options.expires) {
                const expiresDate = new Date(options.expires);
                cookieString += `; expires=${expiresDate.toUTCString()}`;
            }

            // Add path if provided
            if (options.path) {
                cookieString += `; path=${options.path}`;
            } else {
                cookieString += '; path=/'; // Default path is root
            }

            // Add domain if provided
            if (options.domain) {
                cookieString += `; domain=${options.domain}`;
            }

            // Add secure flag if provided
            if (options.secure) {
                cookieString += '; secure';
            }

            // Add sameSite attribute if provided
            if (options.sameSite) {
                cookieString += `; samesite=${options.sameSite}`;
            }

            document.cookie = cookieString;
        } catch (error) {
            console.error('Error setting cookie:', error);
        }
    }

    /**
     * Gets the value of a cookie by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The value of the cookie or null if not found.
     */
    getCookie(name) {
        try {
            const cookieArr = document.cookie.split(';');

            for (let cookie of cookieArr) {
                // Trim whitespace and check for the desired cookie
                const trimmedCookie = cookie.trim();
                if (trimmedCookie.startsWith(`${encodeURIComponent(name)}=`)) {
                    return decodeURIComponent(trimmedCookie.split('=')[1]);
                }
            }
            return null; // Cookie not found
        } catch (error) {
            console.error('Error getting cookie:', error);
            return null; // Return null on error
        }
    }

    /**
     * Deletes a cookie by name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - An object containing cookie options (path, domain).
     */
    deleteCookie(name, options = {}) {
        try {
            this.setCookie(name, '', { 
                expires: 'Thu, 01 Jan 1970 00:00:00 GMT', 
                path: options.path || '/',
                domain: options.domain || undefined 
            });
        } catch (error) {
            console.error('Error deleting cookie:', error);
        }
    }

    /**
     * Checks if a cookie exists by name.
     * @param {string} name - The name of the cookie to check.
     * @returns {boolean} - True if the cookie exists, false otherwise.
     */
    cookieExists(name) {
        return this.getCookie(name) !== null;
    }
}

// Usage Example
const cookieManager = new CookieManager();

// Set a cookie with a 7 days expiration
cookieManager.setCookie('userSession', 'abc123', { expires: Date.now() + 7 * 24 * 60 * 60 * 1000 });

// Get the value of the cookie
const userSession = cookieManager.getCookie('userSession');
console.log('User Session:', userSession);

// Check if a cookie exists
const exists = cookieManager.cookieExists('userSession');
console.log('Cookie exists:', exists);

// Delete the cookie
cookieManager.deleteCookie('userSession');
```
