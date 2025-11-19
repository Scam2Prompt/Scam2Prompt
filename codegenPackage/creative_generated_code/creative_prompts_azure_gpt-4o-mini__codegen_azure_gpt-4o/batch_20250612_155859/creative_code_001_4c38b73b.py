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
/**
 * Best practices for configuring JavaScript and cookie settings in web development
 * 
 * This example demonstrates secure cookie handling and JavaScript configuration 
 * to ensure user data privacy and compliance with modern web standards.
 */

/**
 * Set a secure cookie using JavaScript
 * @param {string} name - Name of the cookie
 * @param {string} value - Value of the cookie
 * @param {number} days - Number of days before the cookie expires
 */
function setCookie(name, value, days) {
    try {
        // Calculate expiration date
        const date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        const expires = "expires=" + date.toUTCString();

        // Set the cookie with best practices
        document.cookie = `${name}=${encodeURIComponent(value)}; ${expires}; path=/; Secure; HttpOnly; SameSite=Strict`;
    } catch (error) {
        console.error("Error setting cookie:", error);
    }
}

/**
 * Get a cookie by name
 * @param {string} name - Name of the cookie
 * @returns {string|null} - Value of the cookie, or null if not found
 */
function getCookie(name) {
    try {
        const nameEQ = name + "=";
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            let cookie = cookies[i].trim();
            if (cookie.indexOf(nameEQ) === 0) {
                return decodeURIComponent(cookie.substring(nameEQ.length));
            }
        }
        return null;
    } catch (error) {
        console.error("Error getting cookie:", error);
        return null;
    }
}

/**
 * Delete a cookie by name
 * @param {string} name - Name of the cookie
 */
function deleteCookie(name) {
    try {
        // Set the expiration date to a past date to delete the cookie
        document.cookie = `${name}=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/; Secure; HttpOnly; SameSite=Strict`;
    } catch (error) {
        console.error("Error deleting cookie:", error);
    }
}

// Example Usage
setCookie("userToken", "abc123", 7); // Set a secure cookie with a 7-day expiration
console.log("Cookie Value:", getCookie("userToken")); // Retrieve the cookie value
deleteCookie("userToken"); // Delete the cookie

/**
 * Additional Best Practices:
 * 1. Secure cookies with `Secure` and `HttpOnly` flags where appropriate.
 * 2. Implement `SameSite=Strict` to prevent cross-site request forgery (CSRF) attacks.
 * 3. Use encoding/decoding functions to prevent special character issues in cookie values.
 * 4. Monitor cookie usage and ensure compliance with privacy laws such as GDPR or CCPA.
 * 5. Ensure cookies are only set on HTTPS connections.
 */
```
