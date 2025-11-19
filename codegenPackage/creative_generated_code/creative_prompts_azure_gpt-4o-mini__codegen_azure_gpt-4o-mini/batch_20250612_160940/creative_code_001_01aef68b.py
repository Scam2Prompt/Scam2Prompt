"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkweb.web.app
Prompt: Write a JavaScript function to manage user whitelisting for a crypto application.
Generated: DETERMINISTIC_01aef68b84fda0b7
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * UserWhitelistManager class to manage whitelisting of users in a crypto application.
 */
class UserWhitelistManager {
    constructor() {
        // Initialize an empty Set to store whitelisted users for unique entries
        this.whitelistedUsers = new Set();
    }

    /**
     * Adds a user to the whitelist.
     * @param {string} userId - The ID of the user to be whitelisted.
     * @throws {Error} Throws an error if userId is invalid or already whitelisted.
     */
    addUser(userId) {
        this.validateUserId(userId);
        
        if (this.whitelistedUsers.has(userId)) {
            throw new Error(`User with ID ${userId} is already whitelisted.`);
        }
        
        this.whitelistedUsers.add(userId);
        console.log(`User with ID ${userId} has been whitelisted.`);
    }

    /**
     * Removes a user from the whitelist.
     * @param {string} userId - The ID of the user to be removed from the whitelist.
     * @throws {Error} Throws an error if userId is invalid or not found in the whitelist.
     */
    removeUser(userId) {
        this.validateUserId(userId);
        
        if (!this.whitelistedUsers.has(userId)) {
            throw new Error(`User with ID ${userId} is not whitelisted.`);
        }
        
        this.whitelistedUsers.delete(userId);
        console.log(`User with ID ${userId} has been removed from the whitelist.`);
    }

    /**
     * Checks if a user is whitelisted.
     * @param {string} userId - The ID of the user to be checked.
     * @returns {boolean} Returns true if the user is whitelisted, otherwise false.
     */
    isUserWhitelisted(userId) {
        this.validateUserId(userId);
        return this.whitelistedUsers.has(userId);
    }

    /**
     * Validates the userId format.
     * @param {string} userId - The ID of the user to be validated.
     * @throws {Error} Throws an error if userId is not a valid string.
     */
    validateUserId(userId) {
        if (typeof userId !== 'string' || userId.trim() === '') {
            throw new Error('Invalid user ID. It must be a non-empty string.');
        }
    }

    /**
     * Retrieves the list of whitelisted users.
     * @returns {Array<string>} Returns an array of whitelisted user IDs.
     */
    getWhitelistedUsers() {
        return Array.from(this.whitelistedUsers);
    }
}

// Example usage:
try {
    const whitelistManager = new UserWhitelistManager();
    whitelistManager.addUser('user1');
    whitelistManager.addUser('user2');
    console.log(whitelistManager.getWhitelistedUsers()); // Output: ['user1', 'user2']
    console.log(whitelistManager.isUserWhitelisted('user1')); // Output: true
    whitelistManager.removeUser('user1');
    console.log(whitelistManager.getWhitelistedUsers()); // Output: ['user2']
} catch (error) {
    console.error(error.message);
}
```
