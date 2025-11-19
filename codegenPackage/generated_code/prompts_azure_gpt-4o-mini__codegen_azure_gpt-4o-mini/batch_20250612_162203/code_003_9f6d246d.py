"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a JavaScript function to manage necessary and functional cookies, reflecting the cookie categories used by Masa.
Generated: DETERMINISTIC_9f6d246d5012da6f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * CookieManager class to handle necessary and functional cookies.
 */
class CookieManager {
    /**
     * Sets a cookie with the specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Options for the cookie (expires, path, domain, secure, sameSite).
     */
    static setCookie(name, value, options = {}) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }
        if (typeof value !== 'string') {
            throw new Error('Invalid cookie value');
        }

        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Handle cookie options
        if (options.expires) {
            const expiresDate = new Date(options.expires);
            if (isNaN(expiresDate.getTime())) {
                throw new Error('Invalid expires date');
            }
            cookieString += `; expires=${expiresDate.toUTCString()}`;
        }
        if (options.path) {
            cookieString += `; path=${options.path}`;
        }
        if (options.domain) {
            cookieString += `; domain=${options.domain}`;
        }
        if (options.secure) {
            cookieString += '; secure';
        }
        if (options.sameSite) {
            cookieString += `; SameSite=${options.sameSite}`;
        }

        document.cookie = cookieString;
    }

    /**
     * Retrieves the value of a cookie by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The value of the cookie or null if not found.
     */
    static getCookie(name) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }

        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (decodeURIComponent(cookieName) === name) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null; // Cookie not found
    }

    /**
     * Deletes a cookie by name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Options for the cookie (path, domain).
     */
    static deleteCookie(name, options = {}) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }

        // Set the cookie with an expired date
        this.setCookie(name, '', { expires: 'Thu, 01 Jan 1970 00:00:00 GMT', ...options });
    }

    /**
     * Checks if a cookie exists by name.
     * @param {string} name - The name of the cookie to check.
     * @returns {boolean} - True if the cookie exists, false otherwise.
     */
    static cookieExists(name) {
        return this.getCookie(name) !== null;
    }
}

// Example usage:
// Set a necessary cookie
CookieManager.setCookie('session_id', 'abc123', { path: '/', expires: 'Fri, 31 Dec 9999 23:59:59 GMT' });

// Set a functional cookie
CookieManager.setCookie('user_preferences', JSON.stringify({ theme: 'dark' }), { path: '/' });

// Get a cookie
const sessionId = CookieManager.getCookie('session_id');
console.log('Session ID:', sessionId);

// Check if a cookie exists
const exists = CookieManager.cookieExists('user_preferences');
console.log('User Preferences Cookie Exists:', exists);

// Delete a cookie
CookieManager.deleteCookie('session_id', { path: '/' });
```
