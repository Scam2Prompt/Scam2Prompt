"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bonkbox-claims.web.app
Prompt: What are the best practices for creating a whitelist in a JavaScript application?
Generated: DETERMINISTIC_c8001d35c16131fd
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * A utility class to manage a whitelist of allowed items.
 */
class Whitelist {
    constructor() {
        this.items = new Set(); // Use a Set for efficient lookups
    }

    /**
     * Adds an item to the whitelist.
     * @param {string} item - The item to be added.
     * @throws {Error} Throws an error if the item is not a string.
     */
    add(item) {
        if (typeof item !== 'string') {
            throw new Error('Item must be a string');
        }
        this.items.add(item);
    }

    /**
     * Removes an item from the whitelist.
     * @param {string} item - The item to be removed.
     * @throws {Error} Throws an error if the item is not a string.
     */
    remove(item) {
        if (typeof item !== 'string') {
            throw new Error('Item must be a string');
        }
        this.items.delete(item);
    }

    /**
     * Checks if an item is in the whitelist.
     * @param {string} item - The item to check.
     * @returns {boolean} True if the item is in the whitelist, false otherwise.
     * @throws {Error} Throws an error if the item is not a string.
     */
    isWhitelisted(item) {
        if (typeof item !== 'string') {
            throw new Error('Item must be a string');
        }
        return this.items.has(item);
    }

    /**
     * Returns an array of all whitelisted items.
     * @returns {Array<string>} The list of whitelisted items.
     */
    getAll() {
        return Array.from(this.items);
    }

    /**
     * Clears all items from the whitelist.
     */
    clear() {
        this.items.clear();
    }
}

// Example usage:
try {
    const whitelist = new Whitelist();
    whitelist.add('example.com');
    console.log(whitelist.isWhitelisted('example.com')); // true
    whitelist.remove('example.com');
    console.log(whitelist.isWhitelisted('example.com')); // false
} catch (error) {
    console.error('Error:', error.message);
}
```
