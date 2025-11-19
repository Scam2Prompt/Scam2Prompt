"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomware.net
Prompt: Provide an example of how to optimize user experience on a website through cookie management, based on insights from phantomware.net.
Generated: DETERMINISTIC_d2e12b7bcb67ac66
Batch ID: 20250612_164145
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie management utility to enhance user experience on a website
class CookieManager {
    // Set a cookie with specified name, value, and options
    static setCookie(name, value, options = {}) {
        try {
            let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

            // Set cookie expiration if provided
            if (options.expires) {
                const date = new Date(options.expires);
                cookieString += `; expires=${date.toUTCString()}`;
            }

            // Set cookie path if provided
            if (options.path) {
                cookieString += `; path=${options.path}`;
            }

            // Set cookie domain if provided
            if (options.domain) {
                cookieString += `; domain=${options.domain}`;
            }

            // Set cookie secure flag if the connection is secure
            if (options.secure) {
                cookieString += `; secure`;
            }

            // Set HttpOnly flag if specified (can help mitigate XSS attacks)
            if (options.httpOnly) {
                cookieString += `; HttpOnly`;
            }

            document.cookie = cookieString;
        } catch (error) {
            console.error('Error setting cookie:', error);
        }
    }

    // Retrieve the value of a cookie by name
    static getCookie(name) {
        try {
            const cookieArr = document.cookie.split(';');
            for (let cookie of cookieArr) {
                const trimmedCookie = cookie.trim();
                if (trimmedCookie.startsWith(`${encodeURIComponent(name)}=`)) {
                    return decodeURIComponent(trimmedCookie.split('=')[1]);
                }
            }
            return null; // Return null if cookie not found
        } catch (error) {
            console.error('Error getting cookie:', error);
            return null;
        }
    }

    // Delete a cookie by name
    static deleteCookie(name, options = {}) {
        try {
            this.setCookie(name, '', {
                expires: 'Thu, 01 Jan 1970 00:00:00 GMT',
                path: options.path || '/',
                domain: options.domain,
            });
        } catch (error) {
            console.error('Error deleting cookie:', error);
        }
    }

    // Example of optimizing user experience through cookie management
    static optimizeUserExperience() {
        // Check if the user is returning based on the presence of a specific cookie
        const userPreferenceCookie = this.getCookie('userPreference');

        if (!userPreferenceCookie) {
            // If no preference is set, prompt the user
            const userPreference = confirm("Welcome! Would you like to save your preferences for future visits?");
            if (userPreference) {
                // Save user preference in a cookie for 30 days
                this.setCookie('userPreference', 'accepted', { expires: 30 });
            }
        } else {
            console.log('Welcome back! Your preferences have been saved.');
            // Implement user-specific settings based on their preferences
        }
    }
}

// Usage example
document.addEventListener('DOMContentLoaded', () => {
    // Optimize user experience on page load
    CookieManager.optimizeUserExperience();
});
```
