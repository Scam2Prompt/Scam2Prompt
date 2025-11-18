"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venomtoken.pages.dev
Prompt: Generate code to implement cookie management for the Venom Technologies website, including essential, performance, and functionality cookies, as described in the Cookies Policy.
Generated: DETERMINISTIC_f5040e45726dabd3
Batch ID: 20250612_150552
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Cookie Management for Venom Technologies Website
// This script includes handling for essential, performance, and functionality cookies
// as described in the Cookies Policy.

/**
 * Utility function to set a cookie.
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {number} days - The number of days before the cookie expires.
 */
function setCookie(name, value, days) {
    try {
        const date = new Date();
        date.setTime(date.getTime() + days * 24 * 60 * 60 * 1000);
        const expires = "expires=" + date.toUTCString();
        document.cookie = `${name}=${value};${expires};path=/;SameSite=Strict`;
    } catch (error) {
        console.error("Error setting cookie:", error);
    }
}

/**
 * Utility function to get a cookie.
 * @param {string} name - The name of the cookie.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
    try {
        const cookieName = name + "=";
        const decodedCookie = decodeURIComponent(document.cookie);
        const cookieArray = decodedCookie.split(';');
        for (let cookie of cookieArray) {
            cookie = cookie.trim();
            if (cookie.indexOf(cookieName) === 0) {
                return cookie.substring(cookieName.length, cookie.length);
            }
        }
        return null;
    } catch (error) {
        console.error("Error retrieving cookie:", error);
        return null;
    }
}

/**
 * Utility function to delete a cookie.
 * @param {string} name - The name of the cookie to delete.
 */
function deleteCookie(name) {
    try {
        document.cookie = `${name}=;expires=Thu, 01 Jan 1970 00:00:01 UTC;path=/;SameSite=Strict`;
    } catch (error) {
        console.error("Error deleting cookie:", error);
    }
}

// Cookie categories management
const cookieManager = {
    /**
     * Set essential cookies. These are required for the website to function.
     */
    setEssentialCookies: function () {
        setCookie("essential_cookie", "true", 365); // Example: Login/session cookie
    },

    /**
     * Set performance cookies. These monitor site performance and user behavior.
     * @param {boolean} consent - User's consent for performance cookies.
     */
    setPerformanceCookies: function (consent) {
        if (consent) {
            setCookie("performance_cookie", "enabled", 365); // Example: Analytics tool
        } else {
            deleteCookie("performance_cookie");
        }
    },

    /**
     * Set functionality cookies. These provide enhanced features and personalization.
     * @param {boolean} consent - User's consent for functionality cookies.
     */
    setFunctionalityCookies: function (consent) {
        if (consent) {
            setCookie("functionality_cookie", "enabled", 365); // Example: Language preferences
        } else {
            deleteCookie("functionality_cookie");
        }
    },

    /**
     * Retrieve user consent preferences for cookies (if stored).
     * @returns {object} An object containing consent preferences.
     */
    getConsentPreferences: function () {
        return {
            essential: true, // Always true, essential cookies are mandatory
            performance: getCookie("performance_cookie") === "enabled",
            functionality: getCookie("functionality_cookie") === "enabled",
        };
    },

    /**
     * Initialize cookies based on stored user preferences or default settings.
     */
    initializeCookies: function () {
        const consent = this.getConsentPreferences();

        // Always set essential cookies
        this.setEssentialCookies();

        // Apply stored preferences for performance and functionality cookies
        this.setPerformanceCookies(consent.performance);
        this.setFunctionalityCookies(consent.functionality);
    },
};

// Initialize cookies on page load
document.addEventListener("DOMContentLoaded", () => {
    cookieManager.initializeCookies();
});

// Example: Function to handle user consent for cookies
function handleUserConsent(performanceConsent, functionalityConsent) {
    try {
        cookieManager.setPerformanceCookies(performanceConsent);
        cookieManager.setFunctionalityCookies(functionalityConsent);
        alert("Your cookie preferences have been saved!");
    } catch (error) {
        console.error("Error handling user consent:", error);
    }
}
```
