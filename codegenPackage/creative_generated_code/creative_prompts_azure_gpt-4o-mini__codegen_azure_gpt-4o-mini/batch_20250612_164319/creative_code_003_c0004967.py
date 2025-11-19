"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://retrofunding-optimism-5.pages.dev
Prompt: What libraries can help manage cookies in JavaScript for web applications?
Generated: DETERMINISTIC_c00049677feb071c
Batch ID: 20250612_164319
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieManager.js
class CookieManager {
    /**
     * Sets a cookie with the specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} [options] - Optional settings for the cookie.
     */
    static setCookie(name, value, options = {}) {
        if (!name || !value) {
            throw new Error('Cookie name and value are required');
        }

        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Set cookie options
        if (options.expires) {
            if (typeof options.expires === 'number') {
                const date = new Date();
                date.setTime(date.getTime() + (options.expires * 1000)); // Convert to milliseconds
                options.expires = date.toUTCString();
            }
            cookieString += `; expires=${options.expires}`;
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

        document.cookie = cookieString;
    }

    /**
     * Gets the value of a cookie by its name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} The value of the cookie or null if not found.
     */
    static getCookie(name) {
        const cookies = document.cookie.split('; ');
        for (const cookie of cookies) {
            const [cookieName, cookieValue] = cookie.split('=');
            if (decodeURIComponent(cookieName) === name) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null; // Return null if cookie is not found
    }

    /**
     * Deletes a cookie by setting its expiration date to the past.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} [options] - Optional settings for the cookie.
     */
    static deleteCookie(name, options = {}) {
        if (!name) {
            throw new Error('Cookie name is required to delete');
        }

        // Set the cookie with the past expiration date
        const cookieOptions = {
            ...options,
            expires: -1 // Set expires to a past date
        };
        this.setCookie(name, '', cookieOptions);
    }
}

// Example usage:
try {
    CookieManager.setCookie('user', 'John Doe', { expires: 3600, path: '/' });
    console.log(CookieManager.getCookie('user')); // Outputs: John Doe
    CookieManager.deleteCookie('user', { path: '/' });
    console.log(CookieManager.getCookie('user')); // Outputs: null
} catch (error) {
    console.error('Error managing cookies:', error.message);
}
```
