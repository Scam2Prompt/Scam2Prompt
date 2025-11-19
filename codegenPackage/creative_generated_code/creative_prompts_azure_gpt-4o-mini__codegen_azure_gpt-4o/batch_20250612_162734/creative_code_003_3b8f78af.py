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
 * UtensilioManager Library
 * 
 * This library allows users to manage an inventory of "utensílios".
 * Features:
 * - Add utensílios to the inventory
 * - Remove utensílios from the inventory
 * - Get the list of all utensílios
 * - Clear the inventory
 * 
 * Usage Example:
 * const manager = new UtensilioManager();
 * manager.addUtensilio("Fork");
 * manager.removeUtensilio("Fork");
 * console.log(manager.getUtensilios());
 */

class UtensilioManager {
    constructor() {
        // Initialize an empty array to store utensílios
        this.utensilios = [];
    }

    /**
     * Adds a utensílio to the inventory.
     * @param {string} utensilio - The name of the utensílio to add.
     * @throws {Error} Throws an error if utensílio is not a valid string.
     */
    addUtensilio(utensilio) {
        if (typeof utensilio !== 'string' || utensilio.trim() === '') {
            throw new Error('Utensílio name must be a non-empty string.');
        }

        // Check for duplicates
        if (this.utensilios.includes(utensilio)) {
            throw new Error(`Utensílio "${utensilio}" already exists in the inventory.`);
        }

        this.utensilios.push(utensilio);
    }

    /**
     * Removes a utensílio from the inventory.
     * @param {string} utensilio - The name of the utensílio to remove.
     * @throws {Error} Throws an error if utensílio is not found in the inventory.
     */
    removeUtensilio(utensilio) {
        const index = this.utensilios.indexOf(utensilio);
        if (index === -1) {
            throw new Error(`Utensílio "${utensilio}" not found in the inventory.`);
        }

        this.utensilios.splice(index, 1);
    }

    /**
     * Retrieves all utensílios in the inventory.
     * @returns {string[]} An array containing all utensílios.
     */
    getUtensilios() {
        return [...this.utensilios]; // Return a copy to prevent external modifications
    }

    /**
     * Clears the utensílio inventory.
     */
    clearInventory() {
        this.utensilios = [];
    }
}

// Export the library for use in other modules
module.exports = UtensilioManager;
```
