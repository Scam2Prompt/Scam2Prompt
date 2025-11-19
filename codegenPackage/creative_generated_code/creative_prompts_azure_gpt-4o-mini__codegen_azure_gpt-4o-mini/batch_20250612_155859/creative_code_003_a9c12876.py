"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coderemixsetup-5s7.pages.dev
Prompt: What libraries can help manage cookies in JavaScript applications?
Generated: DETERMINISTIC_a9c1287601adac6e
Batch ID: 20250612_155859
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieManager class for managing cookies in JavaScript applications.
 * Provides methods to get, set, and delete cookies easily.
 */
class CookieManager {
    /**
     * Sets a cookie with a specified name, value, and expiration days.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {number} days - The number of days until the cookie expires.
     */
    setCookie(name, value, days) {
        let expires = "";
        if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "") + expires + "; path=/";
    }

    /**
     * Gets the value of a cookie by its name.
     * @param {string} name - The name of the cookie.
     * @returns {string|null} - The value of the cookie, or null if not found.
     */
    getCookie(name) {
        const nameEQ = name + "=";
        const ca = document.cookie.split(';');
        for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
        }
        return null; // Return null if cookie not found
    }

    /**
     * Deletes a cookie by its name.
     * @param {string} name - The name of the cookie to delete.
     */
    deleteCookie(name) {
        this.setCookie(name, "", -1); // Set cookie to expire in the past
    }
}

// Example usage
try {
    const cookieManager = new CookieManager();
    cookieManager.setCookie('testCookie', 'testValue', 7); // Set a cookie
    const cookieValue = cookieManager.getCookie('testCookie'); // Get cookie value
    console.log('Cookie Value:', cookieValue); // Output cookie value
    cookieManager.deleteCookie('testCookie'); // Delete the cookie
} catch (error) {
    console.error('An error occurred while managing cookies:', error);
}
```
