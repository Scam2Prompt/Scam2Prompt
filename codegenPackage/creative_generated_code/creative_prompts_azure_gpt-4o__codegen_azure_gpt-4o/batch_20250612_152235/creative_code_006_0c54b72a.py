"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://shibonkgo.web.app
Prompt: Provide an example of a whitelist management system using JavaScript, inspired by the Shibonk Gang web app.
Generated: DETERMINISTIC_0c54b72ad4db316a
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Whitelist Management System
 * 
 * This system allows users to add, remove, and check whether a user is whitelisted.
 * Inspired by the functionality of a web app, the script is designed to be clean,
 * efficient, and production-ready.
 */

class WhitelistManager {
  constructor() {
    // Initialize the whitelist as a Set to ensure unique entries and fast operations
    this.whitelist = new Set();
  }

  /**
   * Adds a user to the whitelist.
   * @param {string} userId - The unique identifier for the user.
   * @returns {boolean} - Returns true if the user was successfully added, false if already present.
   */
  addUser(userId) {
    if (!userId || typeof userId !== 'string') {
      throw new Error('Invalid userId. Must be a non-empty string.');
    }
    // Add user to the Set, returns true if added, false if already exists
    const isAdded = !this.whitelist.has(userId);
    this.whitelist.add(userId);
    return isAdded;
  }

  /**
   * Removes a user from the whitelist.
   * @param {string} userId - The unique identifier for the user.
   * @returns {boolean} - Returns true if the user was successfully removed, false if not found.
   */
  removeUser(userId) {
    if (!userId || typeof userId !== 'string') {
      throw new Error('Invalid userId. Must be a non-empty string.');
    }
    // Remove user from the Set, returns true if removed, false if not found
    return this.whitelist.delete(userId);
  }

  /**
   * Checks if a user is on the whitelist.
   * @param {string} userId - The unique identifier for the user.
   * @returns {boolean} - Returns true if the user is whitelisted, false otherwise.
   */
  isWhitelisted(userId) {
    if (!userId || typeof userId !== 'string') {
      throw new Error('Invalid userId. Must be a non-empty string.');
    }
    // Check if the Set contains the user
    return this.whitelist.has(userId);
  }

  /**
   * Gets all users currently on the whitelist.
   * @returns {Array<string>} - Returns an array of whitelisted users.
   */
  getWhitelistedUsers() {
    // Convert Set to an array for easier manipulation
    return Array.from(this.whitelist);
  }
}

// Example Usage
try {
  const whitelistManager = new WhitelistManager();

  // Add users to the whitelist
  console.log(whitelistManager.addUser('user1')); // true
  console.log(whitelistManager.addUser('user2')); // true
  console.log(whitelistManager.addUser('user1')); // false (already added)

  // Check if users are whitelisted
  console.log(whitelistManager.isWhitelisted('user1')); // true
  console.log(whitelistManager.isWhitelisted('user3')); // false

  // Remove a user from the whitelist
  console.log(whitelistManager.removeUser('user1')); // true
  console.log(whitelistManager.removeUser('user1')); // false (already removed)

  // Get all whitelisted users
  console.log(whitelistManager.getWhitelistedUsers()); // [ 'user2' ]
} catch (error) {
  console.error('Error:', error.message);
}
```
