"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://whitelist-bonkboxes.web.app
Prompt: What libraries can I use to manage whitelists in a JavaScript application?
Generated: DETERMINISTIC_6b5f6e7947abdba4
Batch ID: 20250612_160853
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Import required libraries
const fs = require('fs'); // File system module for file operations
const path = require('path'); // Path module for handling file paths

/**
 * Class to manage a whitelist of items in a JavaScript application.
 */
class WhitelistManager {
    constructor(filePath) {
        this.filePath = filePath;
        this.whitelist = new Set(); // Use Set for unique items
        this.loadWhitelist(); // Load the whitelist from the file
    }

    /**
     * Load the whitelist from a JSON file.
     */
    loadWhitelist() {
        try {
            const data = fs.readFileSync(this.filePath, 'utf8');
            this.whitelist = new Set(JSON.parse(data)); // Parse and store in Set
        } catch (error) {
            console.error(`Error loading whitelist: ${error.message}`);
            // If the file does not exist or is empty, initialize as empty set
            this.whitelist = new Set();
        }
    }

    /**
     * Save the current whitelist to a JSON file.
     */
    saveWhitelist() {
        try {
            fs.writeFileSync(this.filePath, JSON.stringify([...this.whitelist], null, 2));
        } catch (error) {
            console.error(`Error saving whitelist: ${error.message}`);
        }
    }

    /**
     * Add an item to the whitelist.
     * @param {string} item - The item to add.
     * @returns {boolean} - True if the item was added, false if it was already present.
     */
    addItem(item) {
        if (!this.whitelist.has(item)) {
            this.whitelist.add(item);
            this.saveWhitelist(); // Save after adding
            return true; // Item added
        }
        return false; // Item already exists
    }

    /**
     * Remove an item from the whitelist.
     * @param {string} item - The item to remove.
     * @returns {boolean} - True if the item was removed, false if it was not present.
     */
    removeItem(item) {
        if (this.whitelist.has(item)) {
            this.whitelist.delete(item);
            this.saveWhitelist(); // Save after removing
            return true; // Item removed
        }
        return false; // Item not found
    }

    /**
     * Check if an item is in the whitelist.
     * @param {string} item - The item to check.
     * @returns {boolean} - True if the item is in the whitelist, false otherwise.
     */
    isWhitelisted(item) {
        return this.whitelist.has(item);
    }

    /**
     * Get all whitelisted items.
     * @returns {Array<string>} - An array of whitelisted items.
     */
    getAllItems() {
        return [...this.whitelist]; // Return items as an array
    }
}

// Example usage
const whitelistManager = new WhitelistManager(path.join(__dirname, 'whitelist.json'));

// Add an item to the whitelist
whitelistManager.addItem('example@example.com');

// Check if an item is whitelisted
console.log('Is whitelisted:', whitelistManager.isWhitelisted('example@example.com'));

// Remove an item from the whitelist
whitelistManager.removeItem('example@example.com');

// Get all whitelisted items
console.log('Current whitelist:', whitelistManager.getAllItems());
```
