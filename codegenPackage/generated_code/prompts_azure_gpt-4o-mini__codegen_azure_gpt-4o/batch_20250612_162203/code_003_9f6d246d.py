"""
Generated Code Metadata:
========================
Original URL: https://masalaunch.pages.dev
Prompt: Create a JavaScript function to manage necessary and functional cookies, reflecting the cookie categories used by Masa.
Generated: DETERMINISTIC_9f6d246d5012da6f
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Cookie Manager for Necessary and Functional Cookies
 * 
 * This script provides functionality to manage cookies categorized as
 * "Necessary" and "Functional" in compliance with cookie management best practices.
 * 
 * Author: [Your Name]
 * Date: [Today's Date]
 */

/**
 * Sets a cookie with the specified name, value, and options.
 * 
 * @param {string} name - The name of the cookie.
 * @param {string} value - The value of the cookie.
 * @param {Object} options - Additional options for the cookie (e.g., expires, path, secure).
 */
function setCookie(name, value, options = {}) {
    try {
        let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

        if (options.expires) {
            cookieString += `; expires=${options.expires.toUTCString()}`;
        }
        if (options.path) {
            cookieString += `; path=${options.path}`;
        }
        if (options.secure) {
            cookieString += `; secure`;
        }
        if (options.sameSite) {
            cookieString += `; samesite=${options.sameSite}`;
        }

        document.cookie = cookieString;
    } catch (error) {
        console.error("Error setting cookie:", error);
    }
}

/**
 * Gets the value of a cookie by name.
 * 
 * @param {string} name - The name of the cookie to retrieve.
 * @returns {string|null} - The value of the cookie, or null if not found.
 */
function getCookie(name) {
    try {
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
            const [key, value] = cookie.split("=");
            if (decodeURIComponent(key) === name) {
                return decodeURIComponent(value);
            }
        }
        return null;
    } catch (error) {
        console.error("Error getting cookie:", error);
        return null;
    }
}

/**
 * Deletes a cookie by name.
 * 
 * @param {string} name - The name of the cookie to delete.
 * @param {Object} options - Additional options for the cookie (e.g., path).
 */
function deleteCookie(name, options = {}) {
    try {
        setCookie(name, "", {
            ...options,
            expires: new Date(0) // Set expiration date to the past
        });
    } catch (error) {
        console.error("Error deleting cookie:", error);
    }
}

/**
 * Manages cookies based on their category.
 * 
 * @param {string} category - The category of the cookie ("necessary" or "functional").
 * @param {string} action - The action to perform ("set", "get", or "delete").
 * @param {string} name - The name of the cookie.
 * @param {string} [value] - The value of the cookie (required for "set" action).
 * @param {Object} [options] - Additional options for the cookie (e.g., expires, path).
 * @returns {string|null|undefined} - The cookie value for "get", or undefined for other actions.
 */
function manageCookie(category, action, name, value = "", options = {}) {
    try {
        // Validate category
        if (!["necessary", "functional"].includes(category)) {
            throw new Error("Invalid cookie category. Must be 'necessary' or 'functional'.");
        }

        // Perform action based on the input
        switch (action) {
            case "set":
                if (!name || !value) {
                    throw new Error("Name and value are required for setting a cookie.");
                }
                setCookie(name, value, options);
                break;

            case "get":
                if (!name) {
                    throw new Error("Name is required for getting a cookie.");
                }
                return getCookie(name);

            case "delete":
                if (!name) {
                    throw new Error("Name is required for deleting a cookie.");
                }
                deleteCookie(name, options);
                break;

            default:
                throw new Error("Invalid action. Must be 'set', 'get', or 'delete'.");
        }
    } catch (error) {
        console.error("Error managing cookie:", error);
    }
}

// Example Usage:
// Setting a necessary cookie
manageCookie("necessary", "set", "session_id", "abc123", { path: "/", secure: true, sameSite: "Strict" });

// Getting a functional cookie
const theme = manageCookie("functional", "get", "theme");

// Deleting a necessary cookie
manageCookie("necessary", "delete", "session_id", null, { path: "/" });
```
