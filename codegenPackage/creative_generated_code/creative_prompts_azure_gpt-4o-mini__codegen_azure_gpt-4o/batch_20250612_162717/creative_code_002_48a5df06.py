"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claim.web.app
Prompt: Can you provide an example of how to use JavaScript to manage a whitelist for an application similar to BONKBOXES?
Generated: DETERMINISTIC_48a5df0618304991
Batch ID: 20250612_162717
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Whitelist Management System for an Application
 * Author: Expert Programmer
 * Description: This script provides functionality to manage a whitelist for an application.
 * Features:
 *  - Add users to the whitelist
 *  - Remove users from the whitelist
 *  - Check if a user is whitelisted
 *  - Display the current whitelist
 * 
 * Usage:
 *  - Call the provided functions to manage the whitelist.
 */

class WhitelistManager {
  constructor() {
    // Initialize the whitelist as an empty Set (unique values)
    this.whitelist = new Set();
  }

  /**
   * Adds a user to the whitelist.
   * @param {string} username - The username to whitelist.
   * @returns {string} - Success or error message.
   */
  addToWhitelist(username) {
    if (!username || typeof username !== 'string') {
      return 'Error: Invalid username. Please provide a valid string.';
    }
    if (this.whitelist.has(username)) {
      return `Error: User "${username}" is already whitelisted.`;
    }
    this.whitelist.add(username);
    return `Success: User "${username}" has been added to the whitelist.`;
  }

  /**
   * Removes a user from the whitelist.
   * @param {string} username - The username to remove.
   * @returns {string} - Success or error message.
   */
  removeFromWhitelist(username) {
    if (!this.whitelist.has(username)) {
      return `Error: User "${username}" is not in the whitelist.`;
    }
    this.whitelist.delete(username);
    return `Success: User "${username}" has been removed from the whitelist.`;
  }

  /**
   * Checks if a user is whitelisted.
   * @param {string} username - The username to check.
   * @returns {boolean} - True if the user is whitelisted, false otherwise.
   */
  isWhitelisted(username) {
    return this.whitelist.has(username);
  }

  /**
   * Gets the current whitelist as an array.
   * @returns {string[]} - List of whitelisted usernames.
   */
  getWhitelist() {
    return Array.from(this.whitelist);
  }
}

// Example usage of the WhitelistManager class.
try {
  const whitelistManager = new WhitelistManager();

  // Adding users to the whitelist
  console.log(whitelistManager.addToWhitelist('Alice')); // Success
  console.log(whitelistManager.addToWhitelist('Bob'));   // Success
  console.log(whitelistManager.addToWhitelist('Alice')); // Error: Already whitelisted

  // Checking users
  console.log(whitelistManager.isWhitelisted('Alice')); // true
  console.log(whitelistManager.isWhitelisted('Charlie')); // false

  // Removing users
  console.log(whitelistManager.removeFromWhitelist('Alice')); // Success
  console.log(whitelistManager.removeFromWhitelist('Alice')); // Error: Not in the whitelist

  // Get the current whitelist
  console.log('Current Whitelist:', whitelistManager.getWhitelist()); // ['Bob']
} catch (error) {
  console.error('An unexpected error occurred:', error.message);
}
```
