"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://planetaria.world
Prompt: Develop a JavaScript module to manage user interactions within the Planetaria metaverse environment.
Generated: DETERMINISTIC_9c6add47f2e6a28e
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// planetariaUserManager.js

/**
 * UserManager class to handle user interactions within the Planetaria metaverse.
 * This module provides functionalities to create, update, delete, and fetch user data.
 */
class UserManager {
    constructor() {
        this.users = new Map(); // Store users in a Map for efficient access
    }

    /**
     * Adds a new user to the metaverse.
     * @param {string} userId - Unique identifier for the user.
     * @param {Object} userData - An object containing user information.
     * @throws Will throw an error if the userId already exists.
     */
    addUser(userId, userData) {
        if (this.users.has(userId)) {
            throw new Error(`User with ID ${userId} already exists.`);
        }
        this.users.set(userId, userData);
    }

    /**
     * Fetches user data by user ID.
     * @param {string} userId - Unique identifier for the user.
     * @returns {Object|null} User data or null if user does not exist.
     */
    getUser(userId) {
        return this.users.get(userId) || null;
    }

    /**
     * Updates existing user information.
     * @param {string} userId - Unique identifier for the user.
     * @param {Object} newUserData - An object containing the updated user information.
     * @throws Will throw an error if the userId does not exist.
     */
    updateUser(userId, newUserData) {
        if (!this.users.has(userId)) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        this.users.set(userId, { ...this.users.get(userId), ...newUserData });
    }

    /**
     * Deletes a user from the metaverse.
     * @param {string} userId - Unique identifier for the user.
     * @throws Will throw an error if the userId does not exist.
     */
    deleteUser(userId) {
        if (!this.users.has(userId)) {
            throw new Error(`User with ID ${userId} does not exist.`);
        }
        this.users.delete(userId);
    }

    /**
     * Fetches all users in the metaverse.
     * @returns {Array} Array of all user data objects.
     */
    getAllUsers() {
        return Array.from(this.users.values());
    }
}

export default UserManager;

// Usage example (this part can be commented out in production):
// const userManager = new UserManager();
// userManager.addUser('user123', { name: 'Alice', age: 30 });
// console.log(userManager.getUser('user123'));
// userManager.updateUser('user123', { age: 31 });
// userManager.deleteUser('user123');
// console.log(userManager.getAllUsers());
```
