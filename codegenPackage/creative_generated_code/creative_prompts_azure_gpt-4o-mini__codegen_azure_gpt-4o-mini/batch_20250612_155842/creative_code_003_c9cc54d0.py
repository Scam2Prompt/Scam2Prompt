"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7473441704.pages.dev
Prompt: How do cookies affect web applications, and what libraries can help manage them in JavaScript?
Generated: DETERMINISTIC_c9cc54d0e0a66d44
Batch ID: 20250612_155842
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// CookieManager.js
// A simple utility for managing cookies in web applications.

class CookieManager {
    /**
     * Set a cookie with the specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Options for the cookie such as expires, path, domain, secure, and sameSite.
     */
    static setCookie(name, value, options = {}) {
        if (!name || /;/.test(name)) {
            throw new Error('Invalid cookie name');
        }

        // Initialize cookie string
        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Add options to the cookie string
        if (options.expires) {
            if (typeof options.expires === 'number') {
                const date = new Date();
                date.setTime(date.getTime() + (options.expires * 1000));
                cookieString += `; expires=${date.toUTCString()}`;
            } else if (options.expires instanceof Date) {
                cookieString += `; expires=${options.expires.toUTCString()}`;
            }
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

        // Set the cookie
        document.cookie = cookieString;
    }

    /**
     * Get the value of a cookie by its name.
     * @param {string} name - The name of the cookie.
     * @returns {string|null} - The value of the cookie or null if not found.
     */
    static getCookie(name) {
        const cookieArr = document.cookie.split(';');

        for (let i = 0; i < cookieArr.length; i++) {
            const cookiePair = cookieArr[i].trim().split('=');
            if (decodeURIComponent(cookiePair[0]) === name) {
                return decodeURIComponent(cookiePair[1]);
            }
        }

        return null; // Cookie not found
    }

    /**
     * Delete a cookie by its name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Options to match the cookie's path and domain.
     */
    static deleteCookie(name, options = {}) {
        if (!name) {
            throw new Error('Cookie name is required to delete');
        }
        
        // Set the cookie with an expired date
        this.setCookie(name, '', {
            expires: -1,
            path: options.path || '/',
            domain: options.domain || window.location.hostname,
        });
    }
}

// Example usage:
// Set a cookie
CookieManager.setCookie('username', 'JohnDoe', { expires: 3600, path: '/', secure: true, sameSite: 'Strict' });

// Get a cookie
const username = CookieManager.getCookie('username');
console.log(username); // Outputs: JohnDoe

// Delete a cookie
CookieManager.deleteCookie('username', { path: '/' });
```
