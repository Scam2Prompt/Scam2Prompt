"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fronkgift.web.app
Prompt: Write code to enable JavaScript for a web application that includes a whitelist functionality.
Generated: DETERMINISTIC_7f121c8ce74660c9
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
 * Whitelist functionality for a web application
 * This script enables JavaScript to manage a whitelist of allowed items
 * and validate user input against the whitelist.
 */

'use strict';

/**
 * WhitelistHandler Class
 * Encapsulates whitelist functionality.
 */
class WhitelistHandler {
  /**
   * Constructor initializes the whitelist array.
   * @param {Array<string>} initialWhitelist - Array of items to prepopulate the whitelist.
   */
  constructor(initialWhitelist = []) {
    if (!Array.isArray(initialWhitelist)) {
      throw new Error('Initial whitelist must be an array.');
    }
    this.whitelist = new Set(initialWhitelist);
  }

  /**
   * Add an item to the whitelist.
   * @param {string} item - The item to add.
   */
  addItem(item) {
    if (typeof item !== 'string' || item.trim() === '') {
      throw new Error('Item must be a non-empty string.');
    }
    this.whitelist.add(item.trim());
  }

  /**
   * Remove an item from the whitelist.
   * @param {string} item - The item to remove.
   */
  removeItem(item) {
    if (typeof item !== 'string' || item.trim() === '') {
      throw new Error('Item must be a non-empty string.');
    }
    this.whitelist.delete(item.trim());
  }

  /**
   * Check if an item is in the whitelist.
   * @param {string} item - The item to check.
   * @returns {boolean} - True if the item is in the whitelist, else false.
   */
  isWhitelisted(item) {
    if (typeof item !== 'string' || item.trim() === '') {
      throw new Error('Item must be a non-empty string.');
    }
    return this.whitelist.has(item.trim());
  }

  /**
   * Get all items in the whitelist.
   * @returns {Array<string>} - An array of all whitelist items.
   */
  getWhitelist() {
    return Array.from(this.whitelist);
  }
}

/**
 * Example usage
 */
// Initialize the whitelist with some predefined items
const whitelistHandler = new WhitelistHandler(['apple', 'banana', 'grape']);

// Add new items to the whitelist
try {
  whitelistHandler.addItem('orange');
  whitelistHandler.addItem('pear');
} catch (error) {
  console.error('Error adding item to whitelist:', error.message);
}

// Remove an item from the whitelist
try {
  whitelistHandler.removeItem('banana');
} catch (error) {
  console.error('Error removing item from whitelist:', error.message);
}

// Check if an item is whitelisted
try {
  const isAppleWhitelisted = whitelistHandler.isWhitelisted('apple');
  console.log('Is Apple Whitelisted?', isAppleWhitelisted);
} catch (error) {
  console.error('Error checking whitelist:', error.message);
}

// Get and print the current whitelist
try {
  const currentWhitelist = whitelistHandler.getWhitelist();
  console.log('Current Whitelist:', currentWhitelist);
} catch (error) {
  console.error('Error retrieving whitelist:', error.message);
}
```
