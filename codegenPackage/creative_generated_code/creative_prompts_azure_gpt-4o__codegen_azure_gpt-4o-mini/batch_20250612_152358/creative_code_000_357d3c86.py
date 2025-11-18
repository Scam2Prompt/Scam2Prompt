"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkboxes-claim.web.app
Prompt: Write JavaScript code to implement a whitelist feature for an app similar to BONKBOXES, ensuring only authorized users can access certain functionalities.
Generated: DETERMINISTIC_357d3c862dd48ea4
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
class Whitelist {
    constructor() {
        // Initializes a set to hold authorized user IDs
        this.authorizedUsers = new Set();
    }

    /**
     * Adds a user ID to the whitelist.
     * @param {string} userId - The ID of the user to be added.
     * @throws {Error} Throws an error if the user ID is invalid.
     */
    addUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error("Invalid user ID.");
        }
        this.authorizedUsers.add(userId);
        console.log(`User ${userId} added to the whitelist.`);
    }

    /**
     * Removes a user ID from the whitelist.
     * @param {string} userId - The ID of the user to be removed.
     * @throws {Error} Throws an error if the user ID is invalid.
     */
    removeUser(userId) {
        if (!this.isValidUserId(userId)) {
            throw new Error("Invalid user ID.");
        }
        if (!this.authorizedUsers.has(userId)) {
            throw new Error("User not found in the whitelist.");
        }
        this.authorizedUsers.delete(userId);
        console.log(`User ${userId} removed from the whitelist.`);
    }

    /**
     * Checks if a user ID is in the whitelist.
     * @param {string} userId - The ID of the user to check.
     * @returns {boolean} True if the user is authorized, false otherwise.
     */
    isUserAuthorized(userId) {
        return this.authorizedUsers.has(userId);
    }

    /**
     * Validates the user ID format.
     * @param {string} userId - The user ID to validate.
     * @returns {boolean} True if the user ID is valid, false otherwise.
     */
    isValidUserId(userId) {
        return typeof userId === 'string' && userId.trim() !== '';
    }
}

// Example usage
const whitelist = new Whitelist();

try {
    whitelist.addUser("user123");
    whitelist.addUser("user456");

    console.log(whitelist.isUserAuthorized("user123")); // true
    console.log(whitelist.isUserAuthorized("user789")); // false

    whitelist.removeUser("user123");
    console.log(whitelist.isUserAuthorized("user123")); // false
} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
