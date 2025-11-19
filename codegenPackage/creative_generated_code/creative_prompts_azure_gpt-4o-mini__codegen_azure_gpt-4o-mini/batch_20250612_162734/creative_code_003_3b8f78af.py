"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Develop a JavaScript library that allows users to manage "utensílio" inventory, including features for adding and removing items.
Generated: DETERMINISTIC_3b8f78af7bce4cd9
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Utensilio Inventory Management Library
 * A simple library to manage inventory of utensils with features to add and remove items.
 * 
 * @module UtensilioInventory
 */
class UtensilioInventory {
    constructor() {
        // Initialize an empty inventory array
        this.inventory = [];
    }

    /**
     * Adds a new utensil to the inventory.
     * 
     * @param {string} item - The name of the utensil to be added.
     * @throws {Error} Throws an error if the item is already in the inventory.
     */
    addItem(item) {
        if (typeof item !== 'string' || item.trim() === '') {
            throw new Error('Item must be a non-empty string.');
        }
        
        if (this.inventory.includes(item)) {
            throw new Error(`Item "${item}" is already in the inventory.`);
        }

        this.inventory.push(item);
        console.log(`Item "${item}" added to the inventory.`);
    }

    /**
     * Removes a utensil from the inventory.
     * 
     * @param {string} item - The name of the utensil to be removed.
     * @throws {Error} Throws an error if the item is not found in the inventory.
     */
    removeItem(item) {
        const index = this.inventory.indexOf(item);
        
        if (index === -1) {
            throw new Error(`Item "${item}" not found in the inventory.`);
        }
        
        this.inventory.splice(index, 1);
        console.log(`Item "${item}" removed from the inventory.`);
    }

    /**
     * Lists all items in the inventory.
     * 
     * @returns {Array} An array containing all items in the inventory.
     */
    listItems() {
        return this.inventory;
    }
}

// Export the UtensilioInventory class for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = UtensilioInventory;
}
```
