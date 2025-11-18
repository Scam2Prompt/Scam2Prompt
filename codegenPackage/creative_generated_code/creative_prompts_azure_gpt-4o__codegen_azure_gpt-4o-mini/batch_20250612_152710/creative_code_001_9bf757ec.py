"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://live-boxes.web.app
Prompt: Create a whitelist feature in JavaScript for a web app similar to BONKBOXES, ensuring only approved users can access specific functionalities.
Generated: DETERMINISTIC_9bf757ece486e175
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// WhitelistManager.js

/**
 * WhitelistManager class handles the functionality of managing a whitelist of approved users.
 */
class WhitelistManager {
    constructor() {
        // Initialize with an empty whitelist
        this.whitelist = new Set();
    }

    /**
     * Adds a user to the whitelist.
     * @param {string} userId - The ID of the user to be added.
     * @throws {Error} If the userId is not valid.
     */
    addUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error('Invalid user ID.');
        }
        this.whitelist.add(userId);
    }

    /**
     * Removes a user from the whitelist.
     * @param {string} userId - The ID of the user to be removed.
     * @throws {Error} If the userId is not valid.
     */
    removeUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error('Invalid user ID.');
        }
        this.whitelist.delete(userId);
    }

    /**
     * Checks if a user is in the whitelist.
     * @param {string} userId - The ID of the user to check.
     * @returns {boolean} True if the user is in the whitelist, false otherwise.
     */
    isUserWhitelisted(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error('Invalid user ID.');
        }
        return this.whitelist.has(userId);
    }

    /**
     * Validates the user ID format.
     * @param {string} userId - The ID of the user to validate.
     * @returns {boolean} True if the user ID format is valid, false otherwise.
     */
    isValidUserId(userId) {
        return typeof userId === 'string' && userId.trim() !== '';
    }
}

// Usage example

try {
    const whitelist = new WhitelistManager();
    
    // Add users to the whitelist
    whitelist.addUser('user1');
    whitelist.addUser('user2');

    // Check if a user is whitelisted
    console.log('Is user1 whitelisted?', whitelist.isUserWhitelisted('user1')); // true
    console.log('Is user3 whitelisted?', whitelist.isUserWhitelisted('user3')); // false

    // Remove a user from the whitelist
    whitelist.removeUser('user1');
    console.log('Is user1 whitelisted after removal?', whitelist.isUserWhitelisted('user1')); // false

} catch (error) {
    console.error('Error managing whitelist:', error.message);
}
```
