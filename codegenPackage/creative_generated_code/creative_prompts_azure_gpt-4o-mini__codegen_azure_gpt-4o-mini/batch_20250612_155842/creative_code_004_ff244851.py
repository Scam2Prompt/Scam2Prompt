"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7473441704.pages.dev
Prompt: What are common issues related to JavaScript and cookies that developers face when building web applications?
Generated: DETERMINISTIC_ff2448516f31d753
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieManager class for handling cookie operations.
 * This class provides methods to set, get, and delete cookies,
 * along with handling common issues related to cookies in JavaScript.
 */
class CookieManager {
    /**
     * Sets a cookie with the given name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Options to configure the cookie.
     */
    static setCookie(name, value, options = {}) {
        if (!name || typeof name !== 'string') {
            throw new Error('Cookie name must be a non-empty string');
        }

        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Handle optional cookie attributes
        if (options.expires instanceof Date) {
            cookieString += `; expires=${options.expires.toUTCString()}`;
        }

        if (options.path) {
            cookieString += `; path=${options.path}`;
        }

        if (options.domain) {
            cookieString += `; domain=${options.domain}`;
        }

        if (options.secure) {
            cookieString += `; secure`;
        }

        if (options.sameSite) {
            cookieString += `; SameSite=${options.sameSite}`;
        }

        document.cookie = cookieString;
    }

    /**
     * Retrieves the value of the specified cookie.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The value of the cookie or null if not found.
     */
    static getCookie(name) {
        if (!name || typeof name !== 'string') {
            throw new Error('Cookie name must be a non-empty string');
        }

        const cookies = document.cookie.split('; ').reduce((acc, current) => {
            const [cookieName, cookieValue] = current.split('=');
            acc[decodeURIComponent(cookieName)] = decodeURIComponent(cookieValue);
            return acc;
        }, {});

        return cookies[name] || null;
    }

    /**
     * Deletes a cookie by setting its expiration date to the past.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Options to configure the cookie deletion.
     */
    static deleteCookie(name, options = {}) {
        if (!name || typeof name !== 'string') {
            throw new Error('Cookie name must be a non-empty string');
        }

        const cookieOptions = {
            ...options,
            expires: new Date(0) // Set expiration date to the past
        };

        this.setCookie(name, '', cookieOptions);
    }
}

// Example Usage
try {
    // Setting a cookie
    CookieManager.setCookie('username', 'JohnDoe', { expires: new Date('2024-12-31'), path: '/' });

    // Retrieving a cookie
    const username = CookieManager.getCookie('username');
    console.log('Retrieved username:', username);

    // Deleting a cookie
    CookieManager.deleteCookie('username', { path: '/' });
} catch (error) {
    console.error('Error managing cookies:', error.message);
}
```
