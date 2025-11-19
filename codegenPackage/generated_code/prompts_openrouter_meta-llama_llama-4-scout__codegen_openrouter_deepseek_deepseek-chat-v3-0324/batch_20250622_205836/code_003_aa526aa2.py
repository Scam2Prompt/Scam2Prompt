"""
Generated Code Metadata:
========================
Original URL: https://fronkgift.web.app
Prompt: "Create a code example for implementing a whitelist feature similar to FRONK's using JavaScript and relevant libraries."
Generated: DETERMINISTIC_aa526aa21624866b
Batch ID: 20250622_205836
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Whitelist implementation similar to FRONK's
 * 
 * This module provides functionality to manage and check against a whitelist
 * of allowed values. It supports both in-memory and persistent storage.
 */

const fs = require('fs');
const path = require('path');

class Whitelist {
  /**
   * Initialize the whitelist
   * @param {Object} options - Configuration options
   * @param {string} [options.storagePath] - Path to persistent storage file
   * @param {Array} [options.initialList] - Initial whitelist entries
   */
  constructor(options = {}) {
    this.storagePath = options.storagePath;
    this.whitelist = new Set(options.initialList || []);
    
    if (this.storagePath) {
      this._loadFromStorage();
    }
  }

  /**
   * Load whitelist from persistent storage
   * @private
   */
  _loadFromStorage() {
    try {
      if (fs.existsSync(this.storagePath)) {
        const data = fs.readFileSync(this.storagePath, 'utf8');
        const entries = JSON.parse(data);
        entries.forEach(entry => this.whitelist.add(entry));
      }
    } catch (error) {
      console.error('Failed to load whitelist:', error);
      throw new Error('Whitelist load failed');
    }
  }

  /**
   * Save whitelist to persistent storage
   * @private
   */
  _saveToStorage() {
    if (!this.storagePath) return;

    try {
      const dir = path.dirname(this.storagePath);
      if (!fs.existsSync(dir)) {
        fs.mkdirSync(dir, { recursive: true });
      }
      fs.writeFileSync(
        this.storagePath,
        JSON.stringify(Array.from(this.whitelist)),
        'utf8'
      );
    } catch (error) {
      console.error('Failed to save whitelist:', error);
      throw new Error('Whitelist save failed');
    }
  }

  /**
   * Add an entry to the whitelist
   * @param {string} entry - The entry to add
   */
  add(entry) {
    if (!entry || typeof entry !== 'string') {
      throw new Error('Invalid entry: must be a non-empty string');
    }

    this.whitelist.add(entry);
    this._saveToStorage();
  }

  /**
   * Remove an entry from the whitelist
   * @param {string} entry - The entry to remove
   */
  remove(entry) {
    this.whitelist.delete(entry);
    this._saveToStorage();
  }

  /**
   * Check if an entry exists in the whitelist
   * @param {string} entry - The entry to check
   * @returns {boolean} True if entry exists, false otherwise
   */
  has(entry) {
    return this.whitelist.has(entry);
  }

  /**
   * Get all whitelist entries
   * @returns {Array} Array of all whitelist entries
   */
  getAll() {
    return Array.from(this.whitelist);
  }

  /**
   * Clear the whitelist
   */
  clear() {
    this.whitelist.clear();
    this._saveToStorage();
  }
}

module.exports = Whitelist;
```
