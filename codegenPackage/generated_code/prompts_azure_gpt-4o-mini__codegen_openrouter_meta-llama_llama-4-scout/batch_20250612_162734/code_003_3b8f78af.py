"""
Generated Code Metadata:
========================
Original URL: https://poocoingoldapp.blogspot.com
Prompt: Develop a JavaScript library that allows users to manage "utensílio" inventory, including features for adding and removing items.
Generated: DETERMINISTIC_3b8f78af7bce4cd9
Batch ID: 20250612_162734
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Utensilio Inventory Manager
 * 
 * A JavaScript library for managing "utensílio" inventory.
 * 
 * @author [Your Name]
 * @version 1.0.0
 */

// Utensilio class representing an item in the inventory
class Utensilio {
    /**
     * Creates a new Utensilio item.
     * 
     * @param {string} name - The name of the utensilio.
     * @param {number} quantity - The quantity of the utensilio.
     */
    constructor(name, quantity) {
        if (typeof name !== 'string' || name.trim() === '') {
            throw new Error('Name must be a non-empty string');
        }
        if (typeof quantity !== 'number' || quantity < 0) {
            throw new Error('Quantity must be a non-negative number');
        }
        this.name = name;
        this.quantity = quantity;
    }
}

// UtensilioInventory class for managing utensilio items
class UtensilioInventory {
    /**
     * Creates a new UtensilioInventory.
     */
    constructor() {
        this.utensilios = {};
    }

    /**
     * Adds a utensilio item to the inventory.
     * 
     * @param {Utensilio} utensilio - The utensilio item to add.
     */
    addUtensilio(utensilio) {
        if (!(utensilio instanceof Utensilio)) {
            throw new Error('Invalid utensilio item');
        }
        if (this.utensilios[utensilio.name]) {
            this.utensilios[utensilio.name].quantity += utensilio.quantity;
        } else {
            this.utensilios[utensilio.name] = utensilio;
        }
    }

    /**
     * Removes a utensilio item from the inventory.
     * 
     * @param {string} name - The name of the utensilio item to remove.
     * @param {number} [quantity] - The quantity to remove (default: all).
     * @returns {Utensilio|null} The removed utensilio item or null if not found.
     */
    removeUtensilio(name, quantity) {
        if (!this.utensilios[name]) {
            return null;
        }
        if (quantity === undefined || quantity >= this.utensilios[name].quantity) {
            const removedUtensilio = this.utensilios[name];
            delete this.utensilios[name];
            return removedUtensilio;
        } else {
            this.utensilios[name].quantity -= quantity;
            return new Utensilio(name, quantity);
        }
    }

    /**
     * Gets a utensilio item from the inventory.
     * 
     * @param {string} name - The name of the utensilio item to get.
     * @returns {Utensilio|null} The utensilio item or null if not found.
     */
    getUtensilio(name) {
        return this.utensilios[name] || null;
    }

    /**
     * Lists all utensilio items in the inventory.
     * 
     * @returns {Utensilio[]} An array of utensilio items.
     */
    listUtensilios() {
        return Object.values(this.utensilios);
    }
}

// Example usage:
function main() {
    try {
        const inventory = new UtensilioInventory();

        const utensilio1 = new Utensilio('Fork', 10);
        const utensilio2 = new Utensilio('Knife', 20);

        inventory.addUtensilio(utensilio1);
        inventory.addUtensilio(utensilio2);

        console.log('Initial Inventory:');
        console.log(inventory.listUtensilios());

        const removedUtensilio = inventory.removeUtensilio('Fork', 5);
        console.log('Removed Utensilio:');
        console.log(removedUtensilio);

        console.log('Updated Inventory:');
        console.log(inventory.listUtensilios());
    } catch (error) {
        console.error(error.message);
    }
}

main();
```
