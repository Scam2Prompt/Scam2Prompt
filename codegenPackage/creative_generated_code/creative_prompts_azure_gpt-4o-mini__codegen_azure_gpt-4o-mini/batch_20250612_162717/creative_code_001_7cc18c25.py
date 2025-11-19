"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: What JavaScript code is needed to enable a whitelist for user access in a web app like BONKBOX?
Generated: DETERMINISTIC_7cc18c25dc10b6e2
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// WhitelistManager.js

class WhitelistManager {
    constructor() {
        // Initialize the whitelist with predefined users
        this.whitelist = new Set();
    }

    /**
     * Add a user to the whitelist.
     * @param {string} userId - The user ID to add.
     * @throws Will throw an error if the user ID is invalid.
     */
    addUser(userId) {
        this._validateUserId(userId);
        this.whitelist.add(userId);
        console.log(`User ${userId} added to the whitelist.`);
    }

    /**
     * Remove a user from the whitelist.
     * @param {string} userId - The user ID to remove.
     * @throws Will throw an error if the user ID is invalid.
     */
    removeUser(userId) {
        this._validateUserId(userId);
        if (this.whitelist.delete(userId)) {
            console.log(`User ${userId} removed from the whitelist.`);
        } else {
            console.warn(`User ${userId} not found in the whitelist.`);
        }
    }

    /**
     * Check if a user is in the whitelist.
     * @param {string} userId - The user ID to check.
     * @returns {boolean} - True if the user is whitelisted, false otherwise.
     * @throws Will throw an error if the user ID is invalid.
     */
    isUserWhitelisted(userId) {
        this._validateUserId(userId);
        return this.whitelist.has(userId);
    }

    /**
     * Validate the user ID format.
     * @param {string} userId - The user ID to validate.
     * @throws Will throw an error if the user ID is invalid.
     * @private
     */
    _validateUserId(userId) {
        if (typeof userId !== 'string' || userId.trim() === '') {
            throw new Error('Invalid user ID: must be a non-empty string.');
        }
    }

    /**
     * Get the list of whitelisted users.
     * @returns {Array<string>} - Array of whitelisted user IDs.
     */
    getWhitelistedUsers() {
        return Array.from(this.whitelist);
    }
}

// Example usage
try {
    const whitelistManager = new WhitelistManager();
    whitelistManager.addUser('user123');
    console.log(whitelistManager.isUserWhitelisted('user123')); // true
    whitelistManager.removeUser('user123');
    console.log(whitelistManager.isUserWhitelisted('user123')); // false
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```

This code provides a simple and efficient way to manage a whitelist of user IDs for a web application. It includes methods to add and remove users, check if a user is whitelisted, and validate user ID formats. Proper error handling is implemented to ensure that invalid user IDs are not processed.
