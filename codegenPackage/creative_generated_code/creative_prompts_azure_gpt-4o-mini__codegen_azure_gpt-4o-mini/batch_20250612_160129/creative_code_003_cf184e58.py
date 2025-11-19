"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://photon-soitinyastro.pages.dev
Prompt: What libraries can I use to manage cookies in JavaScript for better user experience?
Generated: DETERMINISTIC_cf184e586134f001
Batch ID: 20250612_160129
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
     * Sets a cookie in the browser.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Additional options for the cookie (e.g., expires, path, domain, secure).
     */
    static setCookie(name, value, options = {}) {
        if (!name || !value) {
            throw new Error("Both name and value are required to set a cookie.");
        }

        let expires = options.expires ? `; expires=${options.expires.toUTCString()}` : '';
        let path = options.path ? `; path=${options.path}` : '';
        let domain = options.domain ? `; domain=${options.domain}` : '';
        let secure = options.secure ? '; secure' : '';

        document.cookie = `${name}=${encodeURIComponent(value)}${expires}${path}${domain}${secure}`;
    }

    /**
     * Retrieves a cookie value by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The cookie value or null if cookie doesn't exist.
     */
    static getCookie(name) {
        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === name) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null; // Cookie not found
    }

    /**
     * Deletes a cookie by name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Additional options for the cookie (e.g., path, domain).
     */
    static deleteCookie(name, options = {}) {
        if (!name) {
            throw new Error("Name is required to delete a cookie.");
        }

        const path = options.path ? `; path=${options.path}` : '';
        const domain = options.domain ? `; domain=${options.domain}` : '';
        
        // Set the cookie's expiration date to the past to delete it
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC;${path}${domain}`;
    }
}

// Example usage:
try {
    CookieManager.setCookie('user', 'JohnDoe', { expires: new Date(Date.now() + 1000 * 60 * 60 * 24), path: '/' });
    console.log(CookieManager.getCookie('user')); // Outputs: JohnDoe
    CookieManager.deleteCookie('user', { path: '/' });
    console.log(CookieManager.getCookie('user')); // Outputs: null
} catch (error) {
    console.error('Error managing cookies:', error);
}
```

This code provides a simple `CookieManager` class to handle cookie operations, ensuring proper error handling and following best practices for JavaScript coding.
