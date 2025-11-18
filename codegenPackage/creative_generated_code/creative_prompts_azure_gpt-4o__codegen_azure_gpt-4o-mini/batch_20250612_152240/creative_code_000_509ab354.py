"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claims.web.app
Prompt: Write JavaScript code to create a whitelist system for a web application similar to BONKBOXES, ensuring users are validated before accessing specific features.
Generated: DETERMINISTIC_509ab3542b85d867
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Whitelist System for User Validation in a Web Application

// Define a class to manage the whitelist.
class Whitelist {
    constructor() {
        // Initialize an empty set to store whitelisted users
        this.whitelistedUsers = new Set();
    }

    /**
     * Adds a user to the whitelist.
     * @param {string} userId - The user ID to be added to the whitelist.
     * @throws {Error} Will throw an error if the user ID is invalid or already whitelisted.
     */
    addUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error('Invalid user ID.');
        }
        if (this.whitelistedUsers.has(userId)) {
            throw new Error('User is already whitelisted.');
        }
        this.whitelistedUsers.add(userId);
        console.log(`User ${userId} added to the whitelist.`);
    }

    /**
     * Removes a user from the whitelist.
     * @param {string} userId - The user ID to be removed from the whitelist.
     * @throws {Error} Will throw an error if the user ID is invalid or not in the whitelist.
     */
    removeUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error('Invalid user ID.');
        }
        if (!this.whitelistedUsers.has(userId)) {
            throw new Error('User is not in the whitelist.');
        }
        this.whitelistedUsers.delete(userId);
        console.log(`User ${userId} removed from the whitelist.`);
    }

    /**
     * Validates if a user ID is valid.
     * @param {string} userId - The user ID to validate.
     * @returns {boolean} True if the user ID is valid, false otherwise.
     */
    isValidUserId(userId) {
        return typeof userId === 'string' && userId.trim() !== '';
    }

    /**
     * Checks if a user is whitelisted.
     * @param {string} userId - The user ID to check.
     * @returns {boolean} True if the user is whitelisted, false otherwise.
     */
    isUserWhitelisted(userId) {
        return this.whitelistedUsers.has(userId);
    }
}

// Example usage
const whitelist = new Whitelist();

try {
    whitelist.addUser('user123'); // Add user to the whitelist
    console.log(whitelist.isUserWhitelisted('user123')); // Check if user is whitelisted
    whitelist.removeUser('user123'); // Remove user from the whitelist
} catch (error) {
    console.error(error.message);
}
```
