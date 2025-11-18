"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: Create a JavaScript-based whitelist system for a web app that requires specific users to be pre-approved, similar to the BONKBOXES platform.
Generated: DETERMINISTIC_1e85702ff269d74a
Batch ID: 20250612_150602
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Whitelist System for User Approval in a Web Application

class Whitelist {
    constructor() {
        // Initialize an empty whitelist
        this.approvedUsers = new Set();
    }

    /**
     * Adds a user to the approved whitelist.
     * @param {string} userId - The ID of the user to be added.
     * @throws {Error} Throws an error if the user ID is invalid or already exists in the whitelist.
     */
    addUser(userId) {
        this.validateUserId(userId);
        if (this.approvedUsers.has(userId)) {
            throw new Error(`User ID '${userId}' is already in the whitelist.`);
        }
        this.approvedUsers.add(userId);
        console.log(`User ID '${userId}' has been added to the whitelist.`);
    }

    /**
     * Removes a user from the approved whitelist.
     * @param {string} userId - The ID of the user to be removed.
     * @throws {Error} Throws an error if the user ID is invalid or does not exist in the whitelist.
     */
    removeUser(userId) {
        this.validateUserId(userId);
        if (!this.approvedUsers.has(userId)) {
            throw new Error(`User ID '${userId}' is not in the whitelist.`);
        }
        this.approvedUsers.delete(userId);
        console.log(`User ID '${userId}' has been removed from the whitelist.`);
    }

    /**
     * Checks if a user is in the approved whitelist.
     * @param {string} userId - The ID of the user to be checked.
     * @returns {boolean} Returns true if the user is in the whitelist, otherwise false.
     */
    isUserApproved(userId) {
        this.validateUserId(userId);
        return this.approvedUsers.has(userId);
    }

    /**
     * Validates that the user ID is a non-empty string.
     * @param {string} userId - The ID of the user to validate.
     * @throws {Error} Throws an error if the user ID is invalid.
     */
    validateUserId(userId) {
        if (typeof userId !== 'string' || userId.trim() === '') {
            throw new Error('User ID must be a non-empty string.');
        }
    }

    /**
     * Retrieves a list of all approved users.
     * @returns {Array} An array of approved user IDs.
     */
    getApprovedUsers() {
        return Array.from(this.approvedUsers);
    }
}

// Example Usage
try {
    const whitelist = new Whitelist();
    
    // Add users to the whitelist
    whitelist.addUser('user1'); // Adds user1
    whitelist.addUser('user2'); // Adds user2
    
    console.log(whitelist.getApprovedUsers()); // ['user1', 'user2']

    // Check if a user is approved
    console.log(whitelist.isUserApproved('user1')); // true
    console.log(whitelist.isUserApproved('user3')); // false

    // Remove a user from the whitelist
    whitelist.removeUser('user1');
    console.log(whitelist.getApprovedUsers()); // ['user2']

} catch (error) {
    console.error(`Error: ${error.message}`);
}
```
