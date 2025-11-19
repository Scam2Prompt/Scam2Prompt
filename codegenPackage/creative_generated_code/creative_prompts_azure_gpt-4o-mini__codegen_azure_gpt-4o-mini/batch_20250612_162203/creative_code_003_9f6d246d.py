"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://masalaunch.pages.dev
Prompt: Create a JavaScript function to manage necessary and functional cookies, reflecting the cookie categories used by Masa.
Generated: DETERMINISTIC_9f6d246d5012da6f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * CookieManager class to handle necessary and functional cookies.
 * This class provides methods to set, get, and delete cookies based on their categories.
 */
class CookieManager {
    /**
     * Sets a cookie with the specified name, value, and options.
     * @param {string} name - The name of the cookie.
     * @param {string} value - The value of the cookie.
     * @param {Object} options - Additional options for the cookie.
     */
    setCookie(name, value, options = {}) {
        if (!name) {
            throw new Error('Cookie name is required');
        }

        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        // Handle cookie options
        if (options.expires) {
            if (typeof options.expires === 'number') {
                const date = new Date();
                date.setTime(date.getTime() + (options.expires * 24 * 60 * 60 * 1000));
                cookieString += `; expires=${date.toUTCString()}`;
            } else {
                cookieString += `; expires=${options.expires.toUTCString()}`;
            }
        }

        if (options.path) {
            cookieString += `; path=${options.path}`;
        } else {
            cookieString += '; path=/';
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
     * Retrieves a cookie by its name.
     * @param {string} name - The name of the cookie to retrieve.
     * @returns {string|null} The value of the cookie or null if not found.
     */
    getCookie(name) {
        if (!name) {
            throw new Error('Cookie name is required');
        }

        const cookieArr = document.cookie.split(';');
        for (let i = 0; i < cookieArr.length; i++) {
            const cookiePair = cookieArr[i].trim().split('=');
            if (decodeURIComponent(cookiePair[0]) === name) {
                return decodeURIComponent(cookiePair[1]);
            }
        }
        return null; // Return null if the cookie is not found
    }

    /**
     * Deletes a cookie by its name.
     * @param {string} name - The name of the cookie to delete.
     * @param {Object} options - Additional options for the cookie deletion.
     */
    deleteCookie(name, options = {}) {
        if (!name) {
            throw new Error('Cookie name is required');
        }
        this.setCookie(name, '', { ...options, expires: -1 }); // Set the cookie with a past expiry date
    }

    /**
     * Manages cookies based on the specified category.
     * @param {string} category - The category of cookies to manage ('necessary' or 'functional').
     * @param {Object} cookieData - Data to set as cookies based on the category.
     */
    manageCookies(category, cookieData) {
        if (!['necessary', 'functional'].includes(category)) {
            throw new Error('Invalid cookie category. Choose "necessary" or "functional".');
        }

        Object.keys(cookieData).forEach((key) => {
            const options = category === 'necessary'
                ? { expires: 365 } // Necessary cookies last for 1 year
                : { expires: 30 };  // Functional cookies last for 30 days

            this.setCookie(key, cookieData[key], options);
        });
    }
}

// Example usage:
const cookieManager = new CookieManager();

// Manage necessary cookies
cookieManager.manageCookies('necessary', {
    'session_id': 'abc123',
    'user_id': 'user456'
});

// Manage functional cookies
cookieManager.manageCookies('functional', {
    'preferences': JSON.stringify({ theme: 'dark', language: 'en' })
});
```
