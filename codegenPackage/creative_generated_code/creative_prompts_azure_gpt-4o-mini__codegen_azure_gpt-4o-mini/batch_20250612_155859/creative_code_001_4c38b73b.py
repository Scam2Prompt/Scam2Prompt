"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coderemixsetup-5s7.pages.dev
Prompt: What are the best practices for configuring JavaScript and cookie settings in web development?
Generated: DETERMINISTIC_4c38b73bb8bf900b
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Utility: A simple utility for handling cookies in web applications

class CookieManager {
    /**
     * Sets a cookie with the given name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Additional options for the cookie.
     */
    static setCookie(name, value, options = {}) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }

        // Construct cookie string
        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)};`;

        // Add expiration date if specified
        if (options.expires) {
            if (options.expires instanceof Date) {
                cookieString += `expires=${options.expires.toUTCString()};`;
            } else {
                throw new Error('Expires option must be a Date object');
            }
        }

        // Add path option
        if (options.path) {
            cookieString += `path=${options.path};`;
        }

        // Add secure flag if specified
        if (options.secure) {
            cookieString += `secure;`;
        }

        // Add SameSite attribute
        if (options.sameSite) {
            cookieString += `SameSite=${options.sameSite};`;
        }

        // Set the cookie
        document.cookie = cookieString;
    }

    /**
     * Retrieves the value of a cookie by name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} The value of the cookie or null if not found.
     */
    static getCookie(name) {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }

        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [key, value] = cookie.trim().split('=');
            if (key === encodeURIComponent(name)) {
                return decodeURIComponent(value);
            }
        }
        return null; // Cookie not found
    }

    /**
     * Deletes a cookie by setting its expiration date to a past date.
     * @param {string} name - The name of the cookie to delete.
     * @param {string} path - The path where the cookie was set.
     */
    static deleteCookie(name, path = '/') {
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }
        document.cookie = `${encodeURIComponent(name)}=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=${path};`;
    }
}

// Example usage:
try {
    // Set a cookie
    CookieManager.setCookie('username', 'JohnDoe', { 
        expires: new Date(Date.now() + 86400e3), // 1 day expiration
        path: '/',
        secure: true,
        sameSite: 'Strict' 
    });

    // Retrieve a cookie
    const username = CookieManager.getCookie('username');
    console.log(`Username: ${username}`);

    // Delete the cookie
    CookieManager.deleteCookie('username');
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
