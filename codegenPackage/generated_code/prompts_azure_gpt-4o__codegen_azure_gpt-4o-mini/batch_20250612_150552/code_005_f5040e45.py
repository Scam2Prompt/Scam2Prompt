"""
Generated Code Metadata:
========================
Original URL: https://venomtoken.pages.dev
Prompt: Generate code to implement cookie management for the Venom Technologies website, including essential, performance, and functionality cookies, as described in the Cookies Policy.
Generated: DETERMINISTIC_f5040e45726dabd3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Cookie Management Module for Venom Technologies Website

// CookieManager class to handle cookie operations
class CookieManager {
    // Set a cookie with specified name, value, and options
    static setCookie(name, value, options = {}) {
        // Validate cookie name and value
        if (!name || typeof name !== 'string') {
            throw new Error('Invalid cookie name');
        }
        if (typeof value !== 'string') {
            throw new Error('Invalid cookie value');
        }

        // Set default options
        options = {
            path: '/',
            'max-age': 3600, // Default to 1 hour
            secure: true, // Use secure cookies
            sameSite: 'Lax', // Default SameSite policy
            ...options
        };

        // Construct cookie string
        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Append options to cookie string
        for (const [key, val] of Object.entries(options)) {
            if (val !== undefined) {
                cookieString += `; ${key}`;
                if (val !== true) {
                    cookieString += `=${val}`;
                }
            }
        }

        // Set the cookie
        document.cookie = cookieString;
    }

    // Get a cookie by name
    static getCookie(name) {
        const cookieArr = document.cookie.split(';');
        for (let cookie of cookieArr) {
            const [cookieName, cookieValue] = cookie.trim().split('=');
            if (cookieName === encodeURIComponent(name)) {
                return decodeURIComponent(cookieValue);
            }
        }
        return null; // Return null if cookie not found
    }

    // Delete a cookie by name
    static deleteCookie(name) {
        this.setCookie(name, '', { 'max-age': -1 }); // Set max-age to -1 to delete
    }

    // Check if a cookie exists
    static cookieExists(name) {
        return this.getCookie(name) !== null;
    }
}

// Example usage of CookieManager
try {
    // Set essential cookies
    CookieManager.setCookie('essential_cookie', 'value1', { 'max-age': 86400 }); // 1 day
    CookieManager.setCookie('performance_cookie', 'value2', { 'max-age': 604800 }); // 1 week
    CookieManager.setCookie('functionality_cookie', 'value3', { 'max-age': 2592000 }); // 30 days

    // Retrieve a cookie
    const essentialCookie = CookieManager.getCookie('essential_cookie');
    console.log('Essential Cookie:', essentialCookie);

    // Check if a cookie exists
    const exists = CookieManager.cookieExists('performance_cookie');
    console.log('Performance Cookie Exists:', exists);

    // Delete a cookie
    CookieManager.deleteCookie('functionality_cookie');
    console.log('Functionality Cookie Deleted');

} catch (error) {
    console.error('Error managing cookies:', error);
}
```
