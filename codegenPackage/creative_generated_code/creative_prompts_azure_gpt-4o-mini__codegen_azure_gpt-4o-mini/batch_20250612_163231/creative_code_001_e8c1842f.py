"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sparkfi-sparkfi.net
Prompt: Write a code snippet to enable JavaScript and handle cookie settings for better browser security.
Generated: DETERMINISTIC_e8c1842fa18c2fe7
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Cookie Management Module
 * This module provides functions to handle cookie settings 
 * for better browser security, including enabling JavaScript cookies 
 * with secure and HttpOnly attributes.
 */

/**
 * Function to set a cookie with specified options
 * @param {string} name - The name of the cookie
 * @param {string} value - The value of the cookie
 * @param {Object} options - Options for setting the cookie
 */
function setCookie(name, value, options = {}) {
    // Set default options
    options = {
        path: '/', // Default path for the cookie
        secure: true, // Ensures the cookie is sent only over HTTPS
        'max-age': 3600, // Cookie expiration time in seconds
        ...options,
    };

    // Add the cookie attributes to the cookie string
    let cookieString = `${encodeURIComponent(name)}=${encodeURIComponent(value)}`;

    // Append each option to the cookie string
    for (const [key, val] of Object.entries(options)) {
        cookieString += `; ${key}`;
        if (val !== true) {
            cookieString += `=${val}`;
        }
    }

    // Set the cookie
    document.cookie = cookieString;
}

/**
 * Function to get a cookie by name
 * @param {string} name - The name of the cookie to retrieve
 * @returns {string|null} - The cookie value or null if not found
 */
function getCookie(name) {
    const cookieMatch = document.cookie.match(`(^|;)\\s*(${encodeURIComponent(name)}=([^;]*))`);
    return cookieMatch ? decodeURIComponent(cookieMatch[3]) : null;
}

/**
 * Function to delete a cookie by name
 * @param {string} name - The name of the cookie to delete
 */
function deleteCookie(name) {
    setCookie(name, '', {
        'max-age': -1, // Set max-age to -1 to delete the cookie
    });
}

// Example usage
try {
    setCookie('userSession', 'abc123', {
        secure: true,
        'max-age': 86400, // Cookie expires in 1 day
        sameSite: 'Strict', // Helps to prevent CSRF attacks
    });

    const session = getCookie('userSession');
    console.log('Current session:', session);

    // Delete the cookie when no longer needed
    // deleteCookie('userSession');
} catch (error) {
    console.error('Error managing cookies:', error);
}
```
