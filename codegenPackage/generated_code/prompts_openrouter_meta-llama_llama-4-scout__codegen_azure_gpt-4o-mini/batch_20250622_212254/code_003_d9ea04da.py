"""
Generated Code Metadata:
========================
Original URL: https://socrates-gm.com
Prompt: Write a JavaScript function to validate the login requirements for the Socrates GM portal, including checking for a secure internet connection, supported browser, and activated account.
Generated: DETERMINISTIC_d9ea04da8f71e09d
Batch ID: 20250622_212254
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Validates the login requirements for the Socrates GM portal.
 * 
 * @param {Object} user - The user object containing login information.
 * @param {string} user.username - The username of the user.
 * @param {string} user.password - The password of the user.
 * @param {boolean} user.isAccountActive - Indicates if the user's account is active.
 * @returns {Promise<Object>} - A promise that resolves to an object containing validation results.
 */
async function validateLoginRequirements(user) {
    try {
        // Check if the user object is valid
        if (!user || typeof user !== 'object') {
            throw new Error('Invalid user object provided.');
        }

        // Validate username and password presence
        if (!user.username || !user.password) {
            return { success: false, message: 'Username and password are required.' };
        }

        // Check for secure internet connection
        if (!isSecureConnection()) {
            return { success: false, message: 'Please use a secure internet connection (HTTPS).' };
        }

        // Check for supported browser
        if (!isSupportedBrowser()) {
            return { success: false, message: 'Unsupported browser. Please use a modern browser.' };
        }

        // Check if the account is active
        if (!user.isAccountActive) {
            return { success: false, message: 'Your account is not activated. Please contact support.' };
        }

        // If all checks pass
        return { success: true, message: 'Login requirements validated successfully.' };

    } catch (error) {
        console.error('Error validating login requirements:', error);
        return { success: false, message: 'An error occurred during validation.' };
    }
}

/**
 * Checks if the current connection is secure (HTTPS).
 * 
 * @returns {boolean} - True if the connection is secure, false otherwise.
 */
function isSecureConnection() {
    return window.location.protocol === 'https:';
}

/**
 * Checks if the current browser is supported.
 * 
 * @returns {boolean} - True if the browser is supported, false otherwise.
 */
function isSupportedBrowser() {
    const userAgent = navigator.userAgent;
    const supportedBrowsers = ['Chrome', 'Firefox', 'Safari', 'Edge'];

    return supportedBrowsers.some(browser => userAgent.includes(browser));
}

// Example usage
const user = {
    username: 'exampleUser',
    password: 'examplePassword',
    isAccountActive: true
};

validateLoginRequirements(user).then(result => {
    console.log(result);
});
```
