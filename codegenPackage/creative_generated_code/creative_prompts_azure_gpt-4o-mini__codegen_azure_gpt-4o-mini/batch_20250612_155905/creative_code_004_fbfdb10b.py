"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demoz999.pages.dev
Prompt: How do I troubleshoot issues related to JavaScript and cookie settings on a web page?
Generated: DETERMINISTIC_fbfdb10b1f9f9563
Batch ID: 20250612_155905
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieManager class to handle cookie operations for troubleshooting.
 */
class CookieManager {
    /**
     * Set a cookie with specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Options for the cookie (expires, path, domain, secure, samesite).
     */
    setCookie(name, value, options = {}) {
        if (!name || typeof name !== 'string') {
            console.error('Invalid cookie name');
            return;
        }
        if (typeof value !== 'string') {
            console.error('Invalid cookie value');
            return;
        }

        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Handle cookie options
        if (options.expires) {
            if (typeof options.expires === 'number') {
                const date = new Date();
                date.setTime(date.getTime() + options.expires * 1000);
                cookieString += `; expires=${date.toUTCString()}`;
            } else {
                console.error('Invalid expires option');
            }
        }
        if (options.path) cookieString += `; path=${options.path}`;
        if (options.domain) cookieString += `; domain=${options.domain}`;
        if (options.secure) cookieString += `; secure`;
        if (options.samesite) cookieString += `; samesite=${options.samesite}`;

        document.cookie = cookieString;
    }

    /**
     * Get a cookie by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} - The cookie value or null if not found.
     */
    getCookie(name) {
        if (!name || typeof name !== 'string') {
            console.error('Invalid cookie name');
            return null;
        }

        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === encodeURIComponent(name)) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null; // Cookie not found
    }

    /**
     * Delete a cookie by name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Options for the cookie (path, domain).
     */
    deleteCookie(name, options = {}) {
        if (!name || typeof name !== 'string') {
            console.error('Invalid cookie name');
            return;
        }

        // Set cookie with an expired date
        this.setCookie(name, '', { expires: -1, path: options.path, domain: options.domain });
    }

    /**
     * Log all cookies to the console for troubleshooting.
     */
    logCookies() {
        const cookies = document.cookie.split(';');
        console.log('Current cookies:');
        cookies.forEach(cookie => {
            console.log(cookie.trim());
        });
    }
}

// Example usage:
const cookieManager = new CookieManager();

// Set a cookie
cookieManager.setCookie('testCookie', 'testValue', { expires: 3600, path: '/' });

// Get a cookie
const cookieValue = cookieManager.getCookie('testCookie');
console.log(`Value of testCookie: ${cookieValue}`);

// Log all cookies
cookieManager.logCookies();

// Delete a cookie
cookieManager.deleteCookie('testCookie', { path: '/' });
```
